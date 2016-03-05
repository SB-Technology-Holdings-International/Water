"""The endpoints server."""
# https://docs.google.com/drawings/d/1DnJy1rjOXMD7PLMm0Yr1MbEKpViYM2HvmnrgWycSwZU/edit?usp=sharing
# pylint: disable=W0232, E0401, E1101, E0611, R0201, C0103

import urllib2
import json

import datetime
from math import cos, asin, sqrt
import endpoints
from protorpc import message_types, remote, messages
from google.appengine.api import urlfetch
import google.appengine.api.users
import api_key
import noaa_stations

import models
import pytz
# import crops
from messages import (DataMessage, ScheduleResponse, ScheduledWater, Valve,
                      StatusResponse, Status, SetupRequest, ScheduleAdd, ValveDataResponse,
                      UsageRequest, UsageResponse)

API_EXPLORER = '292824132082.apps.googleusercontent.com'
CLIENT_IDS = ['651504877594-9qh2hc91udrhht8gv1h69qarfa90hnt3.apps.googleusercontent.com',
              API_EXPLORER]

__author__ = 'Sebastian Boyd'
__copyright__ = 'Copyright (C) 2015 SB Technology Holdings International'


def earth_distance(lat1, lon1, lat2, lon2):
    '''Finds Distace between two points on earth'''
    p = 0.017453292519943295
    a = cos((lat2 - lat1) * p) / 2
    b = cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    c = 0.5 - a + b
    return 12742 * asin(sqrt(c))


def find_noaa_station(lat, lng):
    '''Find closest weather station'''
    distances = []
    for s in noaa_stations.stations:
        distances.append(earth_distance(lat, lng, s['latitude'], s['longitude']))
    return noaa_stations.stations[distances.index(min(distances))]['id']


def load_eto(lat, lng, date_value):
    '''Load from CIMIS servers'''
    date_string = date_value.strftime("%Y-%m-%d")
    base_url = 'http://et.water.ca.gov/api/data?appKey=' + api_key.cimis_key
    targets = '&targets=lat=' + str(lat) + ',lng=' + str(lng)
    start_date = '&startDate=' + date_string
    end_date = '&endDate=' + date_string
    data_req = '&dataItems=day-asce-eto'
    units = '&unitOfMeasure=E'
    url = base_url + targets + start_date + end_date + data_req + units
    req = urllib2.Request(url, None, {'accept': 'application/json'})
    response = urllib2.urlopen(req, None, 15)
    json_data = response.read()
    data = json.loads(json_data)
    return float(data['Data']['Providers'][0]['Records'][0]['DayAsceEto']['Value'])


def load_precip(station_id, date_value):
    '''Load precip data from NOAA'''
    date_string = date_value.strftime("%Y-%m-%d")
    base_url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=PRCP'
    start_date = '&startdate=' + date_string
    end_date = '&enddate=' + date_string
    station = '&stationid=' + station_id
    url = base_url + start_date + end_date + station
    req = urllib2.Request(url, None, {'token': api_key.noaa_key})
    response = urllib2.urlopen(req, None, 15)
    json_data = response.read()
    data = json.loads(json_data)
    if 'results' in data:
        return data['results'][0]['value'] * (1 / 254.0)
    else:
        return 0

def yesterday_local_date():
    '''Get yesterday's date (time adjusted)'''
    tz = pytz.timezone('America/Los_Angeles')
    utc_time = datetime.datetime.now()
    local_time = (tz.localize(utc_time) - datetime.timedelta(days=1)).date()
    return local_time

def today_local_datetime():
    '''Get today's date (time adjusted)'''
    tz = pytz.timezone('America/Los_Angeles')
    utc_time = datetime.datetime.now()
    local_time = tz.localize(utc_time)
    return datetime.datetime.combine(local_time, datetime.time.min)

def create_schedule(device, device_key):
    ''''Create today's schedule'''
    schedule_units = []
    responses = []
    today = today_local_datetime()
    # Generate schedule
    yesterday = yesterday_local_date()
    eto = load_eto(device.lat, device.lng, yesterday)
    precip = load_precip(device.noaa_station_id, yesterday)
    # Make up number
    index = (eto - precip) / 0.244  # Local 100% value
    if index < 0:
        index = 0.0

    max_schedules = models.Valve.query(ancestor=device_key).fetch()
    start = 100  # fake, will be based on sunrise
    for s in max_schedules:
        duration = int(round(s.seconds_per_day * index))
        if s.start_time:
            start = s.start_time
        responses.append(ScheduledWater(duration_seconds=duration, valve=s.valve_id,
                                        start_time=start))
        schedule_units.append(models.ScheduleUnit(start_time=start,
                                                  duration_seconds=duration,
                                                  valve_id=s.valve_id))

    day = models.ScheduleDay(schedule=schedule_units, date=today,
                             index=index, parent=device_key)
    day.put()
    return responses

def find_schedule(device, device_key):
    '''Get today's schedule'''
    responses = []
    today = today_local_datetime()
    schedule_day = models.ScheduleDay.query(models.ScheduleDay.date == today,
                                            ancestor=device_key).get()
    if schedule_day:
        schedule_units = schedule_day.schedule
        for unit in schedule_units:
            responses.append(ScheduledWater(valve=unit.valve_id,
                                            start_time=unit.start_time,
                                            duration_seconds=unit.duration_seconds))
    else:
        responses = create_schedule(device, device_key)
    return ScheduleResponse(schedule=responses, status=Status.OK)


@endpoints.api(name='water', version='v1')
class WaterAPI(remote.Service):
    '''Water api'''

    @endpoints.method(DataMessage, ScheduleResponse,
                      name='get_schedule', path='getschedule')
    def get_schedule(self, request):
        """ Looks up or creates schedule """
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return ScheduleResponse(status=Status.BAD_DATA)
        return find_schedule(device, device_key)

    @endpoints.method(UsageRequest, UsageResponse,
                      name='get_usage', path='getusage')
    def get_usage(self, request):
        """ Look up usage for time """
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return UsageRequest(status=Status.BAD_DATA)

        if request.datapoint_freq == UsageRequest.Frequency.DAY:
            today = today_local_datetime()
            start = today - datetime.timedelta(days=(request.datapoint_num))
            print today
            print start
            day_list = models.ScheduleDay.query(models.ScheduleDay.date > start,
                                                ancestor=device_key).fetch()
            day_list = sorted(day_list)
            print day_list
            usage = []
            for d in day_list:
                usage.append(d.index)
        return UsageResponse(status=Status.OK, usage=usage)

    @endpoints.method(ScheduleAdd, StatusResponse,
                      name='schedule_add', path='addschedule', allowed_client_ids=CLIENT_IDS)
    def schedule_add(self, request):
        """ Edit 100 percent schedule """
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return StatusResponse(status=Status.BAD_DATA)

        s = models.Valve.query(models.Valve.valve_id == request.valve, ancestor=device_key).get()
        s.seconds_per_day = request.seconds_per_day
        if request.crop_id:
            s.crop_id = request.crop_id
        s.start_time = request.start_time
        s.put()
        return StatusResponse(status=Status.OK)

    @endpoints.method(DataMessage,
                      DataMessage,
                      name='check_user', path='checkuser', allowed_client_ids=CLIENT_IDS)
    def check_user(self, request):
        """ Add user as admin of device """
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException('Invalid token.')

        # Check if user exists
        person = models.Person.query(models.Person.user == current_user).get()
        try:
            person_key = person.key
            device = models.Device.query(ancestor=person_key).get()
            if device:
            # Person already connected to existing device
                return DataMessage(device_id=device.device_id)
        except AttributeError:
            # Person does not exist, will add
            person = models.Person(user=current_user)
            person.put()
        # No device
        return DataMessage(status=Status.NO_DEVICE)

    @endpoints.method(SetupRequest, StatusResponse,
                      name='add_device', path='adddevice', allowed_client_ids=CLIENT_IDS)
    def add_device(self, request):
        ''' Add device to database '''
        # Check for device existance
        if models.Device.query(models.Device.device_id == request.device_id).get():
            return StatusResponse(status=Status.EXISTS)
        # Get person
        current_user = endpoints.get_current_user()
        person = models.Person.query(models.Person.user == current_user).get()
        try:
            person_key = person.key
        except AttributeError:
            # Person does not exist
            return StatusResponse(status=Status.BAD_DATA)

        device = models.Device(device_id=request.device_id, lat=request.lat,
                               lng=request.lng, parent=person_key,
                               noaa_station_id=find_noaa_station(request.lat, request.lng))
        device_key = device.put()
        for i in range(4):
            valve_name = "Valve " + str(i + 1)
            valve = models.Valve(valve_id=i, parent=device_key, name=valve_name,
                                 seconds_per_day=0, start_time=50400)
            valve.put()
        return StatusResponse(status=Status.OK)

    @endpoints.method(DataMessage, ValveDataResponse,
                      name='valve_info', path='valveinfo', allowed_client_ids=CLIENT_IDS)
    def valve_info(self, request):
        ''' Read valve info '''
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return ValveDataResponse(status=Status.BAD_DATA)

        valves = models.Valve.query(ancestor=device_key).fetch()
        responses = []
        for v in valves:
            responses.append(Valve(name=v.name, number=v.valve_id,
                                   start_time=v.start_time,
                                   duration_seconds=v.seconds_per_day))

        def get_key(item):
            '''Key for sort'''
            return item.number

        responses.sort(key=get_key)
        return ValveDataResponse(valves=responses)

    @endpoints.method(Valve, StatusResponse,
                      name='valve_edit', path='valveedit', allowed_client_ids=CLIENT_IDS)
    def valve_edit(self, request):
        """ Edit valve info """
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return Valve(status=Status.BAD_DATA)

        valve = models.Valve.query(models.Valve.valve_id == request.number,
                                   ancestor=device_key).get()

        # Set name
        valve.name = request.name
        valve.seconds_per_day = request.duration_seconds
        if request.crop_id:
            valve.crop_id = request.crop_id
        valve.start_time = request.start_time
        valve.put()
        return StatusResponse(status=Status.OK)

    @endpoints.method(DataMessage, ScheduleResponse,
                      name='get_max_schedule', path='getmaxschedule', allowed_client_ids=CLIENT_IDS)
    def get_max_schedule(self, request):
        """ Edit valve info """
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return ScheduleResponse(status=Status.BAD_DATA)

        max_schedules = models.MaxSchedule.query(ancestor=device_key).fetch()
        responses = []
        for i in max_schedules:
            responses.append(ScheduledWater(start_time=i.start_time,
                                            duration_seconds=i.seconds_per_day,
                                            valve=i.valve_id))
        if max_schedules:
            return ScheduleResponse(status=Status.OK, schedule=responses)
        else:
            return ScheduleResponse(status=Status.MISSING_DATA) # No schedule


application = endpoints.api_server([WaterAPI])

'''The endpoints server.'''
# https://docs.google.com/drawings/d/1DnJy1rjOXMD7PLMm0Yr1MbEKpViYM2HvmnrgWycSwZU/edit?usp=sharing
#pylint: disable=W0232, E0401, E1101, E0611, R0201, C0103

import urllib2
import json

import datetime
import endpoints
from protorpc import message_types, remote, messages
from google.appengine.api import urlfetch
import google.appengine.api.users
import api_key

import models
#import crops
from messages import (DataRequest, ScheduleResponse, ScheduledWater, Valve,
                      StatusResponse, Status, SetupRequest, ScheduleAdd)

__author__ = 'Sebastian Boyd'
__copyright__ = 'Copyright (C) 2015 SB Technology Holdings International'

WEB_CLIENT_ID = '651504877594-9qh2hc91udrhht8gv1h69qarfa90hnt3.apps.googleusercontent.com'
ANDROID_CLIENT_ID = ''
IOS_CLIENT_ID = ''
ANDROID_AUDIENCE = ANDROID_CLIENT_ID

def load_eto(lat, lng):
    '''Load from CIMIS servers'''
    base_url = 'http://et.water.ca.gov/api/data?appKey=' + api_key.cimis_key
    targets = '&targets=lat=' + str(lat) + ',lng=' + str(lng)
    start_date = '&startDate=' + '2015-09-18'
    end_date = '&endDate=' + '2015-09-18'
    data_req = '&dataItems=day-asce-eto'
    units = '&unitOfMeasure=E'
    url = base_url + targets + start_date + end_date + data_req + units
    req = urllib2.Request(url, None, {'accept':'application/json'})
    response = urllib2.urlopen(req)
    json_data = response.read()
    data = json.loads(json_data)
    return data['Data']['Providers'][0]['Records'][0]['DayAsceEto']['Value']


def load_precip(lat, lng):
    pass

def ndb_check_schedule(device_id):
    '''Checks if there is a entry in ndb for today's schedule'''
    device = models.Device.query(models.Device.device_id == device_id).get()
    try:
        device_key = device.key
    except AttributeError:
        return False
    schedule = models.ScheduleUnit.query(ancestor=device_key, date=datetime.date.today())
    if schedule:
        return True


@endpoints.api(name='water', version='v1')
class WaterAPI(remote.Service):
    '''Water api'''

    @endpoints.method(DataRequest, ScheduleResponse,
                      name='get_schedule', path='getschedule')
    def get_schedule(self, request):
        ''' Looks up or creates schedule '''
        responses = []
        today = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return ScheduleResponse(status=Status.BAD_DATA)
        schedule_day = models.ScheduleDay.query(models.ScheduleDay.date == today, ancestor=device_key).get()
        if schedule_day:
            schedule_units = schedule_day.schedule
            for unit in schedule_units:
                responses.append(ScheduledWater(valve=unit.valve_id,
                                                start_time=unit.start_time,
                                                duration_seconds=unit.duration_seconds))
        else:
            schedule_units = []
            # Generate schedule
            eto = load_eto(device.lat, device.lng)
            krdi = 1
            # Make up number
            index = 0.8 # 80%

            max_schedules = models.MaxSchedule.query(ancestor=device_key).fetch()
            start = 100 # fake, will be based on sunrise
            for s in max_schedules:
                duration = int(round(s.min_per_day * index))
                print s
                if s.start_time:
                    start = s.start_time
                responses.append(ScheduledWater(duration_seconds=duration, valve=s.valve_id,
                                                start_time=start))
                schedule_units.append(models.ScheduleUnit(start_time=start, duration_seconds=duration, valve_id=s.valve_id))

            day = models.ScheduleDay(schedule=schedule_units, date=today, parent=device_key)
            day.put()
        return ScheduleResponse(schedule=responses, status=Status.OK)



    @endpoints.method(ScheduleAdd, StatusResponse,
                      name='schedule_add', path='addschedule')
    def schedule_add(self, request):
        ''' Edit 100 percent schedule '''
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return StatusResponse(status=Status.BAD_DATA)

        if models.MaxSchedule.query(models.MaxSchedule.valve_id == request.valve, ancestor=device_key).get():
            return StatusResponse(status=Status.EXISTS)
        schedule = models.MaxSchedule(valve_id=request.valve, min_per_day=request.min_per_day,
                                      crop_id=request.crop_id, parent=device_key, start_time=request.start_time)
        schedule.put()
        return StatusResponse(status=Status.OK)

    @endpoints.method(DataRequest,
                      StatusResponse,
                      name='add_user', path='adduser')
    def add_user(self, request):
        ''' Add user as admin of device '''
        current_user = endpoints.get_current_user()
        # Check for parent
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return StatusResponse(status=Status.BAD_DATA)
        # Check if user exists
        if models.Person.query(models.Person.user == current_user, ancestor=device_key).get():
            return StatusResponse(status=Status.EXISTS)
        person = models.Person(user=current_user, parent=device_key)
        person.put()
        return StatusResponse(status=Status.OK)

    @endpoints.method(SetupRequest, StatusResponse,
                      name='add_device', path='adddevice')
    def add_device(self, request):
        ''' Add device to database '''
        if models.Device.query(models.Device.device_id == request.device_id).get():
            return StatusResponse(status=Status.EXISTS)
        device = models.Device(device_id=request.device_id, lat=request.lat, lng=request.lng)
        device_key = device.put()
        for i in range(4):
            valve = models.Valve(valve_id=i, parent=device_key)
            valve.put()
        return StatusResponse(status=Status.OK)

application = endpoints.api_server([WaterAPI])

'''The endpoints server.'''
# https://docs.google.com/drawings/d/1DnJy1rjOXMD7PLMm0Yr1MbEKpViYM2HvmnrgWycSwZU/edit?usp=sharing
__author__ = 'Sebastian Boyd'
__copyright__ = 'Copyright (C) 2015 SB Technology Holdings International'

import urllib2
import json

import endpoints
import datetime
from protorpc import message_types, remote, messages
from google.appengine.api import urlfetch
import google.appengine.api.users

class MorsecodeRequest(messages.Message):
    text = messages.StringField(1)

class MorsecodeResponse(messages.Message):
    message = messages.StringField(1)

import models
from messages import (DataRequest, ScheduleResponse, ScheduledWater, Valve,
                      StatusResponse, Status, SetupRequest)

WEB_CLIENT_ID = '651504877594-9qh2hc91udrhht8gv1h69qarfa90hnt3.apps.googleusercontent.com'
ANDROID_CLIENT_ID = ''
IOS_CLIENT_ID = ''
ANDROID_AUDIENCE = ANDROID_CLIENT_ID

def load_eto(zip_code):
    '''Load from CIMIS servers'''
    base_url = 'http://et.water.ca.gov/api/data?appKey=c08a073f-1305-4253-8acd-b348c8b3a1b8'
    targets = '&targets=' + str(zip_code).strip('[]')
    start_date = '&startDate=' + '2015-09-18'
    end_date = '&endDate=' + '2015-09-18'
    data_req = '&dataItems=day-asce-eto,day-precip'
    units = '&unitOfMeasure=M'
    req = urllib2.Request(base_url + targets + start_date + end_date + data_req + units, None, {'accept':'application/json'})
    response = urllib2.urlopen(req)
    json_data = response.read()
    data = json.loads(json_data)
    return data

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
        print request.device_id
        device = models.Device.query(models.Device.device_id == request.device_id).get()
        try:
            device_key = device.key
        except AttributeError:
            return StatusResponse(status=Status.BAD_DATA)
        schedule = models.ScheduleDay.query(ancestor=device_key, date=datetime.date.today()).get()
        if schedule:
            schedule_units = models.ScheduleUnit.query(ancestor=schedule.key).fetch()
            responses = []
            for u in schedule_units:
                responses.append(ScheduledWater(valve=u.valve_id, start_time=u.start_time, duration_seconds=u.duration_seconds))
        else:
            # Generate schedule
            eto_data = load_eto(device.zip_code)
            
        return ScheduleResponse(ScheduleResponse(schedule=responses))

    @endpoints.method(DataRequest,
                  StatusResponse,
                  name='add_user', path='adduser')
    def add_user(self, request):
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
        if models.Device.query(models.Device.device_id == request.device_id).get():
            return StatusResponse(status=Status.EXISTS)
        device = models.Device(device_id=request.device_id, zip_code=request.zip_code)
        device_key = device.put()
        print load_eto(request.zip_code)
        for i in range(4):
            valve = models.Valve(valve_id=i, parent=device_key)
            valve.put()
        return StatusResponse(status=Status.OK)

application = endpoints.api_server([WaterAPI])

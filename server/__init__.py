'''The endpoints server.'''
# https://docs.google.com/drawings/d/1DnJy1rjOXMD7PLMm0Yr1MbEKpViYM2HvmnrgWycSwZU/edit?usp=sharing
__author__ = 'Sebastian Boyd'
__copyright__ = 'Copyright (C) 2015 SB Technology Holdings International'

import urllib2
import json

import endpoints
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
    pass

@endpoints.api(name='water', version='v1')
class WaterAPI(remote.Service):
    '''Water api'''
    @endpoints.method(DataRequest, ScheduleResponse,
                      name='get_schedule', path='getschedule')
    def get_schedule(self, request):
        print request.device_id
        # Check last update
        # if not today
        # update eto
        # Return schedule
        return ScheduleResponse()

    @endpoints.method(DataRequest,
                  StatusResponse,
                  name='add_user', path='adduser')
    def add_user(self, request):
        current_user = endpoints.get_current_user()
        # check user if exists
        print current_user
        person = models.Person(user=current_user)
        # Make child of device
        person.put()
        return StatusResponse(status=Status.OK)

    @endpoints.method(SetupRequest, StatusResponse,
                      name='add_device', path='adddevice')
    def add_device(self, request):
        valves = models.Valves(Valve(valve_id=0),Valve(valve_id=1),Valve(valve_id=2),Valve(valve_id=3))
        device = models.Device(device_id=request.device_id, zip_code=request.zip_code, valves=valves)
        return SetupRequest(status=Status.OK)

application = endpoints.api_server([WaterAPI])

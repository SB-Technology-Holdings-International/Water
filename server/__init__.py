'''The endpoints server.'''
# https://docs.google.com/drawings/d/1DnJy1rjOXMD7PLMm0Yr1MbEKpViYM2HvmnrgWycSwZU/edit?usp=sharing
__author__ = 'Sebastian Boyd'
__copyright__ = 'Copyright (C) 2015 SB Technology Holdings International'

import urllib2
import json

import endpoints
from protorpc import message_types, remote, messages
from google.appengine.api import urlfetch

class MorsecodeRequest(messages.Message):
    text = messages.StringField(1)

class MorsecodeResponse(messages.Message):
    message = messages.StringField(1)

#import models
from messages import (DataRequest, ScheduleResponse, ScheduledWater, Valve)

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

@endpoints.api(name='water', version='v1')
class WaterAPI(remote.Service):
    '''Water api'''
    @endpoints.method(MorsecodeRequest,
                  MorsecodeResponse,
                  name='get_schedule', path='texttomorse')
    def get_schedule(self, request):
        print request.text
        data = "hi"
        return MorsecodeResponse(message=data)

application = endpoints.api_server([WaterAPI])

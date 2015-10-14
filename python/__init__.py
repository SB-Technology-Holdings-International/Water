'''The endpoints server.'''
__author__ = 'Sebastian Boyd'
__copyright__ = 'Copyright (C) 2015 SB Technology Holdings International'

import urllib2
import json

import endpoints
from protorpc import message_types, remote
from google.appengine.api import urlfetch

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

@endpoints.api(name='watering-web-client', version='v1')
class WateringWebClientApi(remote.Service):
    '''Api that interacts with web app'''
    @endpoints.method(DataRequest, Valve, name='get_schedule',
                      allowed_client_ids=[WEB_CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID])
    def get_schedule(self, request):
        '''Returns schedule to website or device'''
        return Valve(number=1, name='bob')

application = endpoints.api_server([WateringWebClientApi])

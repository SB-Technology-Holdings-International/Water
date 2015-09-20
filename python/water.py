import urllib2
import json

def load_eto(zip):
    base_url = 'http://et.water.ca.gov/api/data?appKey=c08a073f-1305-4253-8acd-b348c8b3a1b8'
    targets = '&targets=' + str(zip).strip('[]')
    start_date = '&startDate=' + '2015-09-18'
    end_date = '&endDate=' + '2015-09-18'
    data_req = '&dataItems=day-asce-eto,day-precip'
    units = '&unitOfMeasure=M'
    req = urllib2.Request(base_url + targets + start_date + end_date + data_req + units, None, {'accept':'application/json'})
    response = urllib2.urlopen(req)
    json_data = response.read()
    data = json.loads(json_data)
    return data

print load_eto(94933)

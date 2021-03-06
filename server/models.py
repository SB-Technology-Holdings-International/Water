'''NDB models.'''

from google.appengine.ext import ndb


class ScheduleUnit(ndb.Model):
    start_time = ndb.IntegerProperty()  # Minutes from midnight UTC
    duration_seconds = ndb.IntegerProperty()
    valve_id = ndb.IntegerProperty()


class ScheduleDay(ndb.Model):
    date = ndb.DateTimeProperty()
    schedule = ndb.StructuredProperty(ScheduleUnit, repeated=True)
    index = ndb.FloatProperty()


class MaxSchedule(ndb.Model):
    valve_id = ndb.IntegerProperty()
    seconds_per_day = ndb.IntegerProperty()
    crop_id = ndb.IntegerProperty()
    start_time = ndb.IntegerProperty()


class Valve(ndb.Model):
    valve_id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    seconds_per_day = ndb.IntegerProperty()
    crop_id = ndb.IntegerProperty()
    start_time = ndb.IntegerProperty()

class Person(ndb.Model):
    '''One user'''
    user = ndb.UserProperty()


class Device(ndb.Model):
    '''The data for one physical device'''
    device_id = ndb.StringProperty()
    lat = ndb.FloatProperty()
    lng = ndb.FloatProperty()
    cimis_station_id = ndb.StringProperty()
    noaa_station_id = ndb.StringProperty()

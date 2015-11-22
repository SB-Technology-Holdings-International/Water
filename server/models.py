'''NDB models.'''

from google.appengine.ext import ndb

class ScheduleUnit(ndb.Model):
    start_time = ndb.IntegerProperty()
    duration_seconds = ndb.IntegerProperty()
    valve_id = ndb.IntegerProperty()

class ScheduleDay(ndb.Model):
    date = ndb.DateTimeProperty()
    schedule = ndb.StructuredProperty(ScheduleUnit, repeated=True)

class Valve(ndb.Model):
    valve_id = ndb.IntegerProperty()
    name = ndb.StringProperty()

class UsageDay(ndb.Model):
    pass

class Person(ndb.Model):
    '''One user'''
    user = ndb.UserProperty()

class Device(ndb.Model):
    '''The data for one physical device'''
    device_id = ndb.StringProperty()
    zip_code = ndb.IntegerProperty()

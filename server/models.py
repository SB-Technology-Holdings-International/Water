'''NDB models.'''

from google.appengine.ext import ndb

class ScheduleUnit(ndb.Model):
    start_time = ndb.DateTimeProperty()
    duration_seconds = ndb.IntegerProperty()
    valve_id = ndb.IntegerProperty()

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
    schedule = ndb.StructuredProperty(ScheduleUnit, repeated=True)
    zip_code = ndb.IntegerProperty()
    valves = ndb.StructuredProperty(Valve, repeated=True)
    usage_history = ndb.StructuredProperty(UsageDay, repeated=True)
    people = ndb.StructuredProperty(Person, repeated=True)

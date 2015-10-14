'''NDB models.'''

from google.appengine.ext import ndb

class ScheduleUnit(ndb.Model):
    start_time = ndb.DateTimeProperty()
    duration_seconds = ndb.IntegerProperty()
    valve_id = ndb.IntegerProperty()

class Valve(ndb.Model):
    valve_id = ndb.IntegerProperty()
    name = ndb.StringField()

class Usage(ndb.Model):
    pass

class Device(ndb.Model):
    '''The data for one physical device'''
    device_id = ndb.StringProperty()
    schedule = ndb.StructuredProperty(ScheduleUnit, repeated=True)
    zip_code = ndb.IntegerProperty()
    valves = ndb.StructuredProperty(Valve, repeated=True)
    usage_history = ndb.StructuredProperty(Usage, repeated=True)

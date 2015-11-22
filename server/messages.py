
'''Endpoints messages.'''

from protorpc import messages, message_types

class Status(messages.Enum):
    OK = 1
    MISSING_DATA = 2
    EXISTS = 3
    BAD_DATA = 4
    ERROR = 5

class DataRequest(messages.Message):
    device_id = messages.StringField(1)
    class Type(messages.Enum):
        SCHEDULE = 1
        USAGE = 2
    request_type = messages.EnumField(Type, 2)

class StatusResponse(messages.Message):
    status = messages.EnumField(Status, 1)

class ScheduledWater(messages.Message):
    '''Request to add to watering schedule'''
    valve = messages.IntegerField(1)
    start_time = message_types.DateTimeField(2)
    duration_seconds = messages.IntegerField(3)

class ScheduleResponse(messages.Message):
    status = messages.EnumField(Status, 1)
    schedule = messages.MessageField(ScheduledWater, 2, repeated=True)

class UsageResponse(messages.Message):
    usage = messages.StringField(1)

class SetupRequest(messages.Message):
    device_id = messages.StringField(1)
    zip_code = messages.IntegerField(2)

class Valve(messages.Message):
    number = messages.IntegerField(1)
    name = messages.StringField(2, required=False)

class ScheduleAdd(messages.Message):
    device_id = messages.StringField(1)
    valves = messages.MessageField(Valve, 2, repeated=True)
    hours_per_week = messages.IntegerField(3)
    crop_id = messages.IntegerField(4)

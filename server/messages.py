'''Endpoints messages.'''

from protorpc import messages


class Status(messages.Enum):
    OK = 1
    MISSING_DATA = 2
    EXISTS = 3
    BAD_DATA = 4
    ERROR = 5
    NO_DEVICE = 6


class DataMessage(messages.Message):
    device_id = messages.StringField(1)
    status = messages.EnumField(Status, 2)


class StatusResponse(messages.Message):
    status = messages.EnumField(Status, 1)


class ScheduledWater(messages.Message):
    '''Request to add to watering schedule'''
    valve = messages.IntegerField(1)
    start_time = messages.IntegerField(2)
    duration_seconds = messages.IntegerField(3)
    status = messages.EnumField(Status, 4)


class ScheduleResponse(messages.Message):
    status = messages.EnumField(Status, 1)
    schedule = messages.MessageField(ScheduledWater, 2, repeated=True)


class UsageResponse(messages.Message):
    usage = messages.IntegerField(1, repeated=True)
    datapoint_num = messages.IntegerField(2)
    datapoint_freq = messages.EnumField()
    class Frequency(messages.Enum):
        DAY = 1
        WEEK = 2
        MONTH = 3

class SetupRequest(messages.Message):
    device_id = messages.StringField(1)
    lat = messages.FloatField(2)
    lng = messages.FloatField(3)


class Valve(messages.Message):
    number = messages.IntegerField(1)
    name = messages.StringField(2, required=False)
    device_id = messages.StringField(3)
    status = messages.EnumField(Status, 4)
    start_time = messages.IntegerField(5)
    duration_seconds = messages.IntegerField(6)
    crop_id = messages.IntegerField(7)


class ValveDataResponse(messages.Message):
    valves = messages.MessageField(Valve, 1, repeated=True)
    status = messages.EnumField(Status, 2)


class ScheduleAdd(messages.Message):
    device_id = messages.StringField(1)
    valve = messages.IntegerField(2)
    seconds_per_day = messages.IntegerField(3)
    crop_id = messages.IntegerField(4)
    start_time = messages.IntegerField(5)

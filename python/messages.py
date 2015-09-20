'''Endpoints messages.'''


from protorpc import messages

class ScheduleRequest(messages.Message):
    id = messages.stringField(1);

from json import JSONEncoder

from display_time import DisplayTime


class Show(object):
    def __init__(self, raw_data):
        self.number = raw_data['number']
        self.name = raw_data['name']
        self.duration = DisplayTime(raw_data['duration'])
        self.plan = DisplayTime(raw_data['plan'])


class ShowEncoder(JSONEncoder):
    def default(self, o):
        return {
            "number": o.number,
            "name": o.name,
            "duration": {
                "timeStr": o.duration._time_str,
                "totalSeconds": o.duration.total_seconds,
                "isNegative": o.duration.is_negative,
                "hour": o.duration.hour,
                "minute": o.duration.minute,
                "second": o.duration.second
            },
            "plan": {
                "timeStr": o.plan._time_str,
                "totalSeconds": o.plan.total_seconds,
                "isNegative": o.plan.is_negative,
                "hour": o.plan.hour,
                "minute": o.plan.minute,
                "second": o.plan.second
            }
        }

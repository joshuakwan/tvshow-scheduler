class DisplayTime(object):
    def __init__(self, time_str):
        hour, minute, second = time_str.split(':')
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)
        self._time_str = time_str

        if not hour.startswith('-'):
            self.is_negative = False
            self.total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        else:
            self.is_negative = True
            self.total_seconds = -(abs(self.hour) * 3600 + self.minute * 60 + self.second)

    def get_time_string(self):
        return self._time_str

    def __str__(self):
        return self._time_str

    @staticmethod
    def value_to_str(value):
        if value < 0:
            minus_flag = True
            value = abs(value)
        else:
            minus_flag = False

        hour = value / 3600
        minute = (value % 3600) / 60
        second = value - hour * 3600 - minute * 60

        time_str = '%s:%s:%s' % (str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2))

        if minus_flag:
            time_str = ''.join(['-', time_str])

        return time_str

    def __add__(self, other):
        return DisplayTime(DisplayTime.value_to_str(self.total_seconds + other.total_seconds))

    def __sub__(self, other):
        return DisplayTime(DisplayTime.value_to_str(self.total_seconds - other.total_seconds))

    def __lt__(self, other):
        return self.total_seconds < other.total_seconds

    def __le__(self, other):
        return self.total_seconds <= other.total_seconds

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __ne__(self, other):
        return self.total_seconds != other.total_seconds

    def __gt__(self, other):
        return self.total_seconds > other.total_seconds

    def __ge__(self, other):
        return self.total_seconds >= other.total_seconds

from display_time import DisplayTime


class Show(object):
    def __init__(self, raw_data):
        self.seq, self.name, duration, plan = raw_data
        self.duration = DisplayTime(duration)
        self.plan = DisplayTime(plan)



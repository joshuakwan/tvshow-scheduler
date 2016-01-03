from display_time import DisplayTime


class Show(object):
    def __init__(self, raw_data):
        self.seq = raw_data['seq']
        self.name = raw_data['name']
        self.duration = DisplayTime(raw_data['duration'])
        self.plan = DisplayTime(raw_data['plan'])

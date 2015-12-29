# -*- coding: utf-8 -*-
import datetime
from prettytable import PrettyTable


class Show(object):
    def __init__(self, raw_data):
        self.sequence, self.name, self.duration, self.planned_time = raw_data.split(',')

    def get_current_time(self):
        now = datetime.datetime.now()
        return '%s:%s:%s' % (str(now.hour).zfill(2), str(now.minute).zfill(2), str(now.second).zfill(2))

    def get_table_data(self):
        return [self.sequence, self.name, self.duration, self.planned_time, self.get_current_time(), 0, 0]


class Shows(object):
    def __init__(self, raw_data):
        self.table = PrettyTable(['序号', '名称', '时长', '既定时间', '实时时间', '时差', '备选建议'])
        self.table.padding_width = 1
        self.shows = []
        for line in raw_data:
            if line.startswith('seq,name,duration,plan'):
                continue
            self.shows.append(Show(line))

    def get_table(self):
        for show in self.shows:
            self.table.add_row(show.get_table_data())
        # import pdb
        # pdb.set_trace()
        return self.table


# if __name__ == '__main__':
#     d1 = DisplayTime('01:01:59')
#     d2 = DisplayTime('00:02:04')
#     d3 = d1 + d2
#     print d1._value, d2._value, d3._value
#     print d3
#     # shows = Shows(open('data', 'r'))
#     # print shows.get_table()
#     # html_str = shows.get_table().get_html_string()
#     # f = open('schedule.html', 'a')
#     # f.write(html_str)
#     # f.close()

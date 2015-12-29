from show import Show


class Shows(object):
    def __init__(self, data_entries):
        self._shows = dict()
        for entry in data_entries:
            show = Show(entry)
            self._shows[show.seq] = show

    def add_show(self, show):
        self._shows[show.seq] = show

    def delete_show(self, seq):
        return self._shows.pop(seq)

    def get_count(self):
        return len(self._shows)

    def get_recommendation(self, time_gate):
        '''

        :param time_gate:
        :return:
        '''
        valid_shows = dict()
        for show in self._shows.values():
            if show.plan <= time_gate:
                continue
            else:
                valid_shows[show.seq] = show

        recommendation = dict()

        # A recommendation is '1' => [['2'],['3','4']]
        for show in valid_shows.values():
            gap = show.plan - time_gate
            recommendation[show.seq] = []
            for show_other in valid_shows.values():
                if show_other.seq == show.seq:
                    continue
                if show_other.duration <= gap:
                    recommendation[show.seq].append([show_other.seq])

        return recommendation


if __name__ == '__main__':
    import csv
    from display_time import DisplayTime
    input_file = 'data.csv'
    test_data = []
    with open(input_file, 'r') as f:
        iter = csv.reader(f)
        next(iter)
        for entry in iter:
            test_data.append(entry)

    shows = Shows(test_data)
    print shows.get_recommendation(DisplayTime('20:00:01'))

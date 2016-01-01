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
                    # recommendation[show.seq].append([show_other.seq])
                    recommendation[show.seq].append(show_other.seq)

        return recommendation

    def get_shows_table(self, time_gate):
        recommendation = self.get_recommendation(time_gate)
        shows = []
        for show in self._shows.values():
            table_entry = dict()
            table_entry['seq'] = show.seq
            table_entry['name'] = show.name
            table_entry['duration'] = show.duration.get_time_string()
            table_entry['plan'] = show.plan.get_time_string()
            table_entry['current'] = time_gate.get_time_string()
            table_entry['gap'] = (show.plan - time_gate).get_time_string()
            table_entry['recommendation'] = [] if not recommendation.has_key(show.seq) else sorted(
                recommendation.get(show.seq))
            shows.append(table_entry)

        return sorted(shows, key=lambda k: k['seq'])


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
    print shows.get_shows_table(DisplayTime('20:03:01'))

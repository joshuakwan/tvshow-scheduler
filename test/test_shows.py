import unittest
from scheduler.shows import Shows
from scheduler.display_time import DisplayTime
import csv


class TestShows(unittest.TestCase):
    def setUp(self):
        self.input_file = 'data.csv'
        self.test_data = []
        with open(self.input_file, 'r') as f:
            iter = csv.reader(f)
            next(iter)
            for entry in iter:
                self.test_data.append(entry)

    def testInitialization(self):
        shows = Shows(self.test_data)
        self.assertEqual(shows.get_count(), len(self.test_data))
        print shows.get_recommendation(DisplayTime('20:00:01'))


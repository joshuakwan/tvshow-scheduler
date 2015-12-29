import unittest
from scheduler.show import Show


class TestShow(unittest.TestCase):
    def testInitialization(self):
        show = Show('1,show 1,00:03:00,20:00:00')
        self.assertEqual(show.seq, '1')
        self.assertEqual(show.name,'show 1')
        self.assertEqual(show.duration.get_time_string(),'00:03:00')
        self.assertEqual(show.plan.get_time_string(),'20:00:00')

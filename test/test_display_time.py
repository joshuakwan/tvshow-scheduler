import unittest
from scheduler.display_time import DisplayTime


class TestDisplayTime(unittest.TestCase):
    def test_positive_display_time(self):
        time_str = '01:23:45'
        time = DisplayTime(time_str)
        self.assertFalse(time.is_negative)
        self.assertEqual(1, time.hour)
        self.assertEqual(23, time.minute)
        self.assertEqual(45, time.second)
        self.assertEqual(5025, time.total_seconds)

    def test_negative_display_time(self):
        time_str = '-01:23:45'
        time = DisplayTime(time_str)
        self.assertTrue(time.is_negative)
        self.assertEqual(-1, time.hour)
        self.assertEqual(23, time.minute)
        self.assertEqual(45, time.second)
        self.assertEqual(-5025, time.total_seconds)

    def test_zero_display_time(self):
        time_str = '00:00:00'
        time = DisplayTime(time_str)
        self.assertFalse(time.is_negative)
        self.assertEqual(0, time.hour)
        self.assertEqual(0, time.minute)
        self.assertEqual(0, time.second)
        self.assertEqual(0, time.total_seconds)

    def test_add_ppp(self):
        time_1 = DisplayTime('00:01:23')
        time_2 = DisplayTime('01:45:56')
        time_3 = time_1 + time_2
        self.assertEqual('01:47:19', time_3.get_time_string())

    def test_add_pnp(self):
        time_1 = DisplayTime('01:45:56')
        time_2 = DisplayTime('-01:45:55')
        time_3 = time_1 + time_2
        self.assertEqual('00:00:01', time_3.get_time_string())

    def test_add_pnn(self):
        time_1 = DisplayTime('01:45:56')
        time_2 = DisplayTime('-02:00:00')
        time_3 = time_1 + time_2
        self.assertEqual('-00:14:04', time_3.get_time_string())

    def test_add_nnn(self):
        time_1 = DisplayTime('-01:45:56')
        time_2 = DisplayTime('-03:16:46')
        time_3 = time_1 + time_2
        self.assertEqual('-05:02:42', time_3.get_time_string())

    def test_add_zero(self):
        time_1 = DisplayTime('01:45:56')
        time_2 = DisplayTime('-01:45:56')
        time_3 = time_1 + time_2
        self.assertEqual('00:00:00', time_3.get_time_string())

    def test_sub_ppp(self):
        time_1 = DisplayTime('00:01:23')
        time_2 = DisplayTime('01:45:56')
        time_3 = time_2 - time_1
        self.assertEqual('01:44:33', time_3.get_time_string())

    def test_sub_ppn(self):
        time_1 = DisplayTime('00:01:23')
        time_2 = DisplayTime('01:45:56')
        time_3 = time_1 - time_2
        self.assertEqual('-01:44:33', time_3.get_time_string())

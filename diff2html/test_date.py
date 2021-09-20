
from datetime import datetime
from diff2html.date import get_first_day_of_month
import unittest

class TestDate(unittest.TestCase):
        def test_first_day(self):
                subject = get_first_day_of_month(datetime.strptime("2021-09-30", '%Y-%m-%d'))
                self.assertEqual(subject, "2021-09-31")
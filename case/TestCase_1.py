import unittest
from base.MySqlTools import SqlTools


class TestCase1(unittest.TestCase):
    st = SqlTools()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_run(self):
        sql = "select * from charge_station_info order by id desc limit 1"
        res = self.st.get_data(sql)
        return res

    def test_case(self):
        res = ''
        return res

    def test_case_1(self):
        a = 1
        self.assertEqual(a, 1)

    def test_case_2(self):
        a = 2
        self.assertEqual(a, 1)

import unittest
from api2018.Sendhttp import Sendhttp
from api2018 import Common
class addresslist_test(unittest.TestCase):
    def setUp(self):
        self.loginurl="/common/fgadmin/login"
        self.listurl="/fgadmin/address/list"

    def test_getListSuccess(self):
        user = {"phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"}
        login_result = Sendhttp().run_http(self.loginurl, "POST", user)
        cookies=Common.getcookies(user)
        data = {"message":"success","code":200}
        list_result1 = Sendhttp().sent_get_bycookies(self.listurl,cookies)
        print(list_result1)
        self.assertEqual(list_result1['code'], 200)


import unittest
from api2018.Sendhttp import Sendhttp
from api2018 import Common
class submit(unittest.TestCase):
    def setUp(self):
        self.loginurl="/common/fgadmin/login"

    # def test_loginSuccess1(self):
    #     user = {"phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"}
    #     login_result = Sendhttp().run_http(self.loginurl, "POST", user)
    #     print(login_result)
    #     self.assertEqual(login_result['code'], 200)
    def test_loginFail1(self):
        user1 = {"phoneArea": "a", "phoneNumber": "20000000000", "password": "netease123"}
        login_result1 = Sendhttp().run_http(self.loginurl, "POST", user1)
        print(login_result1)
        self.assertEqual(login_result1['code'], 200)
    def test_loginFail2(self):
        user2 = {"phoneArea": "86", "phoneNumber": "aaaaaaaaaaa", "password": "netease123"}
        login_result2 = Sendhttp().run_http(self.loginurl, "POST", user2)
        print(login_result2)
        self.assertEqual(login_result2['code'], 200)
    def test_loginFail3(self):
        user3 = {"phoneArea": "86", "phoneNumber": "20000000000", "password":"123456" }
        login_result3 = Sendhttp().run_http(self.loginurl, "POST", user3)
        print(login_result3)
        self.assertEqual(login_result3['code'], 200)
    def test_loginFail4(self):
        user4 = { "phoneNumber": "20000000000", "password": "netease123" }
        login_result4 = Sendhttp().run_http(self.loginurl, "POST", user4)
        print(login_result4)
        self.assertEqual(login_result4['code'], 200)
    def test_loginFail5(self):
        user5 = { "phoneArea": "86", "phoneNumber": "20000000000"}
        login_result5 = Sendhttp().run_http(self.loginurl, "POST", user5)
        print(login_result5)
        self.assertEqual(login_result5['code'], 200)
    def test_loginFail6(self):
        user6 = { "phoneArea": "86", "phoneNumber": "1233243243252252352523", "password": "netease123"}
        login_result6 = Sendhttp().run_http(self.loginurl, "POST", user6)
        print(login_result6)
        self.assertEqual(login_result6['code'], 200)
    def test_loginFail7(self):
        user7 = { "phoneArea": "86", "phoneNumber": "10086", "password": "netease123"}
        login_result7 = Sendhttp().run_http(self.loginurl, "POST", user7)
        print(login_result7)
        self.assertEqual(login_result7['code'], 200)
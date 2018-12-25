import unittest
from api2018.Sendhttp import Sendhttp
from api2018 import Common
class submit(unittest.TestCase):
    def setUp(self):
        self.loginurl="/common/fgadmin/login"
        self.submiturl="/fgadmin/orders/submit"
    def test_submitSuccess1(self):
        user={"phoneArea":"86","phoneNumber":"20000000000","password":"netease123"}
        login_result=Sendhttp().run_http(self.loginurl,"POST",user)
        cookies=Common.getcookies(user)
        data={
              "skuIds":"2,3",
              "skuNumbers":"1,1",
              "stockIds":"74966312,74966313",
              "receiverName":"张三",
              "cellPhone":"12615813537",
              "addressDetail":"1 栋 3 单元",
              "province":"浙江省",
              "city":"杭州市",
              "area":"滨江区",
              "voiceStatus":0,
              "needInvoice":0,
              "invoiceHead":"",
              "transportFee":0,
              "logisticsCompanyId":1,
              "accessSource":"noSource",
              "accessDevice":0
              }
        submit_result=Sendhttp().send_post_bycookies(self.submiturl,data,cookies)
        print(submit_result)
        self.assertEqual(submit_result['code'],200)
    def test_submitSuccess2(self):
        user1={"phoneArea":"86","phoneNumber":"20000000000","password":"netease123"}
        login_result1=Sendhttp().run_http(self.loginurl,"POST",user1)
        cookies = Common.getcookies(user1)
        data1={
              "skuIds":"2,3",
              "skuNumbers":"1,1",
              "stockIds":"74966312,74966313",
              "receiverName":"",
              "cellPhone":"",
              "addressDetail":"",
              "province":"",
              "city":"",
              "area":"",
              "voiceStatus":0,
              "needInvoice":0,
              "invoiceHead":"",
              "transportFee":0,
              "logisticsCompanyId":1,
              "accessSource":"noSource",
              "accessDevice":0
              }
        submit_result1 = Sendhttp().send_post_bycookies(self.submiturl, data1, cookies)
        print(submit_result1)
        self.assertEqual(submit_result1['code'],200)

    def test_submitFail1(self):
            user1 = {"phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"}
            login_result1 = Sendhttp().run_http(self.loginurl, "POST", user1)
            cookies = Common.getcookies(user1)
            data2 = {
              "skuIds":"a,b",
              "skuNumbers":"1,1",
              "stockIds":"74966312,74966313",
              "receiverName":"张三",
              "cellPhone":"12615813537",
              "addressDetail":"1 栋 3 单元",
              "province":"浙江省",
              "city":"杭州市",
              "area":"滨江区",
              "voiceStatus":0,
              "needInvoice":0,
              "invoiceHead":"",
              "transportFee":0,
              "logisticsCompanyId":1,
              "accessSource":"noSource",
              "accessDevice":0
            }
            submit_result2= Sendhttp().send_post_bycookies(self.submiturl, data2, cookies)
            print(submit_result2)
            self.assertEqual(submit_result2['code'], 200)

    def test_submitFail2(self):
                user1 = {"phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"}
                login_result1 = Sendhttp().run_http(self.loginurl, "POST", user1)
                cookies = Common.getcookies(user1)
                data3 = {
                    "skuIds": "",
                    "skuNumbers": "1,1",
                    "stockIds": "74966312,74966313",
                    "receiverName": "",
                    "cellPhone": "",
                    "addressDetail": "",
                    "province": "",
                    "city": "",
                    "area": "",
                    "voiceStatus": 0,
                    "needInvoice": 0,
                    "invoiceHead": "",
                    "transportFee": 0,
                    "logisticsCompanyId": 1,
                    "accessSource": "noSource",
                    "accessDevice": 0
                }
                submit_result3 = Sendhttp().send_post_bycookies(self.submiturl, data3, cookies)
                print(submit_result3)
                self.assertEqual(submit_result3['code'], 200)

    def test_submitFail3(self):
                user1 = {"phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"}
                login_result1 = Sendhttp().run_http(self.loginurl, "POST", user1)
                cookies = Common.getcookies(user1)
                data4 = {
                    "skuNumbers": "1,1",
                    "stockIds": "74966312,74966313",
                    "receiverName": "",
                    "cellPhone": "",
                    "addressDetail": "",
                    "province": "",
                    "city": "",
                    "area": "",
                    "voiceStatus": 0,
                    "needInvoice": 0,
                    "invoiceHead": "",
                    "transportFee": 0,
                    "logisticsCompanyId": 1,
                    "accessSource": "noSource",
                    "accessDevice": 0
                }
                submit_result4 = Sendhttp().send_post_bycookies(self.submiturl, data4, cookies)
                print(submit_result4)
                self.assertEqual(submit_result4['code'], 200)

    def test_submitFail4(self):
            user1 = {"phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"}
            login_result1 = Sendhttp().run_http(self.loginurl, "POST", user1)
            cookies = Common.getcookies(user1)
            data5 = {
                "skuIds": "2,3",
                "skuNumbers": "a,b",
                "stockIds": "74966312,74966313",
                "receiverName": "",
                "cellPhone": "",
                "addressDetail": "",
                "province": "",
                "city": "",
                "area": "",
                "voiceStatus": 0,
                "needInvoice": 0,
                "invoiceHead": "",
                "transportFee": 0,
                "logisticsCompanyId": 1,
                "accessSource": "noSource",
                "accessDevice": 0
            }
            submit_result5 = Sendhttp().send_post_bycookies(self.submiturl, data5, cookies)
            print(submit_result5)
            self.assertEqual(submit_result5['code'], 200)
    def test_submitFail5(self):
            user1 = {"phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"}
            login_result1 = Sendhttp().run_http(self.loginurl, "POST", user1)
            cookies = Common.getcookies(user1)
            data6 = {
                "skuIds": "2,3",
                "skuNumbers": "",
                "stockIds": "74966312,74966313",
                "receiverName": "",
                "cellPhone": "",
                "addressDetail": "",
                "province": "",
                "city": "",
                "area": "",
                "voiceStatus": 0,
                "needInvoice": 0,
                "invoiceHead": "",
                "transportFee": 0,
                "logisticsCompanyId": 1,
                "accessSource": "noSource",
                "accessDevice": 0
            }
            submit_result6 = Sendhttp().send_post_bycookies(self.submiturl, data6, cookies)
            print(submit_result6)
            self.assertEqual(submit_result6['code'], 200)
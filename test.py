import requests
import unittest

os.environ["ACCOUNT_I"] = "TEST-9RZ-86Z-K65Z"
os.environ["ACCOUNT_PASSCODE"] = "QOK-KID-GEKL"


class PushTestCase(unittest.TestCase):
   def test_push_request(self):
       data = {
            "event":"1Demo Even211" ,
            "identity":"1demo211", 
            "properties":{"1demo211": "1event211"}
        }
       url="/push"
       response = requests.post(url=url,json=data)
       self.assertEqual(response.status_code, 202)

   def test_push_fail_request(self):
       data = {
            "event":"Demo Even18" ,
            "identity":"", 
            "properties":{"demo18": "event18"}
        }
       url="/push"
       response = requests.post(url=url,json=data)
       self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()

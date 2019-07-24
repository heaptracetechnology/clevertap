import requests
import unittest
import os

class PushTestCase(unittest.TestCase):
   def test_push_request(self):
       data = {
            "event":"1Demo Even211" ,
            "identity":"1demo211", 
            "properties":{"1demo211": "1event211"}
        }
       url="http://localhost:8000/push"
       response = requests.post(url=url,json=data)
       self.assertEqual(response.status_code, 202)

   def test_push_fail_request(self):
       data = {
            "event":"Demo Even18" ,
            "identity":"", 
            "properties":{"demo18": "event18"}
        }
       url="http://localhost:8000/push"
       response = requests.post(url=url,json=data)
       self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

from django.test import TestCase
from hello.models import msgserver
# Create your tests here.
class PlayerTestCase(TestCase):
    def test_create(self):
        print("----------------TEST CREATE DATA-----------------")
        response = self.client.post("/hello/create/", {'Key': 12345678, 'Message':'Hello'})
        p = msgserver.objects.get(Key=12345678)
        self.assertEqual(p.Key, 12345678)
        self.assertEqual(p.Message, 'Hello')
        print(">PASS")

    def test_create_update(self):
        print("----------------TEST DUPLICATED KEY-----------------")
        response = self.client.post("/hello/create/", {'Key': 12345678, 'Message':'Hello'})
        response = self.client.post("/hello/create/", {'Key': 12345678, 'Message':'New Hello'})
        self.assertIn(b'Msgserver with this Key already exists.', response._container[0])
        print(">PASS")
    
    def test_key_message_enforced(self):
        print("----------------TEST CONSTRAINT-----------------")
        response = self.client.post("/hello/create/", {'Key': 123456789, 'Message':'Hello'})
        self.assertIn(b'The key must be 8 number', response._container[0])
        print(">PASS")

        response = self.client.post("/hello/create/", {'Key': 12345678, 'Message':' '})
        self.assertIn(b'This field is required', response._container[0])
        print(">PASS")
        
        putMsg = ''
        for i in range(168):
            putMsg = putMsg + str(i % 10)
        response = self.client.post("/hello/create/", {'Key': 12345677, 'Message':putMsg})
        self.assertIn(b'Ensure this value has at most 165 characters (it has 168)', response._container[0])
        print(">PASS")

    def test_update(self):
        print("----------------TEST UPDATE DATA-----------------")
        response = self.client.post("/hello/create/", {'Key': 12345678, 'Message':'Hello'})
        response = self.client.post("/hello/update/12345678", {'Message':'New Hello'})
        p = msgserver.objects.get(Key=12345678)
        self.assertEqual(p.Key, 12345678)
        self.assertEqual(p.Message, 'New Hello')
        print(">PASS")
    
    def test_json_format(self):
        print("----------------TEST JSON FORMAT-----------------")
        response = self.client.post("/hello/create/", {'Key': 12345678, 'Message':'Hello'})
        response = self.client.post("/hello/create/", {'Key': 12345679, 'Message':'Hello'})
        response = self.client.get("/hello/")
        self.assertIn(b'[{"Key": 12345678, "Message": "Hello"}, {"Key": 12345679, "Message": "Hello"}]', response._container[0])
        print(">PASS")


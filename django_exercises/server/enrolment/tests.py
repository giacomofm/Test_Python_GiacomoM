from django.test import TestCase
import json

class School_Day_Test(TestCase):

    def test_insert(self):
        resp = self.client.post(
            "/school_day",
            '{"first_name":"Giacomo","last_name":"Maniero"}',
            content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_find(self):
        resp = self.client.post(
            "/school_day",
            '{"first_name":"Giacomo","last_name":"Maniero"}',
            content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/school_day')
        self.assertEqual(resp.status_code,200)
        content = json.loads(resp.content)
        self.assertEqual(content[0]['first_name'], 'Giacomo')
        self.assertEqual(content[0]['last_name'], 'Maniero')
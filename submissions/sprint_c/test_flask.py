from flask_testing import TestCase
from sprint_c.app import app


class TestFlask(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.paths = ['/', '/2', '/random', '/vocabulary']

    def test_all_route_connections(self):
        """Tests each of the routes connection successful """
        for path in self.paths:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)

    def test_all_endpoints_json(self):
        """Test if responses are json, and json obj are dicts """
        for path in self.paths:
            response = self.client.get(path)
            self.assertTrue(response.is_json)
            self.assertEquals(type(response.json), dict)

    def test_single_epithet(self):
        """Test what a single epithet is, index, assigned quantity and
        and random quantity all use this method"""
        response = self.client.get('/')
        self.assertEquals(len(response.json.keys()), 1)
        self.assertNotEquals(len(response.json.keys()), 2)
        self.assertEquals(len(response.json['1']), 3)
        self.assertEquals(type(response.json['1']), list)
        for epiteth in response.json['1']:
            self.assertEquals(type(epiteth), str)

    def test_assigned_quantity(self):
        """Checks assigned quantity response lengths match"""
        response = self.client.get('/3')
        response2 = self.client.get('/25')
        self.assertEquals(len(response.json.keys()), 3)
        self.assertEquals(len(response2.json.keys()), 25)

    def test_random_quantity(self):
        """Random quantity designed to give up to 1-10 responses,
        run 20 times to assure success"""
        response = self.client.get('/random')
        for _ in range(20):
            self.assertLess(len(response.json.keys()), 11)
            self.assertGreater(len(response.json.keys()), -1)

    def test_vocabulary(self):
        """Looks at vocabulary, assures columns 3"""
        response = self.client.get('/vocabulary')
        self.assertEquals(len(response.json.keys()), 3)
        self.assertEquals(type(response.json['Column 1']), list)
        for epithet in response.json['Column 1']:
            self.assertEquals(type(epithet), str)

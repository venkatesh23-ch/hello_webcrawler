import os
import unittest
import tempfile
import hello


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, hello.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = hello.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(hello.app.config['DATABASE'])

    def test_welcome_response(self):
        rv = self.app.get('/')
        #assert 'Welcome!' in rv.data
        
    def test_hello_world_response(self):
        rv = self.app.get('/hello')
        assert 'Hello World!' in rv.data
    
    def test_crawl(self):
        self.app.get('/crawl')
#         assert 'Success' in
if __name__ == '__main__':
    unittest.main()

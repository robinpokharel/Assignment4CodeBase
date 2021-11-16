import pytest

from app import app

class TestApp():

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        assert(response.status_code  == 200)
        assert(response.data  == b'Default Home Page')  


   

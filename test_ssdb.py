import pprint
import unittest
import uuid
import ssdb
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.client = ssdb.SSDB(host="192.168.1.105")
        self.client.execute_command("auth", "1" * 32)

    def put_bulk(self, size):
        keys = {str(uuid.uuid4()): i for i in xrange(size)}
        st = time.time()
        self.client.mset(**keys)
        print time.time() - st

    def test_something(self):
        self.put_bulk(1000000)
        pprint.pprint(self.client.execute_command("info"))

if __name__ == '__main__':
    unittest.main()

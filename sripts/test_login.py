import random

import pytest
class TestLogin():
    # def setup(self):
    #     print("setup")
    # def teardown(self):
    #     print("teardown")
    def test_login1(self):
        print("1")
        num = random.randint(3)
        if num ==2:
            assert True
    def test_login2(self):
        print("2")
        assert False
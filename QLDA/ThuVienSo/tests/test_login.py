import unittest

from QLDA.ThuVienSo.dao import auth_login


class TestLogin(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(auth_login("user1", 123))

    def test_case_2(self):
        self.assertFalse(auth_login("user1",123121))



if __name__ == "__main__":
    unittest.main()
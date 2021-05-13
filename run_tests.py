import unittest
import sys

from tests.login_tests import TestLogin
from tests.search_tests import TestSearch
from tests.album_tests import TestAlbum
from tests.favorite_test import TestFavorite
from tests.signup_tests import TestSignup
from tests.subscribes_tests import TestSubscribes

if __name__ == '__main__':
    test_suites = unittest.TestSuite((
        unittest.makeSuite(TestSignup),
        unittest.makeSuite(TestLogin),
        unittest.makeSuite(TestSearch),
        unittest.makeSuite(TestAlbum),
        unittest.makeSuite(TestFavorite),
        unittest.makeSuite(TestSubscribes),
    ))
    result = unittest.TextTestRunner().run(test_suites)

    sys.exit(not result.wasSuccessful())

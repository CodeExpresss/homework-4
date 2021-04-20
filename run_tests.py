import unittest
import sys
from tests.search_tests import TestSearch
from tests.album_tests import TestAlbum
from tests.favorite_test import TestFavorite

if __name__ == '__main__':
    test_suites = unittest.TestSuite((
        unittest.makeSuite(TestSearch),
        unittest.makeSuite(TestAlbum),
        unittest.makeSuite(TestFavorite),
    ))
    result = unittest.TextTestRunner().run(test_suites)

    sys.exit(not result.wasSuccessful())


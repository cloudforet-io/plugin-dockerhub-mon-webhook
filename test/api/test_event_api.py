import logging
import unittest
import os
import json
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json
from pprint import pprint

_LOGGER = logging.getLogger(__name__)


class TestEvent(TestCase):
    def test_parse(self):
        param = {
            "options": {

            },
            "data": {

            }
        }

        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param.get('data')})
        print_json(parsed_data)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)

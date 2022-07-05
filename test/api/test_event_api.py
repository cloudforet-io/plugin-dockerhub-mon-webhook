import logging
import unittest

from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json

_LOGGER = logging.getLogger(__name__)


class TestEvent(TestCase):
    def test_parse(self):
        param = {
            "options": {
            },
            "data": {
              "callback_url": "https://registry.hub.docker.com/u/nigasa12/prs-manager/hook/20a4ccf24e26442fbed482baa234c373/",
              "push_data": {
                "pusher": "spaceoneadmin",
                "pushed_at": 1656906946,
                "tag": "v1.0.0",
                "images": [],
                "media_type": "application/vnd.docker.distribution.manifest.v2+json"
              },
              "repository": {
                "status": "Active",
                "namespace": "spaceone",
                "name": "plugin-dockerhub-mon-webhook",
                "repo_name": "spaceone/plugin-dockerhub-mon-webhook",
                "repo_url": "https://hub.docker.com/r/spaceone/plugin-dockerhub-mon-webhook",
                "description": "",
                "full_description": None,
                "star_count": 0,
                "comment_count": 0,
                "is_private": False,
                "is_trusted": False,
                "is_official": False,
                "owner": "spaceoneadmin",
                "date_created": 1656296314
              }
            }
        }

        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param.get('data')})
        print_json(parsed_data)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)

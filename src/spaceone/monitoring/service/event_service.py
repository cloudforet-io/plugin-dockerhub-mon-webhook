import logging
import requests
import json
from spaceone.core.service import *

from spaceone.monitoring.error.event import ERROR_PARSE_EVENT, ERROR_NOT_DECISION_MANAGER

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@event_handler
class EventService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @transaction
    @check_required(['options', 'data'])
    def parse(self, params):
        """

        Args:
            params (dict): {
                'options': 'dict',
                'raw_data': 'dict'
            }

        Returns:
            plugin_metric_data_response (dict)

        """

        options = params.get('options')
        raw_data = params.get('data')

        # TODO
        _LOGGER.debug(raw_data)
        return raw_data
import logging
from spaceone.core.service import *
from spaceone.monitoring.manager.event_manager import EventManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@event_handler
class EventService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event_manager = EventManager()

    @transaction
    @check_required(['options', 'data'])
    def parse(self, params: dict):
        """

        Args:
            params (dict): {
                'options': 'dict',
                'data': 'dict',
            }

        Returns:
            plugin_metric_data_response (dict)

        """
        options = params.get('options')
        data = params.get('data')
        return self.event_manager.parse(options, data)

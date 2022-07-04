from schematics import Model
from schematics.types import StringType, DateTimeType, DictType

__all__ = ['EventModel']


class EventModel(Model):
    event_key = StringType(required=True)
    event_type = StringType(choices=['RECOVERY', 'ALERT'], default='ALERT')
    title = StringType(required=True)
    description = StringType(default='')
    severity = StringType(choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'NOT_AVAILABLE'], default=None)
    rule = StringType(default='')
    resource = DictType(StringType, default={})
    additional_info = DictType(StringType, default={})
    occurred_at = DateTimeType()

from schematics import Model
from schematics.types import StringType, ModelType, DateTimeType, DictType

__all__ = ['EventModel']


class DockerhubAdditionalInfo(Model):
    version = StringType()
    repository = StringType()


class EventModel(Model):
    event_key = StringType(required=True)
    event_type = StringType(choices=['RECOVERY', 'ALERT'], default='ALERT')
    title = StringType(required=True)
    description = StringType(default='')
    severity = StringType(choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'NOT_AVAILABLE'], default=None)
    resource = DictType(StringType, default={})
    rule = StringType(default='')
    occurred_at = DateTimeType()
    provider = StringType(default='aws')
    account = StringType(default='')
    additional_info = ModelType(DockerhubAdditionalInfo)

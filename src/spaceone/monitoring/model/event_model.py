from schematics import Model
from schematics.types import StringType, DateTimeType, ModelType

__all__ = ['EventModel']


class ResourceModel(Model):
    name = StringType(serialize_when_none=False)


class AdditionalInfoModel(Model):
    repo_url = StringType(serialize_when_none=False)
    repo_name = StringType(serialize_when_none=False)
    namespace = StringType(serialize_when_none=False)
    tag = StringType(serialize_when_none=False)
    pusher = StringType(serialize_when_none=False)


class EventModel(Model):
    event_key = StringType(required=True)
    event_type = StringType(choices=['RECOVERY', 'ALERT'], default='ALERT')
    title = StringType(required=True)
    description = StringType(default='')
    severity = StringType(choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'NOT_AVAILABLE'], default=None)
    rule = StringType(default='')
    resource = ModelType(ResourceModel)
    additional_info = ModelType(AdditionalInfoModel)
    occurred_at = DateTimeType() # pushed_at from docker

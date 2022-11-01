from json import JSONEncoder
from uuid import UUID

old_default_json_encoder = JSONEncoder.default


def new_default_json_encoder(self, obj):
    """UUID serialization fix"""

    if isinstance(obj, UUID):
        return str(obj)

    return old_default_json_encoder(self, obj)


JSONEncoder.default = new_default_json_encoder

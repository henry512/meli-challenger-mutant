import json


class CacheJsonSerde(object):
    def serialize(self, key, value):
        if type(value) == str:
            return value, 1
        return json.dumps(value).encode('utf-8'), 2

    def deserialize(self, key, value, flags):
        if flags == 1:
            return value
        if flags == 2:
            return json.loads(value.decode('utf-8'))
        raise Exception("Unknown serialization format")

import json


class JsonToObject(object):
    def __init__(self, json_str):
        self.__dict__ = json.loads(json_str)


class DictToObject(object):
    def __init__(self, dic):
        self.__dict__ = dic


def object_to_json(o):
    return o.__dict__

import util
import json


def handle_get_with_param(response_pb_class, response_mapper):
    def handle_protocol(func):
        def wrap(*args, **kwargs):
            class_obj = args[0]
            request_obj = args[1]
            response_obj = args[2]

            if request_obj.content_type == "application/json":
                request_obj.decoded_body = util.DictToObject(request_obj.params)
                result = func(*args, **kwargs)
                response_obj.body = json.dumps(response_obj.body, default=util.object_to_json)
            elif request_obj.content_type == "application/x-protobuf":
                request_obj.decoded_body = util.DictToObject(request_obj.params)
                result = func(*args, **kwargs)
                proto_response_obj = response_pb_class
                if response_mapper is not None and response_pb_class is not None:
                    class_obj.response_mapper(proto_response_obj,
                                              response_obj.body)
                    response_obj.body = proto_response_obj.SerializeToString()
            else:
                raise Exception("Not supported content type")
            return result

        return wrap

    return handle_protocol


def handle_post_with_param(request_pb_class, response_pb_class, response_mapper):
    def handle_protocol(func):
        def wrap(*args, **kwargs):
            class_obj = args[0]
            request_obj = args[1]
            response_obj = args[2]

            if request_obj.content_type == "application/json":
                request_obj.decoded_body = util.JsonToObject(request_obj.stream.read().decode('utf-8'))
                result = func(*args, **kwargs)
                response_obj.body = json.dumps(response_obj.body, default=util.object_to_json)
            elif request_obj.content_type == "application/x-protobuf":
                if request_pb_class is not None:
                    proto_obj = request_pb_class
                    proto_obj.ParseFromString(request_obj.stream.read())
                    request_obj.decoded_body = proto_obj
                result = func(*args, **kwargs)
                proto_response_obj = response_pb_class
                if response_mapper is not None and response_pb_class is not None:
                    class_obj.response_mapper(proto_response_obj,
                                              response_obj.body)
                    response_obj.body = proto_response_obj.SerializeToString()
            else:
                raise Exception("Not supported content type")
            return result

        return wrap

    return handle_protocol

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account_login.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='account_login.proto',
  package='account_login_request',
  syntax='proto2',
  serialized_pb=_b('\n\x13\x61\x63\x63ount_login.proto\x12\x15\x61\x63\x63ount_login_request\"5\n\x13\x41\x63\x63ountLoginRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\"X\n\x14\x41\x63\x63ountLoginResponse\x12\x31\n\x04\x63ode\x18\x01 \x02(\x0e\x32#.account_login_request.ResponseCode\x12\r\n\x05token\x18\x02 \x01(\t*P\n\x0cResponseCode\x12\x06\n\x02OK\x10\x00\x12\x14\n\x10INVALID_ARGUMENT\x10\x01\x12\x0f\n\x0b\x41UTH_FAILED\x10\x02\x12\x11\n\rUNKNOWN_ERROR\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_RESPONSECODE = _descriptor.EnumDescriptor(
  name='ResponseCode',
  full_name='account_login_request.ResponseCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ARGUMENT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_FAILED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=191,
  serialized_end=271,
)
_sym_db.RegisterEnumDescriptor(_RESPONSECODE)

ResponseCode = enum_type_wrapper.EnumTypeWrapper(_RESPONSECODE)
OK = 0
INVALID_ARGUMENT = 1
AUTH_FAILED = 2
UNKNOWN_ERROR = 3



_ACCOUNTLOGINREQUEST = _descriptor.Descriptor(
  name='AccountLoginRequest',
  full_name='account_login_request.AccountLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='account_login_request.AccountLoginRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='account_login_request.AccountLoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=99,
)


_ACCOUNTLOGINRESPONSE = _descriptor.Descriptor(
  name='AccountLoginResponse',
  full_name='account_login_request.AccountLoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='account_login_request.AccountLoginResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='account_login_request.AccountLoginResponse.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=189,
)

_ACCOUNTLOGINRESPONSE.fields_by_name['code'].enum_type = _RESPONSECODE
DESCRIPTOR.message_types_by_name['AccountLoginRequest'] = _ACCOUNTLOGINREQUEST
DESCRIPTOR.message_types_by_name['AccountLoginResponse'] = _ACCOUNTLOGINRESPONSE
DESCRIPTOR.enum_types_by_name['ResponseCode'] = _RESPONSECODE

AccountLoginRequest = _reflection.GeneratedProtocolMessageType('AccountLoginRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTLOGINREQUEST,
  __module__ = 'account_login_pb2'
  # @@protoc_insertion_point(class_scope:account_login_request.AccountLoginRequest)
  ))
_sym_db.RegisterMessage(AccountLoginRequest)

AccountLoginResponse = _reflection.GeneratedProtocolMessageType('AccountLoginResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTLOGINRESPONSE,
  __module__ = 'account_login_pb2'
  # @@protoc_insertion_point(class_scope:account_login_request.AccountLoginResponse)
  ))
_sym_db.RegisterMessage(AccountLoginResponse)


# @@protoc_insertion_point(module_scope)

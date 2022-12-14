# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/http/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy/http/config.proto',
  package='v2ray.core.proxy.http',
  syntax='proto3',
  serialized_options=b'\n\031com.v2ray.core.proxy.httpP\001Z\031v2ray.com/core/proxy/http\252\002\025V2Ray.Core.Proxy.Http',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17proxy/http/config.proto\x12\x15v2ray.core.proxy.http\x1a!common/protocol/server_spec.proto\"-\n\x07\x41\x63\x63ount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\xc8\x01\n\x0cServerConfig\x12\x13\n\x07timeout\x18\x01 \x01(\rB\x02\x18\x01\x12\x43\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32\x31.v2ray.core.proxy.http.ServerConfig.AccountsEntry\x12\x19\n\x11\x61llow_transparent\x18\x03 \x01(\x08\x12\x12\n\nuser_level\x18\x04 \x01(\r\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"J\n\x0c\x43lientConfig\x12:\n\x06server\x18\x01 \x03(\x0b\x32*.v2ray.core.common.protocol.ServerEndpointBP\n\x19\x63om.v2ray.core.proxy.httpP\x01Z\x19v2ray.com/core/proxy/http\xaa\x02\x15V2Ray.Core.Proxy.Httpb\x06proto3'
  ,
  dependencies=[common_dot_protocol_dot_server__spec__pb2.DESCRIPTOR,])




_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='v2ray.core.proxy.http.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='v2ray.core.proxy.http.Account.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='v2ray.core.proxy.http.Account.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=130,
)


_SERVERCONFIG_ACCOUNTSENTRY = _descriptor.Descriptor(
  name='AccountsEntry',
  full_name='v2ray.core.proxy.http.ServerConfig.AccountsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v2ray.core.proxy.http.ServerConfig.AccountsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.proxy.http.ServerConfig.AccountsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=333,
)

_SERVERCONFIG = _descriptor.Descriptor(
  name='ServerConfig',
  full_name='v2ray.core.proxy.http.ServerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='v2ray.core.proxy.http.ServerConfig.timeout', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accounts', full_name='v2ray.core.proxy.http.ServerConfig.accounts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_transparent', full_name='v2ray.core.proxy.http.ServerConfig.allow_transparent', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_level', full_name='v2ray.core.proxy.http.ServerConfig.user_level', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SERVERCONFIG_ACCOUNTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=333,
)


_CLIENTCONFIG = _descriptor.Descriptor(
  name='ClientConfig',
  full_name='v2ray.core.proxy.http.ClientConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='v2ray.core.proxy.http.ClientConfig.server', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=409,
)

_SERVERCONFIG_ACCOUNTSENTRY.containing_type = _SERVERCONFIG
_SERVERCONFIG.fields_by_name['accounts'].message_type = _SERVERCONFIG_ACCOUNTSENTRY
_CLIENTCONFIG.fields_by_name['server'].message_type = common_dot_protocol_dot_server__spec__pb2._SERVERENDPOINT
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['ServerConfig'] = _SERVERCONFIG
DESCRIPTOR.message_types_by_name['ClientConfig'] = _CLIENTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'proxy.http.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.http.Account)
  })
_sym_db.RegisterMessage(Account)

ServerConfig = _reflection.GeneratedProtocolMessageType('ServerConfig', (_message.Message,), {

  'AccountsEntry' : _reflection.GeneratedProtocolMessageType('AccountsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVERCONFIG_ACCOUNTSENTRY,
    '__module__' : 'proxy.http.config_pb2'
    # @@protoc_insertion_point(class_scope:v2ray.core.proxy.http.ServerConfig.AccountsEntry)
    })
  ,
  'DESCRIPTOR' : _SERVERCONFIG,
  '__module__' : 'proxy.http.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.http.ServerConfig)
  })
_sym_db.RegisterMessage(ServerConfig)
_sym_db.RegisterMessage(ServerConfig.AccountsEntry)

ClientConfig = _reflection.GeneratedProtocolMessageType('ClientConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTCONFIG,
  '__module__' : 'proxy.http.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.http.ClientConfig)
  })
_sym_db.RegisterMessage(ClientConfig)


DESCRIPTOR._options = None
_SERVERCONFIG_ACCOUNTSENTRY._options = None
_SERVERCONFIG.fields_by_name['timeout']._options = None
# @@protoc_insertion_point(module_scope)

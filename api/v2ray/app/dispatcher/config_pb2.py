# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/dispatcher/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/dispatcher/config.proto',
  package='v2ray.core.app.dispatcher',
  syntax='proto3',
  serialized_options=b'\n\035com.v2ray.core.app.dispatcherP\001Z\035v2ray.com/core/app/dispatcher\252\002\031V2Ray.Core.App.Dispatcher',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x61pp/dispatcher/config.proto\x12\x19v2ray.core.app.dispatcher\"\x15\n\rSessionConfigJ\x04\x08\x01\x10\x02\"D\n\x06\x43onfig\x12:\n\x08settings\x18\x01 \x01(\x0b\x32(.v2ray.core.app.dispatcher.SessionConfigB\\\n\x1d\x63om.v2ray.core.app.dispatcherP\x01Z\x1dv2ray.com/core/app/dispatcher\xaa\x02\x19V2Ray.Core.App.Dispatcherb\x06proto3'
)




_SESSIONCONFIG = _descriptor.Descriptor(
  name='SessionConfig',
  full_name='v2ray.core.app.dispatcher.SessionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=58,
  serialized_end=79,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.app.dispatcher.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='v2ray.core.app.dispatcher.Config.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=81,
  serialized_end=149,
)

_CONFIG.fields_by_name['settings'].message_type = _SESSIONCONFIG
DESCRIPTOR.message_types_by_name['SessionConfig'] = _SESSIONCONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionConfig = _reflection.GeneratedProtocolMessageType('SessionConfig', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONCONFIG,
  '__module__' : 'app.dispatcher.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.dispatcher.SessionConfig)
  })
_sym_db.RegisterMessage(SessionConfig)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'app.dispatcher.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.dispatcher.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

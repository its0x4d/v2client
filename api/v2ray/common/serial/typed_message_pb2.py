# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/serial/typed_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/serial/typed_message.proto',
  package='v2ray.core.common.serial',
  syntax='proto3',
  serialized_options=b'\n\034com.v2ray.core.common.serialP\001Z\034v2ray.com/core/common/serial\252\002\030V2Ray.Core.Common.Serial',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!common/serial/typed_message.proto\x12\x18v2ray.core.common.serial\"+\n\x0cTypedMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x42Y\n\x1c\x63om.v2ray.core.common.serialP\x01Z\x1cv2ray.com/core/common/serial\xaa\x02\x18V2Ray.Core.Common.Serialb\x06proto3'
)




_TYPEDMESSAGE = _descriptor.Descriptor(
  name='TypedMessage',
  full_name='v2ray.core.common.serial.TypedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='v2ray.core.common.serial.TypedMessage.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.common.serial.TypedMessage.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=63,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['TypedMessage'] = _TYPEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TypedMessage = _reflection.GeneratedProtocolMessageType('TypedMessage', (_message.Message,), {
  'DESCRIPTOR' : _TYPEDMESSAGE,
  '__module__' : 'common.serial.typed_message_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.common.serial.TypedMessage)
  })
_sym_db.RegisterMessage(TypedMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

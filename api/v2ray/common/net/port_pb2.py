# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/net/port.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/net/port.proto',
  package='v2ray.core.common.net',
  syntax='proto3',
  serialized_options=b'\n\031com.v2ray.core.common.netP\001Z\031v2ray.com/core/common/net\252\002\025V2Ray.Core.Common.Net',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x63ommon/net/port.proto\x12\x15v2ray.core.common.net\"%\n\tPortRange\x12\x0c\n\x04\x46rom\x18\x01 \x01(\r\x12\n\n\x02To\x18\x02 \x01(\r\";\n\x08PortList\x12/\n\x05range\x18\x01 \x03(\x0b\x32 .v2ray.core.common.net.PortRangeBP\n\x19\x63om.v2ray.core.common.netP\x01Z\x19v2ray.com/core/common/net\xaa\x02\x15V2Ray.Core.Common.Netb\x06proto3'
)




_PORTRANGE = _descriptor.Descriptor(
  name='PortRange',
  full_name='v2ray.core.common.net.PortRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='From', full_name='v2ray.core.common.net.PortRange.From', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='To', full_name='v2ray.core.common.net.PortRange.To', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=48,
  serialized_end=85,
)


_PORTLIST = _descriptor.Descriptor(
  name='PortList',
  full_name='v2ray.core.common.net.PortList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='v2ray.core.common.net.PortList.range', index=0,
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
  serialized_start=87,
  serialized_end=146,
)

_PORTLIST.fields_by_name['range'].message_type = _PORTRANGE
DESCRIPTOR.message_types_by_name['PortRange'] = _PORTRANGE
DESCRIPTOR.message_types_by_name['PortList'] = _PORTLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PortRange = _reflection.GeneratedProtocolMessageType('PortRange', (_message.Message,), {
  'DESCRIPTOR' : _PORTRANGE,
  '__module__' : 'common.net.port_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.common.net.PortRange)
  })
_sym_db.RegisterMessage(PortRange)

PortList = _reflection.GeneratedProtocolMessageType('PortList', (_message.Message,), {
  'DESCRIPTOR' : _PORTLIST,
  '__module__' : 'common.net.port_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.common.net.PortList)
  })
_sym_db.RegisterMessage(PortList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

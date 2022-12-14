# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/net/address.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/net/address.proto',
  package='v2ray.core.common.net',
  syntax='proto3',
  serialized_options=b'\n\031com.v2ray.core.common.netP\001Z\031v2ray.com/core/common/net\252\002\025V2Ray.Core.Common.Net',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x63ommon/net/address.proto\x12\x15v2ray.core.common.net\"7\n\nIPOrDomain\x12\x0c\n\x02ip\x18\x01 \x01(\x0cH\x00\x12\x10\n\x06\x64omain\x18\x02 \x01(\tH\x00\x42\t\n\x07\x61\x64\x64ressBP\n\x19\x63om.v2ray.core.common.netP\x01Z\x19v2ray.com/core/common/net\xaa\x02\x15V2Ray.Core.Common.Netb\x06proto3'
)




_IPORDOMAIN = _descriptor.Descriptor(
  name='IPOrDomain',
  full_name='v2ray.core.common.net.IPOrDomain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='v2ray.core.common.net.IPOrDomain.ip', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='v2ray.core.common.net.IPOrDomain.domain', index=1,
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
    _descriptor.OneofDescriptor(
      name='address', full_name='v2ray.core.common.net.IPOrDomain.address',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=51,
  serialized_end=106,
)

_IPORDOMAIN.oneofs_by_name['address'].fields.append(
  _IPORDOMAIN.fields_by_name['ip'])
_IPORDOMAIN.fields_by_name['ip'].containing_oneof = _IPORDOMAIN.oneofs_by_name['address']
_IPORDOMAIN.oneofs_by_name['address'].fields.append(
  _IPORDOMAIN.fields_by_name['domain'])
_IPORDOMAIN.fields_by_name['domain'].containing_oneof = _IPORDOMAIN.oneofs_by_name['address']
DESCRIPTOR.message_types_by_name['IPOrDomain'] = _IPORDOMAIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IPOrDomain = _reflection.GeneratedProtocolMessageType('IPOrDomain', (_message.Message,), {
  'DESCRIPTOR' : _IPORDOMAIN,
  '__module__' : 'common.net.address_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.common.net.IPOrDomain)
  })
_sym_db.RegisterMessage(IPOrDomain)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smpccs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='smpccs.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0csmpccs.proto\"\x14\n\x04Ping\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x14\n\x04Pong\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x88\x01\n\x08\x46smState\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0ctime_created\x18\x03 \x01(\r\x12\x14\n\x0ctime_updated\x18\x04 \x01(\r\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x0f\n\x07\x63hanged\x18\x06 \x01(\x08\x12\x13\n\x0bquarantaine\x18\n \x01(\x08\x32S\n\rSmpFsmControl\x12\x1a\n\x08PingPong\x12\x05.Ping\x1a\x05.Pong\"\x00\x12&\n\nControlFsm\x12\t.FsmState\x1a\t.FsmState\"\x00\x30\x01\x62\x06proto3')
)




_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Ping.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=16,
  serialized_end=36,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='Pong.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=38,
  serialized_end=58,
)


_FSMSTATE = _descriptor.Descriptor(
  name='FsmState',
  full_name='FsmState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='FsmState.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='FsmState.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_created', full_name='FsmState.time_created', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_updated', full_name='FsmState.time_updated', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='FsmState.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changed', full_name='FsmState.changed', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quarantaine', full_name='FsmState.quarantaine', index=6,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=61,
  serialized_end=197,
)

DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
DESCRIPTOR.message_types_by_name['FsmState'] = _FSMSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), {
  'DESCRIPTOR' : _PING,
  '__module__' : 'smpccs_pb2'
  # @@protoc_insertion_point(class_scope:Ping)
  })
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), {
  'DESCRIPTOR' : _PONG,
  '__module__' : 'smpccs_pb2'
  # @@protoc_insertion_point(class_scope:Pong)
  })
_sym_db.RegisterMessage(Pong)

FsmState = _reflection.GeneratedProtocolMessageType('FsmState', (_message.Message,), {
  'DESCRIPTOR' : _FSMSTATE,
  '__module__' : 'smpccs_pb2'
  # @@protoc_insertion_point(class_scope:FsmState)
  })
_sym_db.RegisterMessage(FsmState)



_SMPFSMCONTROL = _descriptor.ServiceDescriptor(
  name='SmpFsmControl',
  full_name='SmpFsmControl',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=199,
  serialized_end=282,
  methods=[
  _descriptor.MethodDescriptor(
    name='PingPong',
    full_name='SmpFsmControl.PingPong',
    index=0,
    containing_service=None,
    input_type=_PING,
    output_type=_PONG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ControlFsm',
    full_name='SmpFsmControl.ControlFsm',
    index=1,
    containing_service=None,
    input_type=_FSMSTATE,
    output_type=_FSMSTATE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SMPFSMCONTROL)

DESCRIPTOR.services_by_name['SmpFsmControl'] = _SMPFSMCONTROL

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/user.proto',
  package='proto',
  syntax='proto3',
  serialized_pb=_b('\n\x10proto/user.proto\x12\x05proto\"\xf3\x02\n\x0e\x43reateUserInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x11\n\trole_name\x18\x03 \x01(\t\x12\x11\n\tfull_name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\r\n\x05\x65mail\x18\x06 \x01(\t\x12\x11\n\ttelephone\x18\x07 \x01(\t\x12\n\n\x02im\x18\x08 \x01(\t\x12\x13\n\x0b\x61lert_email\x18\t \x01(\t\x12\x1a\n\x12\x61lert_email_prefix\x18\n \x01(\t\x12\x17\n\x0fstored_vm_quota\x18\x0b \x01(\x05\x12\x19\n\x11\x64\x65ployed_vm_quota\x18\x0c \x01(\x05\x12\x15\n\ris_group_role\x18\r \x01(\x08\x12\x19\n\x11is_default_cached\x18\x0e \x01(\x08\x12\x13\n\x0bis_external\x18\x0f \x01(\x08\x12\x18\n\x10is_alert_enabled\x18\x10 \x01(\x08\x12\x12\n\nis_enabled\x18\x11 \x01(\x08\"#\n\x10\x43reateUserResult\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\"\x1e\n\x0e\x44\x65leteUserInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\"#\n\x10\x44\x65leteUserResult\x12\x0f\n\x07\x64\x65leted\x18\x01 \x01(\x08\"\x1c\n\x0cReadUserInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xf2\x02\n\x0eReadUserResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\trole_name\x18\x02 \x01(\t\x12\x11\n\tfull_name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x11\n\ttelephone\x18\x06 \x01(\t\x12\n\n\x02im\x18\x07 \x01(\t\x12\x13\n\x0b\x61lert_email\x18\x08 \x01(\t\x12\x1a\n\x12\x61lert_email_prefix\x18\t \x01(\t\x12\x17\n\x0fstored_vm_quota\x18\n \x01(\x05\x12\x19\n\x11\x64\x65ployed_vm_quota\x18\x0b \x01(\x05\x12\x15\n\ris_group_role\x18\x0c \x01(\x08\x12\x19\n\x11is_default_cached\x18\r \x01(\x08\x12\x13\n\x0bis_external\x18\x0e \x01(\x08\x12\x18\n\x10is_alert_enabled\x18\x0f \x01(\x08\x12\x12\n\nis_enabled\x18\x10 \x01(\x08\x12\x0f\n\x07present\x18\x11 \x01(\x08\"2\n\x0eUpdateUserInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nis_enabled\x18\x02 \x01(\x08\"#\n\x10UpdateUserResult\x12\x0f\n\x07updated\x18\x01 \x01(\x08\x32\xf0\x01\n\x04User\x12:\n\x06\x43reate\x12\x15.proto.CreateUserInfo\x1a\x17.proto.CreateUserResult\"\x00\x12:\n\x06\x44\x65lete\x12\x15.proto.DeleteUserInfo\x1a\x17.proto.DeleteUserResult\"\x00\x12\x34\n\x04Read\x12\x13.proto.ReadUserInfo\x1a\x15.proto.ReadUserResult\"\x00\x12:\n\x06Update\x12\x15.proto.UpdateUserInfo\x1a\x17.proto.UpdateUserResult\"\x00\x62\x06proto3')
)




_CREATEUSERINFO = _descriptor.Descriptor(
  name='CreateUserInfo',
  full_name='proto.CreateUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.CreateUserInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='proto.CreateUserInfo.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_name', full_name='proto.CreateUserInfo.role_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='proto.CreateUserInfo.full_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='proto.CreateUserInfo.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='proto.CreateUserInfo.email', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telephone', full_name='proto.CreateUserInfo.telephone', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='im', full_name='proto.CreateUserInfo.im', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_email', full_name='proto.CreateUserInfo.alert_email', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_email_prefix', full_name='proto.CreateUserInfo.alert_email_prefix', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stored_vm_quota', full_name='proto.CreateUserInfo.stored_vm_quota', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deployed_vm_quota', full_name='proto.CreateUserInfo.deployed_vm_quota', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_group_role', full_name='proto.CreateUserInfo.is_group_role', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_default_cached', full_name='proto.CreateUserInfo.is_default_cached', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_external', full_name='proto.CreateUserInfo.is_external', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_alert_enabled', full_name='proto.CreateUserInfo.is_alert_enabled', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_enabled', full_name='proto.CreateUserInfo.is_enabled', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=399,
)


_CREATEUSERRESULT = _descriptor.Descriptor(
  name='CreateUserResult',
  full_name='proto.CreateUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='proto.CreateUserResult.created', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=436,
)


_DELETEUSERINFO = _descriptor.Descriptor(
  name='DeleteUserInfo',
  full_name='proto.DeleteUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.DeleteUserInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=468,
)


_DELETEUSERRESULT = _descriptor.Descriptor(
  name='DeleteUserResult',
  full_name='proto.DeleteUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deleted', full_name='proto.DeleteUserResult.deleted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=505,
)


_READUSERINFO = _descriptor.Descriptor(
  name='ReadUserInfo',
  full_name='proto.ReadUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.ReadUserInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=535,
)


_READUSERRESULT = _descriptor.Descriptor(
  name='ReadUserResult',
  full_name='proto.ReadUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.ReadUserResult.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_name', full_name='proto.ReadUserResult.role_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='proto.ReadUserResult.full_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='proto.ReadUserResult.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='proto.ReadUserResult.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telephone', full_name='proto.ReadUserResult.telephone', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='im', full_name='proto.ReadUserResult.im', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_email', full_name='proto.ReadUserResult.alert_email', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_email_prefix', full_name='proto.ReadUserResult.alert_email_prefix', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stored_vm_quota', full_name='proto.ReadUserResult.stored_vm_quota', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deployed_vm_quota', full_name='proto.ReadUserResult.deployed_vm_quota', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_group_role', full_name='proto.ReadUserResult.is_group_role', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_default_cached', full_name='proto.ReadUserResult.is_default_cached', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_external', full_name='proto.ReadUserResult.is_external', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_alert_enabled', full_name='proto.ReadUserResult.is_alert_enabled', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_enabled', full_name='proto.ReadUserResult.is_enabled', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='present', full_name='proto.ReadUserResult.present', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=538,
  serialized_end=908,
)


_UPDATEUSERINFO = _descriptor.Descriptor(
  name='UpdateUserInfo',
  full_name='proto.UpdateUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.UpdateUserInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_enabled', full_name='proto.UpdateUserInfo.is_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=910,
  serialized_end=960,
)


_UPDATEUSERRESULT = _descriptor.Descriptor(
  name='UpdateUserResult',
  full_name='proto.UpdateUserResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updated', full_name='proto.UpdateUserResult.updated', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=962,
  serialized_end=997,
)

DESCRIPTOR.message_types_by_name['CreateUserInfo'] = _CREATEUSERINFO
DESCRIPTOR.message_types_by_name['CreateUserResult'] = _CREATEUSERRESULT
DESCRIPTOR.message_types_by_name['DeleteUserInfo'] = _DELETEUSERINFO
DESCRIPTOR.message_types_by_name['DeleteUserResult'] = _DELETEUSERRESULT
DESCRIPTOR.message_types_by_name['ReadUserInfo'] = _READUSERINFO
DESCRIPTOR.message_types_by_name['ReadUserResult'] = _READUSERRESULT
DESCRIPTOR.message_types_by_name['UpdateUserInfo'] = _UPDATEUSERINFO
DESCRIPTOR.message_types_by_name['UpdateUserResult'] = _UPDATEUSERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUserInfo = _reflection.GeneratedProtocolMessageType('CreateUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSERINFO,
  __module__ = 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.CreateUserInfo)
  ))
_sym_db.RegisterMessage(CreateUserInfo)

CreateUserResult = _reflection.GeneratedProtocolMessageType('CreateUserResult', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSERRESULT,
  __module__ = 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.CreateUserResult)
  ))
_sym_db.RegisterMessage(CreateUserResult)

DeleteUserInfo = _reflection.GeneratedProtocolMessageType('DeleteUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _DELETEUSERINFO,
  __module__ = 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.DeleteUserInfo)
  ))
_sym_db.RegisterMessage(DeleteUserInfo)

DeleteUserResult = _reflection.GeneratedProtocolMessageType('DeleteUserResult', (_message.Message,), dict(
  DESCRIPTOR = _DELETEUSERRESULT,
  __module__ = 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.DeleteUserResult)
  ))
_sym_db.RegisterMessage(DeleteUserResult)

ReadUserInfo = _reflection.GeneratedProtocolMessageType('ReadUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _READUSERINFO,
  __module__ = 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.ReadUserInfo)
  ))
_sym_db.RegisterMessage(ReadUserInfo)

ReadUserResult = _reflection.GeneratedProtocolMessageType('ReadUserResult', (_message.Message,), dict(
  DESCRIPTOR = _READUSERRESULT,
  __module__ = 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.ReadUserResult)
  ))
_sym_db.RegisterMessage(ReadUserResult)

UpdateUserInfo = _reflection.GeneratedProtocolMessageType('UpdateUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERINFO,
  __module__ = 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpdateUserInfo)
  ))
_sym_db.RegisterMessage(UpdateUserInfo)

UpdateUserResult = _reflection.GeneratedProtocolMessageType('UpdateUserResult', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERRESULT,
  __module__ = 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpdateUserResult)
  ))
_sym_db.RegisterMessage(UpdateUserResult)



_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='proto.User',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1000,
  serialized_end=1240,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='proto.User.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERINFO,
    output_type=_CREATEUSERRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='proto.User.Delete',
    index=1,
    containing_service=None,
    input_type=_DELETEUSERINFO,
    output_type=_DELETEUSERRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='proto.User.Read',
    index=2,
    containing_service=None,
    input_type=_READUSERINFO,
    output_type=_READUSERRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='proto.User.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEUSERINFO,
    output_type=_UPDATEUSERRESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)

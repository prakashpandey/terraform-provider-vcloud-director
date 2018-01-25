# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/vapp.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (
    lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='proto/vapp.proto',
    package='proto',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x10proto/vapp.proto\x12\x05proto\"\xcd\x01\n\x0e\x43reateVAppInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61talog_name\x18\x02 \x01(\t\x12\x15\n\rtemplate_name\x18\x03 \x01(\t\x12\x0b\n\x03vdc\x18\x04 \x01(\t\x12\x0f\n\x07network\x18\x05 \x01(\t\x12\x1a\n\x12ip_allocation_mode\x18\x06 \x01(\t\x12\x0e\n\x06memory\x18\x07 \x01(\t\x12\x0b\n\x03\x63pu\x18\x08 \x01(\x05\x12\x10\n\x08power_on\x18\t \x01(\x08\x12\x17\n\x0fstorage_profile\x18\n \x01(\t\"P\n\x10\x43reateVAppResult\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\x12+\n\x0cin_vapp_info\x18\x02 \x01(\x0b\x32\x15.proto.CreateVAppInfo\"+\n\x0e\x44\x65leteVAppInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03vdc\x18\x02 \x01(\t\"#\n\x10\x44\x65leteVAppResult\x12\x0f\n\x07\x64\x65leted\x18\x01 \x01(\x08\")\n\x0cReadVAppInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03vdc\x18\x02 \x01(\t\"@\n\x0eReadVAppResult\x12\x0f\n\x07present\x18\x01 \x01(\x08\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x03(\tb\x06proto3'
    ))

_CREATEVAPPINFO = _descriptor.Descriptor(
    name='CreateVAppInfo',
    full_name='proto.CreateVAppInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='proto.CreateVAppInfo.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='catalog_name',
            full_name='proto.CreateVAppInfo.catalog_name',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='template_name',
            full_name='proto.CreateVAppInfo.template_name',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='vdc',
            full_name='proto.CreateVAppInfo.vdc',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='network',
            full_name='proto.CreateVAppInfo.network',
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='ip_allocation_mode',
            full_name='proto.CreateVAppInfo.ip_allocation_mode',
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='memory',
            full_name='proto.CreateVAppInfo.memory',
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='cpu',
            full_name='proto.CreateVAppInfo.cpu',
            index=7,
            number=8,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='power_on',
            full_name='proto.CreateVAppInfo.power_on',
            index=8,
            number=9,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='storage_profile',
            full_name='proto.CreateVAppInfo.storage_profile',
            index=9,
            number=10,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=28,
    serialized_end=233,
)

_CREATEVAPPRESULT = _descriptor.Descriptor(
    name='CreateVAppResult',
    full_name='proto.CreateVAppResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='created',
            full_name='proto.CreateVAppResult.created',
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='in_vapp_info',
            full_name='proto.CreateVAppResult.in_vapp_info',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=235,
    serialized_end=315,
)

_DELETEVAPPINFO = _descriptor.Descriptor(
    name='DeleteVAppInfo',
    full_name='proto.DeleteVAppInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='proto.DeleteVAppInfo.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='vdc',
            full_name='proto.DeleteVAppInfo.vdc',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=317,
    serialized_end=360,
)

_DELETEVAPPRESULT = _descriptor.Descriptor(
    name='DeleteVAppResult',
    full_name='proto.DeleteVAppResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='deleted',
            full_name='proto.DeleteVAppResult.deleted',
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=362,
    serialized_end=397,
)

_READVAPPINFO = _descriptor.Descriptor(
    name='ReadVAppInfo',
    full_name='proto.ReadVAppInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='proto.ReadVAppInfo.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='vdc',
            full_name='proto.ReadVAppInfo.vdc',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=399,
    serialized_end=440,
)

_READVAPPRESULT = _descriptor.Descriptor(
    name='ReadVAppResult',
    full_name='proto.ReadVAppResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='present',
            full_name='proto.ReadVAppResult.present',
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='name',
            full_name='proto.ReadVAppResult.name',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='network',
            full_name='proto.ReadVAppResult.network',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=442,
    serialized_end=506,
)

_CREATEVAPPRESULT.fields_by_name['in_vapp_info'].message_type = _CREATEVAPPINFO
DESCRIPTOR.message_types_by_name['CreateVAppInfo'] = _CREATEVAPPINFO
DESCRIPTOR.message_types_by_name['CreateVAppResult'] = _CREATEVAPPRESULT
DESCRIPTOR.message_types_by_name['DeleteVAppInfo'] = _DELETEVAPPINFO
DESCRIPTOR.message_types_by_name['DeleteVAppResult'] = _DELETEVAPPRESULT
DESCRIPTOR.message_types_by_name['ReadVAppInfo'] = _READVAPPINFO
DESCRIPTOR.message_types_by_name['ReadVAppResult'] = _READVAPPRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateVAppInfo = _reflection.GeneratedProtocolMessageType(
    'CreateVAppInfo',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_CREATEVAPPINFO,
        __module__='proto.vapp_pb2'
        # @@protoc_insertion_point(class_scope:proto.CreateVAppInfo)
    ))
_sym_db.RegisterMessage(CreateVAppInfo)

CreateVAppResult = _reflection.GeneratedProtocolMessageType(
    'CreateVAppResult',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_CREATEVAPPRESULT,
        __module__='proto.vapp_pb2'
        # @@protoc_insertion_point(class_scope:proto.CreateVAppResult)
    ))
_sym_db.RegisterMessage(CreateVAppResult)

DeleteVAppInfo = _reflection.GeneratedProtocolMessageType(
    'DeleteVAppInfo',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_DELETEVAPPINFO,
        __module__='proto.vapp_pb2'
        # @@protoc_insertion_point(class_scope:proto.DeleteVAppInfo)
    ))
_sym_db.RegisterMessage(DeleteVAppInfo)

DeleteVAppResult = _reflection.GeneratedProtocolMessageType(
    'DeleteVAppResult',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_DELETEVAPPRESULT,
        __module__='proto.vapp_pb2'
        # @@protoc_insertion_point(class_scope:proto.DeleteVAppResult)
    ))
_sym_db.RegisterMessage(DeleteVAppResult)

ReadVAppInfo = _reflection.GeneratedProtocolMessageType(
    'ReadVAppInfo',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_READVAPPINFO,
        __module__='proto.vapp_pb2'
        # @@protoc_insertion_point(class_scope:proto.ReadVAppInfo)
    ))
_sym_db.RegisterMessage(ReadVAppInfo)

ReadVAppResult = _reflection.GeneratedProtocolMessageType(
    'ReadVAppResult',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_READVAPPRESULT,
        __module__='proto.vapp_pb2'
        # @@protoc_insertion_point(class_scope:proto.ReadVAppResult)
    ))
_sym_db.RegisterMessage(ReadVAppResult)

try:
    # THESE ELEMENTS WILL BE DEPRECATED.
    # Please use the generated *_pb2_grpc.py files instead.
    import grpc
    from grpc.beta import implementations as beta_implementations
    from grpc.beta import interfaces as beta_interfaces
    from grpc.framework.common import cardinality
    from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
    pass
# @@protoc_insertion_point(module_scope)
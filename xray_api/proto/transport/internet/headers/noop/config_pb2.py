# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/headers/noop/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n,transport/internet/headers/noop/config.proto\x12$xray.transport.internet.headers.noop"\x08\n\x06\x43onfig"\x12\n\x10\x43onnectionConfigB\x8e\x01\n(com.xray.transport.internet.headers.noopP\x01Z9github.com/xtls/xray-core/transport/internet/headers/noop\xaa\x02$Xray.Transport.Internet.Headers.Noopb\x06proto3'
)


_CONFIG = DESCRIPTOR.message_types_by_name["Config"]
_CONNECTIONCONFIG = DESCRIPTOR.message_types_by_name["ConnectionConfig"]
Config = _reflection.GeneratedProtocolMessageType(
    "Config",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONFIG,
        "__module__": "transport.internet.headers.noop.config_pb2"
        # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.noop.Config)
    },
)
_sym_db.RegisterMessage(Config)

ConnectionConfig = _reflection.GeneratedProtocolMessageType(
    "ConnectionConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONNECTIONCONFIG,
        "__module__": "transport.internet.headers.noop.config_pb2"
        # @@protoc_insertion_point(class_scope:xray.transport.internet.headers.noop.ConnectionConfig)
    },
)
_sym_db.RegisterMessage(ConnectionConfig)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n(com.xray.transport.internet.headers.noopP\001Z9github.com/xtls/xray-core/transport/internet/headers/noop\252\002$Xray.Transport.Internet.Headers.Noop"
    _CONFIG._serialized_start = 86
    _CONFIG._serialized_end = 94
    _CONNECTIONCONFIG._serialized_start = 96
    _CONNECTIONCONFIG._serialized_end = 114
# @@protoc_insertion_point(module_scope)

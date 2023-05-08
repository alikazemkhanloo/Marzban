# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/trojan/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.common.protocol import user_pb2 as common_dot_protocol_dot_user__pb2
from xray_api.proto.common.protocol import (
    server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19proxy/trojan/config.proto\x12\x11xray.proxy.trojan\x1a\x1a\x63ommon/protocol/user.proto\x1a!common/protocol/server_spec.proto")\n\x07\x41\x63\x63ount\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x0c\n\x04\x66low\x18\x02 \x01(\t"^\n\x08\x46\x61llback\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x61lpn\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x05 \x01(\t\x12\x0c\n\x04xver\x18\x06 \x01(\x04"D\n\x0c\x43lientConfig\x12\x34\n\x06server\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpoint"i\n\x0cServerConfig\x12)\n\x05users\x18\x01 \x03(\x0b\x32\x1a.xray.common.protocol.User\x12.\n\tfallbacks\x18\x03 \x03(\x0b\x32\x1b.xray.proxy.trojan.FallbackBU\n\x15\x63om.xray.proxy.trojanP\x01Z&github.com/xtls/xray-core/proxy/trojan\xaa\x02\x11Xray.Proxy.Trojanb\x06proto3'
)


_ACCOUNT = DESCRIPTOR.message_types_by_name["Account"]
_FALLBACK = DESCRIPTOR.message_types_by_name["Fallback"]
_CLIENTCONFIG = DESCRIPTOR.message_types_by_name["ClientConfig"]
_SERVERCONFIG = DESCRIPTOR.message_types_by_name["ServerConfig"]
Account = _reflection.GeneratedProtocolMessageType(
    "Account",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACCOUNT,
        "__module__": "proxy.trojan.config_pb2"
        # @@protoc_insertion_point(class_scope:xray.proxy.trojan.Account)
    },
)
_sym_db.RegisterMessage(Account)

Fallback = _reflection.GeneratedProtocolMessageType(
    "Fallback",
    (_message.Message,),
    {
        "DESCRIPTOR": _FALLBACK,
        "__module__": "proxy.trojan.config_pb2"
        # @@protoc_insertion_point(class_scope:xray.proxy.trojan.Fallback)
    },
)
_sym_db.RegisterMessage(Fallback)

ClientConfig = _reflection.GeneratedProtocolMessageType(
    "ClientConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLIENTCONFIG,
        "__module__": "proxy.trojan.config_pb2"
        # @@protoc_insertion_point(class_scope:xray.proxy.trojan.ClientConfig)
    },
)
_sym_db.RegisterMessage(ClientConfig)

ServerConfig = _reflection.GeneratedProtocolMessageType(
    "ServerConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _SERVERCONFIG,
        "__module__": "proxy.trojan.config_pb2"
        # @@protoc_insertion_point(class_scope:xray.proxy.trojan.ServerConfig)
    },
)
_sym_db.RegisterMessage(ServerConfig)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\025com.xray.proxy.trojanP\001Z&github.com/xtls/xray-core/proxy/trojan\252\002\021Xray.Proxy.Trojan"
    _ACCOUNT._serialized_start = 111
    _ACCOUNT._serialized_end = 152
    _FALLBACK._serialized_start = 154
    _FALLBACK._serialized_end = 248
    _CLIENTCONFIG._serialized_start = 250
    _CLIENTCONFIG._serialized_end = 318
    _SERVERCONFIG._serialized_start = 320
    _SERVERCONFIG._serialized_end = 425
# @@protoc_insertion_point(module_scope)

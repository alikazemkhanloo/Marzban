# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/observatory/command/command.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xray_api.proto.app.observatory import (
    config_pb2 as app_dot_observatory_dot_config__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n%app/observatory/command/command.proto\x12!xray.core.app.observatory.command\x1a\x1c\x61pp/observatory/config.proto"\x1a\n\x18GetOutboundStatusRequest"Y\n\x19GetOutboundStatusResponse\x12<\n\x06status\x18\x01 \x01(\x0b\x32,.xray.core.app.observatory.ObservationResult"\x08\n\x06\x43onfig2\xa7\x01\n\x12ObservatoryService\x12\x90\x01\n\x11GetOutboundStatus\x12;.xray.core.app.observatory.command.GetOutboundStatusRequest\x1a<.xray.core.app.observatory.command.GetOutboundStatusResponse"\x00\x42\x80\x01\n%com.xray.core.app.observatory.commandP\x01Z1github.com/xtls/xray-core/app/observatory/command\xaa\x02!Xray.Core.App.Observatory.Commandb\x06proto3'
)


_GETOUTBOUNDSTATUSREQUEST = DESCRIPTOR.message_types_by_name["GetOutboundStatusRequest"]
_GETOUTBOUNDSTATUSRESPONSE = DESCRIPTOR.message_types_by_name[
    "GetOutboundStatusResponse"
]
_CONFIG = DESCRIPTOR.message_types_by_name["Config"]
GetOutboundStatusRequest = _reflection.GeneratedProtocolMessageType(
    "GetOutboundStatusRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETOUTBOUNDSTATUSREQUEST,
        "__module__": "app.observatory.command.command_pb2"
        # @@protoc_insertion_point(class_scope:xray.core.app.observatory.command.GetOutboundStatusRequest)
    },
)
_sym_db.RegisterMessage(GetOutboundStatusRequest)

GetOutboundStatusResponse = _reflection.GeneratedProtocolMessageType(
    "GetOutboundStatusResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETOUTBOUNDSTATUSRESPONSE,
        "__module__": "app.observatory.command.command_pb2"
        # @@protoc_insertion_point(class_scope:xray.core.app.observatory.command.GetOutboundStatusResponse)
    },
)
_sym_db.RegisterMessage(GetOutboundStatusResponse)

Config = _reflection.GeneratedProtocolMessageType(
    "Config",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONFIG,
        "__module__": "app.observatory.command.command_pb2"
        # @@protoc_insertion_point(class_scope:xray.core.app.observatory.command.Config)
    },
)
_sym_db.RegisterMessage(Config)

_OBSERVATORYSERVICE = DESCRIPTOR.services_by_name["ObservatoryService"]
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n%com.xray.core.app.observatory.commandP\001Z1github.com/xtls/xray-core/app/observatory/command\252\002!Xray.Core.App.Observatory.Command"
    _GETOUTBOUNDSTATUSREQUEST._serialized_start = 106
    _GETOUTBOUNDSTATUSREQUEST._serialized_end = 132
    _GETOUTBOUNDSTATUSRESPONSE._serialized_start = 134
    _GETOUTBOUNDSTATUSRESPONSE._serialized_end = 223
    _CONFIG._serialized_start = 225
    _CONFIG._serialized_end = 233
    _OBSERVATORYSERVICE._serialized_start = 236
    _OBSERVATORYSERVICE._serialized_end = 403
# @@protoc_insertion_point(module_scope)

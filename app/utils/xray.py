import json
from app import xray
from app.db import GetDB, Inbound
from app.models.proxy import ProxySettings

from app.xray.config import XRayConfig


# def xray_add_user(user: User):
#     if not isinstance(user, User):
#         user = UserResponse.from_orm(user)
#     for proxy_type, inbound_tags in user.inbounds.items():
#         account = user.get_account(proxy_type)
#         for inbound_tag in inbound_tags:
#             try:
#                 xray.api.add_inbound_user(tag=inbound_tag, user=account)
#             except xray.exc.EmailExistsError:
#                 pass


# def xray_remove_user(user: User):
#     for inbound_tag in xray.config.inbounds_by_tag:
#         try:
#             xray.api.remove_inbound_user(tag=inbound_tag, email=user.username)
#         except xray.exc.EmailNotFoundError:
#             pass


def xray_config_from_db(config: XRayConfig):
    config = config.copy()

    with GetDB() as db:
        inbounds: list[Inbound] = db.query(Inbound).all()
        for inbound in inbounds:
            db_stream_settings = inbound.stream_settings
            stream_settings = {}

            if db_stream_settings.networkSettingsKey:
                stream_settings[
                    db_stream_settings.networkSettingsKey
                ] = db_stream_settings.networkSettings

            if db_stream_settings.securitySettingsKey:
                stream_settings[
                    db_stream_settings.securitySettingsKey
                ] = db_stream_settings.securitySettings
            clients = []
            for dbclient in inbound.clients:
                client = {}
                if dbclient.settings:
                    client = dbclient.settings
                if inbound.client_settings:
                    client = {**client, **inbound.client_settings.settings}
                clients.append(client)

            inbound_dict = {
                "tag": inbound.tag,
                "listen": inbound.listen,
                "port": inbound.port,
                "protocol": inbound.protocol,
                "settings": {"clients": clients, **inbound.settings.settings},
            }
            if len(stream_settings.keys()) > 0:
                inbound_dict["streamSettings"] = stream_settings
            config["inbounds"].append(inbound_dict)

    return config

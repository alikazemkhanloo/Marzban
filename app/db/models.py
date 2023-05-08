import os
from datetime import datetime

from app import xray
from enum import Enum as EnumClass
from app.db.base import Base
from sqlalchemy import (
    JSON,
    BigInteger,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship


class ClientStatus(str, EnumClass):
    active = "active"
    disabled = "disabled"
    limited = "limited"
    expired = "expired"


class UserStatusModify(str, EnumClass):
    active = "active"
    disabled = "disabled"


class ClientDataLimitResetStrategy(str, EnumClass):
    no_reset = "no_reset"
    day = "day"
    week = "week"
    month = "month"
    year = "year"


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(34), unique=True, index=True)
    hashed_password = Column(String(128))
    clients = relationship("Client", back_populates="admin")
    created_at = Column(DateTime, default=datetime.utcnow)


class ClientUsageResetLogs(Base):
    __tablename__ = "client_usage_logs"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="logs")
    used_traffic_at_reset = Column(BigInteger, nullable=False)
    reset_at = Column(DateTime, default=datetime.utcnow)


class Inbound(Base):
    __tablename__ = "inbounds"
    id = Column(Integer, primary_key=True, index=True)

    tag = Column(String, nullable=False)
    listen = Column(String, nullable=False)
    port = Column(String, nullable=False)
    protocol = Column(String, nullable=False)
    settings = Column(JSON, nullable=True)

    stream_settings_id = Column(Integer, ForeignKey("stream_settings.id"))
    stream_settings = relationship("StreamSettings")

    settings_id = Column(Integer, ForeignKey("inbound_settings.id"))
    settings = relationship("InboundSettings")

    client_settings_id = Column(Integer, ForeignKey("inbound_client_settings.id"))
    client_settings = relationship("InboundClientSettings")

    clients = relationship("Client", back_populates="inbound")


class StreamSettings(Base):
    __tablename__ = "stream_settings"

    id = Column(Integer, primary_key=True, index=True)
    network = Column(String, nullable=True)
    networkSettingsKey = Column(String, nullable=True)
    networkSettings = Column(JSON, nullable=True)

    security = Column(String, nullable=True)
    securitySettingsKey = Column(String, nullable=True)
    securitySettings = Column(JSON, nullable=True)


class InboundSettings(Base):
    __tablename__ = "inbound_settings"

    id = Column(Integer, primary_key=True, index=True)
    settings = Column(JSON, nullable=True)


class InboundClientSettings(Base):
    __tablename__ = "inbound_client_settings"

    id = Column(Integer, primary_key=True, index=True)
    settings = Column(
        JSON,
        nullable=True,
    )


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    inbound_id = Column(Integer, ForeignKey("inbounds.id"))
    inbound = relationship("Inbound", back_populates="clients")
    data = Column(JSON, nullable=False)

    status = Column(Enum(ClientStatus), nullable=False, default=ClientStatus.active)
    used_traffic = Column(BigInteger, default=0)
    data_limit = Column(BigInteger, nullable=True)
    data_limit_reset_strategy = Column(
        Enum(ClientDataLimitResetStrategy),
        nullable=False,
        default=ClientDataLimitResetStrategy.no_reset,
    )
    logs = relationship("ClientUsageResetLogs", back_populates="client")
    expire = Column(Integer, nullable=True)
    admin_id = Column(Integer, ForeignKey("admins.id"))
    admin = relationship("Admin", back_populates="clients")
    created_at = Column(DateTime, default=datetime.utcnow)
    settings = Column(JSON, nullable=True)

    @property
    def lifetime_used_traffic(self):
        return (
            sum([log.used_traffic_at_reset for log in self.usage_logs])
            + self.used_traffic
        )

    @property
    def last_traffic_reset_time(self):
        return self.usage_logs[-1].reset_at if self.usage_logs else self.created_at


class System(Base):
    __tablename__ = "system"

    id = Column(Integer, primary_key=True, index=True)
    uplink = Column(BigInteger, default=0)
    downlink = Column(BigInteger, default=0)


class JWT(Base):
    __tablename__ = "jwt"

    id = Column(Integer, primary_key=True)
    secret_key = Column(
        String(64), nullable=False, default=lambda: os.urandom(32).hex()
    )

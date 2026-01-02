from sqlmodel import SQLModel

CORE_SCHEMA: str = "core"
TENANT_SCHEMA: str = "tenant1"


class CoreMixin(SQLModel):
    __table_args__ = {"schema": CORE_SCHEMA}


class TenantMixin(SQLModel):
    __table_args__ = {"schema": TENANT_SCHEMA}
    pass

from sqlmodel import SQLModel


class TenantMixin(SQLModel):
    __table_args__ = {"tenant_table": True}

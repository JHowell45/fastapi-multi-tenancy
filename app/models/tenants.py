from sqlmodel import Field

from .traits.core import DateTimeMixin
from .traits.tenants import CoreMixin


class Tenant(CoreMixin, DateTimeMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy.sql import func
from sqlmodel import DateTime, Field, Relationship, SQLModel

from .traits.tenants import TenantMixin

if TYPE_CHECKING:
    from .gigs import Gig


class BandBase(SQLModel):
    name: str = Field(unique=True)
    description: str


class Band(TenantMixin, BandBase, table=True):
    __tablename__ = "bands"

    id: int | None = Field(default=None, primary_key=True)
    started_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=DateTime,
        sa_column_kwargs={"server_default": func.now()},
        nullable=False,
    )

    gigs: list[Gig] = Relationship(back_populates="primary_band")

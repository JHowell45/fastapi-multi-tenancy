from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy.sql import func
from sqlmodel import DateTime, Field, Relationship, SQLModel

from .relationship_linkers import BandSupportGigLink
from .traits.core import DateTimeMixin
from .traits.tenants import TenantMixin

if TYPE_CHECKING:
    from .gigs import Gig


class BandBase(SQLModel):
    name: str = Field(unique=True)
    description: str


class Band(DateTimeMixin, TenantMixin, BandBase, table=True):
    __tablename__ = "bands"

    id: int | None = Field(default=None, primary_key=True)
    started_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=DateTime,
        sa_column_kwargs={"server_default": func.now()},
        nullable=False,
    )

    headline_gigs: list["Gig"] = Relationship(back_populates="primary_band")
    support_gigs: list["Gig"] = Relationship(
        back_populates="support_bands", link_model=BandSupportGigLink
    )


class BandNoGigPublic(BandBase):
    id: int
    started_at: datetime
    created_at: datetime
    updated_at: datetime


class BandGigPublic(SQLModel):
    id: int
    primary_band: BandNoGigPublic
    support_bands: list[BandNoGigPublic]


class BandPublic(BandBase):
    id: int

    gigs: list[BandGigPublic]

    started_at: datetime
    created_at: datetime
    updated_at: datetime

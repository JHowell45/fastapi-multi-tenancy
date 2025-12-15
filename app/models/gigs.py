from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from .traits.tenants import TenantMixin

if TYPE_CHECKING:
    from .bands import Band


class Gig(TenantMixin, table=True):
    __tablename__ = "gigs"

    id: int | None = Field(default=None, primary_key=True)

    primary_band_id: int = Field(foreign_key="bands.id")
    primary_band: list[Band] = Relationship(back_populates="gigs")
    primary_band_id: int = Field(foreign_key="bands.id")
    primary_band: list[Band] = Relationship(back_populates="gigs")

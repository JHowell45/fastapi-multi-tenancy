from sqlmodel import Field

from .traits.tenants import TenantMixin


class BandSupportGigLink(TenantMixin, table=True):
    band_id: int = Field(foreign_key="bands.id", primary_key=True)
    gig_id: int = Field(foreign_key="gigs.id", primary_key=True)

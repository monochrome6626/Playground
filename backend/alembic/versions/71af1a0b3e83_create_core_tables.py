"""create core tables

Revision ID: 71af1a0b3e83
Revises: 
Create Date: 2026-04-01 22:50:40.693418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71af1a0b3e83'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "spots",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("elevation_m", sa.Float(), nullable=True),
        sa.Column("prefecture", sa.String(length=50), nullable=True),
        sa.Column("memo", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "landmarks",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("base_elevation_m", sa.Float(), nullable=True),
        sa.Column("height_m", sa.Float(), nullable=False),
        sa.Column("target_point_type", sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "search_requests",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("spot_id", sa.String(length=64), nullable=False),
        sa.Column("landmark_id", sa.String(length=64), nullable=False),
        sa.Column("date_from", sa.Date(), nullable=False),
        sa.Column("date_to", sa.Date(), nullable=False),
        sa.Column("body_types", sa.JSON(), nullable=False),
        sa.Column("event_types", sa.JSON(), nullable=False),
        sa.Column("azimuth_tolerance_deg", sa.Float(), nullable=False),
        sa.Column("altitude_tolerance_deg", sa.Float(), nullable=False),
        sa.Column("interval_sec", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False),
        sa.ForeignKeyConstraint(["landmark_id"], ["landmarks.id"]),
        sa.ForeignKeyConstraint(["spot_id"], ["spots.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "matches",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("search_request_id", sa.String(length=64), nullable=False),
        sa.Column("spot_id", sa.String(length=64), nullable=False),
        sa.Column("landmark_id", sa.String(length=64), nullable=False),
        sa.Column("body", sa.String(length=20), nullable=False),
        sa.Column("event_type", sa.String(length=20), nullable=False),
        sa.Column("observed_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("azimuth_diff_deg", sa.Float(), nullable=False),
        sa.Column("altitude_diff_deg", sa.Float(), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(["landmark_id"], ["landmarks.id"]),
        sa.ForeignKeyConstraint(["search_request_id"], ["search_requests.id"]),
        sa.ForeignKeyConstraint(["spot_id"], ["spots.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("matches")
    op.drop_table("search_requests")
    op.drop_table("landmarks")
    op.drop_table("spots")

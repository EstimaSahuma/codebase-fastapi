"""Create User Model

Revision ID: 8b0b53f14856
Revises: f4923f49f696
Create Date: 2023-08-07 16:46:51.622559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b0b53f14856'
down_revision = 'f4923f49f696'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("username", sa.String(250), unique=True, nullable=False),
        sa.Column("hashed_password", sa.String(250), unique=False, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("users")

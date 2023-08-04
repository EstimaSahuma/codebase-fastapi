"""Create Exemple Table

Revision ID: f4923f49f696
Revises: 
Create Date: 2023-08-04 15:14:42.427450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4923f49f696'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "examples",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(250), unique=True, nullable=False),
        sa.Column("description", sa.String(250), unique=False, nullable=True)
    )


def downgrade() -> None:
    op.drop_table("examples")

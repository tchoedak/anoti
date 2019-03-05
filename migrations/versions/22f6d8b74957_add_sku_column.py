"""add sku column

Revision ID: 22f6d8b74957
Revises: 03f1875c077c
Create Date: 2018-12-16 01:25:08.370037+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f6d8b74957'
down_revision = '03f1875c077c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('amazon_orders', sa.Column('sku', sa.String()))


def downgrade():
    op.drop_column('amazon_orders', 'sku')

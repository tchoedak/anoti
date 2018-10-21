"""create orders table

Revision ID: 03f1875c077c
Revises: 
Create Date: 2018-10-21 00:05:50.302664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03f1875c077c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('amazon_order_id', sa.String, primary_key=True),
        sa.Column('is_prime', sa.Boolean),
        sa.Column('item', sa.String),
        sa.Column('price', sa.Float),
        sa.Column('purchase_date', sa.DateTime),
        sa.Column('order_status', sa.String),
        sa.Column('order_type', sa.String),
        sa.Column('ship_service_level', sa.String),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )

def downgrade():
    op.drop_table('orders')

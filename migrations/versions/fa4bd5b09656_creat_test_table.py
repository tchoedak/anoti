"""creat test table

Revision ID: fa4bd5b09656
Revises: 03f1875c077c
Create Date: 2018-11-30 17:13:59.531278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa4bd5b09656'
down_revision = '03f1875c077c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "test_table",
        sa.Column("id", sa.Integer, primary_key=True)
    )


def downgrade():
    op.drop_table(
        "test_table"
    )

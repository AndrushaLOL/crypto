"""create tickers table

Revision ID: 028ab3128e31
Revises: 
Create Date: 2019-08-04 00:22:24.939467

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = '028ab3128e31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tickers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('timestamp', sa.DateTime, default=datetime.datetime.now),
        sa.Column('symbol', sa.String),
        sa.Column('open', sa.Float),
        sa.Column('close', sa.Float),
        sa.Column('high', sa.Float),
        sa.Column('low', sa.Float),
        sa.Column('volume', sa.Float),
    )


def downgrade():
    op.drop_table('tickers')

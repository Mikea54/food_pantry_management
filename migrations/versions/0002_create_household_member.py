"""create household_member table

Revision ID: 0002
Revises: 0001
Create Date: 2024-01-01 00:00:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'household_member',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('household_id', sa.Integer(), sa.ForeignKey('household.id'), nullable=False),
        sa.Column('name', sa.String(length=100)),
        sa.Column('age', sa.Integer()),
        sa.Column('relation', sa.String(length=50)),
    )


def downgrade():
    op.drop_table('household_member')

"""create household table

Revision ID: 0001
Revises: 
Create Date: 2024-01-01 00:00:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'household',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('head_name', sa.String(length=100), nullable=False),
        sa.Column('contact_phone', sa.String(length=20)),
        sa.Column('address', sa.String(length=200)),
        sa.Column('eligibility_status', sa.String(length=50)),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )


def downgrade():
    op.drop_table('household')

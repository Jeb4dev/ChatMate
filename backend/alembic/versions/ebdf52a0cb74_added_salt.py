"""Added salt

Revision ID: ebdf52a0cb74
Revises: 6d46958a0f9b
Create Date: 2023-01-08 00:11:31.317900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebdf52a0cb74'
down_revision = '6d46958a0f9b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('salt', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'salt')
    # ### end Alembic commands ###

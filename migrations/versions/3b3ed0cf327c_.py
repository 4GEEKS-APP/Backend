"""empty message

Revision ID: 3b3ed0cf327c
Revises: 54abe74b8732
Create Date: 2021-10-01 16:57:39.365889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b3ed0cf327c'
down_revision = '54abe74b8732'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('gender', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'gender')
    # ### end Alembic commands ###
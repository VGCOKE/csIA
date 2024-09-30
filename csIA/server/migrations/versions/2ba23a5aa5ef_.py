"""empty message

Revision ID: 2ba23a5aa5ef
Revises: bc7ab696abe4
Create Date: 2024-09-17 23:47:08.705699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ba23a5aa5ef'
down_revision = 'bc7ab696abe4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history',
    sa.Column('rid', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('rid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('history')
    # ### end Alembic commands ###

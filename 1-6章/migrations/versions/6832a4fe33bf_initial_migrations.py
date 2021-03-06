"""initial migrations

Revision ID: 6832a4fe33bf
Revises: 
Create Date: 2017-08-26 15:54:59.490932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6832a4fe33bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('userid', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_userid'), 'users', ['userid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_userid'), table_name='users')
    op.drop_column('users', 'userid')
    # ### end Alembic commands ###

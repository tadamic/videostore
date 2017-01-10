"""Added User.api_key

Revision ID: 9651ddd5d59e
Revises: 8640c1dab484
Create Date: 2017-01-10 13:47:33.980522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9651ddd5d59e'
down_revision = '8640c1dab484'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('api_key', sa.String(length=255), nullable=False))
    op.create_index(op.f('ix_users_api_key'), 'users', ['api_key'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_api_key'), table_name='users')
    op.drop_column('users', 'api_key')
    # ### end Alembic commands ###

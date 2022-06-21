"""fixed time column

Revision ID: a1b7e3f41c0e
Revises: c28dccaffba6
Create Date: 2022-06-21 14:09:33.075822

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a1b7e3f41c0e'
down_revision = 'c28dccaffba6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inbox', sa.Column('created_at', sa.DateTime(timezone=True), server_default='2022-06-21 14:09:32', nullable=True))
    op.drop_column('inbox', 'time_created')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inbox', sa.Column('time_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True))
    op.drop_column('inbox', 'created_at')
    # ### end Alembic commands ###

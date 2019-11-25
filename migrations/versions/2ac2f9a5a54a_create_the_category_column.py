"""create the category column

Revision ID: 2ac2f9a5a54a
Revises: eb52402f682e
Create Date: 2019-11-24 19:28:53.804276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ac2f9a5a54a'
down_revision = 'eb52402f682e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_title', sa.String(length=255), nullable=True),
    sa.Column('pitch_body', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitch')
    # ### end Alembic commands ###
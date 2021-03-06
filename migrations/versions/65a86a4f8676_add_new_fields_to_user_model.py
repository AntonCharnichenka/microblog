"""Add new fields to user model

Revision ID: 65a86a4f8676
Revises: 77ce72b55fb1
Create Date: 2019-12-08 21:35:17.978179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65a86a4f8676'
down_revision = '77ce72b55fb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###

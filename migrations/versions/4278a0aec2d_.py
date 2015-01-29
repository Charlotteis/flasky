"""empty message

Revision ID: 4278a0aec2d
Revises: 508008ef8a1
Create Date: 2015-01-29 20:44:47.067461

"""

# revision identifiers, used by Alembic.
revision = '4278a0aec2d'
down_revision = '508008ef8a1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###

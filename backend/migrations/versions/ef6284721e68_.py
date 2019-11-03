"""empty message

Revision ID: ef6284721e68
Revises: 
Create Date: 2019-11-02 10:01:32.982534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef6284721e68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workorder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workorder', sa.String(length=1024), nullable=False),
    sa.Column('folder', sa.String(length=128), nullable=False),
    sa.Column('found', sa.Boolean(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('workorder')
    )
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=500), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('workorder_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['workorder_id'], ['workorder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('action')
    op.drop_table('workorder')
    # ### end Alembic commands ###

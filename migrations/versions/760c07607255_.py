"""empty message

Revision ID: 760c07607255
Revises: 
Create Date: 2022-06-13 21:19:10.610862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '760c07607255'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nse_stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('sector', sa.String(), nullable=False),
    sa.Column('isin_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isin_code')
    )
    op.create_table('stock_price',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stock_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('closing_price', sa.Float(), nullable=True),
    sa.Column('prev_year_high', sa.Float(), nullable=True),
    sa.Column('prev_year_low', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['stock_id'], ['nse_stock.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', 'date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_price')
    op.drop_table('nse_stock')
    # ### end Alembic commands ###

"""Removed User table. Added Company, Financial Statement and Dividend tables

Revision ID: e4a2626a7b4d
Revises: d4867f3a4c0a
Create Date: 2020-05-01 12:34:20.801574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a2626a7b4d'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('isin', sa.String(), nullable=True),
    sa.Column('number_of_shares', sa.BigInteger(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('ipo_date', sa.DateTime(), nullable=True),
    sa.Column('stock_exchange', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isin'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_index(op.f('ix_company_id'), 'company', ['id'], unique=False)
    op.create_table('dividend',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('ex_dividend_date', sa.DateTime(), nullable=True),
    sa.Column('pay_date', sa.DateTime(), nullable=True),
    sa.Column('dividend_payout', sa.Float(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dividend_id'), 'dividend', ['id'], unique=False)
    op.create_table('financial_statement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('period', sa.String(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('audited', sa.Boolean(), nullable=True),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('non_current_assets', sa.BigInteger(), nullable=True),
    sa.Column('current_assets', sa.BigInteger(), nullable=True),
    sa.Column('total_assets', sa.BigInteger(), nullable=True),
    sa.Column('total_equity', sa.BigInteger(), nullable=True),
    sa.Column('long_term_liabilities', sa.BigInteger(), nullable=True),
    sa.Column('current_liabilities', sa.BigInteger(), nullable=True),
    sa.Column('total_liabilities', sa.BigInteger(), nullable=True),
    sa.Column('total_equities_and_liabilities', sa.BigInteger(), nullable=True),
    sa.Column('total_revenues', sa.BigInteger(), nullable=True),
    sa.Column('gross_profit', sa.BigInteger(), nullable=True),
    sa.Column('operating_income', sa.BigInteger(), nullable=True),
    sa.Column('profit_before_tax', sa.BigInteger(), nullable=True),
    sa.Column('net_income', sa.BigInteger(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_index(op.f('ix_financial_statement_id'), 'financial_statement', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_financial_statement_id'), table_name='financial_statement')
    op.drop_table('financial_statement')
    op.drop_index(op.f('ix_dividend_id'), table_name='dividend')
    op.drop_table('dividend')
    op.drop_index(op.f('ix_company_id'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###
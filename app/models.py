from sqlalchemy import Column, Integer, String, Table, Float
from .config import metadata


products = Table(
    'products',
    metadata,
    Column('id', Integer,  primary_key=True),
    Column('name', String(100), nullable=True),
    Column('price', Float),
    Column('amount', Integer),
    Column('description', String(500), nullable=True),
)
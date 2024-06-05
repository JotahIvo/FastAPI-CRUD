from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://postgres:password@db:5432/tasks"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

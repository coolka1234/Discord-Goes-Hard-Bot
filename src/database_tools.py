from typing import Any, Tuple
from sqlalchemy import MetaData, Select, Table, select, func
def get_last_index(engine, table_name):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    stmt: Select[Tuple[Any]] = select(func.max(table.columns.index))
    with engine.connect() as connection:
        result = connection.execute(stmt)
        return result.scalar() if result.scalar() is not None else -1

# def get_last_row(engine, table_name):
#     obj = session.query(ObjectRes).order_by(ObjectRes.id.desc()).first()
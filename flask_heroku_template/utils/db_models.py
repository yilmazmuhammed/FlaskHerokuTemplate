import math
import os
from pony.orm import *

db = Database()


class FirstTable(db.Entity):
    id = PrimaryKey(int, auto=True)


def paging_to_query(query, page_num=0, page_size=50):
    return query.page(pagenum=page_num, pagesize=page_size)


def get_paging_variables(entities_query, page_size, page_num):
    total_count = entities_query.count()
    page_count = math.ceil(total_count / page_size)
    first_index = total_count - (page_num - 1) * page_size
    transactions = paging_to_query(entities_query, page_num=page_num, page_size=page_size)
    return total_count, page_count, first_index, transactions


DATABASE_PROVIDER = os.getenv("DATABASE_PROVIDER")

if DATABASE_PROVIDER == "postgres":
    DATABASE_URL = os.getenv("DATABASE_URL")
    db.bind(provider="postgres", dsn=DATABASE_URL)
elif DATABASE_PROVIDER == "mysql":
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_DB = os.getenv("DATABASE_DB")
    db.bind(provider="mysql", host=DATABASE_HOST, user=DATABASE_USER, passwd=DATABASE_PASSWORD, db=DATABASE_DB)
else:
    db.bind(provider="sqlite", filename='database.sqlite', create_db=True)


db.generate_mapping(create_tables=True)

if __name__ == '__main__':
    with db_session:
        # Initialize operations
        pass

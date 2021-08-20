# Fill in credentials
host='__________'
port='__________'
database='______'
user='__________'
password='______'

## Do NOT change anything below!
# sqlalchemy engine for writing data to a database
from sqlalchemy import create_engine    
engine = create_engine(f'postgres+psycopg2://{user}:{password}@{host}:{port}/{database}')

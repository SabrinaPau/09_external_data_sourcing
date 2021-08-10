# Fill in credentials
host='__________'
port='__________'
database='______'
user='__________'
password='______'

## Do NOT change anything below!
# psycopg2 connection for querying data from a database
import psycopg2
conn = psycopg2.connect(host=host,
                        port=port,
                        database=database,
                        user=user,
                        password=password)

# sqlalchemy engine for writing data to a database
from sqlalchemy import create_engine    
engine = create_engine('postgresql+psycopg2://' + user + ':' + host + ':' + port + '/' + database)

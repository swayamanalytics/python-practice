import sqlalchemy
from sqlalchemy import Table,Column,MetaData
from urllib import parse
engine=sqlalchemy.create_engine("mysql://appsql:%s@192.168.131.4/hr"%parse.unquote('Welcome#123'))
connectionstr=engine.connect()
meta=MetaData()
employees=Table('employees',meta,autoload=True,autoload_with=engine)
stmt=sqlalchemy.select([employees])
ed=connectionstr.execute(stmt)
fg=ed.fetchone()
print(fg)

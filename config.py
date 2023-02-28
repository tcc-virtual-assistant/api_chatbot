import databases
import sqlalchemy
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
TESTE_DATABASE = os.getenv('TESTE_DATABASE', 'false') in ('true', 'yes')
#  setar o teste database caso queira apenas testar sem ter que enviar os dados para o banco de dados
database = databases.Database(DATABASE_URL, force_rollback=TESTE_DATABASE)
metadata = sqlalchemy.MetaData()
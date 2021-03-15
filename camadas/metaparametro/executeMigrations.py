# Script para criar as tabelas

import os
from peewee import *
from models.clienteModel import ClienteModel
from models.contaPoupancaModel import ContaPoupancaModel
from models.contaCorrenteModel import ContaCorrenteModel


databaseName = 'database.db'
if os.path.exists(databaseName):
    os.remove(databaseName)

db = SqliteDatabase('database.db')
db.connect()
db.create_tables([ClienteModel, ContaPoupancaModel, ContaCorrenteModel])

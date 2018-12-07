#!/bin/bash
# Author: Gustavo Soares de Lima

# apagando o banco
rm db.sqlite3

# apagando as migrações
rm clientes/migrations/* -R
rm comercial/migrations/* -R
rm estoque/migrations/* -R
rm financeiro/migrations/* -R
rm fornecedores/migrations/* -R
rm rh/migrations/* -R

python3 manage.py migrate --run-syncdb
python3 manage.py createsuperuser
python3 manage.py runserver 8080


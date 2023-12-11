# Lacrei Saúde: API Consultas Médicas

Esta é uma API RESTful construída com Django Rest Framework (DRF) que oferece operações CRUD (Create, Read, Update, Delete) em um banco de dados SQLite. 

A finalidade da API é poder realizar o cadastro, leitura, edição e exclusão de Consultas Médicas. Cada consulta contém o id da pessoa profissional responsável pelo atendimento, id do paciente, id da consulta e a data da consulta.
É possível também cadastrar uma pessoa profissional, com o nome social e id. Também existe a rota de cadastro de paciente, contendo os campos id e nome social do paciente.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Recomenda-se o uso de um ambiente virtual.

```bash
pip install virtualenv
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

Versões das libs utilizadas:
Django==4.2.7
django-cors-headers==4.3.1
djangorestframework==3.14.0

## Pré-requisitos

Fazer o clone do projeto em sua máquina e rodar o seguinte comando:
py manage.py runserver

from typing import Any
import psycopg2
import requests

HEAD_HUNTER_URL = 'https://api.hh.ru/vacancies'


def get_vacancies(companies: dict) -> list[dict[str, Any]]:
    """Загрузка вакансий с HH.ru"""
    print("Загружаю вакансии")
    all_vacs = []
    for company in companies:
        params = {
            'employer_id': company,
            'page': 0,
            'per_page': 100,
            'only_with_salary': True
        }
        response = requests.get(HEAD_HUNTER_URL, params)
        result_page = response.json()
        vacancies = result_page['items']
        while len(result_page['items']) == 100:
            params['page'] += 1
            response = requests.get(HEAD_HUNTER_URL, params)
            result_page = response.json()
            if len(vacancies) == 500:
                break
            elif result_page.get('items'):
                vacancies.extend(result_page['items'])
            else:
                break
        for vacancy in vacancies:
            all_vacs.append({'vacancy_id': vacancy['id'],
                             'vacancy_name': vacancy['name'],
                             'vacancy_salary_from': vacancy['salary']['from'],
                             'vacancy_salary_to': vacancy['salary']['to'],
                             'vacancy_url': vacancy['alternate_url'],
                             'company_id': vacancy['employer']['id'],
                             'published_date': vacancy['published_at']
                             })
    return all_vacs


def create_database(db_name, params):
    """Создание базы данных"""
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('DROP DATABASE IF EXISTS ' + db_name)
    cur.execute('CREATE DATABASE ' + db_name)
    cur.close()
    conn.close()


def create_company_table(cur):
    """Создание таблицы companies"""
    query = """
        DROP TABLE IF EXISTS companies;
        CREATE TABLE companies
        (
            company_id int PRIMARY KEY,
            company_name varchar(50) NOT NULL
        );
    """
    cur.execute(query)


def create_vacancy_table(cur):
    """Создание таблицы vacancies"""
    query = """
        DROP TABLE IF EXISTS vacancies;
        CREATE TABLE vacancies
        (
            vacancy_id int PRIMARY KEY,
            vacancy_name varchar(100) NOT NULL,
            vacancy_salary_from int,
            vacancy_salary_to int,
            vacancy_url text,
            company_id int,
            published_date date
        );
    """
    cur.execute(query)

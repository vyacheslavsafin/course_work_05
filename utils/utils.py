from typing import Any
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
    # return all_vacs
    print(all_vacs)

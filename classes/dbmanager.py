import psycopg2


class DBManager:
    """Класс для работы с базой данных"""

    def __init__(self, params):
        self.conn = psycopg2.connect(**params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        self.cur.execute("SELECT company_name, COUNT(*) FROM vacancies JOIN companies USING(company_id)"
                         " GROUP BY company_name")
        companies_list = self.cur.fetchall()
        return companies_list

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        self.cur.execute("SELECT company_name, vacancy_name, vacancy_salary_from, vacancy_salary_to, vacancy_url"
                         " FROM vacancies JOIN companies USING(company_id)")
        vacancies_list = self.cur.fetchall()
        return vacancies_list

    def close_connection(self):
        """закрывает соединение с БД"""
        self.cur.close()
        self.conn.close()

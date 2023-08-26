from config import config
from utils.utils import *

companies = {
    2180: "Ozon",
    1455: "HeadHunter",
    1740: "Яндекс",
    6093775: "Aston",
    1329: "Европлан",
    67611: "Тензор",
    733: "Ланит",
    4759060: "HR Prime",
    1532045: "CarPrice",
    87021: "WILDBERRIES"
}

db_name = "vacancies"

params = config()

def main():
    vacancies_list = get_vacancies(companies)
    create_database(db_name, params)
    print("База данных создана успешно")
    params.update({"dbname": db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                create_company_table(cur)
                print("Таблица companies создана успешно")
                create_vacancy_table(cur)
                print("Таблица vacancies создана успешно")
                insert_to_companies_table(cur, companies)
                print("Таблица companies заполнена")
                insert_to_vacancies_table(cur, vacancies_list)
                print("Таблица vacancies заполнена")
    finally:
        conn.close()

if __name__ == '__main__':
    main()

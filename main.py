from config import config
from utils.utils import *

companies = {2180: "Ozon", 1455: "HeadHunter", 1740: "Яндекс", 6093775: "Aston", 1329: "Европлан",
             67611: "Тензор", 733: "Ланит", 4759060: "HR Prime", 1532045: "CarPrice", 87021: "WILDBERRIES"}

db_name = "vacancies"

params = config()

def main():
    vacancies_list = get_vacancies(companies)
    create_database(db_name, params)
    print("База данных создана успешно")

if __name__ == '__main__':
    main()

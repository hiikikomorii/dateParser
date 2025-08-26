import requests
from bs4 import BeautifulSoup
from datetime import date,datetime
from colorama import init,Fore,Style,Back
import time

init(autoreset=True)
datee = date.today()
timee = datetime.now().strftime("%H:%M:%S")

def logo():
    print(f"""{Fore.LIGHTWHITE_EX}{Style.BRIGHT}
                                                  
                        ▀███▀▀▀██▄       ██     ███▀▀██▀▀███ ███▀▀▀███ 
                          ██    ▀██▄    ▄██▄    █▀   ██   ▀█  ██    ▀█ 
                          ██     ▀██   ▄█▀██▄        ██       ██   █   
                          ██      ██  ▄█  ▀██        ██       ██████   
                          ██     ▄██  ████████       ██       ██   █  ▄
                          ██    ▄██▀ █▀      ██      ██       ██     ▄█
                        ▄████████▀ ▄███▄   ▄████▄  ▄████▄   ▄██████████
                                              
                                    {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{datee} {timee}{Back.RESET}
""")

def logotext():
    print(f"""{Fore.LIGHTWHITE_EX}
      1 - Новый Год       2 - Рождество        3 - Старый новый Год      4 - Китайский новый Год
      5 - Пасха           6 - Крещение         7 - Крещение Руси         8 - Катол.Рождество
      9 - Зима            10 - Весна           11 - Лето                 12 - Осень
      13 - День ВДВ       14 - День ВВС        15 - Защита отечества     16 - День Победы
      17 - День знаний    18 - день учителя    19 - день студента        20 - день космонавтики   
                    
                                       21 - {Fore.LIGHTRED_EX}Exit""")

def clear():
    print("\n" * 8)

logo()
logotext()

while True:
    userchoice = input("введите цифру: ")

    if userchoice == "1":
        url = "https://calculator888.ru/skolko-dney-do-novogo-goda"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            date1 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date1.get_text(" ", strip=True)}")
            print(f"{Fore.LIGHTWHITE_EX}Дней до НГ: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(f"{Fore.LIGHTWHITE_EX}Часов до НГ: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "2":
        url = "https://calculator888.ru/skolko-dney/do-rozdestva/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date2 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date2.get_text(" ", strip=True)}")
            print(f"{Fore.LIGHTWHITE_EX}Дней до рождества: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(f"{Fore.LIGHTWHITE_EX}Часов до рождества: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "3":
        url = "https://calculator888.ru/skolko-dney/do-starogo-novogo-goda/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date3 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date3.get_text(" ", strip=True)}")
            print(f"{Fore.LIGHTWHITE_EX}Дней до old НГ: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(f"{Fore.LIGHTWHITE_EX}Часов до old НГ: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "4":
        url = "https://calculator888.ru/skolko-dney/do-kitayskiy-novyy-god/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date4 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date4.get_text(" ", strip=True)}")
            print(f"{Fore.LIGHTWHITE_EX}Дней до China НГ: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(f"{Fore.LIGHTWHITE_EX}Часов до China НГ: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "5":
        url = "https://calculator888.ru/skolko-dney-do-pasha/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date5 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date5.get_text(" ", strip=True)}")
            print(f"{Fore.LIGHTWHITE_EX}Дней до Пасхи: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(f"{Fore.LIGHTWHITE_EX}Часов до Пасхи: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "6":
        url = "https://calculator888.ru/skolko-dney/do-kreshcheniye/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date6 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date6.get_text(" ", strip=True)}")
            print(f"{Fore.LIGHTWHITE_EX}Дней до Крещения: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(f"{Fore.LIGHTWHITE_EX}Часов до Крещения: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "7":
        url = "https://calculator888.ru/skolko-dney/do-den-kreshcheniya-rusi/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date7 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date7.get_text(" ", strip=True)}")
            print(f"{Fore.LIGHTWHITE_EX}Дней до Крещения Руси: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(f"{Fore.LIGHTWHITE_EX}Часов до Крещения Руси: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()

    elif userchoice == "8":
        url = "https://calculator888.ru/skolko-dney/do-katolicheskoye-rozhdestvo/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date8 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date8.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до Катол.Рождества: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до Катол.Рождества: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "9":
        url = "https://calculator888.ru/skolko-dney-do-zimy/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date9 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date9.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до Зимы: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до Зимы: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "9":
        url = "https://calculator888.ru/skolko-dney-do-zimy/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date9 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date9.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до Зимы: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до Зимы: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "10":
        url = "https://calculator888.ru/skolko-dney-do-vesny/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date10 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date10.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до Весны: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до Весны: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "11":
        url = "https://calculator888.ru/skolko-dney-do-leta/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date11 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date11.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до Лета: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до Лета: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "12":
        url = "https://calculator888.ru/skolko-dney-do-oseni/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date12 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date12.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до Осени: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до Осени: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "13":
        url = "https://calculator888.ru/skolko-dney/do-den-vdv/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date13 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date13.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до ВДВ: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до ВДВ: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "14":
        url = "https://calculator888.ru/skolko-dney/do-den-vvs/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date14 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date14.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до ВВС: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до ВВС: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "15":
        url = "https://calculator888.ru/skolko-dney/do-dnya-zashchitnika-otechestva/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date15 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date15.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до Защиты Отечества: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до Защиты Отечества: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "16":
        url = "https://calculator888.ru/skolko-dney-den-pobeda/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date16 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date16.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до Победы: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до Победы: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "17":
        url = "https://calculator888.ru/skolko-dney/do-den-znaniy/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date17 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date17.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до дня Знаний: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до дня Знаний: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "18":
        url = "https://calculator888.ru/skolko-dney/do-den-uchitelya/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date18 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date18.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до дня Учителя: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до дня Учителя: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "19":
        url = "https://calculator888.ru/skolko-dney/do-tatyanin-den/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date18 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date18.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до дня Студента: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до дня Студента: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "19":
        url = "https://calculator888.ru/skolko-dney/do-tatyanin-den/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date19 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date19.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до дня Студента: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до дня Студента: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "20":
        url = "https://calculator888.ru/skolko-dney/do-den-kosmonavtika/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            date18 = soup.find("div", class_="korp_skolko_do_datta")
            dni = soup.find("span", class_="korp_skolko_do_chsla_cifr_1")
            chas = soup.find("div", class_="korp_skolko_do_chs")

            print(
                f"{Fore.LIGHTWHITE_EX}Дата: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{date18.get_text(" ", strip=True)}")
            print(
                f"{Fore.LIGHTWHITE_EX}Дней до дня Космонавтики: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{dni.get_text(strip=True)} дней")
            print(
                f"{Fore.LIGHTWHITE_EX}Часов до дня Космонавтики: {Fore.RESET}{Back.LIGHTWHITE_EX}{Fore.BLACK}{chas.get_text(strip=True)}")
            input(f"{Fore.LIGHTGREEN_EX}{Back.BLACK}Enter{Back.RESET}: ")
            time.sleep(0.5)
            clear()
            logo()
            logotext()
        else:
            print("Ошибка:", response.status_code)
            break

    elif userchoice == "21":
        print(f"{Fore.LIGHTRED_EX}{Back.BLACK}выход")
        break

    else:
        print(f"{Fore.LIGHTRED_EX}{Back.BLACK}неверный выбор, попробуйте снова")

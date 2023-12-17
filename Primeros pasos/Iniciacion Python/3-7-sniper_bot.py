from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.coolmod.com/gigabyte-geforce-rtx-4090-windforce-24gb-gddr6x/"
session = HTMLSession()


def get_stock():
    while True:
        try:
            r = session.get(url)
            r.raise_for_status()  # Lanza una excepción si la solicitud falla
            buy_zone = r.html.find("#productbuybutton1")
            if buy_zone:
                print("HAY STOCK!!!")
                buy_product(url)
            else:
                print("Sigue sin haber stock")
        except Exception as e:
            print(f"Error: {e}")

        sleep(30)


def buy_product(url):
    # Iniciar el navegador (en este caso, Firefox)
    driver = webdriver.Firefox()
    driver.get(url)

    # Esperar a que la página se cargue completamente
    sleep(2)

    try:
        driver.find_element(By.CLASS_NAME, "fa-clipboard-check").click()
        driver.find_element(By.CLASS_NAME, "fa-times-circle").click()
        sleep(1)
        buy = driver.find_element(By.ID, "productbuybutton1")
        driver.execute_script("arguments[0].click();", buy)
        sleep(2)
        driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
        sleep(1)
        driver.find_element(By.CLASS_NAME, "fa-hand-point-right").click()

        driver.find_element(By.ID, "inputEmail").send_keys("leo@gmail.com")
        driver.find_element(By.ID, "inputPassword").send_keys("123456")
        driver.find_element(By.CLASS_NAME, "sendlogin").click()

    except:
        print("Error")


def main():
    get_stock()


if __name__ == "__main__":
    main()

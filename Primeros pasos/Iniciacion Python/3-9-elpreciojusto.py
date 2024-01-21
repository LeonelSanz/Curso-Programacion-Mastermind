import random
from io import BytesIO

from requests_html import HTMLSession
from speak_and_listen import speak, hear_me
from PIL import Image


def hear_price_and_get_number():
    while True:
        try:
            price = hear_me()
            price.replace(" $", "").replace(" dolares", "").replace(",", ".").replace(" con ", ".")
            final_price = float(price)
            print(final_price)
            return final_price
        except ValueError:
            speak("No te he entendido, repite")


def get_page_categories(session):
    main_site = session.get("https://www.coolmod.com/")
    return main_site.html.find(".subfamilyheadertittle")


def get_random_product_attributes(session, categories):
    category = random.choice(categories)

    while category.text == "Configura tu PC a Medida":
        category = random.choice(categories)

    list_page = session.get(list(category.absolute_links)[0])
    products_lists = list_page.html.find(".subcatcatcontainer")
    product_list = random.choice(products_lists)
    product_page = session.get(list(product_list.absolute_links)[0])

    products = product_page.html.find(".productflex")
    product = random.choice(products)
    product_details = session.get(list(product.absolute_links)[0])
    image_src = product_details.html.find("#productmainimageitem")[0].attrs["src"]
    product_name = product_details.html.find(".productTitle")[0].text
    product_price = product_details.html.find("#normalpricenumber")[0].text

    final_price = float(product_price.replace("$", "").replace(",", "."))

    return image_src, product_name, final_price


def show_img(session, image_src):
    img_downloaded = session.get(image_src)
    img = Image.open(BytesIO(img_downloaded.content))
    img.show()


def main():
    session = HTMLSession()

    speak("Bienvenido al precio justo, vamos a intentar adivinar los precios de algunos productos")

    page_categories = get_page_categories(session)
    image_src, product_name, final_price = get_random_product_attributes(session, page_categories)

    show_img(session, image_src)
    print(product_name)

    speak("El nombre del producto es: {}, cuanto crees que vale?".format(product_name))

    user_guess = input("Precio del producto:\n")

    print("El precio era: {}".format(final_price))
    speak("El precio era: {}".format(final_price))


if __name__ == "__main__":
    main()

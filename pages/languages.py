from selenium.webdriver.common.by import By

languages = {
    "ar": "acl uill alu",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "To kaká8l gaç eívar ádelo.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "gu47t boauct",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "0 carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
    "en-US": "Your basket is empty."
}

def get_language_from_ui(cart_message):
    for lang_code, lang_text in languages.items():
        if cart_message == lang_text:
            return lang_code

    return "unknown"
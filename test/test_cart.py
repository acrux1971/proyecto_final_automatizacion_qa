from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from utils.logger import logger


def test_cart(driver_logged):
    # Inicio de la prueba
    logger.info("Iniciando prueba: test_cart")

    driver = driver_logged


    # Agregar el primer producto disponible al carrito
    logger.info("Agregando el primer producto al carrito")
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    

    # Verificar que el contador del carrito se actualice
    logger.info("Verificando contador de productos en el carrito")
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador_cart.text == "1", "La cantidad de productos agregados al carrito no es correcta"

    logger.info("Contador del carrito actualizado correctamente")


    # Obtener el nombre del producto agregado
    logger.info("Obteniendo nombre del producto agregado")
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    logger.info(f"Producto seleccionado: {product_name}")


    # Navegar al carrito de compras
    logger.info("Accediendo al carrito de compras")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


    # Obtener el nombre del producto dentro del carrito
    logger.info("Obteniendo producto almacenado en el carrito")
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    logger.info(f"Producto encontrado en carrito: {cart_item}")


    # Verificar que el producto agregado sea el mismo que aparece en el carrito
    logger.info("Validando coincidencia del producto")
    assert cart_item == product_name, "El producto agregado no coincide"

    
    

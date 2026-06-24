from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from utils.data_reader import read_products_json
from utils.logger import logger


def test_cart_json(driver_logged):
    # Inicio de la prueba
    logger.info("Iniciando prueba: test_cart_json")

    # Crear instancias de las paginas
    logger.info("Creando instancia de InventoryPage")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Creando instancia de CartPage")
    cart_page = CartPage(driver_logged)

    # Cargar productos desde el archivo JSON
    logger.info("Leyendo productos desde el archivo JSON")
    productos = read_products_json()

    # Agregar cada producto al carrito
    for producto in productos:
        logger.info(
            f"Agregando producto al carrito: {producto['nombre']} "
            f"({producto['precio']})"
        )
        inventory_page.agregar_producto_por_nombre(producto["nombre"])

     # Navegar al carrito
    logger.info("Accediendo al carrito de compras")
    inventory_page.ir_al_carrito()

    # Obtener productos presentes en el carrito
    logger.info("Obteniendo productos del carrito")
    productos_carrito = cart_page.obtener_productos_carrito()

    # Verificar que todos los productos del JSON estén presentes
    logger.info("Validando productos agregados al carrito")

    for producto_json in productos:
        encontrado = False
        for producto_carrito in productos_carrito:
            if ( (producto_carrito["nombre"] == producto_json["nombre"]) and (producto_carrito["precio"] == producto_json["precio"])):
                encontrado = True
                logger.info(
                    f"Producto validado correctamente: "
                    f"{producto_json['nombre']}"
                )
                break

        assert encontrado, f"Producto incorrecto o faltante: {producto_json["nombre"]}"

    logger.info(
        f"Validacion completada. Se verificaron {len(productos)} productos."
    )
    logger.info("Finaliza prueba: test_cart_json")

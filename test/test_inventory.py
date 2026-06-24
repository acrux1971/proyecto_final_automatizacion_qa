from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page.inventory_page import InventoryPage
from page.login_page import LoginPage
from utils.logger import logger


def test_inventory_title(driver_logged):
    # Inicio de la prueba
    logger.info("Iniciando prueba: test_inventory_title")

    # Crear instancia de InventoryPage
    logger.info("Creando instancia de InventoryPage")
    inventory_page = InventoryPage(driver_logged)

    # Obtener título de la página
    logger.info("Obteniendo titulo de la pagina")
    titulo = inventory_page.obtener_titulo()

    # Verificar que el titulo sea el esperado
    logger.info("Validando titulo de la pagina")
    assert titulo == "Swag Labs", "El titulo de la pagina no es correcto"

    logger.info("Titulo validado correctamente")
    logger.info("Finaliza prueba: test_inventory_title")


def test_productos_visibles(driver_logged):
    # Inicio de la prueba
    logger.info("Iniciando prueba: test_productos_visibles")

     # Crear instancia de InventoryPage
    logger.info("Creando instancia de InventoryPage")
    inventory_page = InventoryPage(driver_logged)

    # Obtener listado de productos
    logger.info("Obteniendo listado de productos")
    productos = inventory_page.obtener_productos()

    # Verificar que existan productos visibles
    logger.info("Validando que existan productos en la pagina")
    assert len(productos) > 0, "No se encontraron productos visibles en el inventario"
    
    logger.info(f"Se encontraron {len(productos)} productos visibles")
    logger.info("Finaliza prueba: test_productos_visibles")


def test_ui_elements(driver_logged):
    # Inicio de la prueba
    logger.info("Iniciando prueba: test_ui_elements")

    # Crear instancia de InventoryPage
    logger.info("Creando instancia de InventoryPage")
    inventory_page = InventoryPage(driver_logged)

    # Validar presencia del menu
    logger.info("Verificando visibilidad del menu")
    assert inventory_page.menu_visible(), "El menu no esta presente en la pagina"

    logger.info("Menu visible correctamente")

    # Validar presencia del filtro
    logger.info("Verificando visibilidad del filtro de productos")
    assert inventory_page.filtro_visible(), "El filtro no esta presente en la pagina"

    logger.info("Filtro visible correctamente")
    logger.info("Finaliza prueba: test_ui_elements")
from page.login_page import LoginPage
from utils.logger import logger

def test_login_ok(driver):
    # Inicio de la prueba
    logger.info("Inicializando el driver para test_login_ok")

    # Crear instancia de la página Login
    logger.info("Creando instancia de LoginPage")
    login_page = LoginPage(driver)
    
    # Ingresar credenciales válidas
    logger.info("Ingresando credenciales validas")
    login_page.login("standard_user","secret_sauce")
    
    # Verificar que el usuario fue redirigido al inventario
    logger.info("Verificando redireccion a la pagina de inventario")
    assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"

    # Confirmar resultado exitoso   
    logger.info("Login exitoso. Se redirigio correctamente al inventario")
    logger.info("Finaliza test_login_ok")


def test_login_invalid_password(driver):
    # Inicio de la prueba
    logger.info("Inicializando el driver para test_login_invalid_password")

    # Crear instancia de la página Login
    logger.info("Creando instancia de LoginPage")
    login_page = LoginPage(driver)
    
    # Ingresar usuario válido con contraseña incorrecta
    logger.info("Ingresando usuario valido con contraseña invalida")
    login_page.login("standard_user","123456")

    # Obtener mensaje de error mostrado por la aplicacion
    logger.info("Obteniendo mensaje de error")
    error = login_page.get_error_message()

    # Validar que el mensaje sea el esperado
    logger.info("Verificando que el mensaje de error sea el esperado")

    assert "Epic sadface: Username and password do not match any user in this service" in error

    # Confirmar resultado esperado
    logger.info("Se mostro correctamente el mensaje de error por contraseña invalida")
    logger.info("Finaliza test_login_invalid_password")
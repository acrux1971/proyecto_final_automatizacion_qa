from page.login_page import LoginPage
from utils.data_reader import read_users_csv
import pytest
from utils.logger import logger


@pytest.mark.parametrize("user",read_users_csv())
def test_login(driver,user):
    # Inicio de la prueba para el usuario actual
    logger.info(f"Iniciando test de login para el usuario: {user['username']}")

    # Crear instancia de la pagina Login
    logger.info("Creando instancia de LoginPage")
    login_page = LoginPage(driver)

    # Ingresar credenciales del usuario
    logger.info(
        f"Ingresando credenciales para el usuario: {user['username']}"
    )
    login_page.login(user["username"],user["password"])

    logger.info("Intentando iniciar sesion")

    # Validación para usuarios con acceso validos
    if user["valid"] == "true":
        logger.info("Usuario marcado como valido")
        logger.info("Verificando redireccion a la pagina de inventario")

        assert "/inventory.html" in driver.current_url, (
            f"El usuario {user['username']} no fue redirigido al inventario"
        )

        logger.info(
            f"Login exitoso para el usuario: {user['username']}"
        )

    # Validacion para usuarios con acceso invalido
    else:
        logger.info("Usuario marcado como invalido")
        logger.info("Obteniendo mensaje de error")

        error = login_page.get_error_message()

        logger.info("Verificando mensaje de error esperado")

        assert "Epic sadface" in error, "El mensaje de error no es el esperado"

        logger.info("Se mostro correctamente el mensaje de error por credenciales invalidas")

    # Fin de la prueba
    logger.info(f"Finaliza test_login para el usuario: {user['username']}")   
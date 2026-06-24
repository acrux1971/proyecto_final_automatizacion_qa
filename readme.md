# Proyecto Final de Automatizacion QA - Natalia Castagnetto

## Descripcion

Proyecto de Automatizacion de Pruebas realizado con Python, Selenium WebDriver y Pytest.

Este proyecto tiene como objetivo automatizar pruebas funcionales del sitio web **Sauce Demo**, validando los principales flujos de usuario mediante pruebas automatizadas.


## Funcionalidades Implementadas

- Automatización del proceso de inicio de sesión con distintos usuarios.
- Validación de acceso exitoso y manejo de credenciales inválidas.
- Gestión del carrito de compras:
    - Agregar productos al carrito.
    - Verificar la cantidad de productos agregados.
    - Validar la información de los productos seleccionados.
- Lectura de datos de prueba desde archivos CSV y JSON.
- Implementación del patrón Page Object Model (POM) para mejorar la mantenibilidad y reutilización del código.
- Uso de fixtures de Pytest para la configuración y cierre automático del navegador.
- Generación de logs para el seguimiento de la ejecución de las pruebas.
- Organización de pruebas mediante marcadores personalizados de Pytest (smoke, regression, api, etc.).

## Tecnologias utilizadas

- Python como lenguaje de programacion
- Pytest como framework de testing
- Selenium WebDriver para automatizacion de interfaces web 
- WebDriver Manager
- Pytest HTML para la generacion de reporte de tests
- JSON y CSV para datos de prueba
- Logging de Python
- Git para control de versiones
- GitHub como repositorio de codigo


## Instalacion

`git clone https://github.com/acrux1971/proyecto_final_automatizacion_qa.git`


## Instalacion dependencias

`pip install -r requirements.txt`


## Funcionamiento de las pruebas

- Test login: Prueba de validacion del acceso al sistema utilizando credenciales validas.
- Test inventory: Comprende la verificacion del titulo de la pagina, visualización de productos disponibles y verificacion de elementos en la interfaz: icono de menu y de filtro.
- Test cart: Validacion del proceso de agregado de productos al carrito, incluyendo que el contador se incremente correctamente y que el producto agregado sea el seleccionado en la pagina de inventario.
- Test login csv: Verifica el comportamiento del proceso de autenticación utilizando múltiples combinaciones de credenciales almacenadas en un archivo CSV.
- Test cart json: Verifica que los productos definidos en un archivo JSON sean agregados correctamente al carrito de compras y que la información mostrada coincida con los datos esperados.


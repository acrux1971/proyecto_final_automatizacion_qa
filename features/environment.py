from selenium import webdriver

# Los nombres de las funciones y los parametros que se pasan son palabras reservadas

def before_scenario(context,scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context,scenario):
    context.driver.quit()
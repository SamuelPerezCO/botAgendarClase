from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")

    # Ocultar los logs molestos de DevTools
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver_path = 'C:\\APPS\\ChromeDriver v138\\chromedriver-win64\\chromedriver.exe'
    
    # No mostrar logs del chromedriver
    service = Service(driver_path, log_path='NUL')  # En Linux/Mac sería '/dev/null'

    driver = webdriver.Chrome(service=service, options=options)

    driver.set_window_position(0, 0)   
    driver.maximize_window()

    driver.get('https://schoolpack.smart.edu.co/idiomas/alumnos.aspx')

    return driver

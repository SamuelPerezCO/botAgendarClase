from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")

    driver_path = 'C:\\APPS\\ChromeDriver v138\\chromedriver-win64\\chromedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.set_window_position(0, 0)   
    driver.maximize_window()

    # Initialization of the browser
    driver.get('https://schoolpack.smart.edu.co/idiomas/alumnos.aspx')

    return driver
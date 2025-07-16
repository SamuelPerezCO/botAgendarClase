from config import USER , PASSWORD
from logger.utils.logger_config import logger
import tasks
import driver_setup

driver = driver_setup.setup()

logger.info("-" * 25 + "INICIO" + "-" * 25)

tasks.login(USER ,PASSWORD ,driver)
tasks.closePopUpAndClickOnSchedule(driver)
tasks.classList(driver)
tasks.scheduleClass(driver)
# tasks.scheduleBranchDayTime(driver)

logger.info("-" * 25 + "FIN" + "-" * 25)
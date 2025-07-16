from config import USER , PASSWORD
from logger.utils.logger_config import logger
import tasks
import driver_setup

logger.info("Empezo el logger")

driver = driver_setup.setup()

tasks.login(USER ,PASSWORD ,driver)
tasks.closePopUpAndClickOnSchedule(driver)
tasks.classList(driver)
tasks.scheduleClass(driver)
# tasks.scheduleBranchDayTime(driver)
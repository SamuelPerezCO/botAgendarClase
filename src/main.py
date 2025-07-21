from logger.utils.logger_config import logger
from config import USER , PASSWORD
import driver_setup
import tasks

driver = driver_setup.setup()

logger.info("-" * 25 + "INICIO" + "-" * 25)

tasks.login(USER ,PASSWORD ,driver)
tasks.closePopUpAndClickOnSchedule(driver)
tasks.classList(driver)
#Le tengo que enviar la clase
tasks.scheduleClass(driver)
tasks.scheduleBranchDayTime(driver)
tasks.outOfWebPage(driver)

logger.info("-" * 25 + "FIN" + "-" * 25)

# if __name__ == "__main__":
#     main()
from config import USER , PASSWORD
import tasks
import driver_setup

driver = driver_setup.setup()

tasks.login(USER ,PASSWORD ,driver)
tasks.closePopUpAndClickOnSchedule(driver)
tasks.classList(driver)
tasks.scheduleClass(driver)
# tasks.scheduleBranchDayTime(driver)
from config import USER , PASSWORD
import tasks
import driver_setup

driver = driver_setup.setup()

tasks.login(USER=USER , PASSWORD=PASSWORD ,driver=driver)
tasks.closePopUpAndClickOnSchedule(driver=driver)
tasks.classList(driver=driver)
tasks.scheduleClass(driver)
# tasks.scheduleBranchDayTime()
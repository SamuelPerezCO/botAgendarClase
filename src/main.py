from config import USER , PASSWORD
import tasks

tasks.login(USER=USER , PASSWORD=PASSWORD)
tasks.closePopUpAndClickOnSchedule()
tasks.classList()
tasks.openMenuClasses()
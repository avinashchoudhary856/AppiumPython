from Pages.BasePage import BasePage
from Utilities.scroll_util import ScrollUtil


class VillasScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def searchVilla(self, city):
        self.click("area_XPATH")
        self.type("searchtext_ID", city)
        self.clickIndex("selectlocation_ID", 0)
        self.click("fromDate_XPATH")
        self.click("toDate_XPATH")
        # self.click("continue_XPATH")
        ScrollUtil.scrollToTextByAndroidUIAutomator("CONTINUE", self.driver)
        self.click("viewstays_XPATH")

        #ScrollUtil.scrollToTextByAndroidUIAutomator("Shubham Vilas", driver)

# encoding = utf-8
import unittest
from Libs.login import Login
from selenium import webdriver
from Libs.get_selector import GetSelector
from time import sleep
from utx import *


class HomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = r"C:\Users\glimmer.zhang\Documents\Python\HD Automation\config\home_page.json"
        cls.s = GetSelector(cls.config_path)
        cls.v = cls.s.get_selector()
        cls.driver = webdriver.Chrome()
        cls.browser = Login(cls.driver).login()

    def test_LearnToRide(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["LearnToRide"])
        b = a.get_attribute('textContent')
        log.debug("Learn To Ride: %s" % b)
        self.assertEqual("Learn To Ride ", b)

        a.click()
        sleep(5)

        c = driver.find_element_by_css_selector(v["LearnToRide"]).get_attribute("data-dropdown")
        log.debug("Learn To Ride drop down: %s" % c)
        self.assertEqual("learn-to-ride-dropdown", c)

        d = driver.find_element_by_css_selector(v["LearnToRide_dropdown"]).get_attribute("style")
        log.debug("Learn To Ride style: %s" % d)
        self.assertIn("display: block", d)

    def test_NewToRiding(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["NewToRiding"]).get_attribute("textContent")
        log.debug("New To Riding: %s" % a)
        self.assertEqual("New To Riding", a)

    def test_SkillsPractice(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["SkillsPractice"]).get_attribute("textContent")
        log.debug("Skills Practice: %s" % a)
        self.assertEqual("Skilled Rider - Skills Practice", a)

    def test_LicenseWaiver(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["LicenseWaiver"]).get_attribute("textContent")
        log.debug("License Waiver: %s" % a)
        self.assertEqual("Skilled Rider - License Waiver", a)

    def test_3WheeledRiding(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["3WheeledRiding"]).get_attribute("textContent")
        log.debug("3 Wheeled Riding: %s" % a)
        self.assertEqual("3 Wheeled Riding", a)

    def test_Explore(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Explore"])
        b = a.get_attribute("textContent")
        log.debug("Explore: %s" % b)
        self.assertEqual("Explore ", b)

        a.click()
        sleep(3)

        c = driver.find_element_by_css_selector(v["Explore_dropdown"]).get_attribute("style")
        log.debug("Explore style: %s" % c)
        self.assertIn("display: block", c)

    def test_DiscoverHD(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["DiscoverHD"]).get_attribute("textContent")
        log.debug("Discover HD: %s" % a)
        self.assertEqual("Discover H-D", a)

    def test_HDApp(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["HDApp"]).get_attribute("textContent")
        log.debug("HD App: %s" % a)
        self.assertEqual("H-D App", a)

    def test_XGames(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["XGames"]).get_attribute("textContent")
        log.debug("XGame: %s" % a)
        self.assertEqual("X Games", a)

    def test_FactoryTours(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["FactoryTours"]).get_attribute("textContent")
        log.debug("Factory Tours: %s" % a)
        self.assertEqual("Factory Tours", a)

    def test_HDHistory(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["HDHistory"]).get_attribute("textContent")
        log.debug("HD History: %s" % a)
        self.assertEqual("H-D History", a)

    def test_StayInTheKnow(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["StayInTheKnow"]).get_attribute("textContent")
        log.debug("Stay In The Know: %s" % a)
        self.assertEqual("Stay in the Know", a)

    def test_Events(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Events"]).get_attribute("textContent")
        log.debug("Events: %s" % a)
        self.assertEqual("Events", a)

    def test_EventsCalendar(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["EventsCalendar"]).get_attribute("textContent")
        log.debug("Events Calendar: %s" % a)
        self.assertEqual("Events Calendar", a)

    def test_OpenHouse(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["OpenHouse"]).get_attribute("textContent")
        log.debug("Open House: %s" % a)
        self.assertEqual("Open House", a)

    def test_Sturgis(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Sturgis"]).get_attribute("textContent")
        log.debug("Sturgis: %s" % a)
        self.assertEqual("Sturgis", a)

    def test_DaytonaBikeWeek(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["DaytonaBikeWeek"]).get_attribute("textContent")
        log.debug("Daytona Bike Week: %s" % a)
        self.assertEqual("Daytona Bike week", a)

    @skip(r"removed")
    def test_InternationalMotorcycleShow(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["InternationalMotorcycleShow"]).get_attribute("textContent")
        log.debug("International Motorcycle Show: %s" % a)
        self.assertEqual("International Motorcycle Show", a)

    def test_Racing(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["InternationalMotorcycleShow"]).get_attribute("textContent")
        log.debug("Racing: %s" % a)
        self.assertEqual("Racing", a)

    def test_RidePlanning(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["RidePlanning"]).get_attribute("textContent")
        log.debug("Ride Planning: %s" % a)
        self.assertEqual("Ride Planning", a)

    def test_PlanYourRoute(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["PlanYourRoute"]).get_attribute("textContent")
        log.debug("Plan Your Route: %s" % a)
        self.assertEqual("Plan Your Route", a)

        b = driver.find_element_by_css_selector(v["PlanYourRoute"]).get_attribute("target")
        log.debug("target: %s" % b)
        self.assertEqual("_blank", b)

        # c = driver.find_element_by_css_selector(v["PlanYourRoute_icon"]).is_displayed()
        # self.assertIs(c, True)

    def test_RoadTripTips(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["RoadTripTips"]).get_attribute("textContent")
        log.debug("Road Trip Tips: %s" % a)
        self.assertEqual("Road Trip Tips", a)

    def test_CampingTips(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["CampingTips"]).get_attribute("textContent")
        log.debug("Camping Tips: %s" % a)
        self.assertEqual("Camping Tips", a)

    def test_RentalsTours(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["RentalsTours"]).get_attribute("textContent")
        log.debug("Rentals Tours: %s" % a)
        self.assertEqual("Rentals & Tours", a)

    def test_RentAHarley(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["RentAHarley"]).get_attribute("textContent")
        log.debug("Rent A Harley: %s" % a)
        self.assertEqual("Rent a Harley", a)

    def test_MotorcycleTours(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["MotorcycleTours"]).get_attribute("textContent")
        log.debug("Motorcycle Tours: %s" % a)
        self.assertEqual("Motorcycle Tours", a)

    def test_RentABike(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["RentABike"]).get_attribute("textContent")
        log.debug("Rent A Bike: %s" % a)
        self.assertEqual("Rent a Bike", a)

        b = driver.find_element_by_css_selector(v["RentABike"]).get_attribute("href")
        log.debug("Rent A Bike link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/rent-a-bike.html", b)

        c = driver.find_element_by_css_selector(v["RentABike"]).get_attribute("target")
        log.debug("Rent A Bike target: %s" % c)
        self.assertEqual("_self", c)

    def test_Owners(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Owners"])

        b = a.get_attribute("textContent")
        log.debug("Owners: %s" % b)
        self.assertEqual("Owners ", b)

        c = driver.find_element_by_css_selector(v["Owners"]).get_attribute("data-dropdown")
        log.debug("Owners class drop down: %s" % c)
        self.assertIn("owners-dropdown", c)

        a.click()
        sleep(3)

        d = driver.find_element_by_css_selector(v["Owners_dropdown"]).get_attribute("style")
        log.debug("Owners style: %s" % d)
        self.assertIn("display: block", d)

    def test_FinanceInsurance(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["FinanceInsurance"]).get_attribute("textContent")
        log.debug("Finance Insurance: %s" % a)
        self.assertEqual("Finance & Insurance", a)

        b = driver.find_element_by_css_selector(v["FinanceInsurance"]).get_attribute("target")
        log.debug("Finance Insurance target: %s" % b)
        self.assertEqual("_self", b)

        c = driver.find_element_by_css_selector(v["FinanceInsurance"]).get_attribute("href")
        log.debug("Finance Insurance link: %s" % c)
        self.assertEqual("https://www.harley-davidson.com/us/en/owners/financing-and-insurance.html", c)

    def test_MakeAPayment(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["MakeAPayment"]).get_attribute("textContent")
        log.debug("Make A Payment: %s" % a)
        self.assertEqual("Make a Payment", a)

        b = driver.find_element_by_css_selector(v["MakeAPayment"]).get_attribute("target")
        log.debug("Make A Payment target: %s" % b)
        self.assertEqual("_blank", b)

        # c = driver.find_element_by_css_selector(v["MakeAPayment_icon"]).is_displayed()
        # self.assertIs(c, True)

    def test_OffersFinancing(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["OffersFinancing"]).get_attribute("textContent")
        log.debug("Offers Financing: %s" % a)
        self.assertEqual("Offers & Financing", a)

    def test_PrivatePartyFinancing(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["PrivatePartyFinancing"]).get_attribute("textContent")
        log.debug("Private Party Financing: %s" % a)
        self.assertEqual("Private Party Financing", a)

    def test_MotorcycleInsurance(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["MotorcycleInsurance"]).get_attribute("textContent")
        log.debug("Motorcycle Insurance: %s" % a)
        self.assertEqual("Motorcycle Insurance", a)

        b = driver.find_element_by_css_selector(v["MotorcycleInsurance"]).get_attribute("target")
        log.debug("Motorcycle Insurance target: %s" % b)
        self.assertEqual("_blank", b)

        # c = driver.find_element_by_css_selector(v["MotorcycleInsurance_icon"]).is_displayed()
        # self.assertIs(c, True)

    def test_ExtendedService(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ExtendedService"]).get_attribute("textContent")
        log.debug("Extended Service: %s" % a)
        self.assertEqual("Extended Service", a)

    def text_ProtectionPlans(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ProtectionPlans"]).get_attribute("textContent")
        log.debug("Protection Plans: %s" % a)
        self.assertEqual("Protection Plans", a)

    def test_CreditCard(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["CreditCard"]).get_attribute("textContent")
        log.debug("Credit Card: %s" % a)
        self.assertEqual("Credit Card", a)

        b = driver.find_element_by_css_selector(v["CreditCard"]).get_attribute("target")
        log.debug("Credit Card target: %s" % b)
        self.assertEqual("_blank", b)

        # c = driver.find_element_by_css_selector(v["CreditCard_icon"]).is_displayed()
        # self.assertIs(c, True)

    def test_MotorcycleMaintenanceService(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["MotorcycleMaintenanceService"]).get_attribute("textContent")
        log.debug("Motorcycle Maintenance & Service: %s" % a)
        self.assertEqual("Motorcycle Maintenance & Service", a)

        b = driver.find_element_by_css_selector(v["MotorcycleMaintenanceService"]).get_attribute("target")
        log.debug("Motorcycle Maintenance & Service target: %s" % b)
        self.assertEqual("_self", b)

        c = driver.find_element_by_css_selector(v["MotorcycleMaintenanceService"]).get_attribute("href")
        log.debug("Motorcycle Maintenance & Service link: %s" % c)
        self.assertEqual("https://www.harley-davidson.com/us/en/owners/motorcycle-maintenance.html", c)

    def test_HDAuthorizedService(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["HDAuthorizedService"]).get_attribute("textContent")
        log.debug("HD Authorized Service: %s" % a)
        self.assertEqual("H-D Authorized Service", a)

    def test_OwnersManuals(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["OwnersManuals"]).get_attribute("textContent")
        log.debug("Owner's Manuals: %s" % a)
        self.assertEqual("Owner's Manuals", a)

        b = driver.find_element_by_css_selector(v["OwnersManuals"]).get_attribute("target")
        log.debug("Owner's Manuals: %s" % b)
        self.assertEqual("_blank", b)

        # c = driver.find_element_by_css_selector(v["OwnersManuals_icon"]).is_displayed()
        # self.assertIs(c, True)

    def test_MaintenanceSchedules(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["MaintenanceSchedules"]).get_attribute("textContent")
        log.debug("Maintenance Schedules: %s" % a)
        self.assertEqual("Maintenance Schedules", a)

        b = driver.find_element_by_css_selector(v["MaintenanceSchedules"]).get_attribute("target")
        log.debug("Maintenance Schedules: %s" % b)
        self.assertEqual("_blank", b)

        # c = driver.find_element_by_css_selector(v["MaintenanceSchedules_icon"]).is_displayed()
        # self.assertIs(c, True)

    def test_ServiceRecall(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ServiceRecall"]).get_attribute("textContent")
        log.debug("Service Recall: %s" % a)
        self.assertEqual("Service Recall", a)

    def test_HarleyOwnersGroup(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["HarleyOwnersGroup"]).get_attribute("textContent")
        log.debug("Harley Owners Group: %s" % a)
        self.assertEqual("Harley Owners Group", a)

        b = driver.find_element_by_css_selector(v["HarleyOwnersGroup"]).get_attribute("target")
        log.debug("Harley Owners Group target: %s" % b)
        self.assertEqual("_self", b)

        c = driver.find_element_by_css_selector(v["HarleyOwnersGroup"]).get_attribute("href")
        log.debug("Harley Owners Group link: %s" % c)
        self.assertEqual("https://www.harley-davidson.com/us/en/owners/hog.html", c)

    def test_MembershipTypes(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["MembershipTypes"]).get_attribute("textContent")
        log.debug("Membership Types: %s" % a)
        self.assertEqual("Membership Types", a)

    def test_MembershipBenefits(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["MembershipBenefits"]).get_attribute("textContent")
        log.debug("Membership Benefits: %s" % a)
        self.assertEqual("Membership Benefits", a)

    def test_HOGMemberEvents(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["HOGMemberEvents"]).get_attribute("textContent")
        log.debug("HOG Member Events: %s" % a)
        self.assertEqual("HOG Member Events", a)

    def test_LocalChapters(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["LocalChapters"]).get_attribute("textContent")
        log.debug("Local Chapters: %s" % a)
        self.assertEqual("Local Chapters", a)

    def test_AudioNavigationSoftware(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["AudioNavigationSoftware"]).get_attribute("textContent")
        log.debug("Audio & Navigation Software: %s" % a)
        self.assertEqual("Audio & Navigation Software", a)

        b = driver.find_element_by_css_selector(v["AudioNavigationSoftware"]).get_attribute("target")
        log.debug("Audio & Navigation Software target: %s" % b)
        self.assertEqual("_self", b)

        c = driver.find_element_by_css_selector(v["AudioNavigationSoftware"]).get_attribute("href")
        log.debug("Audio & Navigation Software link: %s" % c)
        self.assertEqual("https://www.harley-davidson.com/us/en/owners/audio-navigation.html", c)

    def test_BoxGTS(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["BoxGTS"]).get_attribute("textContent")
        log.debug("Box GTS: %s" % a)
        self.assertEqual("Boom!™ Box GTS", a)

    def test_BoxGT(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["BoxGT"]).get_attribute("textContent")
        log.debug("Box GT: %s" % a)
        self.assertEqual("Boom!™ Box 6.5GT", a)

    def test_Box(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Box"]).get_attribute("textContent")
        log.debug("Box: %s" % a)
        self.assertEqual("Boom!™ Box 4.3", a)

    def test_HarmanKardonAudio(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["HarmanKardonAudio"]).get_attribute("textContent")
        log.debug("Harman/Kardon® Audio: %s" % a)
        self.assertEqual("Harman/Kardon® Audio", a)

    def test_RoadTech(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["RoadTech"]).get_attribute("textContent")
        log.debug("Road Tech: %s" % a)
        self.assertEqual("Road Tech™ Zumo® GPS", a)

    def test_WirelessConnectivity(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["WirelessConnectivity"]).get_attribute("textContent")
        log.debug("Wireless Connectivity: %s" % a)
        self.assertEqual("Wireless Connectivity", a)

    def test_EnginePrograms(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["EnginePrograms"]).get_attribute("textContent")
        log.debug("Engine Programs: %s" % a)
        self.assertEqual("Engine Programs", a)

        b = driver.find_element_by_css_selector(v["EnginePrograms"]).get_attribute("target")
        log.debug("Engine Programs target: %s" % b)
        self.assertEqual("_self", b)

        c = driver.find_element_by_css_selector(v["EnginePrograms"]).get_attribute("href")
        log.debug("EnginePrograms link: %s" % c)
        self.assertEqual("https://www.harley-davidson.com/us/en/owners/engines.html", c)

    def test_LongBlockEngineProgram(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["LongBlockEngineProgram"]).get_attribute("textContent")
        log.debug("LongBlock Engine Program: %s" % a)
        self.assertEqual("Longblock Engine Program", a)

    def test_CompleteCrateEngines(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["CompleteCrateEngines"]).get_attribute("textContent")
        log.debug("CompleteCrateEngines: %s" % a)
        self.assertEqual("Complete Crate Engines", a)

        b = driver.find_element_by_css_selector(v["Owners"])
        b.click()
        sleep(3)

    def test_Museum(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Museum"]).get_attribute("textContent")
        log.debug("Museum: %s" % a)
        self.assertEqual("Museum", a)

        b = driver.find_element_by_css_selector(v["Museum"]).get_attribute("target")
        log.debug("Museum target: %s" % b)
        self.assertEqual("_self", b)

        c = driver.find_element_by_css_selector(v["Museum"]).get_attribute("href")
        log.debug("Museum link: %s" % c)
        self.assertEqual("https://www.harley-davidson.com/us/en/museum.html", c)

    def test_Motorcycles(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Motorcycles"]).get_attribute("textContent")
        log.debug("Motorcycles: %s" % a)
        self.assertIn("Motorcycles", a)
        b = driver.find_element_by_css_selector(v["Motorcycles"]).get_attribute("target")
        log.debug("Motorcycles target: %s" % b)
        self.assertEqual("_self", b)

        c = driver.find_element_by_css_selector(v["Motorcycles"]).get_attribute("href")
        log.debug("Motorcycles link: %s" % c)
        self.assertEqual("https://www.harley-davidson.com/us/en/motorcycles/index.html", c)

        d = driver.find_element_by_css_selector(v["Motorcycles_icon"]).is_displayed()
        self.assertIs(d, True)

    def test_ShoppingTools(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ShoppingTools"])
        b = driver.find_element_by_css_selector(v["ShoppingTools"]).get_attribute("textContent")
        log.debug("Shopping Tools: %s" % b)
        self.assertIn("Shopping Tools", b)

        a.click()
        sleep(3)

        c = driver.find_element_by_css_selector(v["ShoppingTools_dropdown"]).get_attribute("style")
        log.debug("Shopping Tools style: %s" % c)
        self.assertIn("display: block", c)

        d = driver.find_element_by_css_selector(v["ShoppingTools_icon"]).is_displayed()
        self.assertIs(d, True)

    def test_CompareBikes(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["CompareBikes"]).get_attribute("textContent")
        log.debug("Compare Bikes: %s" % a)
        self.assertIn("Compare Bikes", a)

        b = driver.find_element_by_css_selector(v["CompareBikes"]).get_attribute("href")
        log.debug("Compare Bikes link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/tools/compare-bikes.html", b)

        c = driver.find_element_by_css_selector(v["CompareBikes_icon"]).is_displayed()
        self.assertIs(c, True)

    def test_EstimatePayment(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["EstimatePayment"]).get_attribute("textContent")
        log.debug("Estimate Payment: %s" % a)
        self.assertIn("Estimate payment", a)

        b = driver.find_element_by_css_selector(v["EstimatePayment"]).get_attribute("href")
        log.debug("Estimate Payment link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/tools/estimate-payment.html", b)

        c = driver.find_element_by_css_selector(v["EstimatePayment_icon"]).is_displayed()
        self.assertIs(c, True)

    def test_ScheduleATestRide(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ScheduleATestRide"]).get_attribute("textContent")
        log.debug("Schedule A Test Ride: %s" % a)
        self.assertIn("Schedule A Test Ride", a)

        b = driver.find_element_by_css_selector(v["ScheduleATestRide"]).get_attribute("href")
        log.debug("Schedule A Test Ride link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/tools/test-ride.html", b)

        c = driver.find_element_by_css_selector(v["ScheduleATestRide_icon"]).is_displayed()
        self.assertIs(c, True)

    def test_OffersFinancing1(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["OffersFinancing1"]).get_attribute("textContent")
        log.debug("Offers Financing: %s" % a)
        self.assertIn("Offers & Financing", a)

        b = driver.find_element_by_css_selector(v["OffersFinancing1"]).get_attribute("href")
        log.debug("Offers & Financing link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/owners/financing-and-insurance/finance-your-ride.html",
                         b)

        c = driver.find_element_by_css_selector(v["OffersFinancing1_icon"]).is_displayed()
        self.assertIs(c, True)

    def test_ApplyForCredit(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ApplyForCredit"]).get_attribute("textContent")
        log.debug("Apply For Credit: %s" % a)
        self.assertIn("Apply For Credit", a)

        b = driver.find_element_by_css_selector(v["ApplyForCredit"]).get_attribute("href")
        log.debug("Apply For Credit link: %s" % b)
        self.assertEqual("https://creditapplication.harley-davidson.com/", b)

        c = driver.find_element_by_css_selector(v["ApplyForCredit"]).get_attribute("target")
        log.debug("Apply For Credit target: %s" % c)
        self.assertEqual("_blank", c)

        d = driver.find_element_by_css_selector(v["ApplyForCredit_icon"]).is_displayed()
        self.assertIs(d, True)

        e = driver.find_element_by_css_selector(v["ApplyForCredit_icon1"]).is_displayed()
        self.assertIs(e, True)

    def test_FindADealer(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["FindADealer"]).get_attribute("textContent")
        log.debug("Find A Dealer: %s" % a)
        self.assertIn("Find A Dealer", a)

        b = driver.find_element_by_css_selector(v["FindADealer"]).get_attribute("href")
        log.debug("Find A Dealer link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/tools/find-a-dealer.html", b)

        c = driver.find_element_by_css_selector(v["FindADealer_icon"]).is_displayed()
        self.assertIs(c, True)

    def test_GetACatalog(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["GetACatalog"]).get_attribute("textContent")
        log.debug("Get A Catalog: %s" % a)
        self.assertIn("Get A Catalog", a)

        b = driver.find_element_by_css_selector(v["GetACatalog"]).get_attribute("href")
        log.debug("Get A Catalog link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/tools/get-a-catalog.html", b)

        c = driver.find_element_by_css_selector(v["GetACatalog_icon"]).is_displayed()
        self.assertIs(c, True)

    def test_PartsAccessories(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["PartsAccessories"])
        b = driver.find_element_by_css_selector(v["PartsAccessories"]).get_attribute("textContent")
        log.debug("Parts & Accessories: %s" % b)
        self.assertIn("Parts & Accessories", b)

        a.click()
        sleep(3)

        c = driver.find_element_by_css_selector(v["PartsAccessories_dropdown"]).get_attribute("style")
        log.debug("Parts & Accessories style: %s" % c)
        self.assertIn("display: block", c)

        d = driver.find_element_by_css_selector(v["PartsAccessories_icon"]).is_displayed()
        self.assertIs(d, True)

    def test_ShopAll(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ShopAll"]).get_attribute("textContent")
        log.debug("Shop All: %s" % a)
        self.assertIn("Shop All", a)

        b = driver.find_element_by_css_selector(v["ShopAll"]).get_attribute("href")
        log.debug("Shop All link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/shop/motorcycle-parts-accessories", b)

        c = driver.find_element_by_css_selector(v["ShopAll"]).get_attribute("target")
        log.debug("Shop All target: %s" % c)
        self.assertEqual("_blank", c)

        # d = driver.find_element_by_css_selector(v["ShopAll_icon"]).is_displayed()
        # self.assertIs(d, True)

    def test_NewArrivals(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["NewArrivals"]).get_attribute("textContent")
        log.debug("New Arrivals: %s" % a)
        self.assertIn("New Arrivals", a)

        b = driver.find_element_by_css_selector(v["NewArrivals"]).get_attribute("href")
        log.debug("New Arrivals: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/shop/motorcycle-parts-accessories-new-arrivals", b)

        c = driver.find_element_by_css_selector(v["NewArrivals"]).get_attribute("target")
        log.debug("Shop All target: %s" % c)
        self.assertEqual("_blank", c)

        # d = driver.find_element_by_css_selector(v["NewArrivals_icon"]).is_displayed()
        # self.assertIs(d, True)

    def test_Gifts(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Gifts"]).get_attribute("textContent")
        log.debug("Gifts: %s" % a)
        self.assertIn("Gifts", a)

        b = driver.find_element_by_css_selector(v["Gifts"]).get_attribute("href")
        log.debug("Gifts: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/shop/gifts-for-the-bike", b)

        c = driver.find_element_by_css_selector(v["Gifts"]).get_attribute("target")
        log.debug("Gifts: %s" % c)
        self.assertEqual("_blank", c)

    def test_ClothingGear(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ClothingGear"])
        b = driver.find_element_by_css_selector(v["ClothingGear"]).get_attribute("textContent")
        log.debug("Clothing & Gears: %s" % b)
        self.assertIn("Clothing & Gear", b)

        a.click()
        sleep(3)

        c = driver.find_element_by_css_selector(v["ClothingGear_dropdown"]).get_attribute("style")
        log.debug("Clothing & Gear style: %s" % c)
        self.assertIn("display: block", c)

        d = driver.find_element_by_css_selector(v["ClothingGear_icon"]).is_displayed()
        self.assertIs(d, True)

    def test_ShopAll_CG(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["ShopAll_CG"]).get_attribute("textContent")
        log.debug("Shop All: %s" % a)
        self.assertIn("Shop All", a)

        b = driver.find_element_by_css_selector(v["ShopAll_CG"]).get_attribute("href")
        log.debug("Shop All link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/store/", b)

        c = driver.find_element_by_css_selector(v["ShopAll"]).get_attribute("target")
        log.debug("Shop All target: %s" % c)
        self.assertEqual("_blank", c)

    def test_Men(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Men"]).get_attribute("textContent")
        log.debug("Men: %s" % a)
        self.assertIn("Men", a)

        b = driver.find_element_by_css_selector(v["Men"]).get_attribute("href")
        log.debug("Men link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/shop/mens-motorcycle-clothes", b)

        c = driver.find_element_by_css_selector(v["Men"]).get_attribute("target")
        log.debug("Men target: %s" % c)
        self.assertEqual("_blank", c)

    def test_Women(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Women"]).get_attribute("textContent")
        log.debug("Women: %s" % a)
        self.assertIn("Women", a)

        b = driver.find_element_by_css_selector(v["Women"]).get_attribute("href")
        log.debug("Women link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/shop/womens-motorcycle-clothes", b)

        c = driver.find_element_by_css_selector(v["Women"]).get_attribute("target")
        log.debug("Women target: %s" % c)
        self.assertEqual("_blank", c)

    def test_NewArrivals_CG(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["NewArrivals_CG"]).get_attribute("textContent")
        log.debug("New Arrivals: %s" % a)
        self.assertIn("New Arrivals", a)

        b = driver.find_element_by_css_selector(v["NewArrivals_CG"]).get_attribute("href")
        log.debug("New Arrivals link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/shop/new-arrival", b)

        c = driver.find_element_by_css_selector(v["NewArrivals_CG"]).get_attribute("target")
        log.debug("New Arrivals target: %s" % c)
        self.assertEqual("_blank", c)

    def test_Gifts_CG(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Gifts_CG"]).get_attribute("textContent")
        log.debug("Gifts: %s" % a)
        self.assertIn("Gifts", a)

        b = driver.find_element_by_css_selector(v["Gifts_CG"]).get_attribute("href")
        log.debug("Gifts link: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/shop/gifts", b)

        c = driver.find_element_by_css_selector(v["Gifts_CG"]).get_attribute("target")
        log.debug("Gifts target: %s" % c)
        self.assertEqual("_blank", c)

        d = driver.find_element_by_css_selector(v["ClothingGear"])
        d.click()
        sleep(3)

    def test_FindADealer_R(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["FindADealer_R"]).get_attribute("textContent")
        log.debug("Find A Dealer_R: %s" % a)
        self.assertIn("Find A Dealer", a)

        b = driver.find_element_by_css_selector(v["FindADealer_R"]).get_attribute("href")
        log.debug("FindADealer_R: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/tools/find-a-dealer.html", b)

        c = driver.find_element_by_css_selector(v["FindADealer_R"]).get_attribute("target")
        log.debug("Find A Dealer_R target: %s" % c)
        self.assertEqual("_self", c)

    def test_TestRide(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["TestRide"]).get_attribute("textContent")
        log.debug("Test Ride: %s" % a)
        self.assertIn("Test Ride", a)

        b = driver.find_element_by_css_selector(v["TestRide"]).get_attribute("href")
        log.debug("TestRide: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/tools/test-ride.html", b)

        c = driver.find_element_by_css_selector(v["TestRide"]).get_attribute("target")
        log.debug("TestRide target: %s" % c)
        self.assertEqual("_self", c)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(HomePage("test_NewArrivals"))
    runner = unittest.TextTestRunner()
    runner.run(suite)



# coding = utf-8
""" Author: Glimmer.Zhang@mullenloweprofero.com
    PROD Home Page test cases """
import unittest
from Libs.login import Login
from selenium import webdriver
from Libs.get_selector import GetSelector
from utx import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from Libs.driver import Driver


class HomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = r"C:\Users\glimmer.zhang\Documents\Python\HD Automation\config\home_page.json"
        cls.s = GetSelector(cls.config_path)
        cls.v = cls.s.get_selector()
        cls.driver = Driver.browser
        cls.browser = Login(cls.driver).login()

    def test_Logo(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["LogoHeader"])
        self.assertIs(a.is_displayed(), True)

    def test_LearnToRide(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["LearnToRide"])
        b = a.get_attribute("textContent")
        log.debug("Learn To Ride: %s" % b)
        self.assertEqual("Learn To Ride ", b)

        a.click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          v["LearnToRide_dropdown"])))

        c = driver.find_element_by_css_selector(v["LearnToRide_dropdown"]).get_attribute("style")
        log.debug("Learn To Ride style: %s" % c)
        self.assertIn("display: block", c)

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
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, v["Explore_dropdown"])))

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

    def test_LaconiaMotorcycleWeek(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["LaconiaMotorcycleWeek"]).get_attribute("textContent")
        log.debug("Laconia Motorcycle Week: %s" % a)
        self.assertEqual("Laconia Motorcycle Week", a)

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
        a = driver.find_element_by_css_selector(v["Racing"]).get_attribute("textContent")
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

        a.click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, v["Owners_dropdown"])))

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

    def test_ProtectionPlans(self):
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
        WebDriverWait(driver, 30).until(ec.invisibility_of_element((By.CSS_SELECTOR, v["Owners_dropdown"])))

        c = driver.find_element_by_css_selector(v["Owners_dropdown"]).get_attribute("style")
        self.assertIn("display: none", c)

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
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          v["ShoppingTools_dropdown"])))

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
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          v["PartsAccessories_dropdown"])))

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
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          v["ClothingGear_dropdown"])))

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
        WebDriverWait(driver, 30).until(ec.invisibility_of_element((By.CSS_SELECTOR,
                                                                    v["ClothingGear_dropdown"])))

    def test_FindADealer_R(self):
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["FindADealer_R"]).text
        log.debug("Find A Dealer_R: %s" % a)
        self.assertIn("FIND A DEALER", a)

        b = driver.find_element_by_css_selector(v["FindADealer_R"]).get_attribute("href")
        log.debug("FindADealer_R: %s" % b)
        self.assertEqual("https://www.harley-davidson.com/us/en/tools/find-a-dealer.html", b)

        c = driver.find_element_by_css_selector(v["FindADealer_R"]).get_attribute("target")
        log.debug("Find A Dealer_R target: %s" % c)
        self.assertEqual("_self", c)

        d = driver.find_element_by_css_selector(v["FindADealer_R_icon"])
        self.assertIs(d.is_displayed(), True)

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

        d = driver.find_element_by_css_selector(v["TestRide_icon"]).is_displayed()
        self.assertIs(d, True)

    def test_SignIn_Login(self):
        """登陆界面测试
        1. 输入错误密码，提示异常
        2. 登陆成功"""
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["SignIn"])

        b = a.get_attribute("textContent")
        log.debug("Sign In: %s" % b)
        self.assertIn("Sign In", b)

        c = driver.find_element_by_css_selector(v["SignIn_icon"]).is_displayed()
        self.assertIs(c, True)

        a.click()
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          v["LoginForm"])))

        # 输入错误的登陆信息
        driver.find_element_by_id(v["LoginForm_Email_id"]).send_keys("test@123.com")
        driver.find_element_by_id(v["LoginForm_Password_id"]).send_keys("123456")
        driver.find_element_by_css_selector(v["LoginForm_Submit"]).click()
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          v["LoginForm_Errormsg"])))

        # 输入正确的登陆信息
        driver.find_element_by_id(v["LoginForm_Email_id"]).clear()
        driver.find_element_by_id(v["LoginForm_Email_id"]).send_keys("xiang.zhang226@gmail.com")
        driver.find_element_by_id(v["LoginForm_Password_id"]).clear()
        driver.find_element_by_id(v["LoginForm_Password_id"]).send_keys("Heaven226!")
        driver.find_element_by_css_selector(v["LoginForm_Submit"]).click()

        WebDriverWait(driver, 10).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                          v["LoginText"]), "HI"))

    def test_SignIn_Logout(self):
        """登陆成功后，登出"""
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["SignIn"])
        a.click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          v["SignIn_dropdown"])))
        b = driver.find_element_by_css_selector(v["SignOut"])
        ActionChains(driver).click(b).perform()
        WebDriverWait(driver, 120).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, v["LoginText"]),
                                                                          "SIGN IN"))

    def test_Search(self):
        """搜索"""
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["Search"])
        self.assertEqual(a.text, "SEARCH")

        b = driver.find_element_by_css_selector(v["Search_icon"])
        self.assertIs(b.is_displayed(), True)

        # 搜索“Street”，跳转到搜索结果页面，然后点击返回首页
        c = driver.find_element_by_name(v["SearchField_name"])
        a.click()
        d = driver.find_element_by_css_selector(v["SearchButton"])
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR, v["QuickLinks"])))
        c.send_keys("Street")
        d.click()
        WebDriverWait(driver, 60).until(ec.title_is("Street | Harley-Davidson Search"))

        e = driver.find_element_by_css_selector(v["LogoHeader"])
        e.click()
        WebDriverWait(driver, 30).until(ec.title_is("Harley-Davidson USA"))

    def test_HeroMarquee(self):
        """checkpoint: 1. 自动播放
                       2. CTA button"""
        driver = self.driver
        v = self.v

        # 自动播放
        a = driver.find_element_by_css_selector(v["Video"])
        log.debug("autoplay : %s" % a.get_attribute("autoplay"))
        self.assertEqual(a.get_attribute("autoplay"), 'true')

        # SeeLiveWire CTA
        b = driver.find_element_by_css_selector(v["SeeLiveWire"])
        log.debug("SeeLiveWire href : %s" % b.get_attribute("href"))
        self.assertEqual(b.get_attribute("href"), "https://www.harley-davidson.com/us/en/"
                                                  "motorcycles/future-vehicles/livewire.html")
        self.assertEqual(b.get_attribute("target"), "_self")

        c = driver.find_element_by_css_selector(v["SeeLiveWireLabel"])
        log.debug("See LiveWire Label: %s" % c.get_attribute("textContent"))
        self.assertEqual(c.get_attribute("textContent"), "See Livewire")

        # PreOderNOW CTA
        d = driver.find_element_by_css_selector(v["PreOrderNow"])
        log.debug("PreOrderNow href: %s" % d.get_attribute("href"))
        self.assertEqual(d.get_attribute("href"), "https://www.harley-davidson.com/us/en/"
                                                  "motorcycles/future-vehicles/electric/dealer-locator.html")
        self.assertEqual(d.get_attribute("target"), "_self")

        e = driver.find_element_by_css_selector(v["PreOrderNowLabel"])
        log.debug("Pre OrderNow Label: %s" % e.get_attribute("textContent"))
        self.assertEqual(e.get_attribute("textContent"), "Pre-order now")

    def test_SeeWhatsComing(self):
        """Content CTA See What's Coming button"""
        driver = self.driver
        v = self.v
        a = driver.find_element_by_css_selector(v["SeeWhatsComing"])
        # CTA是否显示
        self.assertIs(a.is_displayed(), True)

        # 是否新窗口打开
        log.debug("target: %s" % a.get_attribute("target"))
        self.assertEqual(a.get_attribute("target"), "_self")

        # CTA链接
        log.debug("href: %s" % a.get_attribute("href"))
        self.assertEqual(a.get_attribute("href"), "https://www.harley-davidson.com/us/en/"
                                                  "about-us/more-roads.html#intcmp_HP-BB-MoreRoads")

    def test_PromoCard_1(self):
        """Promo Card component: card 1"""
        driver = self.driver
        v = self.v

        # image1 left
        image1 = driver.find_element_by_css_selector(v["PromoCard_image1"])
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CSS_SELECTOR, v["PromoCard_image1"])))
        driver.execute_script("arguments[0].scrollIntoView();", image1)
        self.assertIs(image1.is_displayed(), True)

        # image1 tag
        image1_tag = driver.find_element_by_css_selector(v["PromoCard_image1_tag"])
        log.debug("tag: %s" % image1_tag.get_attribute("textContent"))
        self.assertEqual(image1_tag.get_attribute("textContent"), "Genuine Merchandise")

        # image1 CTA
        image1_cta = driver.find_element_by_css_selector(v["PromoCard_image1_CTA"])
        log.debug("CTA: %s" % image1_cta.get_attribute("textContent"))
        log.debug("href: %s" % image1_cta.get_attribute("href"))
        self.assertEqual(image1_cta.get_attribute("textContent"), "Shop Now")
        self.assertEqual(image1_cta.get_attribute("href"), "https://www.harley-davidson.com/store/shop/new-arrival"
                                                           "?cm_sp=Desktop_HP-_-BB10-_-promo-_-MayNewArrivals")

    def test_PromoCard_2(self):
        """Promo Card component: card 2"""
        driver = self.driver
        v = self.v
        # image2 middle
        image2 = driver.find_element_by_css_selector(v["PromoCard_image2"])
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CSS_SELECTOR, v["PromoCard_image2"])))
        self.assertIs(image2.is_displayed(), True)

        # image2 tag
        image2_tag = driver.find_element_by_css_selector(v["PromoCard_image2_tag"])
        log.debug("tag: %s" % image2_tag.get_attribute("textContent"))
        self.assertEqual(image2_tag.get_attribute("textContent"), "H-D App")

        # image2 CTA
        image2_cta = driver.find_element_by_css_selector(v["PromoCard_image2_CTA"])
        log.debug("CTA: %s" % image2_cta.get_attribute("textContent"))
        log.debug("href: %s" % image2_cta.get_attribute("href"))
        self.assertEqual(image2_cta.get_attribute("textContent"), "Learn More")
        self.assertEqual(image2_cta.get_attribute("href"), "https://www.harley-davidson.com/us/en/explore/"
                                                           "discover/harley-davidson-app.html")

    def test_PromoCard_3(self):
        """Promo Card component: card 3"""
        driver = self.driver
        v = self.v
        # image3 right
        image3 = driver.find_element_by_css_selector(v["PromoCard_image3"])
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CSS_SELECTOR, v["PromoCard_image3"])))
        self.assertIs(image3.is_displayed(), True)

        # image3 tag
        image3_tag = driver.find_element_by_css_selector(v["PromoCard_image3_tag"])
        log.debug("tag: %s" % image3_tag.get_attribute("textContent"))
        self.assertEqual(image3_tag.get_attribute("textContent"), "Parts & Accessories")

        # image3 CTA
        image3_cta = driver.find_element_by_css_selector(v["PromoCard_image3_CTA"])
        log.debug("CTA: %s" % image3_cta.get_attribute("textContent"))
        log.debug("href: %s" % image3_cta.get_attribute("href"))
        self.assertEqual(image3_cta.get_attribute("textContent"), "Shop Lighting")
        self.assertEqual(image3_cta.get_attribute("href"), "https://www.harley-davidson.com/shop/motorcycle-lights"
                                                           "?cm_sp=Desktop_HP-_-BB10-_-promo-_-AprLighting")

    def test_GlobalFooter_Title1(self):
        """Global Footer: Stay In The Know"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["GlobalFooter_Title1"])
        driver.execute_script("arguments[0].scrollIntoView();", a)
        log.debug("title: %s" % a.text)
        self.assertEqual(a.text, "STAY IN THE KNOW")

    def test_GlobalFooter_Email(self):
        """Global Footer: Sign Up For Email"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["GlobalFooter_Mail"])
        log.debug("target: %s" % a.get_attribute("target"))
        log.debug("href: %s" % a.get_attribute("href"))
        self.assertEqual(a.get_attribute("target"), "_self")
        self.assertEqual(a.get_attribute("href"), "https://www.harley-davidson.com/us/en/profile/"
                                                  "email-subscribe-global.html")

        b = driver.find_element_by_css_selector(v["GlobalFooter_Mail_Label"])
        log.debug("text: %s" % b.text)
        self.assertEqual(b.text, "SIGN UP FOR EMAIL")

    def test_GlobalFooter_FaceBook(self):
        """Global Footer: FaceBook icon"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["FaceBook"])
        self.assertIs(a.is_displayed(), True)

        log.debug("target: %s" % a.get_attribute("target"))
        self.assertEqual(a.get_attribute("target"), "_blank")

        log.debug("href: %s" % a.get_attribute("href"))
        self.assertEqual(a.get_attribute("href"), "https://www.facebook.com/harley-davidson/")

    def test_GlobalFooter_Twitter(self):
        """Global Footer: Twitter icon"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["Twitter"])
        self.assertIs(a.is_displayed(), True)

        log.debug("target: %s" % a.get_attribute("target"))
        self.assertEqual(a.get_attribute("target"), "_blank")

        log.debug("href: %s" % a.get_attribute("href"))
        self.assertEqual(a.get_attribute("href"), "https://twitter.com/harleydavidson")

    def test_GlobalFooter_Instagram(self):
        """Global Footer: Instagram icon"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["Instagram"])
        self.assertIs(a.is_displayed(), True)

        log.debug("target: %s" % a.get_attribute("target"))
        self.assertEqual(a.get_attribute("target"), "_blank")

        log.debug("href: %s" % a.get_attribute("href"))
        self.assertEqual(a.get_attribute("href"), "https://www.instagram.com/harleydavidson")

    def test_GlobalFooter_Youtube(self):
        """Global Footer: Youtube icon"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["Youtube"])
        self.assertIs(a.is_displayed(), True)

        log.debug("target: %s" % a.get_attribute("target"))
        self.assertEqual(a.get_attribute("target"), "_blank")

        log.debug("href: %s" % a.get_attribute("href"))
        self.assertEqual(a.get_attribute("href"), "http://www.youtube.com/harleydavidson")

    def test_GlobalFooter_Pinterest(self):
        """Global Footer: Pinterest icon"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["Pinterest"])
        self.assertIs(a.is_displayed(), True)

        log.debug("target: %s" % a.get_attribute("target"))
        self.assertEqual(a.get_attribute("target"), "_blank")

        log.debug("href: %s" % a.get_attribute("href"))
        self.assertEqual(a.get_attribute("href"), "https://www.pinterest.com/harleydavidson/")

    def test_GlobalFooter_Title2(self):
        """Global Footer: About Us"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["GlobalFooter_Title2"])
        self.assertIs(a.is_displayed(), True)

        log.debug("text: %s" % a.text)
        self.assertEqual(a.text, "ABOUT US")

    def test_GlobalFooter_Title3(self):
        """Global Footer: Resources"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["GlobalFooter_Title3"])
        self.assertIs(a.is_displayed(), True)

        log.debug("text: %s" % a.text)
        self.assertEqual(a.text, "RESOURCES")

    def test_GlobalFooter_Icon(self):
        """Global Footer: Icon"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["GlobalFooter_Icon"])
        self.assertIs(a.is_displayed(), True)

    def test_GlobalFooter_Disclaimer(self):
        """Global Footer: Disclaimer"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["GlobalFooter_Disclaimer"])

        WebDriverWait(driver, 30).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, v["GlobalFooter_Disclaimer"])))
        a.click()
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.CSS_SELECTOR, v["Disclaimer"])))

        b = driver.find_element_by_css_selector(v["Disclaimer_button"])
        driver.execute_script("arguments[0].scrollIntoView();", b)
        self.assertIs(b.is_displayed(), True)

        close = driver.find_element_by_css_selector(v["Disclaimer_Close"])
        close.click()
        WebDriverWait(driver, 30).until(ec.invisibility_of_element_located((By.CSS_SELECTOR, v["Disclaimer"])))

    def test_GlobalFooter_SwitchCountries(self):
        """Global Footer: Switch Countries"""
        driver = self.driver
        v = self.v

        a = driver.find_element_by_css_selector(v["GlobalFooter_SwitchCountries"])
        driver.execute_script("arguments[0].scrollIntoView();", a)

        Select(a).select_by_value("/gb/en/")
        WebDriverWait(driver, 60).until(ec.title_is("Harley-Davidson UK"))
        log.debug("title: %s" % driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

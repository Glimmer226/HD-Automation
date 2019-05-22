# coding = utf-8
""" Author: Glimmer.Zhang@mullenloweprofero.com
    runner for the automation test """
from utx import *
import logging
from selenium import webdriver
import argparse
from Libs.driver import Driver


def main():
    parser = argparse.ArgumentParser(description="H-D Automation Testing",
                                     epilog="That's how to run the %(prog)s")

    parser.add_argument("-c", "--chrome", action="store_true", dest="chrome",
                        help="select the webdriver to chrome")
    parser.add_argument("-f", "--firefox", action="store_true", dest="firefox",
                        help="select the webdriver to firefox")
    parser.add_argument("-i", "--ie", action="store_true", dest="ie",
                        help="select the webdriver to IE")

    args = parser.parse_args()

    if args.chrome:
        Driver.browser = webdriver.Chrome()
    elif args.firefox:
        Driver.browser = webdriver.Firefox()
    elif args.ie:
        Driver.browser = webdriver.Ie()
    else:
        parser.print_help()
        exit(0)

    setting.run_case = {Tag.ALL}
    setting.check_case_doc = False
    setting.sort_case = True
    setting.create_report_by_style_1 = False
    setting.create_report_by_style_2 = True

    log.set_level(logging.DEBUG)

    runner = TestRunner()
    runner.add_case_dir(r"testcases")
    runner.run_test(report_title="Smoke Testing Report")


if __name__ == "__main__":
    main()


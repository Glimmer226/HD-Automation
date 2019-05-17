# coding = utf-8
from utx import *
import logging


if __name__ == "__main__":
    setting.run_case = {Tag.SMOKE}
    setting.check_case_doc = False
    setting.sort_case = True
    setting.create_report_by_style_1 = False
    setting.create_report_by_style_2 = False

    log.set_level(logging.DEBUG)

    runner = TestRunner()
    runner.add_case_dir(r"testcases")
    runner.run_test(report_title="Smoke Testing Report")

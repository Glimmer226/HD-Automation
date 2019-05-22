# coding = utf-8
"""author: GLimmer.Zhang@mullenloweprofero.com

   Login initiate, browser parameters setting"""


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, url="https://www.harley-davidson.com/us/en/index.html"):
        driver = self.driver
        driver.maximize_window()
        driver.get(url)


if __name__ == '__main__':

    pass








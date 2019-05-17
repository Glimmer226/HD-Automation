# coding = utf-8
import json
import os


class GetSelector:
    def __init__(self, path):
        self.path = path

    def get_selector(self):
        path = os.path.isfile(self.path)
        if path:
            with open(self.path, 'r') as f:
                results = json.load(f)
            return results
        else:
            raise EOFError("Input wrong config file")


if __name__ == '__main__':
    g = GetSelector(r"C:\Users\glimmer.zhang\Documents\Python\HD Automation\config\home_page.json")
    v = g.get_selector()["VideoID"]
    print(v)

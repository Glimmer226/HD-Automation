# encoding = utf-8
import json


class GetSelector:
    def __init__(self, path):
        self.path = path

    def get_selector(self):
        with open(self.path, 'r') as f:
            results = json.load(f)

        return results


if __name__ == '__main__':
    g = GetSelector(r"C:\Users\glimmer.zhang\Documents\Python\HD Automation\config\home_page.json")
    v = g.get_selector()["VideoID"]
    print(v)

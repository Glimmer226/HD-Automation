# encoding = utf-8
""" Author: Glimmer.Zhang@mullenloweprofero.com
    Can find the config.json file from the testing page"""
import os


def get_config(file):
    if os.path.isdir(r"config"):
        os.chdir(r"config")
    else:
        raise OSError("Folder not exist")

    current_path = os.getcwd()
    file_path = current_path + "\\" + file

    if os.path.isfile(file_path):
        return file_path
    else:
        raise OSError("File not exist!!!")


if __name__ == "__main__":

    a = os.path.abspath('')
    print(a)
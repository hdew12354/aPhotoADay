#from flask import Flask, render_template, Response

import config as cfg

import os

pastImages = []

def reloadPastImages():
    pastImages.clear()
    for file in os.listdir(cfg.localSavePath):
        if file.endswith(cfg.imageNameSuffix):
            print(os.path.join(cfg.localSavePath, file))
            pastImages.append(os.path.join(cfg.localSavePath, file))
    print("Loaded Preview Images")

reloadPastImages()

# print(cfg.roboname)
# cfg.setVar(cfg.roboname, "test")
# print(cfg.roboname)

from flask import Flask, render_template, Response
#import main
import json, os
import config as cfg
frame = "static/img/pain.png"

### SITE LOGIC ###
print("flask start")
app = Flask(__name__)

pastImages = []

def reloadPastImages():
    pastImages.clear()
    for file in os.listdir(cfg.localSavePath):
        if file.endswith(cfg.imageNameSuffix):
            print(os.path.join(cfg.localSavePath, file))
            pastImages.append(os.path.join(cfg.localSavePath, file))
    print("Loaded Past Images")
    return pastImages



@app.route('/')
def home():
    
    print("user on home")
    return render_template('APAD Homepae/homepage.html', clientCfg=cfg, image=frame)

@app.route('/configpanel')
def config():

    print("user on config panel")
    pastImages = reloadPastImages()
    print(pastImages)
    print("NEXT OUTPUT IS pastImages BUT CASTED TO STRING")
    pastImagesString = str(pastImages).replace("'",'') # on it's own line/variable for clarity
    print(pastImagesString)
    print("moyai")
    # pastImagesStringVerified = pastImagesString but remove the '&'s


    return render_template('APAD Homepae/configPanel.html', clientCfg=cfg, image=frame, pastImages = pastImagesString)


if(__name__ == '__main__'):
    app.run(host='127.0.0.1', port=5000, debug=True)

print("flask uuh it got past flask lines")

###/ SITE LOGIC ###
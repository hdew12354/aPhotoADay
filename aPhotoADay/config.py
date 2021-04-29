###config class###

#vars#
roboname = "Claire"
localSavePath = "static/img/DailyPhotos2"
faceCascade = 'haarcascade_frontalface_default.xml'
imageNamePrefix = 'Day~'
imageNameSuffix = '.png'
lastSavedImagePath = ""
pictureTimeframe = [0, 23]

homepage = "APAD Homepae/homepage.html"
configPanel = "APAD Homepae/configPanel.html"

#[7, 11] #24 hour, when can the picture be atempted?
drawFaceBox = True
#/vars#
#<img src="{{ url_for(image)}}" alt="webcam view"><br>

# def setVar(varName, newValue):
#     if(varName == "roboname"):
#         roboname = newValue
#     elif(varName == "localSavePath"):
#         localSavePath = newValue
#     elif(varName == "faceCascade"):
#         faceCascade = newValue
#     elif(varName == "imageNamePrefix"):
#         imageNamePrefix = newValue
#     elif(varName == "imageNameSuffix"):
#         imageNameSuffix = newValue
#     elif(varName == "lastSavedImagePath"):
#         lastSavedImagePath = newValue
#     elif(varName == "pictureTimeframe"):
#         pictureTimeframe = newValue
#     elif(varName == "drawFaceBox"):
#         drawFaceBox = newValue
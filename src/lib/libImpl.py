from RecognitionLib import *

print("hello")
path = "../trainedModel.sav"

clf = loadModel(path)

print(predict(clf, "../../audio/ok.wav"))



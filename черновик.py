file = 'Michael_Jackson_-_Smooth_Criminal_[NaijaGreen.Com]_' 
import numpy as np
import pandas as pd
import librosa as lbs
from scipy.io.wavfile import write

audioarr, sr = lbs.load(file)

#def read():
#def cut(sound):
#def classify(sound):

#print(classify(cut(read(file)))) #чтобы допИсать, нужно заставить неработающее говно работать
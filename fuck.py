file = r'C:/Users/gelos/Desktop/movie_1' #нерабочее

import pydub 
import numpy as np

def read(f, normalized=False):
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    return y
print(read(file))
print('j')
#def cut(sound):

#def classify(sound):

#print(classify(cut(convertsound(file)))) #чтобы дописать, нужно заставить неработающую шнягу работать
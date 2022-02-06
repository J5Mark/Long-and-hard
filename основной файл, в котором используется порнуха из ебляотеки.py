import tensorflow as tf
import keras_preprocessing
import random as rd
import numpy as np

wave = read_wave(r"C:\Users\gelos\Downloads\Voice1")

def convert(file):
  #ldfjvnkdfjvn
  return(aud)

def invert(aud):
  return(aud[::-1])

def putnose(aud):
  k = aud
  for element in k:
    element += rd.choice(0, 15)
  return(k)

  def fixlength(aud):
    return(aud)

  def convolute(aud):

n, k = 1, 2#хер знает, пусть пока 1 и 2 будут
p, f = 17, 17# ну ты понял.
modelforaud = tf.keras.models.Sequential([
                                  #some 1d convolution layers
    tf.keras.layers.Dense(k, activation='relu')#k зависит от средней длительности кашля после свёртки
    tf.keras.layers.Dense(n, activation='softmax')#n зависит от того, сколько там состояний лёгких мы сможем насобирать
])
modelforquests = tf.keras.models.Sequential([
    tf.keras.layers.Dense(p, activation='relu')#p зависит от того, сколько вопросов мы в опроснике поставим. р = колво вопросов + 1, где 1 - вердикт предыдущей сетки
    tf.keras.layers.Dense(30, activation='relu')
    tf.keras.layers.Dense(30, activation='relu')
    tf.keras.layers.Dense(30, activation='relu')#хер знает, пусть будет пока по 30 нейронов три слоя, потом посмотрим
    tf.keras.layers.Dense(f, activation='softmax')#f зависит от колва болячек с +-конкретнфми названиями, которые мы сможем насобирать. эта нейросетка выдаёт окончательный приговор пацтенту
])

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
import numpy as np
import PIL
from PIL import Image
import time
import functools
import IPython.display as display
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
# Create your views here.
context={}
def home(request):
    return render(request,'transfer/home.html')
def modelview(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
    return render(request,'transfer/model.html',context)
#class Home(TemplateView):
#    template_name='home.html'
def download(request):
    def load_img(path_to_img):
        img = tf.io.read_file(path_to_img)
        # Workaround
        img = tf.image.decode_png(img, channels=3)
        img = tf.image.convert_image_dtype(img, np.float32)
        #img = tf.image.resize(img, [800, 800])
        img = img[tf.newaxis, :]
        return img
    def tensor_to_image(tensor):
        tensor = tf.image.convert_image_dtype(tensor, np.uint8)
        tensor = tf.squeeze(tensor)
        plt.figure(figsize=(20,10))
        plt.axis('off')
        c=tf.keras.backend.eval(tensor)
        plt.imsave("media/new.jpg",c)
        #context['url']="media/new.jpg"
        return None
    model = load_model("static/car_model.h5",compile=False)
    s=context['url']
    x=load_img('{}'.format(s[1:]))
    l=load_img("static/style.jpeg")
    p=model(x)
    plt.subplot(1, 2, 1)
    tensor_to_image(p)
    return render(request,'transfer/download.html',context)

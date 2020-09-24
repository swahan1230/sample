from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
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
from django.conf import settings
from . import models as md
from django.contrib.auth.models import User
models={}
models['1'] = load_model("static/car_model.h5",compile=False)
models['2'] = load_model("static/model1.h5",compile=False)
models['3'] = load_model("static/model2.h5",compile=False)
models['4'] = load_model("static/model3.h5",compile=False)
models['5'] = load_model("static/model4.h5",compile=False)
models['6'] = load_model("static/model5.h5",compile=False)
models['7'] = load_model("static/model6.h5",compile=False)
models['8'] = load_model("static/model7.h5",compile=False)
models['9'] = load_model("static/model8.h5",compile=False)
# Create your views here.
context={}
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
    plt.imsave(context['path'],c)
    #context['url']="media/new.jpg"
    return None
def home(request):
    for i in os.listdir(settings.MEDIA_ROOT):
        os.remove(settings.MEDIA_ROOT+'/'+i)
    return render(request,'transfer/first_page.html')
def modelview(request,value):
    models['req']=models[str(value)]
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['path']='media/'+str(uploaded_file.name)
        context['url']=fs.url(name)
        context['value']=value
    return render(request,'transfer/upload.html',context)
#class Home(TemplateView):
#    template_name='home.html'
def download(request):
    model=models['req']
    s=context['url']
    x=load_img('{}'.format(s[1:]))
    #l=load_img("static/style.jpeg")
    p=model(x)
    plt.subplot(1, 2, 1)
    tensor_to_image(p)
    return render(request,'transfer/edit_style-1.html',context)
def returnhome(request):
    path=context['path']
    os.remove(path)
    return render(request,'transfer/first_page.html')
def about(request):
    return render(request,'transfer/about_us.html')
def feedback(request):
    return render(request,'transfer/feedback.html')
def submit(request):
    fname=request.POST['firstname']
    lname=request.POST['lastname']
    mail=request.POST['mailid']
    country=request.POST['country']
    feed=request.POST['subject']
    user1=md.user(fname=fname,lname=lname,mail=mail,country=country,feed=feed)
    user1.save()
    return render(request,'transfer/first_page.html')

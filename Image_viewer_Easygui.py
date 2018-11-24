#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:40:03 2018

=================================
Simple Image Viewer Using EasyGui
=================================

inputs:  image folder address
output:  imageViewer
created: 24/11/2018
Author: Sujit M Deokar
mail-id:   sujitdeokar30@gmail.com
"""

from easygui import diropenbox, buttonbox
import glob
state = True
j=0
path = diropenbox(msg=None, title=None, default='/home/sujit/Dell_Inspiron/dataset/CASIA-WebFace')
message = 'Image Viewer - Using Easygui'
choice = ('Previous', 'Next', 'Exit')
image_set = glob.glob(path + '/*.jpg') 
choice_select = buttonbox(msg=message, title=' ', choices=choice, image=image_set[0])
while state:
    if choice_select == 'Next':
        if j< len(image_set)-1:
            j=j+1
            choice_select = buttonbox(msg=message, title=' ', choices=choice, image=image_set[j])
        else:
            j=0
            choice_select = buttonbox(msg=message, title=' ', choices=choice, image=image_set[j])
    if choice_select == 'Previous':
        j-=1
        choice_select = buttonbox(msg=message, title=' ', choices=choice, image=image_set[j])
    if choice_select == 'Exit':
        state = False
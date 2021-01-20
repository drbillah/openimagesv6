#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:16:33 2021

@author: masum
"""


from pycocotools.coco import COCO
import requests

coco = COCO('/home/masum/3017/lab/cattle/code/Data/raw/coco/annotations_trainval2017/annotations/instances_val2017.json')

cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['cow'])
imgIds = coco.getImgIds(catIds=catIds )
images = coco.loadImgs(imgIds)
print("imgIds: ", imgIds)
print("images: ", images)

for im in images:
    print("im: ", im)
    img_data = requests.get(im['coco_url']).content
    with open('val/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)
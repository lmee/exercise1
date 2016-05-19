# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests

from scrapy import log
from tutorial.tutorial1.tutorial1 import settings
import os
class Tutorial1Pipeline(object):
    def process_item(self, item, spider):
        if 'img_url' in item:
            imgs = []
            dir_path = '%s/%s'%(settings.IMAGES_STORE,spider.name)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for img_url in item['img_url']:
                us ='_'.join(img_url.split('/')[-2:])
                filepath = '%s/%s'%(dir_path,us)
                imgs.append(filepath)
                if os.path.exists(filepath):
                    continue

                with open(filepath,'wb') as handle:
                    response = requests.get(img_url,stream = True)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)
            item['images'] = imgs
            return item

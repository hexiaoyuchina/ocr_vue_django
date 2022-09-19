# -*- coding:utf-8 -*-

import os
import torch
from torch.autograd import Variable
from crnn import utils
from crnn import dataset
from PIL import Image, ImageFont, ImageDraw
import crnn.models.crnn as crnn
from config import config

crnn_model_path = config.reg_model
corp_images_dir = config.corp_image_path
line_image_dir = config.write_line_path


def get_image_path(image_dir):
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk(image_dir):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print('Find {} images'.format(len(files)))
    return files

def recognition(file_path):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

    model = crnn.CRNN(32, 1, 37, 256)
    if torch.cuda.is_available():
        model = model.cuda()
    print('loading pretrained model from %s' % crnn_model_path)
    model.load_state_dict(torch.load(crnn_model_path))

    converter = utils.strLabelConverter(alphabet)

    transformer = dataset.resizeNormalize((100, 32))

    corp_images_dir =os.path.join(os.path.dirname(file_path), 'corp_image')
    corp_image_paths = get_image_path(corp_images_dir)

    line_image_path = os.path.join(os.path.dirname(file_path), 'detect.jpg')

    line_image = Image.open(line_image_path)
    draw = ImageDraw.Draw(line_image)

    detect_reg_text = open(os.path.join(os.path.dirname(file_path), 'detect_reg.txt'), 'w')
    # 整张图片每一个小图进行识别
    for corp_image_path in corp_image_paths:
        image = Image.open(corp_image_path).convert('L')
        image = transformer(image)
        if torch.cuda.is_available():
            image = image.cuda()
        image = image.view(1, *image.size())
        image = Variable(image)

        model.eval()
        preds = model(image)

        _, preds = preds.max(2)
        preds = preds.transpose(1, 0).contiguous().view(-1)

        preds_size = Variable(torch.IntTensor([preds.size(0)]))
        raw_pred = converter.decode(preds.data, preds_size.data, raw=True)
        sim_pred = converter.decode(preds.data, preds_size.data, raw=False)
        print('%-20s => %-20s' % (raw_pred, sim_pred))

        with open(os.path.join(corp_images_dir, os.path.splitext(os.path.basename(corp_image_path))[0]) + ".txt",
             "r") as f:
            boxes_text = f.read().replace('\r\n', '')
            boxes = boxes_text.split(',')
            left = int(boxes[0])
            top = int(boxes[1])

        # # 字体的格式 这里的SimHei.ttf需要有这个字体
        fontStyle = ImageFont.truetype("font/simhei.ttf", 100)
        draw.text((left, top), sim_pred, fill=(255, 0, 0), font=fontStyle)
        # draw.text((left, top), text, text_color, font=fontStyle)
        detect_reg_text.writelines(boxes_text+','+sim_pred+'\r\n')
        with open(os.path.join(corp_images_dir, os.path.splitext(os.path.basename(corp_image_path))[0]) + "_text.txt",
                  "w") as f:
            f.write(sim_pred)

    detect_reg_text.close()
    line_image.save(os.path.join(line_image_dir, 'detect_reg.jpg'))
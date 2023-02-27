# -*- coding: utf-8 -*-
# @File    : eval.py
# @Author  : AaronJny
# @Time    : 2019/12/30
# @Desc    :
from model.poetry_generator.dataset import tokenizer
from model.poetry_generator import model
from model.poetry_generator import settings
from model.poetry_generator import utils

# 加载训练好的模型
model.load_weights(settings.BEST_MODEL_PATH)
# 随机生成一首诗
# print(utils.generate_random_poetry(tokenizer, model))
# 给出部分信息的情况下，随机生成剩余部分
# print(utils.generate_random_poetry(tokenizer, model, s='床前明月光，'))
# 生成藏头诗
print(utils.generate_acrostic(tokenizer, model, head='草泥马的逼'))
# print(utils.generate_acrostic(tokenizer, model, head='天道酬勤'))

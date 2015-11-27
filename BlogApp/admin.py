# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post

#注册Post表
admin.site.register(Post)
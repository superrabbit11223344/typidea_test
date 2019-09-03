from django.contrib import admin


from typidea_test.custom_site import custom_site
from .models import Comment

import xadmin


@xadmin.sites.register(Comment)
class CommentAdmin(object):
    list_display = [
        'target', 'nickname', 'content', 'website', 'created_time'
    ]



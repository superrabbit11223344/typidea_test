from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Post, Category, Tag
from typidea_test.custom_site import custom_site
from typidea_test.custom_admin import BaseOwnerAdmin

from .adminforms import PostAdminForm

from xadmin.layout import Row, Fieldset
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter
import xadmin


class CategoryOwnerFilter(RelatedFieldListFilter):

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        # 重新获取lookup_choices,根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)  # site自定义
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = [
        'title', 'category','status_show',
        'pv', 'uv', 'created_time', 'operator',
                    ]
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category__name']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    date_hierarchy = 'created_time'

    form_layout = (
        Fieldset(
            '基础信息',
            Row('title', 'category'),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'is_nav', 'created_time']
    fields = (
        'name', 'status',
        'is_nav',
    )


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'created_time']
    fields = (
        'name', 'status'
    )







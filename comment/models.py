from django.db import models
from blog.models import Post


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    # post = models.ForeignKey(Post, verbose_name="文章", on_delete=True)
    target = models.CharField(max_length=2000, null=True, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = "评论"

    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(target=target, status=cls.STATUS_NORMAL)

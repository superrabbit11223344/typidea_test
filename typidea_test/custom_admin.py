from django.contrib import admin


class BaseOwnerAdmin:
    """
    针对有owner属性的数据，重写:
    1. save_model -保证每条数据都属于当前用户
    2. 重写get_queryset -保证每个用户只看到自己的文章
    """
    # exclude = ('owner', )

    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        return qs.filter(owner=request.user)

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()

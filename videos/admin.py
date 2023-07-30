from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Video, Comment , CommentFeedback






class VideoAdmin(SummernoteModelAdmin):
    list_display = ['author']
    list_filter = ['author']
    search_fields = ['author']
    summernote_fields = '__all__'
    

admin.site.register(Comment, VideoAdmin )
admin.site.register(Video)
admin.site.register(CommentFeedback, VideoAdmin)
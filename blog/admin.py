from django.contrib import admin
from .models import Post, Author
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = [
        'title',
        'date_created',
        'date_updated'
    ]


# admin.site.register(Post)
# admin.site.register(Model, )
admin.site.register(Post, PostAdmin)

admin.site.register(Author)
from django.contrib import admin
from .models import Authwiki, Comments, Enquiry
# Register your models here.

class CommentInline(admin.StackedInline): # new
    model = Comments
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [CommentInline,]

admin.site.register(Authwiki)
admin.site.register(Comments)
admin.site.register(Enquiry)
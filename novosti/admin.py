from django.contrib import admin

from .models import Post,PostImage,PostImageThumb



#admin.site.register(Post)

#admin.site.register(PostImage)



class PostImageAdmin(admin.StackedInline):

    model = PostImage

class PostImageThumbAdmin(admin.StackedInline):

    model = PostImageThumb   



@admin.register(Post)

class PostAdmin(admin.ModelAdmin):

    inlines = [PostImageAdmin,PostImageThumbAdmin]

    class Meta:

        model=Post
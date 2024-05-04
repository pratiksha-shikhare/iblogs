from django.contrib import admin
from .models import Category,Post

# Register your models here.

# for configuration of category admin(manually)
# jevha MODEL adminpannel la register kela tevha tya model cha data tabular form mde display
# karaycha aahe tyasathi ha class create kela and to class pn model sobat register kela 
#           @admin.register(Category,CategoryAdmin)
#           class CategoryAdmin(admin.ModelAdmin):
#                 list_display = ['title','description','url'] 
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['image_tag','title','description','url','add_date']
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',) #admin pannel la search cha option add hoil tyat 'title' type karun data search kru shakto
    list_filter = ('cat',)  # he stat. filter sathi ajun ek block admin pannel vr display karel right top la. jya category object vr click karel tyach category chya all post distil c
    list_per_page = 5                        # bcoz filter lavlay 'cat' clm nusar(ji fk aahe Post mde ani pk ahe category tbl mde). bydefault categoryobject as display krte actual name display hot nahi category che so tyasathi models.py mde method override karavi lagel str

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)

    
    
    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
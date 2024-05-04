from django.db import models
from django.utils.html import format_html
# from tinymce.models import HTMLField

# Create your models here.

# Category model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/') # image jail category folder mde.jo navin folder create hoil. folderName:category image:Real image
    add_date = models.DateTimeField(auto_now_add=True,null=True) # auto_now_add-date add karel.null-jr nahi date date dili tr null store karel
    
    def image_tag(self): # ha ek format aahe to html sathi use hoto. hya code mule image pn admin pannel display honar
        return format_html('<img src="/media/{}"style="width:40px;height:40px;border-radius:50%;"/>'.format(self.image))
    
    def __str__(self): # jevha object print karto aapn(Category object(1)) tevha bydefault str method call krto
        return self.title  # so aata actual category chi name distil filter mde rather than(Categoy object(1))
    
# Post model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100) # hi post access karnyasathi hi url aahe. hya url var click kelyavr post disel
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    
    def __str__(self): # jevha object print karto aapn(Category object(1)) tevha bydefault str method call krto
        return self.title
    
# media navacha folder create kela manually because jevdya image use hotil project mde tya hya media folder mde store krun theven.setting.py file la 
# sangav lagel jevde pn uploaded resources aahet te sagle hya folder mde store krun thev. settings.py file mde code lihila
# Configuration done manually by me for image.
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
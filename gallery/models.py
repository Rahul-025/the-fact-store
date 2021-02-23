from django.db import models

class GalleryCategory(models.Model):
    cat_title = models.CharField(max_length=30)
    cat_desc  = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_title

class GalleryPost(models.Model):
    post_title = models.CharField(max_length=30)
    post_desc  = models.CharField(max_length=50)
    post_image   = models.ImageField(upload_to = 'GalleryPosts')
    date_posted = models.DateTimeField()
    post_cat = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

class ArticleCategory(models.Model):
    cat_title = models.CharField(max_length=30)
    cat_desc  = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_title


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=100)
    article_author = models.CharField(max_length=20)
    article_desc  = models.TextField()
    article_main_image  = models.ImageField(upload_to = 'ArticleImages/MainImage')
    date_posted = models.DateTimeField()
    article_cat = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title

class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article_images  = models.ImageField(upload_to = 'ArticleImages')

    def __str__(self):
        return self.article.article_title

class ArticleContent(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article_content = models.TextField()

    def __str__(self):
        return self.article.article_title
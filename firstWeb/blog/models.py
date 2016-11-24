from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=50,null=True)  # Null means the title is not necessary.
	writer = models.CharField(max_length=50)
	created_date = models.DateField(auto_now_add = True)
	modify_date = models.DateField(auto_now = True)
	content = models.TextField()
	is_show = models.BooleanField( )

	class Meta:
	 	db_table = "article"

	def __str__(self):
	 	return self.title

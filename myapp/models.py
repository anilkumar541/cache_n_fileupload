from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Faq(models.Model):
    question=models.CharField(max_length=200)
    answer=models.TextField()
    attachment=models.FileField(upload_to="file_data/", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    class Meta:
        db_table ="faqs"


    def __str__(self):
        return self.question    




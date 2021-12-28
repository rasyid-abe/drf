from django.db import models
from authentication.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

def file_size(value): # add this to some file where you can import it from
    print(value)
    max_size = 5
    limit = max_size * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed {} MiB.'.format(max_size))

class Picture(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='file_img/',
        null=True,
        blank=True,
        validators=[file_size]
    )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100,50)],
        format='webm',
        options={'quality':60}
    )
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return str(self.owner)+'s picture'

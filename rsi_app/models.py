from django.db import models
from django.core.urlresolvers import reverse
from photologue.models import Photo

class Founders(models.Model):
    name = models.CharField(max_length=256, default='', blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=255)
    birth_year = models.PositiveIntegerField(default=1700)
    death_year = models.PositiveIntegerField(default=1700)
    position = models.CharField(max_length=256)
    bio = models.TextField(max_length=10000)
    picture = models.ForeignKey(Photo, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('practice_app.views.post', args=[self.slug])

    class Meta:
        verbose_name_plural = "Founders"

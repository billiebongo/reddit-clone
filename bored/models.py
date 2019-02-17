from django.db import models

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Name', max_length=40)
    username = models.EmailField(blank=False, unique=True)
    location = models.ForeignKey('Location', null=True, blank=True) #country
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    password_recently_reset = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Post(models.Model):
    post_title = models.CharField('Activation Token', max_length=40)
    text = models.CharField('Activation Token', max_length=40)
    tags = models.CharField('Activation Token', max_length=40)

class Tag(models.Model):
    tag_name = models.CharField('Activation Token', max_length=40)


class ActivationToken(models.Model):
    POSSIBLE_STATUSES = (
        ('A', 'ACTIVE'),
        ('E', 'EXPIRED')
    )
    user = models.ForeignKey(User, related_name='tokenuser')
    token = models.CharField('Activation Token', max_length=40)
    status = models.CharField(max_length=1, choices=POSSIBLE_STATUSES, default='A')
    date_added = models.DateTimeField('date', default=timezone.now, null=True)

    def __str__(self):
        return "{}'s activation token".format(self.user.name)

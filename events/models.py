from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

from taggit.managers import TaggableManager


class Event(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)
    guests = models.ManyToManyField(User, through='EventGuest')
    date = models.DateTimeField()
    location = models.TextField()
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_event', kwargs=({'pk': self.pk}))


class EventGuest(models.Model):
    status_choices = (
        (0, _('Host')),
        (1, _('Guest')),
        (2, _('Desisted')),
        (3, _('Confirmed')),
    )
    event = models.ForeignKey(Event)
    guest = models.ForeignKey(User)
    status = models.IntegerField(choices=status_choices)

    class Meta:
        unique_together = ('event', 'guest')

    def __str__(self):
        return self.guest.username


class Circle(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User)

    def contacts(self):
        return self.userinfo_set.all()

    def is_in_circle(self, user):
        if user in self.user_info.contact_set.all():
            return True
        return False

    def get_absolute_url(self):
        return reverse('circle_detail', kwargs=({'pk':self.pk}))

    def __str__(self):
        return self.name



class UserInfo(models.Model):
    circle = models.ManyToManyField(Circle, blank=True)
    notes = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('contact_detail', kwargs=({'pk':self.contact.pk}))


class Contact(models.Model):
    owner = models.ForeignKey(User)
    user = models.ForeignKey(User, related_name='friend')
    invitation_send = models.BooleanField()
    invitation_accepted = models.BooleanField()
    optional_informations = models.OneToOneField(UserInfo, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)
        if self.optional_informations == None:
            infos = UserInfo.objects.create()
            self.optional_informations = infos
            self.save()
            infos.save()

    def delete(self, *args, **kwargs):
        optional_informations = self.optional_informations
        super(Contact, self).delete(*args, **kwargs)
        optional_informations.delete()

    def all_contacts(self, user):
        return Contact.objects.filter(owner=user)

    def all_circles(self, user):
        return Circle.objects.filter(owner=user)

    def get_absolute_url(self):
        return reverse('contact_detail', kwargs=({'pk':self.pk}))

    def __str__(self):
        return self.user.username


class Invitation(models.Model):
    email = models.EmailField()
    sender = models.ForeignKey(User)

    class Meta:
        unique_together = ('email', 'sender')

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('invitation_list')


def create_contact_on_user_create(sender, instance, created, **kwargs):
    if created == True:
        try:
            invitations = Invitation.objects.filter(email=instance.email)
            for invitation in invitations:
                contact = Contact(owner=invitation.sender, user=instance, invitation_send=True, invitation_accepted=True)
                contact.save()
                invitation.delete()
        except Invitation.DoesNotExist:
            pass

post_save.connect(create_contact_on_user_create, sender=User)

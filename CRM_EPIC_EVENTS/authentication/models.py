from django.contrib.auth.models import AbstractUser
from django.core.exceptions import PermissionDenied
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

TEAM_LIMIT = 3
STATUS_LIMIT = 3


class Team(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None and Team.objects.count() >= TEAM_LIMIT:
            raise PermissionDenied("You are not permitted to create teams.")
        super().save(*args, **kwargs)

    def delete(self):
        raise PermissionDenied("You are not permitted to delete teams.")


@receiver(post_migrate)
def create_teams(sender, **kwargs):
    teams_to_create = ["MANAGEMENT", "SALES", "SUPPORT"]

    for team_name in teams_to_create:
        if not Team.objects.filter(name=team_name).exists():
            team = Team(name=team_name)
            team.save()


class EventStatus(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Event Status"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None and EventStatus.objects.count() >= STATUS_LIMIT:
            raise PermissionDenied("You are not permitted to create statuses.")
        super().save(*args, **kwargs)

    def delete(self):
        raise PermissionDenied("You are not permitted to delete statuses.")


@receiver(post_migrate)
def create_event_status(sender, **kwargs):
    status_to_create = ["IN PROGRESS", "COMPLETED", "PENDING"]

    for status_name in status_to_create:
        if not EventStatus.objects.filter(name=status_name).exists():
            status = EventStatus(name=status_name)
            status.save()


class User(AbstractUser):
    phone = models.CharField(max_length=30, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return f"User {self.id} is {self.username}"

    def save(self, *args, **kwargs):
        self.is_superuser = self.is_staff = self.team_id == 1
        return super().save(*args, **kwargs)

from django.core.validators import RegexValidator
from django.db import models


class Location(models.Model):
    city = models.CharField(
        max_length=15,
        validators=[
            RegexValidator("^[a-zA-Z' ]{3,15}$")
        ]
    )
    state = models.CharField(
        max_length=14,
        validators=[
            RegexValidator("^[a-zA-Z' ]{4,14}$")
        ]
    )
    zipcode = models.CharField(
        max_length=5,
        unique=True,
        validators=[
            RegexValidator("^[0-9]{5}$")
        ]
    )

    class Meta:
        unique_together = (
            ('city', 'state', 'zipcode'),
        )

    @property
    def full_name(self):
        return '{}, {} {}'.format(self.city, self.state, self.zipcode)

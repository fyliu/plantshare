from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.models import TitleDescriptionModel
from django_extensions.db.models import TitleSlugDescriptionModel


class AbstractBaseModel(TimeStampedModel):
    """
    Base abstract model
    """

    class Meta:
        abstract = True

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.pk}>"


class User(AbstractUser, AbstractBaseModel):
    """
    Default custom user model for Plant Share.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    offers = models.ManyToManyField(
        "Commodity",
        through="Offer",
        through_fields=("user", "commodity"),
        related_name="offers",
    )
    wants = models.ManyToManyField(
        "Commodity",
        through="Want",
        through_fields=("user", "commodity"),
        related_name="wants",
    )

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Category(AbstractBaseModel, TitleSlugDescriptionModel):
    """
    Category of commodity
    """

    class Meta:
        verbose_name_plural = "Categories"


class Commodity(AbstractBaseModel, TitleDescriptionModel):
    """
    Commodity being traded
    """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Commodities"


class Offer(AbstractBaseModel):
    """
    What a user wants to offer
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)

    quantity = models.IntegerField()


class Want(AbstractBaseModel):
    """
    What a user wants to get
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)

    quantity = models.IntegerField()

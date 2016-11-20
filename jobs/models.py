# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from jobs.utils import format_currency


class JobFeed(models.Model):
    """RSS - источники импорта вакансий."""
    name = models.CharField(
        max_length=255,
        verbose_name=_('Source name'),
    )

    link = models.URLField(
        max_length=255, verbose_name=_('Link'),
    )

    in_edit = models.BooleanField(
        verbose_name=_('In edit'),
        default=False,
    )

    is_activated = models.BooleanField(
        verbose_name=_('Is activated'),
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Source of job import")
        verbose_name_plural = _("Sources of job import")


class RejectedList(models.Model):
    title = models.CharField(_('String'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('List of rejected')
        verbose_name_plural = _('Strings to reject')


class AcceptedList(models.Model):
    title = models.CharField(_('String'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('List of accepted')
        verbose_name_plural = _('Strings to accept')


class JobItem(models.Model):
    title = models.CharField(_('Name'), max_length=255)
    link = models.URLField(_('link'))
    description = models.TextField(
        _('Job description'),
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        _('Date of creation'),
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        _('Date of update'),
        auto_now=True,
        null=True,
        blank=True
    )
    published_at = models.DateTimeField(
        _('Date of publication'),
        null=True,
        editable=False
    )
    src_id = models.CharField(
        _('ID in the source'),
        max_length=50,
        null=True,

        blank=True
    )
    src_place_name = models.CharField(
        _("Place's name in the source"),
        max_length=255,
        null=True,
        blank=True
    )
    src_place_id = models.CharField(
        _("Place's ID in the source"),
        max_length=20,
        db_index=True,
        null=True,
        blank=True
    )
    url_api = models.URLField(
        'URL API',
        null=True,
        blank=True
    )
    url_logo = models.URLField(
        _("Logo's URL"),
        null=True,
        blank=True
    )
    employer_name = models.CharField(
        _('Employer'),
        max_length=255,
        null=True,
        blank=True
    )
    salary_from = models.PositiveIntegerField(
        _('Salary'),
        null=True,
        blank=True
    )
    salary_till = models.PositiveIntegerField(
        _('Salary till'),
        null=True,
        blank=True
    )
    salary_currency = models.CharField(
        _('Currency'),
        max_length=255,
        null=True,
        blank=True
    )
    def get_salary_str(self) -> str:
        result = ''
        low_limit = format_currency(self.salary_from) \
            if self.salary_from else ''
        high_limit = format_currency(self.salary_till) \
            if self.salary_till else ''
        result += str(_(' from {low}')).format(low=low_limit)
        result += str(_(' to {high}')).format(high=high_limit)
        result += ' ' + self.salary_currency \
            if self.salary_currency else ''
        return result

    get_salary_str.short_description = _('Salary')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')

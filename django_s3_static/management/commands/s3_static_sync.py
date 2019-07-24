#!/usr/bin/env python
from django.conf import settings
from django.core.management.base import BaseCommand

from django_s3_static.utils import aws_cli


class Command(BaseCommand):
    help = 'sync static directory with s3 bucket'

    def handle(self, *args, **options):
        path = settings.STATIC_ROOT
        uri = "s3://%s" % settings.AWS_STATIC_BUCKET
        aws_cli(['s3', 'sync', path, uri, '--quiet'])

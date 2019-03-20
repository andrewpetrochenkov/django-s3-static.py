#!/usr/bin/env python
from django.core.management.base import BaseCommand
from django.conf import settings
import subprocess

"""
https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html
aws s3 sync --quiet static s3://$(STATIC_BUCKET)/static
"""

class Command(BaseCommand):
    help = 'sync static directory with s3 bucket'

    def handle(self, *args, **options):
        path = settings.STATIC_ROOT
        uri = "s3://%s" % settings.AWS_STATIC_BUCKET_NAME
        args = ["aws", "s3", "sync", "--quiet", path, uri]
        subprocess.check_call(args)

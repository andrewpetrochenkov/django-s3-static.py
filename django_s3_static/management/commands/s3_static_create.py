#!/usr/bin/env python
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import temp

from django_s3_static.utils import aws_cli

POLICY = """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::%s/*"
            ]
        }
    ]
}
"""

class Command(BaseCommand):
    help = 'create s3 bucket and policy'

    def handle(self, *args, **options):
        if not settings.AWS_STATIC_BUCKET:
            raise CommandError("setting.AWS_STATIC_BUCKET is empty")
        self.mb()
        self.policy()

    def mb(self):
        uri = "s3://%s" % settings.AWS_STATIC_BUCKET
        aws_cli(["s3", "mb", uri])

    def policy(self):
        path = temp.tempfile()
        open(path, "w").write(POLICY % settings.AWS_STATIC_BUCKET)
        args = ["s3api", "put-bucket-policy", "--bucket", settings.AWS_STATIC_BUCKET, "--policy", "file://%s" % path]
        aws_cli(args)



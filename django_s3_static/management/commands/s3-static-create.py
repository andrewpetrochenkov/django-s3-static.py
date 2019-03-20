#!/usr/bin/env python
from django.core.management.base import BaseCommand
from django.conf import settings
import subprocess
import temp


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
        self.mb()
        self.policy()

    def mb(self):
        name = settings.AWS_STATIC_BUCKET_NAME
        uri = "s3://%s" % name
        args = ["aws", "s3", "mb", uri]
        subprocess.check_call(args)

    def policy(self):
        name = settings.AWS_STATIC_BUCKET_NAME
        path = temp.tempfile()
        open(path, "w").write(POLICY % settings.AWS_STATIC_BUCKET_NAME)
        args = ["aws", "s3api", "put-bucket-policy", "--bucket", name, "--policy", "file://%s" % path]
        subprocess.check_call(args)



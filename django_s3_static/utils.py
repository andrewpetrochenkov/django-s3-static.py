#!/usr/bin/env python
from awscli.clidriver import create_clidriver
from django.conf import settings
from django.core.management.base import CommandError
import os

def aws_cli(args):
    old_env = dict(os.environ)
    try:
        env = os.environ.copy()
        env['LC_CTYPE'] = u'en_US.UTF'
        if not settings.AWS_STATIC_ACCESS_KEY_ID:
            raise CommandError('settings.AWS_STATIC_ACCESS_KEY_ID is empty')
        if not settings.AWS_S3_TEMPLATES_SECRET_ACCESS_KEY:
            raise CommandError('settings.AWS_STATIC_SECRET_ACCESS_KEY is empty')
        env['AWS_ACCESS_KEY_ID'] = settings.AWS_STATIC_ACCESS_KEY_ID
        env['AWS_SECRET_ACCESS_KEY'] = settings.AWS_STATIC_SECRET_ACCESS_KEY
        os.environ.update(env)
        exit_code = create_clidriver().main(args)
        if exit_code > 0:
            raise RuntimeError('AWS CLI exited with code {}'.format(exit_code))
    finally:
        os.environ.clear()
        os.environ.update(old_env)

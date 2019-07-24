<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-s3-static.svg?longCache=True)](https://pypi.org/project/django-s3-static/)
[![](https://img.shields.io/pypi/v/django-s3-static.svg?maxAge=3600)](https://pypi.org/project/django-s3-static/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/django-s3-static.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/django-s3-static.py/)

#### Installation
```bash
$ [sudo] pip install django-s3-static
```

#### `settings.py`
```python
INSTALLED_APPS = [
    "django_s3_static",
]
```

`settings/dev.py`
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
```

`settings/prod.py`
```python
AWS_STATIC_ACCESS_KEY_ID = os.getenv('AWS_STATIC_ACCESS_KEY_ID')
AWS_STATIC_SECRET_ACCESS_KEY = os.getenv('AWS_STATIC_SECRET_ACCESS_KEY')
AWS_STATIC_BUCKET = os.getenv('AWS_STATIC_BUCKET')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "https://%s.s3.amazonaws.com/" % AWS_STATIC_BUCKET
```

#### Commands
command|`help`
-|-
`python manage.py s3_static_create` |create s3 bucket and policy
`python manage.py s3_static_sync` |sync static directory with s3 bucket

#### Examples
```bash
$ python manage.py s3_static_create # create s3 bucket and policy
$ python manage.py s3_static_sync   # sync static folder with s3 bucket
```

```html
{% load static %}
<link rel="stylesheet" href="{% static "css/file.css" %}">
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>
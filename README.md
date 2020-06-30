<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-s3-static.svg?maxAge=3600)](https://pypi.org/project/django-s3-static/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-s3-static.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-s3-static.py/actions)

### Installation
```bash
$ [sudo] pip install django-s3-static
```

##### `settings.py`
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
    <a href="https://readme42.com/">readme42.com</a>
</p>
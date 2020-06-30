import setuptools

setuptools.setup(
    name='django-s3-static',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)

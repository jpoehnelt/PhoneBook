from setuptools import setup

setup(
    author='Justin Poehnelt',
    author_email='justin.poehnelt@gmail.com',
    description='A phone book implementation for an assignment',
    include_package_data=True,
    name='PhoneBook',
    platforms='any',
    packages=['phone_book'],
    version='0.1.0-dev',
    zip_safe=False,
    test_suite='tests'
)
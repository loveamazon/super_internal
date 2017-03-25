from distutils.core import setup

setup(
    name='backend',
    version='0.0.1',
    packages=['', 'tests', 'tests.login', 'tests.utils', 'tests.account', 'tests.session',
              'tests.session.token_provider', 'backend', 'backend.login', 'backend.login.google', 'backend.utils',
              'backend.config', 'backend.account', 'backend.account.external', 'backend.account.external.google',
              'backend.session', 'backend.session.token_provider', 'backend.constants', 'backend.container',
              'falcon_webserver'],
    url='',
    license='',
    author='',
    author_email='',
    description='backend lib'
)

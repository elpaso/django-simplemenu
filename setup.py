from distutils.core import setup

setup(name='django-simplemenu',
      version='0.1.0',
      url='http://github.com/alexvasi/django-simplemenu',
      license='BSD',
      description='Menu app for Django with ordering and ability to link menu item with model instance, view or URL.',
      author='Alex Vasi, Alessandro Pasotti',
      author_email='eee@someuser.com',
      include_package_data = True, 
      packages=['simplemenu', 'simplemenu.templatetags'])

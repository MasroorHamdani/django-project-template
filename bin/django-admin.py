#!/usr/bin/python


import sys
sys.path[0:0] = [
  '/home/hasher/project/django-project/django-project-template/src',
  '/home/hasher/project/django-project/django-project-template/lib/buildout/eggs/eventlet-0.15.0-py2.7.egg',
  '/home/hasher/project/django-project/django-project-template/lib/buildout/eggs/gunicorn-19.0.0-py2.7.egg',
  '/home/hasher/project/django-project/django-project-template/lib/buildout/eggs/greenlet-0.4.2-py2.7-linux-x86_64.egg',
  '/home/hasher/project/django-project/django-project-template/lib/buildout/eggs/Django-1.5.5-py2.7.egg',
  '/usr/lib/python2.7/dist-packages',
  ]


from django.core import management

if __name__ == "__main__":
    management.execute_from_command_line()

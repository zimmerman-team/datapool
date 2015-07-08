"""
WSGI config for datapool project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""


ALLDIRS = ['/home/siem/sites/datapool/site/','/home/siem/sites/datapool/site/datapool','/home/siem/sites/datapoolEnv/lib/python2.7/site-packages']
import os
import sys 
import site 

# Remember original sys.path.
prev_sys_path = list(sys.path) 

# Add each new site-packages directory.
for directory in ALLDIRS:
  site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = [] 
for item in list(sys.path): 
    if item not in prev_sys_path: 
        new_sys_path.append(item) 
        sys.path.remove(item) 
sys.path[:0] = new_sys_path 
# Activate your virtual env
os.environ["DJANGO_SETTINGS_MODULE"] = "datapool.settings_live"

activate_env=os.path.expanduser("/home/siem/sites/datapoolEnv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
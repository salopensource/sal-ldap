# Django settings for sal project.
from settings_import import ADMINS, TIME_ZONE, LANGUAGE_CODE, ALLOWED_HOSTS, DISPLAY_NAME, DEBUG
from system_settings import *
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

AUTHENTICATION_BACKENDS = ('django_auth_ldap.backend.LDAPBackend','django.contrib.auth.backends.ModelBackend',)

AUTH_LDAP_SERVER_URI = os.environ['SAL_LDAP_SERVER_URI']
if os.environ['SAL_LDAP_START_TLS'].lower() == 'true':
    AUTH_LDAP_START_TLS = True
else:
    AUTH_LDAP_START_TLS = False

if os.environ['SAL_LDAP_BIND_DN']:
    AUTH_LDAP_BIND_DN = os.environ['SAL_LDAP_BIND_DN']

if os.environ['SAL_LDAP_BIND_PASSWORD']:
    AUTH_LDAP_BIND_PASSWORD = os.environ['SAL_LDAP_BIND_PASSWORD']

if os.environ['SAL_LDAP_USER_SEARCH']:
    AUTH_LDAP_USER_SEARCH = LDAPSearch(os.environ['SAL_LDAP_USER_SEARCH'],
    ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")



AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

if os.environ['SAL_LDAP_GROUP_SEARCH']:
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(os.environ['SAL_LDAP_GROUP_SEARCH'],
        ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
    )
    AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

if os.environ['SAL_LDAP_REQUIRE_GROUP']:
    AUTH_LDAP_REQUIRE_GROUP = os.environ['SAL_LDAP_REQUIRE_GROUP']

if os.environ['SAL_LDAP_LOGGING'].lower() == 'true':
    import logging

    logger = logging.getLogger('django_auth_ldap')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'db/sal.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# PG Database
if os.environ.has_key('DB_PORT_5432_TCP_ADDR'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASS'],
            'HOST': os.environ['DB_PORT_5432_TCP_ADDR'],
            'PORT': os.environ['DB_PORT_5432_TCP_PORT'],
        }
    }

# Sal-LDAP

This image expands on Sal and allows it to leverage LDAP authentication. There are numerous customizations that are necessary - this image is in use and working for several AD environments, but may not 100% work in yours. You should mount your own ``settings.py`` in the container, at least while figuring out what options you need. This image uses [django-auth-ldap](https://pythonhosted.org/django-auth-ldap/index.html_) to connect to LDAP, so please refer to the documentation there if you need more details on the configuration options.

## Usage

For full usage instructions for [macadmins/sal](https://registry.hub.docker.com/u/macadmins/sal/), please see its repository.

## Environment variables

* ``SAL_LDAP_SERVER_URI``: The URI of your LDAP server. Defaults to ``ldap://ldap``
* ``SAL_LDAP_BIND_DN``: The distinguished name of your bind account.
* ``SAL_LDAP_BIND_PASSWORD``: The password for your bind account.
* ``SAL_LDAP_USER_SEARCH``: The search path for users.
* ``SAL_LDAP_GROUP_SEARCH``: The search path for groups.
* ``SAL_LDAP_REQUIRE_GROUP``: A group object to restrict login to.
* ``SAL_LDAP_START_TLS``: Set to ``true`` to use TLS. Defaults to ``false``
* ``SAL_LDAP_USER_ATTR``: The ldap attribute to identify the user. Defaults to ``sAMAccountName`` - NOT WORKING, MUST EDIT ``SETTINGS.PY`` TO MAKE THIS CHANGE CURRENTLY
* ``SAL_LDAP_LOGGING``: Set to ``true`` to enable logging of requests for debugging. Defaults to ``false``.

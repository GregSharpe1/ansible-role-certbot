ansible-role-certbot
=========

Install certbot

Requirements
------------

None.

This role has been tested solely against Ubuntu Xenial (16.04 LTS). This role
may work against other distros, but it has not been tested.

Role Variables
--------------

| Name | Default | Description |
|------|---------|-------------|
| `certbot_required_packages` | `['software-properties-common']` | List of dependent packages to install |

Dependencies
------------

None.

Testing
-------

This role has [molecule](http://molecule.readthedocs.io/en/latest/) (v2.0.0.0rc11) testing. The molcule configuration can be found under `molecule/`. Testing is done through the [testinfra](http://testinfra.readthedocs.io/en/latest) framework.

Tests are currently configured to use the `vagrant` provider against `ubuntu/xenial64`.

Usage
-----

    - hosts: servers
      become: yes
      become_user: root
      become_method: sudo
      roles:
         - { role: ansible-role-certbot }

License
-------

BSD

Author Information
------------------

Nathan Davies ~ [ndavies.io](https://ndavies.io) ~ [me@ndavies.io](mailto://me@ndavies.io)

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_certbot_installed(host):
    assert host.package("software-properties-common").is_installed
    assert host.package("certbot").is_installed

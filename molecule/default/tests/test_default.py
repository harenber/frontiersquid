import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_package(host):
    p = host.package('frontier-squid')

    assert p.is_installed


def test_hosts_service(host):
    s = host.service('frontier-squid')

    assert s.is_running
    assert s.is_enabled


def test_hosts_cachehit(host):
    f = host.file('/var/log/squid/access.log')

    assert f.contains('TCP_MEM_HIT')

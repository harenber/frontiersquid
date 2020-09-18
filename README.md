# frontiersquid Ansible Role

This is derived from the module from Dietrich Liko found [here](https://gitlab.cern.ch/hephyvienna/ansible/role/frontiersquid). It contains a couple of bugfixes (unfortunately, the original gitlab repo did neither contain a bug tracker nor pull requests. This is the reason for the fork.)

Install and configure a [Frontier squid cache](https://twiki.cern.ch/twiki/bin/view/Frontier/InstallSquid)

Inspired by the [Puppet Module](https://github.com/desalvo/puppet-frontier)

## Requirements

*   EL6/7
*   Optional UMD4 or OSG Repositories

## Role Variables

Enable the CERN frontier repository as alternative to the grid repositories

    frontiersquid_enable_repo: false

Check the documentation for details

    frontiersquid_net_local:
      - 0.0.0.0/0

Restict the squid service to the local networks

    frontiersquid_cache_mem: 128 MB

Memory cache. Can be small as the memory is used as disk cache anyway

    frontiersquid_cache_disk: 10000

Size of the disk cache in MB.

    frontiersquid_cpu_affinity: false

Bind thread to CPU to boost performance.

    frontiersquid_customize:

If the previous option do not add sufficient flexibility, one can replace
the whole sequence.

Run several instances. See the [documentation](https://twiki.cern.ch/twiki/bin/view/Frontier/InstallSquid#Running_multiple_services) for details

    frontiersquid_num_services: 1

Maximum size of the logfile for one service

    frontiersquid_max_access_log: 5G

Disable compressing of log files

    frontiersquid_compress_logs: true

## Example Playbook

    - hosts: servers
      roles:
         - role: hephyvienna.frontiersquid
           vars:
             frontiersquid_customize: |
                   setoption("acl NET_LOCAL src", "10.0.0.0/8 172.16.0.0/12 192.168.0.0/16 fc00::/7 fe80::/10")
                   setoption("cache_mem", "128 MB")
                   setoptionparameter("cache_dir", 3, "10000")
## License

MIT

(## Author Information

Written by [Dietrich Liko](http://hephy.at/dliko) in May 2019

[Institute for High Energy Physics](http://www.hephy.at) of the
[Austrian Academy of Sciences](http://www.oeaw.ac.at)

Bugfixes/Enhancesments by Torsten Harenberg for [the Pleiades HPC Cluster at the University of Wuppertal](http://www.pleiades.uni-wuppertal.de)

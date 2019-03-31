Experitest - Cloud NV ansible role
=========

This role will install \ uninstall cloud nv for linux os hosts

Requirements
------------

This role assumes that you have java 8 installed on the instance
Supports linux os hosts only.

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| state | should the application be present or absent | present, absent, restart | present | no |
| app_version | application version to install | string | 12.4.114 | no |
| server_port | port number for the server | number | 8888 | no |
| proxy_port | port number for the server | number | 9200 | no |
| tunneling_port | port number for the server | number | 9700 | no |
| installation_folder | the folder in which the applction will be installed | string | /opt/Experitest/NV/Server | no |
| custom_download_url | custom url to download the installation from (.sh file) | string |  | no |
| reboot_after_install | should instance reboot after installation is completed | boolean | True | no |
| clear_temp_folder | remove temp folder after installation | boolean | False | no |
| clear_before_install | removing old installation before installing new version | boolean | False | no |
| backup_old_installation | take backup old installation before install | boolean | False | no |
| uplink_eth | can provide ethernet name for uplink | string | Auto | no |
| wifi_eth | can provide ethernet name for wifi | string | Auto | no |

Example Playbook
----------------

#### [see working example](/example)

In requirements.yml file

    - src: git+https://github.com/ExperitestOfficial/ansible-role-cloud-nv.git
      version: master
      name: cloud-nv


In site.yml file

    - hosts: cloud-nv
      roles:
        - role: cloud-nv
          state: present
          app_version: 12.4.114

To invoke, run the following commands:

- install dependencies \
  *ansible-galaxy install -r requirements.yml*

- run the playbook \
  *ansible-playbook site.yml*

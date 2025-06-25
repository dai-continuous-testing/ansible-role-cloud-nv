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
| state | should the application be present or absent | present, absent, restarted | present | no |
| app_version | application version to install | string | 12.12.197 | no |
| server_port | port number for the server | number | 8888 | no |
| extra_application_properties | additional props to be override in application.properties file | dict | {} | no |
| proxy_port | port number for the server | number | 9200 | no |
| tunneling_port | port number for the server | number | 9700 | no |
| extra_java_options | extend java options | array of strings | [] | no |
| installation_folder | the folder in which the applction will be installed | string | /opt/Experitest/NV/Server | no |
| custom_download_url | custom url to download the installation from (.sh file) | string |  | no |
| reboot_after_install | should instance reboot after installation is completed | boolean | True | no |
| clear_temp_folder | remove temp folder after installation | boolean | False | no |
| clear_before_install | removing old installation before installing new version | boolean | False | no |
| backup_old_installation | take backup old installation before install | boolean | False | no |
| uplink_eth | can provide ethernet name for uplink | string | Auto | no |
| wifi_eth | can provide ethernet name for wifi | string | Auto | no |
| mitm_port | mitm proxy port number | number | 12121 | no |
| mitm_use_certificate | should we run MITM proxy with client side certificate | boolean | False | no |
| mitm_certificate_path | client certificate full path, only if "mitm_use_certificate" is true | string |  | no |
| download | only download the release version | boolean | True | no |
| deploy | only deploy the release version | boolean | True | no |

Example Playbook
----------------

#### [see working example](/example)

#!/usr/bin/python


class FilterModule(object):
    def filters(self):
        return {
            'os_family_to_os_type': self.os_family_to_os_type
        }

    def os_family_to_os_type(self, os_family):

        os_family_to_os_type_dict = dict({
            "redhat": "linux",
            "debian": "linux",
            "suse": "linux",
            "darwin": "darwin",
            "windows": "windows"
        })                   

        return os_family_to_os_type_dict[os_family.lower()]

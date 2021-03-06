# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineCaptureParameters(Model):
    """Capture Virtual Machine parameters.

    :param vhd_prefix: the captured VirtualHardDisk's name prefix.
    :type vhd_prefix: str
    :param destination_container_name: the destination container name.
    :type destination_container_name: str
    :param overwrite_vhds: whether it overwrites destination VirtualHardDisk
     if true, in case of conflict.
    :type overwrite_vhds: bool
    """ 

    _validation = {
        'vhd_prefix': {'required': True},
        'destination_container_name': {'required': True},
        'overwrite_vhds': {'required': True},
    }

    _attribute_map = {
        'vhd_prefix': {'key': 'vhdPrefix', 'type': 'str'},
        'destination_container_name': {'key': 'destinationContainerName', 'type': 'str'},
        'overwrite_vhds': {'key': 'overwriteVhds', 'type': 'bool'},
    }

    def __init__(self, vhd_prefix, destination_container_name, overwrite_vhds):
        self.vhd_prefix = vhd_prefix
        self.destination_container_name = destination_container_name
        self.overwrite_vhds = overwrite_vhds

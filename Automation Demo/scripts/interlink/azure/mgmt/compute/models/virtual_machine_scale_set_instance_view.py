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


class VirtualMachineScaleSetInstanceView(Model):
    """The instance view of a virtual machine scale set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar virtual_machine: the instance view status summary for the virtual
     machine scale set.
    :vartype virtual_machine:
     :class:`VirtualMachineScaleSetInstanceViewStatusesSummary
     <azure.mgmt.compute.models.VirtualMachineScaleSetInstanceViewStatusesSummary>`
    :ivar extensions: the extensions information.
    :vartype extensions: list of
     :class:`VirtualMachineScaleSetVMExtensionsSummary
     <azure.mgmt.compute.models.VirtualMachineScaleSetVMExtensionsSummary>`
    :param statuses: the resource status information.
    :type statuses: list of :class:`InstanceViewStatus
     <azure.mgmt.compute.models.InstanceViewStatus>`
    """ 

    _validation = {
        'virtual_machine': {'readonly': True},
        'extensions': {'readonly': True},
    }

    _attribute_map = {
        'virtual_machine': {'key': 'virtualMachine', 'type': 'VirtualMachineScaleSetInstanceViewStatusesSummary'},
        'extensions': {'key': 'extensions', 'type': '[VirtualMachineScaleSetVMExtensionsSummary]'},
        'statuses': {'key': 'statuses', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, statuses=None):
        self.virtual_machine = None
        self.extensions = None
        self.statuses = statuses

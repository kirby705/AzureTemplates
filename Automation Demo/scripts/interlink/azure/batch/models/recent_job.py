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


class RecentJob(Model):
    """Information about the most recent job to run under the job schedule.

    :param id: The id of the job.
    :type id: str
    :param url: The URL of the job.
    :type url: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, id=None, url=None):
        self.id = id
        self.url = url

# coding: utf-8

# Copyright © 2019 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# [http://www.apache.org/licenses/LICENSE-2.0]
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

############# This file is auto-generated.  Do not edit! #############

"""
    SDC Service: Ingest API

    Use the Ingest service in Splunk Cloud Services to send event and metrics data, or upload a static file, to Splunk Cloud Services.

    OpenAPI spec version: v1beta2.2 (recommended default)
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.ingest.v1beta2.gen_models import Error
from splunk_sdk.ingest.v1beta2.gen_models import Event
from splunk_sdk.ingest.v1beta2.gen_models import HTTPResponse
from splunk_sdk.ingest.v1beta2.gen_models import List
from splunk_sdk.ingest.v1beta2.gen_models import MetricEvent


class IngestAPI(BaseService):
    """
    Ingest API
    Version: v1beta2.2
    Use the Ingest service in Splunk Cloud Services to send event and metrics data, or upload a static file, to Splunk Cloud Services.
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def post_events(self, event: List[Event] = None, query_params: Dict[str, object] = None) -> HTTPResponse:
        """
        Sends events.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/ingest/v1beta2/events").substitute(path_params)
        url = self.base_client.build_url(path)
        data = [e.to_dict() for e in event]
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, HTTPResponse)

    def post_metrics(self, metric_event: List[MetricEvent] = None, query_params: Dict[str, object] = None) -> HTTPResponse:
        """
        Sends metric events.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/ingest/v1beta2/metrics").substitute(path_params)
        url = self.base_client.build_url(path)
        data = [e.to_dict() for e in metric_event]
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, HTTPResponse)



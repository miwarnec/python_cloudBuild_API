# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found at https://build.cloud.unity3d.com/login/me  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please [contact support](cloudbuild@unity3d.com) if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ``` 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ ProjectsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.projects_api.ProjectsApi()

    def tearDown(self):
        pass

    def test_add_project(self):
        """
        Test case for add_project

        Create project
        """
        pass

    def test_archive_project(self):
        """
        Test case for archive_project

        Archive project
        """
        pass

    def test_get_audit_log(self):
        """
        Test case for get_audit_log

        Get audit log
        """
        pass

    def test_get_billing_plans(self):
        """
        Test case for get_billing_plans

        Get billing plan
        """
        pass

    def test_get_project(self):
        """
        Test case for get_project

        Get project details
        """
        pass

    def test_get_project_by_upid(self):
        """
        Test case for get_project_by_upid

        Get project details
        """
        pass

    def test_get_ssh_key(self):
        """
        Test case for get_ssh_key

        Get SSH Key
        """
        pass

    def test_get_stats(self):
        """
        Test case for get_stats

        Get project statistics
        """
        pass

    def test_list_projects_for_org(self):
        """
        Test case for list_projects_for_org

        List all projects (org)
        """
        pass

    def test_list_projects_for_user(self):
        """
        Test case for list_projects_for_user

        List all projects (user)
        """
        pass

    def test_update_project(self):
        """
        Test case for update_project

        Update project details
        """
        pass


if __name__ == '__main__':
    unittest.main()

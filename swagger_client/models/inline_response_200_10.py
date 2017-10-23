# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found at https://build.cloud.unity3d.com/login/me  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please [contact support](cloudbuild@unity3d.com) if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ``` 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20010(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'job_count': 'float',
        'build_success_health': 'float',
        'build_poor_health': 'float',
        'build_cancel_health': 'float',
        'build_pending_health': 'float',
        'successful_builds': 'float',
        'canceled_builds': 'float',
        'failed_builds': 'float',
        'average_time': 'float',
        'average_workspace_size': 'float'
    }

    attribute_map = {
        'job_count': 'jobCount',
        'build_success_health': 'buildSuccessHealth',
        'build_poor_health': 'buildPoorHealth',
        'build_cancel_health': 'buildCancelHealth',
        'build_pending_health': 'buildPendingHealth',
        'successful_builds': 'successfulBuilds',
        'canceled_builds': 'canceledBuilds',
        'failed_builds': 'failedBuilds',
        'average_time': 'averageTime',
        'average_workspace_size': 'averageWorkspaceSize'
    }

    def __init__(self, job_count=None, build_success_health=None, build_poor_health=None, build_cancel_health=None, build_pending_health=None, successful_builds=None, canceled_builds=None, failed_builds=None, average_time=None, average_workspace_size=None):
        """
        InlineResponse20010 - a model defined in Swagger
        """

        self._job_count = None
        self._build_success_health = None
        self._build_poor_health = None
        self._build_cancel_health = None
        self._build_pending_health = None
        self._successful_builds = None
        self._canceled_builds = None
        self._failed_builds = None
        self._average_time = None
        self._average_workspace_size = None

        if job_count is not None:
          self.job_count = job_count
        if build_success_health is not None:
          self.build_success_health = build_success_health
        if build_poor_health is not None:
          self.build_poor_health = build_poor_health
        if build_cancel_health is not None:
          self.build_cancel_health = build_cancel_health
        if build_pending_health is not None:
          self.build_pending_health = build_pending_health
        if successful_builds is not None:
          self.successful_builds = successful_builds
        if canceled_builds is not None:
          self.canceled_builds = canceled_builds
        if failed_builds is not None:
          self.failed_builds = failed_builds
        if average_time is not None:
          self.average_time = average_time
        if average_workspace_size is not None:
          self.average_workspace_size = average_workspace_size

    @property
    def job_count(self):
        """
        Gets the job_count of this InlineResponse20010.

        :return: The job_count of this InlineResponse20010.
        :rtype: float
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count):
        """
        Sets the job_count of this InlineResponse20010.

        :param job_count: The job_count of this InlineResponse20010.
        :type: float
        """

        self._job_count = job_count

    @property
    def build_success_health(self):
        """
        Gets the build_success_health of this InlineResponse20010.

        :return: The build_success_health of this InlineResponse20010.
        :rtype: float
        """
        return self._build_success_health

    @build_success_health.setter
    def build_success_health(self, build_success_health):
        """
        Sets the build_success_health of this InlineResponse20010.

        :param build_success_health: The build_success_health of this InlineResponse20010.
        :type: float
        """

        self._build_success_health = build_success_health

    @property
    def build_poor_health(self):
        """
        Gets the build_poor_health of this InlineResponse20010.

        :return: The build_poor_health of this InlineResponse20010.
        :rtype: float
        """
        return self._build_poor_health

    @build_poor_health.setter
    def build_poor_health(self, build_poor_health):
        """
        Sets the build_poor_health of this InlineResponse20010.

        :param build_poor_health: The build_poor_health of this InlineResponse20010.
        :type: float
        """

        self._build_poor_health = build_poor_health

    @property
    def build_cancel_health(self):
        """
        Gets the build_cancel_health of this InlineResponse20010.

        :return: The build_cancel_health of this InlineResponse20010.
        :rtype: float
        """
        return self._build_cancel_health

    @build_cancel_health.setter
    def build_cancel_health(self, build_cancel_health):
        """
        Sets the build_cancel_health of this InlineResponse20010.

        :param build_cancel_health: The build_cancel_health of this InlineResponse20010.
        :type: float
        """

        self._build_cancel_health = build_cancel_health

    @property
    def build_pending_health(self):
        """
        Gets the build_pending_health of this InlineResponse20010.

        :return: The build_pending_health of this InlineResponse20010.
        :rtype: float
        """
        return self._build_pending_health

    @build_pending_health.setter
    def build_pending_health(self, build_pending_health):
        """
        Sets the build_pending_health of this InlineResponse20010.

        :param build_pending_health: The build_pending_health of this InlineResponse20010.
        :type: float
        """

        self._build_pending_health = build_pending_health

    @property
    def successful_builds(self):
        """
        Gets the successful_builds of this InlineResponse20010.

        :return: The successful_builds of this InlineResponse20010.
        :rtype: float
        """
        return self._successful_builds

    @successful_builds.setter
    def successful_builds(self, successful_builds):
        """
        Sets the successful_builds of this InlineResponse20010.

        :param successful_builds: The successful_builds of this InlineResponse20010.
        :type: float
        """

        self._successful_builds = successful_builds

    @property
    def canceled_builds(self):
        """
        Gets the canceled_builds of this InlineResponse20010.

        :return: The canceled_builds of this InlineResponse20010.
        :rtype: float
        """
        return self._canceled_builds

    @canceled_builds.setter
    def canceled_builds(self, canceled_builds):
        """
        Sets the canceled_builds of this InlineResponse20010.

        :param canceled_builds: The canceled_builds of this InlineResponse20010.
        :type: float
        """

        self._canceled_builds = canceled_builds

    @property
    def failed_builds(self):
        """
        Gets the failed_builds of this InlineResponse20010.

        :return: The failed_builds of this InlineResponse20010.
        :rtype: float
        """
        return self._failed_builds

    @failed_builds.setter
    def failed_builds(self, failed_builds):
        """
        Sets the failed_builds of this InlineResponse20010.

        :param failed_builds: The failed_builds of this InlineResponse20010.
        :type: float
        """

        self._failed_builds = failed_builds

    @property
    def average_time(self):
        """
        Gets the average_time of this InlineResponse20010.

        :return: The average_time of this InlineResponse20010.
        :rtype: float
        """
        return self._average_time

    @average_time.setter
    def average_time(self, average_time):
        """
        Sets the average_time of this InlineResponse20010.

        :param average_time: The average_time of this InlineResponse20010.
        :type: float
        """

        self._average_time = average_time

    @property
    def average_workspace_size(self):
        """
        Gets the average_workspace_size of this InlineResponse20010.

        :return: The average_workspace_size of this InlineResponse20010.
        :rtype: float
        """
        return self._average_workspace_size

    @average_workspace_size.setter
    def average_workspace_size(self, average_workspace_size):
        """
        Sets the average_workspace_size of this InlineResponse20010.

        :param average_workspace_size: The average_workspace_size of this InlineResponse20010.
        :type: float
        """

        self._average_workspace_size = average_workspace_size

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse20010):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
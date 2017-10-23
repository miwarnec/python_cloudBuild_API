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


class InlineResponse2005(object):
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
        'udid': 'str',
        'devicename': 'str',
        'os': 'str',
        'osversion': 'str',
        'product': 'str',
        'status': 'str'
    }

    attribute_map = {
        'udid': 'udid',
        'devicename': 'devicename',
        'os': 'os',
        'osversion': 'osversion',
        'product': 'product',
        'status': 'status'
    }

    def __init__(self, udid=None, devicename=None, os=None, osversion=None, product=None, status=None):
        """
        InlineResponse2005 - a model defined in Swagger
        """

        self._udid = None
        self._devicename = None
        self._os = None
        self._osversion = None
        self._product = None
        self._status = None

        self.udid = udid
        if devicename is not None:
          self.devicename = devicename
        if os is not None:
          self.os = os
        if osversion is not None:
          self.osversion = osversion
        if product is not None:
          self.product = product
        if status is not None:
          self.status = status

    @property
    def udid(self):
        """
        Gets the udid of this InlineResponse2005.

        :return: The udid of this InlineResponse2005.
        :rtype: str
        """
        return self._udid

    @udid.setter
    def udid(self, udid):
        """
        Sets the udid of this InlineResponse2005.

        :param udid: The udid of this InlineResponse2005.
        :type: str
        """
        if udid is None:
            raise ValueError("Invalid value for `udid`, must not be `None`")
        if udid is not None and len(udid) > 40:
            raise ValueError("Invalid value for `udid`, length must be less than or equal to `40`")
        if udid is not None and len(udid) < 40:
            raise ValueError("Invalid value for `udid`, length must be greater than or equal to `40`")

        self._udid = udid

    @property
    def devicename(self):
        """
        Gets the devicename of this InlineResponse2005.

        :return: The devicename of this InlineResponse2005.
        :rtype: str
        """
        return self._devicename

    @devicename.setter
    def devicename(self, devicename):
        """
        Sets the devicename of this InlineResponse2005.

        :param devicename: The devicename of this InlineResponse2005.
        :type: str
        """

        self._devicename = devicename

    @property
    def os(self):
        """
        Gets the os of this InlineResponse2005.

        :return: The os of this InlineResponse2005.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this InlineResponse2005.

        :param os: The os of this InlineResponse2005.
        :type: str
        """

        self._os = os

    @property
    def osversion(self):
        """
        Gets the osversion of this InlineResponse2005.

        :return: The osversion of this InlineResponse2005.
        :rtype: str
        """
        return self._osversion

    @osversion.setter
    def osversion(self, osversion):
        """
        Sets the osversion of this InlineResponse2005.

        :param osversion: The osversion of this InlineResponse2005.
        :type: str
        """

        self._osversion = osversion

    @property
    def product(self):
        """
        Gets the product of this InlineResponse2005.

        :return: The product of this InlineResponse2005.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this InlineResponse2005.

        :param product: The product of this InlineResponse2005.
        :type: str
        """

        self._product = product

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2005.

        :return: The status of this InlineResponse2005.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2005.

        :param status: The status of this InlineResponse2005.
        :type: str
        """
        allowed_values = ["disabled", "active"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

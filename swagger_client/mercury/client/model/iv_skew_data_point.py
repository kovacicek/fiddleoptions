# coding: utf-8

"""
    Fiddle Options Platform

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IVSkewDataPoint(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'strike': 'float',
        'iv': 'float'
    }

    attribute_map = {
        'strike': 'strike',
        'iv': 'iv'
    }

    def __init__(self, strike=None, iv=None):  # noqa: E501
        """IVSkewDataPoint - a model defined in Swagger"""  # noqa: E501

        self._strike = None
        self._iv = None
        self.discriminator = None

        if strike is not None:
            self.strike = strike
        if iv is not None:
            self.iv = iv

    @property
    def strike(self):
        """Gets the strike of this IVSkewDataPoint.  # noqa: E501


        :return: The strike of this IVSkewDataPoint.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this IVSkewDataPoint.


        :param strike: The strike of this IVSkewDataPoint.  # noqa: E501
        :type: float
        """

        self._strike = strike

    @property
    def iv(self):
        """Gets the iv of this IVSkewDataPoint.  # noqa: E501


        :return: The iv of this IVSkewDataPoint.  # noqa: E501
        :rtype: float
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        """Sets the iv of this IVSkewDataPoint.


        :param iv: The iv of this IVSkewDataPoint.  # noqa: E501
        :type: float
        """

        self._iv = iv

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IVSkewDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

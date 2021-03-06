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


class Greeks(object):
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
        'delta': 'float',
        'gamma': 'float',
        'vega': 'float',
        'theta': 'float',
        'rho': 'float'
    }

    attribute_map = {
        'delta': 'delta',
        'gamma': 'gamma',
        'vega': 'vega',
        'theta': 'theta',
        'rho': 'rho'
    }

    def __init__(self, delta=None, gamma=None, vega=None, theta=None, rho=None):  # noqa: E501
        """Greeks - a model defined in Swagger"""  # noqa: E501

        self._delta = None
        self._gamma = None
        self._vega = None
        self._theta = None
        self._rho = None
        self.discriminator = None

        if delta is not None:
            self.delta = delta
        if gamma is not None:
            self.gamma = gamma
        if vega is not None:
            self.vega = vega
        if theta is not None:
            self.theta = theta
        if rho is not None:
            self.rho = rho

    @property
    def delta(self):
        """Gets the delta of this Greeks.  # noqa: E501


        :return: The delta of this Greeks.  # noqa: E501
        :rtype: float
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this Greeks.


        :param delta: The delta of this Greeks.  # noqa: E501
        :type: float
        """

        self._delta = delta

    @property
    def gamma(self):
        """Gets the gamma of this Greeks.  # noqa: E501


        :return: The gamma of this Greeks.  # noqa: E501
        :rtype: float
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this Greeks.


        :param gamma: The gamma of this Greeks.  # noqa: E501
        :type: float
        """

        self._gamma = gamma

    @property
    def vega(self):
        """Gets the vega of this Greeks.  # noqa: E501


        :return: The vega of this Greeks.  # noqa: E501
        :rtype: float
        """
        return self._vega

    @vega.setter
    def vega(self, vega):
        """Sets the vega of this Greeks.


        :param vega: The vega of this Greeks.  # noqa: E501
        :type: float
        """

        self._vega = vega

    @property
    def theta(self):
        """Gets the theta of this Greeks.  # noqa: E501


        :return: The theta of this Greeks.  # noqa: E501
        :rtype: float
        """
        return self._theta

    @theta.setter
    def theta(self, theta):
        """Sets the theta of this Greeks.


        :param theta: The theta of this Greeks.  # noqa: E501
        :type: float
        """

        self._theta = theta

    @property
    def rho(self):
        """Gets the rho of this Greeks.  # noqa: E501


        :return: The rho of this Greeks.  # noqa: E501
        :rtype: float
        """
        return self._rho

    @rho.setter
    def rho(self, rho):
        """Sets the rho of this Greeks.


        :param rho: The rho of this Greeks.  # noqa: E501
        :type: float
        """

        self._rho = rho

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
        if not isinstance(other, Greeks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

from swagger_client.mercury.client.model.greeks import Greeks  # noqa: F401,E501


class DataPoint(object):
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
        'date': 'date',
        'underlying_price': 'float',
        'profit': 'float',
        'greeks': 'Greeks'
    }

    attribute_map = {
        'date': 'date',
        'underlying_price': 'underlyingPrice',
        'profit': 'profit',
        'greeks': 'greeks'
    }

    def __init__(self, date=None, underlying_price=None, profit=None, greeks=None):  # noqa: E501
        """DataPoint - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._underlying_price = None
        self._profit = None
        self._greeks = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if underlying_price is not None:
            self.underlying_price = underlying_price
        if profit is not None:
            self.profit = profit
        if greeks is not None:
            self.greeks = greeks

    @property
    def date(self):
        """Gets the date of this DataPoint.  # noqa: E501


        :return: The date of this DataPoint.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DataPoint.


        :param date: The date of this DataPoint.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def underlying_price(self):
        """Gets the underlying_price of this DataPoint.  # noqa: E501


        :return: The underlying_price of this DataPoint.  # noqa: E501
        :rtype: float
        """
        return self._underlying_price

    @underlying_price.setter
    def underlying_price(self, underlying_price):
        """Sets the underlying_price of this DataPoint.


        :param underlying_price: The underlying_price of this DataPoint.  # noqa: E501
        :type: float
        """

        self._underlying_price = underlying_price

    @property
    def profit(self):
        """Gets the profit of this DataPoint.  # noqa: E501


        :return: The profit of this DataPoint.  # noqa: E501
        :rtype: float
        """
        return self._profit

    @profit.setter
    def profit(self, profit):
        """Sets the profit of this DataPoint.


        :param profit: The profit of this DataPoint.  # noqa: E501
        :type: float
        """

        self._profit = profit

    @property
    def greeks(self):
        """Gets the greeks of this DataPoint.  # noqa: E501


        :return: The greeks of this DataPoint.  # noqa: E501
        :rtype: Greeks
        """
        return self._greeks

    @greeks.setter
    def greeks(self, greeks):
        """Sets the greeks of this DataPoint.


        :param greeks: The greeks of this DataPoint.  # noqa: E501
        :type: Greeks
        """

        self._greeks = greeks

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
        if not isinstance(other, DataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

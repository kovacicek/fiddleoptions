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


class OptionLeg(object):
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
        'expiration_date': 'date',
        'direction': 'str',
        'type': 'str',
        'quantity': 'int',
        'strike': 'float'
    }

    attribute_map = {
        'expiration_date': 'expirationDate',
        'direction': 'direction',
        'type': 'type',
        'quantity': 'quantity',
        'strike': 'strike'
    }

    # def __init__(self, option_contract=None, direction=None, quantity=None):  # noqa: E501
    #     """OptionLeg - a model defined in Swagger"""  # noqa: E501
    #     # Added opening_price
    #     self._expiration_date = None
    #     self._direction = None
    #     self._type = None
    #     self._quantity = None
    #     self._strike = None
    #     self._opening_price = None
    #     self.discriminator = None
    #
    #     if option_contract is not None:
    #         self.option_contract = option_contract
    #         self.expiration_date = option_contract.expiration_date
    #         self.strike = option_contract.strike
    #         self.type = 'CALL' if option_contract.call else 'PUT'
    #     if direction is not None:
    #         self.direction = direction
    #     if quantity is not None:
    #         self.quantity = quantity

    def __init__(self,
                 expiration_date=None,
                 direction=None,
                 type=None,
                 quantity=None,
                 strike=None):
        """OptionLeg - a model defined in Swagger"""  # noqa: E501

        self._expiration_date = None
        self._direction = None
        self._type = None
        self._quantity = None
        self._strike = None
        self.discriminator = None

        if expiration_date is not None:
            self.expiration_date = expiration_date
        if direction is not None:
            self.direction = direction
        if type is not None:
            self.type = type
        if quantity is not None:
            self.quantity = quantity
        if strike is not None:
            self.strike = strike

    @property
    def expiration_date(self):
        """Gets the expiration_date of this OptionLeg.  # noqa: E501


        :return: The expiration_date of this OptionLeg.  # noqa: E501
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this OptionLeg.


        :param expiration_date: The expiration_date of this OptionLeg.  # noqa: E501
        :type: date
        """

        self._expiration_date = expiration_date

    @property
    def direction(self):
        """Gets the direction of this OptionLeg.  # noqa: E501


        :return: The direction of this OptionLeg.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this OptionLeg.


        :param direction: The direction of this OptionLeg.  # noqa: E501
        :type: str
        """
        allowed_values = ["LONG", "SHORT"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def type(self):
        """Gets the type of this OptionLeg.  # noqa: E501


        :return: The type of this OptionLeg.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OptionLeg.


        :param type: The type of this OptionLeg.  # noqa: E501
        :type: str
        """
        allowed_values = ["PUT", "CALL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def quantity(self):
        """Gets the quantity of this OptionLeg.  # noqa: E501


        :return: The quantity of this OptionLeg.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OptionLeg.


        :param quantity: The quantity of this OptionLeg.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def strike(self):
        """Gets the strike of this OptionLeg.  # noqa: E501


        :return: The strike of this OptionLeg.  # noqa: E501
        :rtype: float
        """
        return self._strike

    @strike.setter
    def strike(self, strike):
        """Sets the strike of this OptionLeg.


        :param strike: The strike of this OptionLeg.  # noqa: E501
        :type: float
        """

        self._strike = strike

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
        if not isinstance(other, OptionLeg):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
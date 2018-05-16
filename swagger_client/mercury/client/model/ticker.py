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


class Ticker(object):
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
        'name': 'str',
        'full_name': 'str',
        'exchange': 'str',
        'type': 'str',
        'sector': 'str',
        'industry': 'str',
        'fully_tracked': 'bool',
        'num_missing_dates': 'int',
        'first_trading_date': 'date',
        'last_trading_date': 'date',
        'etf': 'bool',
        'equity': 'bool',
        'index': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'full_name': 'fullName',
        'exchange': 'exchange',
        'type': 'type',
        'sector': 'sector',
        'industry': 'industry',
        'fully_tracked': 'fullyTracked',
        'num_missing_dates': 'numMissingDates',
        'first_trading_date': 'firstTradingDate',
        'last_trading_date': 'lastTradingDate',
        'etf': 'etf',
        'equity': 'equity',
        'index': 'index'
    }

    def __init__(self, name=None, full_name=None, exchange=None, type=None, sector=None, industry=None, fully_tracked=None, num_missing_dates=None, first_trading_date=None, last_trading_date=None, etf=None, equity=None, index=None):  # noqa: E501
        """Ticker - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._full_name = None
        self._exchange = None
        self._type = None
        self._sector = None
        self._industry = None
        self._fully_tracked = None
        self._num_missing_dates = None
        self._first_trading_date = None
        self._last_trading_date = None
        self._etf = None
        self._equity = None
        self._index = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if full_name is not None:
            self.full_name = full_name
        if exchange is not None:
            self.exchange = exchange
        if type is not None:
            self.type = type
        if sector is not None:
            self.sector = sector
        if industry is not None:
            self.industry = industry
        if fully_tracked is not None:
            self.fully_tracked = fully_tracked
        if num_missing_dates is not None:
            self.num_missing_dates = num_missing_dates
        if first_trading_date is not None:
            self.first_trading_date = first_trading_date
        if last_trading_date is not None:
            self.last_trading_date = last_trading_date
        if etf is not None:
            self.etf = etf
        if equity is not None:
            self.equity = equity
        if index is not None:
            self.index = index

    @property
    def name(self):
        """Gets the name of this Ticker.  # noqa: E501


        :return: The name of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Ticker.


        :param name: The name of this Ticker.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def full_name(self):
        """Gets the full_name of this Ticker.  # noqa: E501


        :return: The full_name of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Ticker.


        :param full_name: The full_name of this Ticker.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def exchange(self):
        """Gets the exchange of this Ticker.  # noqa: E501


        :return: The exchange of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Ticker.


        :param exchange: The exchange of this Ticker.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def type(self):
        """Gets the type of this Ticker.  # noqa: E501


        :return: The type of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Ticker.


        :param type: The type of this Ticker.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def sector(self):
        """Gets the sector of this Ticker.  # noqa: E501


        :return: The sector of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this Ticker.


        :param sector: The sector of this Ticker.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def industry(self):
        """Gets the industry of this Ticker.  # noqa: E501


        :return: The industry of this Ticker.  # noqa: E501
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this Ticker.


        :param industry: The industry of this Ticker.  # noqa: E501
        :type: str
        """

        self._industry = industry

    @property
    def fully_tracked(self):
        """Gets the fully_tracked of this Ticker.  # noqa: E501


        :return: The fully_tracked of this Ticker.  # noqa: E501
        :rtype: bool
        """
        return self._fully_tracked

    @fully_tracked.setter
    def fully_tracked(self, fully_tracked):
        """Sets the fully_tracked of this Ticker.


        :param fully_tracked: The fully_tracked of this Ticker.  # noqa: E501
        :type: bool
        """

        self._fully_tracked = fully_tracked

    @property
    def num_missing_dates(self):
        """Gets the num_missing_dates of this Ticker.  # noqa: E501


        :return: The num_missing_dates of this Ticker.  # noqa: E501
        :rtype: int
        """
        return self._num_missing_dates

    @num_missing_dates.setter
    def num_missing_dates(self, num_missing_dates):
        """Sets the num_missing_dates of this Ticker.


        :param num_missing_dates: The num_missing_dates of this Ticker.  # noqa: E501
        :type: int
        """

        self._num_missing_dates = num_missing_dates

    @property
    def first_trading_date(self):
        """Gets the first_trading_date of this Ticker.  # noqa: E501


        :return: The first_trading_date of this Ticker.  # noqa: E501
        :rtype: date
        """
        return self._first_trading_date

    @first_trading_date.setter
    def first_trading_date(self, first_trading_date):
        """Sets the first_trading_date of this Ticker.


        :param first_trading_date: The first_trading_date of this Ticker.  # noqa: E501
        :type: date
        """

        self._first_trading_date = first_trading_date

    @property
    def last_trading_date(self):
        """Gets the last_trading_date of this Ticker.  # noqa: E501


        :return: The last_trading_date of this Ticker.  # noqa: E501
        :rtype: date
        """
        return self._last_trading_date

    @last_trading_date.setter
    def last_trading_date(self, last_trading_date):
        """Sets the last_trading_date of this Ticker.


        :param last_trading_date: The last_trading_date of this Ticker.  # noqa: E501
        :type: date
        """

        self._last_trading_date = last_trading_date

    @property
    def etf(self):
        """Gets the etf of this Ticker.  # noqa: E501


        :return: The etf of this Ticker.  # noqa: E501
        :rtype: bool
        """
        return self._etf

    @etf.setter
    def etf(self, etf):
        """Sets the etf of this Ticker.


        :param etf: The etf of this Ticker.  # noqa: E501
        :type: bool
        """

        self._etf = etf

    @property
    def equity(self):
        """Gets the equity of this Ticker.  # noqa: E501


        :return: The equity of this Ticker.  # noqa: E501
        :rtype: bool
        """
        return self._equity

    @equity.setter
    def equity(self, equity):
        """Sets the equity of this Ticker.


        :param equity: The equity of this Ticker.  # noqa: E501
        :type: bool
        """

        self._equity = equity

    @property
    def index(self):
        """Gets the index of this Ticker.  # noqa: E501


        :return: The index of this Ticker.  # noqa: E501
        :rtype: bool
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Ticker.


        :param index: The index of this Ticker.  # noqa: E501
        :type: bool
        """

        self._index = index

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
        if not isinstance(other, Ticker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
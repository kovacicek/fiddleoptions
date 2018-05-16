# coding: utf-8

"""
    Fiddle Options Platform

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest
from datetime import date

from swagger_client.mercury.client.api.marketdata_api import MarketdataApi


class TestMarketdataApi(unittest.TestCase):
    """MarketdataApi unit test stubs"""

    def setUp(self):
        self.api = MarketdataApi()

    def tearDown(self):
        pass

    def test_get_equity_quote(self):
        """Test case for get_equity_quote

        Returns equity quotes for each trading day for the given ticker and time period  # noqa: E501
        """
        name = "SPX"
        data = {'_from': date(2018, 4, 1),
                'to': date(2018, 5, 1)}
        response = self.api.get_equity_quote(name, **data)
        # TODO: add assertion to response

    # Ignored
    def test_get_expirations(self):
        """Test case for get_expirations

        Returns expirations for the given symbol and trading date  # noqa: E501
        """
        name = "SPX"
        dt = date(2018, 4, 1)
        data = {'date': dt}
        response = self.api.get_expirations(name, **data)
        # TODO: add assertion to response

    def test_get_horizontally_sliced_option_chain_by_delta(self):
        """Test case for get_horizontally_sliced_option_chain_by_delta

        Returns horizontal slice of option chain for the given symbol, option type, trading dates, expiration, and the delta strike range  # noqa: E501
        """
        name = "SPX"
        data = {'is_call': True,
                'from_strike': 0.4,
                'to_strike': 0.5,
                'from_date': date(2018, 4, 9),
                'to_date': date(2018, 4, 12),
                'expiration': date(2018, 6, 15)}
        response = self.api.get_horizontally_sliced_option_chain_by_delta(name, **data)
        # TODO: add assertion to response

    def test_get_horizontally_sliced_option_chain_by_strike(self):
        """Test case for get_horizontally_sliced_option_chain_by_strike

        Returns horizontal slice of option chain for the given symbol, option type, trading dates, expiration, and the strike range  # noqa: E501
        """
        name = "SPX"
        data = {'is_call': True,
                'from_strike': 2200.0,
                'to_strike': 2250.0,
                'from_date': date(2018, 4, 9),
                'to_date': date(2018, 4, 12),
                'expiration': date(2018, 6, 15)}
        response = self.api.get_horizontally_sliced_option_chain_by_strike(name, **data)
        # TODO: add assertion to response

    # Ignored
    def test_get_option_chain(self):
        """Test case for get_option_chain

        Returns option chain for the given symbol, trading date, and expiration date  # noqa: E501
        """
        name = "SPX"
        data = {'date': date(2018, 4, 9),
                'expiration': date(2018, 6, 15)}
        response = self.api.get_option_chain(name, **data)
        # TODO: add assertion to response

    def test_get_server_time(self):
        """Test case for get_server_time

        Get the current server time  # noqa: E501
        """
        response = self.api.get_server_time()
        # TODO: add assertion to response

    def test_get_trading_dates(self):
        """Test case for get_trading_dates

        Returns actual trading days in specified from/to date range  # noqa: E501
        """
        name = "SPX"
        data = {'_from': date(2018, 4, 9),
                'to': date(2018, 5, 9)}
        response = self.api.get_trading_dates(name, **data)
        # TODO: add assertion to response

    def test_get_vertically_sliced_option_chain_by_delta(self):
        """Test case for get_vertically_sliced_option_chain_by_delta

        Returns vertical slice of option chain for the given symbol, option type, trading date, expiration, and the delta strike range  # noqa: E501
        """
        name = "SPX"
        data = {'is_call': True,
                'from_strike': 0.3,
                'to_strike': 0.5,
                'date': date(2018, 4, 9),
                'expiration': date(2018, 6, 15)}
        response = self.api.get_vertically_sliced_option_chain_by_delta(name, **data)
        # TODO: add assertion to response

    def test_get_vertically_sliced_option_chain_by_strike(self):
        """Test case for get_vertically_sliced_option_chain_by_strike

        Returns vertical slice of option chain for the given symbol, option type, trading date, expiration, and the strike range  # noqa: E501
        """
        name = "SPX"
        data = {'is_call': True,
                'from_strike': 2100.0,
                'to_strike': 2100.0,
                'date': date(2018, 4, 9),
                'expiration': date(2018, 6, 15)}
        response = self.api.get_vertically_sliced_option_chain_by_strike(name, **data)
        # TODO: add assertion to response

    def test_get_volatility_skew(self):
        """Test case for get_volatility_skew

        Returns volatility skews for the given trading symbol, the expiration and the observation dates  # noqa: E501
        """
        data = {'symbol': 'SPX',
                'expirations': [date(2018, 6, 15)],
                'date': [date(2018, 4, 9)]}
        response = self.api.get_volatility_skew(**data)
        # TODO: add assertion to response

    def test_search_tickers(self):
        """Test case for search_tickers

        Searchs for symbols in the system with an optional query parameter. If query parameter is not used all symbols are returned  # noqa: E501
        """
        data = {'query': 'SPX'}
        response = self.api.search_tickers(**data)
        # TODO: add assertion to response


if __name__ == '__main__':
    unittest.main()
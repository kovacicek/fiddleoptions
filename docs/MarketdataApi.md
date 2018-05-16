# swagger_client.MarketdataApi

All URIs are relative to *https://localhost/mercury/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_equity_quote**](MarketdataApi.md#get_equity_quote) | **GET** /marketdata/equity/{name} | Returns equity quotes for each trading day for the given ticker and time period
[**get_expirations**](MarketdataApi.md#get_expirations) | **GET** /marketdata/option-chain/expirations/{name} | Returns expirations for the given symbol and trading date
[**get_horizontally_sliced_option_chain_by_delta**](MarketdataApi.md#get_horizontally_sliced_option_chain_by_delta) | **GET** /marketdata/option-chain/{name}/horizontal-slice-by-delta | Returns horizontal slice of option chain for the given symbol, option type, trading dates, expiration, and the delta strike range
[**get_horizontally_sliced_option_chain_by_strike**](MarketdataApi.md#get_horizontally_sliced_option_chain_by_strike) | **GET** /marketdata/option-chain/{name}/horizontal-slice-by-strike | Returns horizontal slice of option chain for the given symbol, option type, trading dates, expiration, and the strike range
[**get_option_chain**](MarketdataApi.md#get_option_chain) | **GET** /marketdata/option-chain/{name} | Returns option chain for the given symbol, trading date, and expiration date
[**get_server_time**](MarketdataApi.md#get_server_time) | **GET** /marketdata/servertime | Get the current server time
[**get_trading_dates**](MarketdataApi.md#get_trading_dates) | **GET** /marketdata/tradingdates/{symbol} | Returns actual trading days in specified from/to date range
[**get_vertically_sliced_option_chain_by_delta**](MarketdataApi.md#get_vertically_sliced_option_chain_by_delta) | **GET** /marketdata/option-chain/{name}/vertical-slice-by-delta | Returns vertical slice of option chain for the given symbol, option type, trading date, expiration, and the delta strike range
[**get_vertically_sliced_option_chain_by_strike**](MarketdataApi.md#get_vertically_sliced_option_chain_by_strike) | **GET** /marketdata/option-chain/{name}/vertical-slice-by-strike | Returns vertical slice of option chain for the given symbol, option type, trading date, expiration, and the strike range
[**get_volatility_skew**](MarketdataApi.md#get_volatility_skew) | **GET** /marketdata/iv-skew | Returns volatility skews for the given trading symbol, the expiration and the observation dates
[**search_tickers**](MarketdataApi.md#search_tickers) | **GET** /marketdata/tickers | Searchs for symbols in the system with an optional query parameter. If query parameter is not used all symbols are returned


# **get_equity_quote**
> list[EquityQuote] get_equity_quote(name, _from=_from, to=to)

Returns equity quotes for each trading day for the given ticker and time period



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
name = 'name_example' # str | 
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)

try:
    # Returns equity quotes for each trading day for the given ticker and time period
    api_response = api_instance.get_equity_quote(name, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_equity_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 

### Return type

[**list[EquityQuote]**](EquityQuote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expirations**
> list[date] get_expirations(name, date=date)

Returns expirations for the given symbol and trading date



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
name = 'name_example' # str | 
date = '2013-10-20' # date |  (optional)

try:
    # Returns expirations for the given symbol and trading date
    api_response = api_instance.get_expirations(name, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_expirations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **date** | **date**|  | [optional] 

### Return type

**list[date]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_horizontally_sliced_option_chain_by_delta**
> list[OptionChain] get_horizontally_sliced_option_chain_by_delta(name, is_call=is_call, from_strike=from_strike, to_strike=to_strike, from_date=from_date, to_date=to_date, expiration=expiration)

Returns horizontal slice of option chain for the given symbol, option type, trading dates, expiration, and the delta strike range



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
name = 'name_example' # str | 
is_call = true # bool |  (optional)
from_strike = 1.2 # float |  (optional)
to_strike = 1.2 # float |  (optional)
from_date = '2013-10-20' # date |  (optional)
to_date = '2013-10-20' # date |  (optional)
expiration = '2013-10-20' # date |  (optional)

try:
    # Returns horizontal slice of option chain for the given symbol, option type, trading dates, expiration, and the delta strike range
    api_response = api_instance.get_horizontally_sliced_option_chain_by_delta(name, is_call=is_call, from_strike=from_strike, to_strike=to_strike, from_date=from_date, to_date=to_date, expiration=expiration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_horizontally_sliced_option_chain_by_delta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **is_call** | **bool**|  | [optional] 
 **from_strike** | **float**|  | [optional] 
 **to_strike** | **float**|  | [optional] 
 **from_date** | **date**|  | [optional] 
 **to_date** | **date**|  | [optional] 
 **expiration** | **date**|  | [optional] 

### Return type

[**list[OptionChain]**](OptionChain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_horizontally_sliced_option_chain_by_strike**
> list[OptionChain] get_horizontally_sliced_option_chain_by_strike(name, is_call=is_call, from_strike=from_strike, to_strike=to_strike, from_date=from_date, to_date=to_date, expiration=expiration)

Returns horizontal slice of option chain for the given symbol, option type, trading dates, expiration, and the strike range



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
name = 'name_example' # str | 
is_call = true # bool |  (optional)
from_strike = 1.2 # float |  (optional)
to_strike = 1.2 # float |  (optional)
from_date = '2013-10-20' # date |  (optional)
to_date = '2013-10-20' # date |  (optional)
expiration = '2013-10-20' # date |  (optional)

try:
    # Returns horizontal slice of option chain for the given symbol, option type, trading dates, expiration, and the strike range
    api_response = api_instance.get_horizontally_sliced_option_chain_by_strike(name, is_call=is_call, from_strike=from_strike, to_strike=to_strike, from_date=from_date, to_date=to_date, expiration=expiration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_horizontally_sliced_option_chain_by_strike: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **is_call** | **bool**|  | [optional] 
 **from_strike** | **float**|  | [optional] 
 **to_strike** | **float**|  | [optional] 
 **from_date** | **date**|  | [optional] 
 **to_date** | **date**|  | [optional] 
 **expiration** | **date**|  | [optional] 

### Return type

[**list[OptionChain]**](OptionChain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_option_chain**
> OptionChain get_option_chain(name, date=date, expiration=expiration)

Returns option chain for the given symbol, trading date, and expiration date



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
name = 'name_example' # str | 
date = '2013-10-20' # date |  (optional)
expiration = '2013-10-20' # date |  (optional)

try:
    # Returns option chain for the given symbol, trading date, and expiration date
    api_response = api_instance.get_option_chain(name, date=date, expiration=expiration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_option_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **date** | **date**|  | [optional] 
 **expiration** | **date**|  | [optional] 

### Return type

[**OptionChain**](OptionChain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_time**
> str get_server_time()

Get the current server time



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()

try:
    # Get the current server time
    api_response = api_instance.get_server_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_server_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trading_dates**
> list[date] get_trading_dates(symbol, _from=_from, to=to)

Returns actual trading days in specified from/to date range



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
symbol = 'symbol_example' # str | 
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)

try:
    # Returns actual trading days in specified from/to date range
    api_response = api_instance.get_trading_dates(symbol, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_trading_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 

### Return type

**list[date]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vertically_sliced_option_chain_by_delta**
> OptionChain get_vertically_sliced_option_chain_by_delta(name, is_call=is_call, from_strike=from_strike, to_strike=to_strike, date=date, expiration=expiration)

Returns vertical slice of option chain for the given symbol, option type, trading date, expiration, and the delta strike range



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
name = 'name_example' # str | 
is_call = true # bool |  (optional)
from_strike = 1.2 # float |  (optional)
to_strike = 1.2 # float |  (optional)
date = '2013-10-20' # date |  (optional)
expiration = '2013-10-20' # date |  (optional)

try:
    # Returns vertical slice of option chain for the given symbol, option type, trading date, expiration, and the delta strike range
    api_response = api_instance.get_vertically_sliced_option_chain_by_delta(name, is_call=is_call, from_strike=from_strike, to_strike=to_strike, date=date, expiration=expiration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_vertically_sliced_option_chain_by_delta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **is_call** | **bool**|  | [optional] 
 **from_strike** | **float**|  | [optional] 
 **to_strike** | **float**|  | [optional] 
 **date** | **date**|  | [optional] 
 **expiration** | **date**|  | [optional] 

### Return type

[**OptionChain**](OptionChain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vertically_sliced_option_chain_by_strike**
> OptionChain get_vertically_sliced_option_chain_by_strike(name, is_call=is_call, from_strike=from_strike, to_strike=to_strike, date=date, expiration=expiration)

Returns vertical slice of option chain for the given symbol, option type, trading date, expiration, and the strike range



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
name = 'name_example' # str | 
is_call = true # bool |  (optional)
from_strike = 1.2 # float |  (optional)
to_strike = 1.2 # float |  (optional)
date = '2013-10-20' # date |  (optional)
expiration = '2013-10-20' # date |  (optional)

try:
    # Returns vertical slice of option chain for the given symbol, option type, trading date, expiration, and the strike range
    api_response = api_instance.get_vertically_sliced_option_chain_by_strike(name, is_call=is_call, from_strike=from_strike, to_strike=to_strike, date=date, expiration=expiration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_vertically_sliced_option_chain_by_strike: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **is_call** | **bool**|  | [optional] 
 **from_strike** | **float**|  | [optional] 
 **to_strike** | **float**|  | [optional] 
 **date** | **date**|  | [optional] 
 **expiration** | **date**|  | [optional] 

### Return type

[**OptionChain**](OptionChain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volatility_skew**
> list[IVSkew] get_volatility_skew(symbol=symbol, expirations=expirations, date=date)

Returns volatility skews for the given trading symbol, the expiration and the observation dates



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
symbol = 'symbol_example' # str |  (optional)
expirations = ['2013-10-20'] # list[date] |  (optional)
date = ['2013-10-20'] # list[date] |  (optional)

try:
    # Returns volatility skews for the given trading symbol, the expiration and the observation dates
    api_response = api_instance.get_volatility_skew(symbol=symbol, expirations=expirations, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->get_volatility_skew: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | [optional] 
 **expirations** | [**list[date]**](date.md)|  | [optional] 
 **date** | [**list[date]**](date.md)|  | [optional] 

### Return type

[**list[IVSkew]**](IVSkew.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tickers**
> list[Ticker] search_tickers(query=query)

Searchs for symbols in the system with an optional query parameter. If query parameter is not used all symbols are returned



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketdataApi()
query = 'query_example' # str |  (optional)

try:
    # Searchs for symbols in the system with an optional query parameter. If query parameter is not used all symbols are returned
    api_response = api_instance.search_tickers(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketdataApi->search_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 

### Return type

[**list[Ticker]**](Ticker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


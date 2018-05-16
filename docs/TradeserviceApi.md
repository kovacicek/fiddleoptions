# swagger_client.TradeserviceApi

All URIs are relative to *https://localhost/mercury/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_decomposed_pn_l**](TradeserviceApi.md#calculate_decomposed_pn_l) | **POST** /tradeservice/dpnlCalculator | Returns the P&amp;L timeline decomposed by greeks for the given trade and the specified time range
[**calculate_historical_pn_l**](TradeserviceApi.md#calculate_historical_pn_l) | **POST** /tradeservice/histpnlCalculator | Returns the P&amp;L timeline for the given trade and the specified time range
[**calculate_historical_value**](TradeserviceApi.md#calculate_historical_value) | **POST** /tradeservice/histvalueCalculator | Returns the historical dollar denominated value for the given trade and the time window
[**calculate_instant_decomposed_pn_l**](TradeserviceApi.md#calculate_instant_decomposed_pn_l) | **POST** /tradeservice/instantdpnlCalculator | Returns the greek decomposed P&amp;L for the given trade and the time window
[**calculate_pn_l**](TradeserviceApi.md#calculate_pn_l) | **POST** /tradeservice/pnlCalculator | Returns the the t+0 curve and expiration PnL curve for the given trade


# **calculate_decomposed_pn_l**
> list[DataPoint] calculate_decomposed_pn_l(body=body, _from=_from, to=to)

Returns the P&L timeline decomposed by greeks for the given trade and the specified time range



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradeserviceApi()
body = swagger_client.Position() # Position |  (optional)
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)

try:
    # Returns the P&L timeline decomposed by greeks for the given trade and the specified time range
    api_response = api_instance.calculate_decomposed_pn_l(body=body, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeserviceApi->calculate_decomposed_pn_l: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Position**](Position.md)|  | [optional] 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 

### Return type

[**list[DataPoint]**](DataPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_historical_pn_l**
> list[DataPoint] calculate_historical_pn_l(body=body, _from=_from, to=to)

Returns the P&L timeline for the given trade and the specified time range



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradeserviceApi()
body = swagger_client.Position() # Position |  (optional)
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)

try:
    # Returns the P&L timeline for the given trade and the specified time range
    api_response = api_instance.calculate_historical_pn_l(body=body, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeserviceApi->calculate_historical_pn_l: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Position**](Position.md)|  | [optional] 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 

### Return type

[**list[DataPoint]**](DataPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_historical_value**
> list[DateValueDataPointDouble] calculate_historical_value(body=body, _from=_from, to=to)

Returns the historical dollar denominated value for the given trade and the time window



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradeserviceApi()
body = swagger_client.Position() # Position |  (optional)
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)

try:
    # Returns the historical dollar denominated value for the given trade and the time window
    api_response = api_instance.calculate_historical_value(body=body, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeserviceApi->calculate_historical_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Position**](Position.md)|  | [optional] 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 

### Return type

[**list[DateValueDataPointDouble]**](DateValueDataPointDouble.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_instant_decomposed_pn_l**
> DataPoint calculate_instant_decomposed_pn_l(body=body, _from=_from, to=to)

Returns the greek decomposed P&L for the given trade and the time window



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradeserviceApi()
body = swagger_client.Position() # Position |  (optional)
_from = '2013-10-20' # date |  (optional)
to = '2013-10-20' # date |  (optional)

try:
    # Returns the greek decomposed P&L for the given trade and the time window
    api_response = api_instance.calculate_instant_decomposed_pn_l(body=body, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeserviceApi->calculate_instant_decomposed_pn_l: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Position**](Position.md)|  | [optional] 
 **_from** | **date**|  | [optional] 
 **to** | **date**|  | [optional] 

### Return type

[**DataPoint**](DataPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_pn_l**
> PnL calculate_pn_l(body=body, date=date)

Returns the the t+0 curve and expiration PnL curve for the given trade



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TradeserviceApi()
body = swagger_client.Position() # Position |  (optional)
date = '2013-10-20' # date |  (optional)

try:
    # Returns the the t+0 curve and expiration PnL curve for the given trade
    api_response = api_instance.calculate_pn_l(body=body, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeserviceApi->calculate_pn_l: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Position**](Position.md)|  | [optional] 
 **date** | **date**|  | [optional] 

### Return type

[**PnL**](PnL.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


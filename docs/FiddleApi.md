# swagger_client.FiddleApi

All URIs are relative to *https://localhost/mercury/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_fiddle**](FiddleApi.md#delete_fiddle) | **DELETE** /fiddle/delete/{id} | Deletes Fiddle with specified id
[**get_fiddle**](FiddleApi.md#get_fiddle) | **GET** /fiddle/load/{id} | Returns the Fiddle with specified id
[**get_fiddle_list**](FiddleApi.md#get_fiddle_list) | **GET** /fiddle/{userId}/list | Returns the list of Fiddles for the specified user
[**get_position_legs**](FiddleApi.md#get_position_legs) | **POST** /fiddle/position/legs | Returns all options contracts that the specified options position is consisted of
[**get_trade_from_tos_string**](FiddleApi.md#get_trade_from_tos_string) | **POST** /fiddle/position/fromTOSString | Creates a list of positions from a list of trades specified in ThinkOrSwim format
[**save_fiddle**](FiddleApi.md#save_fiddle) | **POST** /fiddle/{userId}/save | Saves a new Fiddle or updates an existing one


# **delete_fiddle**
> delete_fiddle(id)

Deletes Fiddle with specified id



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FiddleApi()
id = 'id_example' # str | 

try:
    # Deletes Fiddle with specified id
    api_instance.delete_fiddle(id)
except ApiException as e:
    print("Exception when calling FiddleApi->delete_fiddle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiddle**
> Fiddle get_fiddle(id)

Returns the Fiddle with specified id



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FiddleApi()
id = 'id_example' # str | 

try:
    # Returns the Fiddle with specified id
    api_response = api_instance.get_fiddle(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiddleApi->get_fiddle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Fiddle**](Fiddle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiddle_list**
> list[object] get_fiddle_list(user_id)

Returns the list of Fiddles for the specified user



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FiddleApi()
user_id = 'user_id_example' # str | 

try:
    # Returns the list of Fiddles for the specified user
    api_response = api_instance.get_fiddle_list(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiddleApi->get_fiddle_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position_legs**
> list[object] get_position_legs(body=body)

Returns all options contracts that the specified options position is consisted of



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FiddleApi()
body = swagger_client.Trade() # Trade |  (optional)

try:
    # Returns all options contracts that the specified options position is consisted of
    api_response = api_instance.get_position_legs(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiddleApi->get_position_legs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Trade**](Trade.md)|  | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trade_from_tos_string**
> list[object] get_trade_from_tos_string(body=body)

Creates a list of positions from a list of trades specified in ThinkOrSwim format



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FiddleApi()
body = [swagger_client.list[str]()] # list[str] |  (optional)

try:
    # Creates a list of positions from a list of trades specified in ThinkOrSwim format
    api_response = api_instance.get_trade_from_tos_string(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiddleApi->get_trade_from_tos_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**|  | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_fiddle**
> Fiddle save_fiddle(user_id, body=body)

Saves a new Fiddle or updates an existing one



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FiddleApi()
user_id = 'user_id_example' # str | 
body = swagger_client.Fiddle() # Fiddle |  (optional)

try:
    # Saves a new Fiddle or updates an existing one
    api_response = api_instance.save_fiddle(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiddleApi->save_fiddle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**Fiddle**](Fiddle.md)|  | [optional] 

### Return type

[**Fiddle**](Fiddle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


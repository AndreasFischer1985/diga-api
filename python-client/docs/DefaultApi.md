# diga.DefaultApi

All URIs are relative to *https://diga-api.bfarm.de/diga-vz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_get**](DefaultApi.md#apps_get) | **GET** /apps | Liste aller DiGAs
[**apps_id_get**](DefaultApi.md#apps_id_get) | **GET** /apps/{id} | Detail-Informationen zu einer DiGa.
[**prescriptions_get**](DefaultApi.md#prescriptions_get) | **GET** /prescriptions | Technische Informationen zu einer DiGa.


# **apps_get**
> Digalist apps_get()

Liste aller DiGAs

### Example


```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from deutschland.diga.model.digalist import Digalist
from pprint import pprint
# Defining the host is optional and defaults to https://diga-api.bfarm.de/diga-vz
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga-api.bfarm.de/diga-vz"
)


# Enter a context with an instance of the API client
with diga.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Liste aller DiGAs
        api_response = api_instance.apps_get()
        pprint(api_response)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->apps_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Digalist**](Digalist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_id_get**
> Digadetails apps_id_get(id)

Detail-Informationen zu einer DiGa.

Detail-Informationen zu einer DiGa.

### Example


```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from deutschland.diga.model.digadetails import Digadetails
from pprint import pprint
# Defining the host is optional and defaults to https://diga-api.bfarm.de/diga-vz
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga-api.bfarm.de/diga-vz"
)


# Enter a context with an instance of the API client
with diga.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = 961 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Detail-Informationen zu einer DiGa.
        api_response = api_instance.apps_id_get(id)
        pprint(api_response)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->apps_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Digadetails**](Digadetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prescriptions_get**
> Digaprescription prescriptions_get(filter5_bapp5_d)

Technische Informationen zu einer DiGa.

Detail-Informationen zu einer DiGa.

### Example


```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from deutschland.diga.model.digaprescription import Digaprescription
from pprint import pprint
# Defining the host is optional and defaults to https://diga-api.bfarm.de/diga-vz
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga-api.bfarm.de/diga-vz"
)


# Enter a context with an instance of the API client
with diga.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    filter5_bapp5_d = 961 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Technische Informationen zu einer DiGa.
        api_response = api_instance.prescriptions_get(filter5_bapp5_d)
        pprint(api_response)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->prescriptions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter5_bapp5_d** | **int**|  |

### Return type

[**Digaprescription**](Digaprescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


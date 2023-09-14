# diga.DefaultApi

All URIs are relative to *https://diga.bfarm.de/api/fhir/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_entry_get**](DefaultApi.md#catalog_entry_get) | **GET** /CatalogEntry | CatalogEntry
[**charge_item_definition_get**](DefaultApi.md#charge_item_definition_get) | **GET** /ChargeItemDefinition | ChargeItemDefinition
[**device_definition_get**](DefaultApi.md#device_definition_get) | **GET** /DeviceDefinition | DeviceDefinition
[**organization_get**](DefaultApi.md#organization_get) | **GET** /Organization | Organization
[**questionnaire_get**](DefaultApi.md#questionnaire_get) | **GET** /Questionnaire | Questionnaire
[**questionnaire_response_get**](DefaultApi.md#questionnaire_response_get) | **GET** /QuestionnaireResponse | Questionnaire


# **catalog_entry_get**
> catalog_entry_get(count, profile)

CatalogEntry

### Example

* Bearer Authentication (bearerAuth):

```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://diga.bfarm.de/api/fhir/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga.bfarm.de/api/fhir/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = diga.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with diga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    count = 1000 # int | 
    profile = "https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppCatalogEntry" # str | 

    # example passing only required values which don't have defaults set
    try:
        # CatalogEntry
        api_instance.catalog_entry_get(count, profile)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->catalog_entry_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  |
 **profile** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_item_definition_get**
> charge_item_definition_get(count, profile)

ChargeItemDefinition

### Example

* Bearer Authentication (bearerAuth):

```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://diga.bfarm.de/api/fhir/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga.bfarm.de/api/fhir/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = diga.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with diga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    count = 1000 # int | 
    profile = "https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppPrescriptionUnit" # str | 

    # example passing only required values which don't have defaults set
    try:
        # ChargeItemDefinition
        api_instance.charge_item_definition_get(count, profile)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->charge_item_definition_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  |
 **profile** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_definition_get**
> device_definition_get(count, profile)

DeviceDefinition

### Example

* Bearer Authentication (bearerAuth):

```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://diga.bfarm.de/api/fhir/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga.bfarm.de/api/fhir/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = diga.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with diga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    count = 1000 # int | 
    profile = "https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthApp" # str | 

    # example passing only required values which don't have defaults set
    try:
        # DeviceDefinition
        api_instance.device_definition_get(count, profile)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->device_definition_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  |
 **profile** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_get**
> organization_get(count, profile)

Organization

### Example

* Bearer Authentication (bearerAuth):

```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://diga.bfarm.de/api/fhir/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga.bfarm.de/api/fhir/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = diga.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with diga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    count = 1000 # int | 
    profile = "https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppManufacturer" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Organization
        api_instance.organization_get(count, profile)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->organization_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  |
 **profile** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **questionnaire_get**
> questionnaire_get(count, profile)

Questionnaire

### Example

* Bearer Authentication (bearerAuth):

```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://diga.bfarm.de/api/fhir/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga.bfarm.de/api/fhir/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = diga.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with diga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    count = 1000 # int | 
    profile = "https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppQuestionnaire" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Questionnaire
        api_instance.questionnaire_get(count, profile)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->questionnaire_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  |
 **profile** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **questionnaire_response_get**
> questionnaire_response_get(count, profile)

Questionnaire

### Example

* Bearer Authentication (bearerAuth):

```python
import time
from deutschland import diga
from deutschland.diga.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://diga.bfarm.de/api/fhir/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = diga.Configuration(
    host = "https://diga.bfarm.de/api/fhir/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = diga.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with diga.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    count = 1000 # int | 
    profile = "https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppQuestionnaireResponse" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Questionnaire
        api_instance.questionnaire_response_get(count, profile)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->questionnaire_response_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  |
 **profile** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# diga
API zum DiGA-Verzeichnis https://diga.bfarm.de/de/ des Bundesinstituts für Arzneimittel und Medizinprodukte BfArM. Das Verzeichnis bietet eine Auswahl an digitalen Gesundheitsanwendungen (DiGA), die vom BfArM gemäß § 139e SGB V bewertet wurden. 

Anfragen sind als GET-requests zu stellen, wobei zur Authorisierung ein Bearer Token im Header \"authorization\" anzugeben ist, der wiederum einem GET-request an https://diga.bfarm.de/de/verzeichnis zu entnehmen ist (Im contetn von meta name=\"host-app/config/environment\" unter \"APP\"/\"fhir\"/\"token\").


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/AndreasFischer1985/diga-api](https://github.com/AndreasFischer1985/diga-api)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

```sh
pip install deutschland[diga]
```

### poetry install

```sh
poetry add deutschland -E diga
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Usage

Import the package:
```python
from deutschland import diga
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
from deutschland import diga
from pprint import pprint
from deutschland.diga.api import default_api
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

    try:
        # CatalogEntry
        api_instance.catalog_entry_get(count, profile)
    except diga.ApiException as e:
        print("Exception when calling DefaultApi->catalog_entry_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://diga.bfarm.de/api/fhir/v2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**catalog_entry_get**](docs/DefaultApi.md#catalog_entry_get) | **GET** /CatalogEntry | CatalogEntry
*DefaultApi* | [**charge_item_definition_get**](docs/DefaultApi.md#charge_item_definition_get) | **GET** /ChargeItemDefinition | ChargeItemDefinition
*DefaultApi* | [**device_definition_get**](docs/DefaultApi.md#device_definition_get) | **GET** /DeviceDefinition | DeviceDefinition
*DefaultApi* | [**organization_get**](docs/DefaultApi.md#organization_get) | **GET** /Organization | Organization
*DefaultApi* | [**questionnaire_get**](docs/DefaultApi.md#questionnaire_get) | **GET** /Questionnaire | Questionnaire
*DefaultApi* | [**questionnaire_response_get**](docs/DefaultApi.md#questionnaire_response_get) | **GET** /QuestionnaireResponse | Questionnaire


## Documentation For Models



## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication


## Author

andreasfischer1985@web.de


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in diga.apis and diga.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from deutschland.diga.api.default_api import DefaultApi`
- `from deutschland.diga.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
from deutschland import diga
from deutschland.diga.apis import *
from deutschland.diga.models import *
```


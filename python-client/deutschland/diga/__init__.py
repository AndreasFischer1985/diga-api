# flake8: noqa

"""
    DiGA API

    API zum DiGA-Verzeichnis https://diga.bfarm.de/de/ des Bundesinstituts für Arzneimittel und Medizinprodukte BfArM. Das Verzeichnis bietet eine Auswahl an digitalen Gesundheitsanwendungen (DiGA), die vom BfArM gemäß § 139e SGB V bewertet wurden.   Anfragen sind als GET-requests zu stellen, wobei zur Authorisierung ein Bearer Token im Header \"authorization\" anzugeben ist, der wiederum einem GET-request an https://diga.bfarm.de/de/verzeichnis zu entnehmen ist (Im contetn von meta name=\"host-app/config/environment\" unter \"APP\"/\"fhir\"/\"token\").   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


__version__ = "0.1.0"

# import ApiClient
from deutschland.diga.api_client import ApiClient

# import Configuration
from deutschland.diga.configuration import Configuration

# import exceptions
from deutschland.diga.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

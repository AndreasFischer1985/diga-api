# DiGA API 

API zum DiGA-Verzeichnis https://diga.bfarm.de/de/ des Bundesinstituts für Arzneimittel und Medizinprodukte BfArM. Das Verzeichnis bietet eine Auswahl an digitalen Gesundheitsanwendungen (DiGA), die vom BfArM gemäß § 139e SGB V bewertet wurden. 

Anfragen sind als GET-requests zu stellen, wobei zur Authorisierung ein Bearer Token im Header "authorization" anzugeben ist, der wiederum einem GET-request an https://diga.bfarm.de/de/verzeichnis zu entnehmen ist (Im contetn von meta name="host-app/config/environment" unter "APP"/"fhir"/"token").

## Beispiel

```bash
token="116b0a73-6e3b-4a88-9313-9947a4fed9ef"

devDef1=$(curl -m 60 \
-H "authorization: Bearer $token" \
'https://diga.bfarm.de/api/fhir/v2.0/DeviceDefinition?_count=1000&_profile=https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthApp')

devDev2=$(curl -m 60 \
-H "authorization: Bearer $token" \
'https://diga.bfarm.de/api/fhir/v2.0/DeviceDefinition?_count=1000&_profile=https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppModule')

catalogEntry=$(curl -m 60 \
-H "authorization: Bearer $token" \
'https://diga.bfarm.de/api/fhir/v2.0/CatalogEntry?_count=1000&_profile=https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppCatalogEntry')

organization=$(curl -m 60 \
-H "authorization: Bearer $token" \
'https://diga.bfarm.de/api/fhir/v2.0/Organization?_count=1000&_profile=https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppManufacturer')

chargeItemDefinition=$(curl -m 60 \
-H "authorization: Bearer $token" \
'https://diga.bfarm.de/api/fhir/v2.0/ChargeItemDefinition?_count=1000&_profile=https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppPrescriptionUnit')

questionnaire=$(curl -m 60 \
-H "authorization: Bearer $token" \
'https://diga.bfarm.de/api/fhir/v2.0/Questionnaire?_count=1000&_profile=https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppQuestionnaire')

questionnaireResponse=$(curl -m 60 \
-H "authorization: Bearer $token" \
'https://diga.bfarm.de/api/fhir/v2.0/QuestionnaireResponse?_count=1000&_profile=https%3A%2F%2Ffhir.bfarm.de%2FStructureDefinition%2FHealthAppQuestionnaireResponse')

```

# DiGA API 

API zum DiGA-Verzeichnis https://diga.bfarm.de/de/ des Bundesinstituts für Arzneimittel und Medizinprodukte BfArM. Das Verzeichnis bietet eine Auswahl an digitalen Gesundheitsanwendungen (DiGA), die vom BfArM gemäß § 139e SGB V bewertet wurden. 

## Beispiel

```bash
apps=$(curl 'https://diga-api.bfarm.de/diga-vz/apps/')
appDetails=$(curl 'https://diga-api.bfarm.de/diga-vz/apps/961')
appPrescription=$(curl 'https://diga-api.bfarm.de/diga-vz/prescriptions?filter%5Bapp%5D=961')
```

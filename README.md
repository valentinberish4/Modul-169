# Modul-169
## Repository für das Modul 169 - Services mit Containern bereitstellen
Modulidentifikation: https://www.modulbaukasten.ch/module/169/1/de-DE?title=Services-mit-Containern-bereitstellen

### FastApi
------
FastAPI ist ein Python-Framework zur Entwicklung von schnellen und skalierbaren Webanwendungen und APIs. Es basiert auf dem ASGI-Server und bietet automatische Dokumentation, Validierung von Anfragedaten, Typüberprüfung und schnelle Ausführung. Es wird oft für die Entwicklung von Microservices, RESTful APIs und Backend-Systemen verwendet, die hohe Leistung, Echtzeitkommunikation und effiziente Verarbeitung von HTTP-Anfragen erfordern.
Für die Leistungsbeurteilung (LB) habe ich ein einfaches Fastapi-Projekt mithilfe von Docker deployed.

### Requirements
------
Lediglich Docker und das latest Python Image:
```
docker pull python
```
### Get started:
------
Zunächst Repo clonen:
```
git clone https://github.com/valentinberish4/Modul-169.git
```
Mit folgenden Befehl die Webapp starten:
```
docker-compose up -d
```
Nun sollte auf http://localhost:8000/docs Fastapi zu sehen sein.
Wenn Änderungen getätigt werden, kann mit folgenden Befehl der Container neugestartet werden:
```
docker restart core-api-container
```

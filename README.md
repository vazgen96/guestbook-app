# guestbook-app

## Projektbeschreibung
Eine einfache Gästebuch-Webanwendung. Benutzer können ihren Namen eintragen, der in einer Redis-Datenbank gespeichert und auf der Startseite angezeigt wird.

## Voraussetzungen
- Docker
- Docker Compose

## Startanleitung
1. Repository klonen:
```bash
   git clone https://github.com/vazgen96/guestbook-app.git
   cd guestbook-app
```


2. `.env` Datei erstellen:
```bash
   cp .env.example .env
```

## Konfiguration
Eine `.env` Datei wird benötigt. Kopiere die Beispieldatei:
```bash
cp .env.example .env
```

3. Anwendung starten:
```bash
   docker compose up
```


4. Im Browser öffnen:
```
   http://localhost:5000
```

## Hinweis: Port bereits belegt?

Falls Port 5000 bereits belegt ist, kann der externe Port in der `docker-compose.yml` geändert werden:
```yaml
ports:
  - "5000:5000"  # linke Zahl ändern
```

Danach die App unter http://localhost:8080 öffnen.

Belegten Port prüfen:

Windows:
```bash
netstat -ano | findstr :5000
```

Mac/Linux:
```bash
lsof -i :5000
```

## Verwendete Technologien
- Python 3
- Flask
- Redis
- Docker
- Docker Compose

## Autor
vazgen96 
# Lektionens trin

🌐 [English](Lecture-Steps) · **Dansk** · [Bahasa Melayu](Lecture-Steps-ms)

## Trin 1: Kør den færdige blog lokalt

**Hvad vi fik ud af det:** Bloggen fra dag 69 og 70 er udgangspunktet. Ved at køre den først bevises det, at koden virker, før noget ændres, så et senere problem vides at komme fra udrulningsarbejdet.

![Skærmbillede 01-blog-home](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/01-blog-home.png)

## Trin 2: Sæt projektet under versionsstyring

**Hvad vi fik ud af det:** Git gemmer hver ændring med en besked. Historikken kan læses, sammenlignes og fortrydes, og det er den, hostingplatformen udruller fra.

![Skærmbillede 02-commit-history](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/02-commit-history.png)

## Trin 3: Flyt hemmeligheder til miljøvariabler

**Hvad vi fik ud af det:** Den hemmelige nøgle, databaseadressen og mail-loginet står ikke længere i kildekoden. `FLASK_KEY`, `DB_URI` og `MAIL_*` læses fra miljøet, så den samme kode kører på en bærbar og på en server, og ingen hemmelighed havner i repositoriet. `debug` er slået fra.

![Skærmbillede 03-environment-variables](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/03-environment-variables.png)

## Trin 4: Server appen med gunicorn og en Procfile

**Hvad vi fik ud af det:** Flasks indbyggede server er kun til udvikling. En WSGI-server som gunicorn taler HTTP med omverdenen og kalder Flask-`app`. Linjen `web: gunicorn main:app` i `Procfile` fortæller værten, hvilken kommando der starter webprocessen.

![Skærmbillede 04-procfile-gunicorn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/04-procfile-gunicorn.png)

## Trin 5: Skub projektet til git-værten

**Hvad vi fik ud af det:** Repositoriet på git-værten er den ene kilde, udrulningen bygges fra. En `.gitignore` holder det virtuelle miljø, databasefilen og hemmeligheder ude.

![Skærmbillede 05-repository-files](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/05-repository-files.png)

## Trin 6: Host appen i containere

**Hvad vi fik ud af det:** Heroku har ikke længere en gratis plan, så Docker tager dens plads. `Dockerfile` bygger imaget, og `compose.yaml` starter bloggen sammen med databasen. Det samme image kan køre på enhver maskine med Docker.

![Skærmbillede 06-docker-compose](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/06-docker-compose.png)

## Trin 7: Opgrader SQLite til PostgreSQL

**Hvad vi fik ud af det:** SQLite er én fil og kan gå tabt, når en vært flytter filsystemet. PostgreSQL er en rigtig databaseserver. Fordi SQLAlchemy skjuler forskellen, er det kun `DB_URI`, der ændres; koden er den samme. `psycopg` er driveren.

![Skærmbillede 07-postgres-tables](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/07-postgres-tables.png)

## Trin 8: Gå live: opret bruger, log ind og skriv det første indlæg

**Hvad vi fik ud af det:** På en tom database bliver den første oprettede bruger administrator og kan skrive indlæg. Andre brugere kan læse og kommentere. Siderne viser bloggen kørende fra containeren med PostgreSQL.

![Skærmbillede 10-register-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/10-register-form.png)

![Skærmbillede 11-login-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/11-login-form.png)

![Skærmbillede 12-new-post-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/12-new-post-form.png)

![Skærmbillede 13-blog-post](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/13-blog-post.png)

![Skærmbillede 14-about](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/14-about.png)

## Trin 9: Kontroller resultatet med tests

**Hvad vi fik ud af det:** Pytest-suiten beviser, at bloggen, konfigurationen og Procfile stadig opfører sig rigtigt efter flytningen. Kør den før hvert push.

![Skærmbillede 09-tests](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/09-tests.png)


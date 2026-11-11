# Lecture steps

🌐 **English** · [Dansk](Lecture-Steps-da) · [Bahasa Melayu](Lecture-Steps-ms)

## Step 1: Run the finished blog locally

**What we gained:** The blog from day 69 and 70 is the starting point. Running it first proves that the code works before anything is changed, so a later problem is known to come from the deployment work.

![Screenshot 01-blog-home](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/01-blog-home.png)

## Step 2: Put the project under version control

**What we gained:** Git records every change with a message. The history can be read, compared and undone, and it is what the hosting platform deploys from.

![Screenshot 02-commit-history](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/02-commit-history.png)

## Step 3: Move secrets into environment variables

**What we gained:** The secret key, database address and mail login are no longer in the source. `FLASK_KEY`, `DB_URI` and `MAIL_*` are read from the environment, so the same code runs on a laptop and on a server and no secret ends up in the repository. `debug` is switched off.

![Screenshot 03-environment-variables](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/03-environment-variables.png)

## Step 4: Serve the app with gunicorn and a Procfile

**What we gained:** Flask's built-in server is only for development. A WSGI server such as gunicorn talks HTTP to the world and calls the Flask `app`. The `Procfile` line `web: gunicorn main:app` tells the host which command starts the web process.

![Screenshot 04-procfile-gunicorn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/04-procfile-gunicorn.png)

## Step 5: Push the project to the git host

**What we gained:** The repository on the git host is the single source the deployment is built from. A `.gitignore` keeps the virtual environment, the database file and secrets out of it.

![Screenshot 05-repository-files](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/05-repository-files.png)

## Step 6: Host the app in containers

**What we gained:** Heroku no longer has a free plan, so Docker takes its place. The `Dockerfile` builds the image and `compose.yaml` starts the blog together with its database. The same image can run on any machine with Docker.

![Screenshot 06-docker-compose](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/06-docker-compose.png)

## Step 7: Upgrade SQLite to PostgreSQL

**What we gained:** SQLite is a single file and can be lost when a host moves the file system. PostgreSQL is a real database server. Because SQLAlchemy hides the difference, only the `DB_URI` changes; the code stays the same. `psycopg` is the driver.

![Screenshot 07-postgres-tables](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/07-postgres-tables.png)

## Step 8: Go live: register, sign in and write the first post

**What we gained:** On an empty database the first registered user becomes the administrator and can write posts. Other users can read and comment. These pages show the blog running from the container with PostgreSQL.

![Screenshot 10-register-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/10-register-form.png)

![Screenshot 11-login-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/11-login-form.png)

![Screenshot 12-new-post-form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/12-new-post-form.png)

![Screenshot 13-blog-post](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/13-blog-post.png)

![Screenshot 14-about](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/14-about.png)

## Step 9: Check the result with tests

**What we gained:** The pytest suite proves the blog, the configuration and the Procfile still behave after the move. Run it before every push.

![Screenshot 09-tests](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/071-blog-for-deployment/raw/branch/main/docs/images/09-tests.png)


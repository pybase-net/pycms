# PyCMS

## Software Information

1. Version: 0.1
2. Description: A headless CMS built by Django and VueJS
3. Main features: manage pages, manage posts and categories

Development concepts, we'll implement layer architecture:

1. Presentation Layer

- Views: response can be json/html

2. Business Layer

- Services

3. Persistence Layer

- Models

## Prerequisites

## Quick start

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) as package management then run these following commands

```sh
make setup
make run
```

## Development

```sh
source .venv/bin/activate
uv .venv
uv add Django

django-admin help
django-admin startproject cms .
```

### High level design

**Modules**

- user
- pages
- posts

**apps**

- backoffice : we'll create a SPA inside django

### Creating app(modules) in django

```sh
mkdir -p modules/user
django-admin startapp user modules/user

mkdir -p apps/backoffice
django-admin startapp backoffice apps/backoffice
```

### Using uv

```sh
# add new package
uv add package-name
# lock package
uv lock
# exporting lockfile
uv export --format requirements-txt > requirements.txt
# sync
uv sync
```

## Reference

- [uv package management](https://docs.astral.sh/uv/getting-started/installation/)
- [install django](https://docs.djangoproject.com/en/5.1/topics/install/#installing-official-release)

#!/usr/bin/bash

set -e

# Удаляем .py файлы в папках migrations, исключая venv
find . -path "./venv" -prune -o -path "*/migrations/*.py" -not -name "__init__.py" -exec rm -f {} \;

# Удаляем .pyc файлы в папках migrations, исключая venv
find . -path "./venv" -prune -o -path "*/migrations/*.pyc" -exec rm -f {} \;

find . -name "db.sqlite3" -exec rm {} \;


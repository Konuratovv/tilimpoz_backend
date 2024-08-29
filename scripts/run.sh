#!/usr/bin/bash/

set -e

PS3="Вы запускаете локально или на сервере(1-локально 2-на сервере): "

select opt in "Локально" "На сервере"; do
    case $opt in
        "Локально")
            echo "Поднимаем локально"

            PS3="Выбери опцию(1-Удалить миграции 2-Не удалять миграции): "

            select opt in "Удалить миграции" "Не удалять миграции"; do

                case $opt in
                    "Удалить миграции")
                        chmod +x ./scripts/delete-migrations.sh
                        sh ./scripts/delete-migrations.sh
                        echo "Миграции удалены"
                        break
                        ;;
                    "Не удалять миграции")
                        echo "Не удаляем миграции"
                        break
                        ;;
                    *)
                        echo "Вводи только 1 или 2 $REPLY"
                        break
                        ;;
                esac
            done

            python manage.py makemigrations
            python manage.py migrate

            python manage.py shell < ./scripts/create-superuser.py
            python manage.py runserver
            break
            ;;
        
        "На сервере")
            echo "Поднимаем на сервере"
            PS3="Удалять волюмы?(1-ДА 2-НЕТ): "
            select opt in "Да" "Нет"; do
                case $opt in
                    "Да")
                        docker-compose down -v
                        docker-compose up --build
                        break
                        ;;
                    "Нет")
                        docker-compose down
                        docker-compose up --build
                        break
                        ;;
                esac
            done
    esac
done
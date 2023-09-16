# Cервис проверки файлов
Разработанный на Django сервис для загрузки и проверки файлов .py с регистрацией и авторизацией пользователя, отложенным запуском проверки и отправкой результатов на почту с использованием Celery/Redis.

Каждые 5 секунд Celery Beat запускает задачу start_run_checks, которая отбирает загруженные/измененные файлы и формирует задачи process_file.
Задача process_file имитирует обработку файла и формирует задачу send_report с результатом обработки.

## Конфигурация
Конфигурация в `src/.env`, пример `src/.env.example`

## Установка
```bash
cp src/.env.example src/.env  # default environment variables
docker-compose up -d
```

## Запуск тестов
```bash
make test
```

## Интерфейс
![Alt text](images/home.jpeg)
Список загруженных файлов

![Alt text](images/detail.jpeg)
Отчет проверки файла

![Alt text](images/flower.jpeg)
Мониторинг в Flower

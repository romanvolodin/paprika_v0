# paprika

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в формате `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:

- `PAPRIKA_SECRET_KEY` — секретный ключ проекта.
- `PAPRIKA_DEBUG` — режим отладки. Поставьте `true`, чтобы увидеть отладочную информацию в случае ошибки.
- `PAPRIKA_ALLOWED_HOSTS` — список доменов/хостов, на которых будет работать сайт. Подробнее в [документации Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts)

Пример:

```env
PAPRIKA_SECRET_KEY=r394nkk!dh&=jg!=-g4@f$o4de%ho0e+srarblw$-z3@(k07a1
PAPRIKA_DEBUG=false
PAPRIKA_ALLOWED_HOSTS=localhost,127.0.0.1,example.com,www.example.com
```
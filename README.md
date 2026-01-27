# Traffk - Telegram-бот для безопасных сделок

## Описание
Traffk - это Telegram-бот, который выступает в роли гаранта в сделках между рекламодателями и арбитражниками. Система работает по принципу эскроу: средства замораживаются на счете рекламодателя до подтверждения выполнения задания.

## Функционал

### Рекламодатель (Advertiser)
- Создание заданий с фиксированной оплатой
- Пополнение баланса
- Подтверждение выполнения заданий и автоматическая оплата трафику

### Трафик (Traffic)
- Просмотр ленты публичных заданий
- Взятие заданий в работу
- Получение уникальных ссылок для отслеживания
- Отметка заданий как выполненных
- Вывод заработанных средств

### Администратор (Admin)
- Ручное управление спорами
- Пополнение и вывод средств пользователей
- Арбитраж в спорных ситуациях

## Технические требования

- Python 3.11+
- Aiogram 3.x
- PostgreSQL (или SQLite для MVP)
- Redis (для хранения состояний FSM)

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd traffk_bot
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` и укажите переменные окружения:
```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=sqlite+aiosqlite:///./traffk_bot.db
REDIS_URL=redis://localhost:6379
SECRET_KEY=your_secret_key
ADMIN_IDS=123456789,987654321
TINKOFF_CARD=your_tinkoff_card_number
USDT_ADDRESS=your_usdt_wallet_address
```

4. Запустите бота:
```bash
python -m traffk_bot.main
```

## Структура проекта

```
traffk_bot/
├── main.py                 # Основной файл запуска
├── config/
│   └── settings.py         # Настройки приложения
├── models/                 # Модели базы данных
│   ├── __init__.py
│   ├── database.py
│   ├── user.py
│   ├── task.py
│   ├── assignment.py
│   └── transaction.py
├── services/               # Бизнес-логика
│   ├── __init__.py
│   ├── user_service.py
│   ├── task_service.py
│   ├── assignment_service.py
│   ├── transaction_service.py
│   └── escrow_service.py
├── handlers/               # Обработчики команд бота
│   ├── __init__.py
│   ├── start_handler.py
│   ├── balance_handler.py
│   ├── history_handler.py
│   ├── task_handlers.py
│   ├── feed_handler.py
│   ├── my_assignments_handler.py
│   └── my_tasks_handler.py
└── utils/                  # Вспомогательные функции
    ├── __init__.py
    └── helpers.py
```

## Используемые команды

- `/start` - регистрация и главное меню
- `/balance` - проверка баланса
- `/history` - история транзакций
- `/create_task` - создание нового задания
- `/feed` - лента публичных заданий
- `/my_assignments` - мои взятые задания
- `/my_tasks` - мои созданные задачи

## Принцип работы системы эскроу

1. Рекламодатель создает задание и оплачивает его, средства замораживаются на его счете
2. Трафик берет задание в работу и получает уникальную ссылку
3. После выполнения задания трафик отмечает его как выполненное
4. Рекламодатель получает уведомление и подтверждает выполнение
5. Средства автоматически переводятся трафику

## Лицензия
MIT
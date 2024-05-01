
Assync Currency Tracker

Overview
This project is built using Docker Compose and leverages the Arq library for Python along with Beanie for asynchronous MongoDB operations. The worker component executes a cron job every minute to capture specified currencies asynchronously.

Components
Scheduler: Utilizes Arq library for asynchronous job execution. The worker is configured to run a cron job every minute, fetching currency data and storing it in MongoDB using Beanie.

MongoDB: Data is stored in MongoDB using asynchronous operations through Beanie, which simplifies the process of defining and interacting with MongoDB documents.

Redis: Redis is used as the message broker and task queue for Arq, facilitating job distribution and management.

File Structure
.
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── src/
│   ├── configs/
│   │   ├── config.py
│   │   └── redis_config.py
│   ├── jobs/
│   │   ├── controllers/
│   │   │   └── insert_new_value.py
│   │   ├── contracts/
│   │   │   └── implementations/
│   │   │       └── beanie/
│   │   │           └── document.py
│   │   └── daily_currency.py
│   |
│   └── scheduler.py
└── tests/
    └── test.py


## **Assync Currency Tracker **

## **Overview **
This project is built using Docker Compose and leverages the Arq library for Python along with Beanie for asynchronous MongoDB operations. The worker component executes a cron job every minute to capture specified currencies asynchronously.

## **Components **
Scheduler: Utilizes Arq library for asynchronous job execution. The worker is configured to run a cron job every minute, fetching currency data and storing it in MongoDB using Beanie.

MongoDB: Data is stored in MongoDB using asynchronous operations through Beanie, which simplifies the process of defining and interacting with MongoDB documents.

Redis: Redis is used as the message broker and task queue for Arq, facilitating job distribution and management.

## **File Structure **
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

## **Installation **

**Clone the Repository:**
```bash
Copy code
git clone <https://github.com/davidsonsalinas/AssyncCurrencyTracker.git>
cd <AssyncCurrencyTracker>
Environment Setup:
Create a .env file based on .env.example with appropriate configurations.
Install Dependencies:
bash
Copy code
poetry install
Run with Docker Compose:
bash
Copy code
docker-compose up --build
```
## **Usage **

The scheduler will start executing the defined cron job (daily_currency) every minute.

The insert_new_value job can be triggered manually or integrated into other workflows.

## **Configuration **

MongoDB: Configure the MongoDB URL (MONGODB_URL) and document models (DOCUMENT_MODELS) in config.py.
Redis: Configure Redis connection details in redis_config.py.

## **Additional Notes **

Ensure that Redis and MongoDB services are accessible and properly configured as per the project settings.
Customize the cron jobs and worker functions (insert_new_value, etc.) based on project requirements.

## **Contributors **
Davidson salinas

## Development and testing environment

- Python 3
- Django 2

## How to run the application

Clone the repository and then change directory to the cloned repository.
1. Setup and active your virtual environment
```sh
python3 -m venv venv
source venv/bin/activate
```
2. Install Python dependencies
```sh
pip install -r requirements-dev.txt
```
3. Run the database migrations and load data into the database
```sh
python manage.py migrate
python manage.py loaddata metrics
```
4. Run the API
```sh
python manage.py runserver
```

## API endpoint URL

- [http://localhost:8000/api/metrics/](http://localhost:8000/api/metrics/)

## API use-cases

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
- [http://localhost:8000/api/metrics/?fields=impressions,clicks,channel,country&groupby=channel,country&date_to=2017-05-31&ordering=-clicks](http://localhost:8000/api/metrics/?fields=impressions,clicks,channel,country&groupby=channel,country&date_to=2017-05-31&ordering=-clicks)
2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
- [http://localhost:8000/api/metrics/?fields=installs,date&groupby=date&os=ios&date_from=2017-05-01&date_to=2017-05-31&ordering=date](http://localhost:8000/api/metrics/?fields=installs,date&groupby=date&os=ios&date_from=2017-05-01&date_to=2017-05-31&ordering=date)
3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
- [http://localhost:8000/api/metrics/?fields=revenue,os&groupby=os&date=2017-06-01&country=US&ordering=-revenue](http://localhost:8000/api/metrics/?fields=revenue,os&groupby=os&date=2017-06-01&country=US&ordering=-revenue)
4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.
- [http://localhost:8000/api/metrics/?fields=cpi,spend,channel&groupby=channel&country=CA&ordering=-cpi](http://localhost:8000/api/metrics/?fields=cpi,spend,channel&groupby=channel&country=CA&ordering=-cpi)

## How to run tests

Run the tests
```sh
python manage.py test
```

## TODO

- Dockerize the application.

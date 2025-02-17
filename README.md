
# External data sourcing
In this repository you're going to learn how to import external data and save it to your database to extend your existing data.

## Why external data sourcing?
In order to make the best decisions, data is vital. Having extensive and detailed data available enables sophisticated analyses and allows to predict the future more accurately. To facilitate this, a Data Analyst needs to be able to not only work with internal data but also with data from different external sources. They need to be able to access different data storages such as other databases or APIs, import, clean and prepare the data and ultimately make it available to all relevant stakeholders by adding it to existing internal data sources.
<br></br>
## Tasks
### Set up your environment
#### For the Data Analytics Full-Time Bootcamp:
- Before you start, activate your nf_sql environment.
#### For the Data Part-Time Bootcamp:
- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install jupyterlab
    pip install pandas==2.0.1
    pip install python-dotenv
    pip install sqlalchemy==1.4.39
    pip install psycopg2-binary
    ```
---
### Important: sql_functions.py and .env
- Copy your versions of the files ```sql_functions.py``` and ```.env``` from the 'Internal Data Sourcing' repository in this folder.
for example using the terminal:
```bash
cp ../da-internal_data_sourcing/notebooks/.env .
```
- Please work through all the notebooks.
## Part 1: Add carriers to the database
1. Import data that is stored online in a csv directly from the web into python
2. Store the data into an existing database
<br></br>
## Part 2: Add aircrafts to the database
1. Download data stored in a zip file to your local file storage using python
2. Unpack the contents of the zip file with python
3. Apply data transformation and cleaning
4. Combine data from multiple files
5. Subset aircraft data based on existing data in database
6. Store data into an existing database
<br></br>
## Part 3: Getting Started with API
1. Learn about OpenWeather API's available data and limitations
2. Sign-up to the OpenWeather API (if not already done yet)
<br></br>
## Part 4: Get Weather from API
1. Use your API key to make your first call to the OpenWeather API
2. Learn how to adjust your API calls to get the data you need
3. Learn how to access and extract data from your JSON
4. Learn how to flatten nested JSON data and transform it into a DataFrame for future analysis
5. Learn how to make multiple calls to the API with different parameters in an automated way
<br></br>



## 📌 README: Climate Analysis & API Development
---
# 🏄 Honolulu Climate Analysis & API

📍 A Python-based climate analysis project using SQLAlchemy, Pandas, Matplotlib, and Flask.


## 📖 Project Overview:

This project analyzes climate data from Honolulu, Hawaii, using a SQLite database and provides an interactive Flask API to serve the data.

###🔹 Part 1: Climate Data Analysis (Jupyter Notebook)

- Connects to a SQLite database (`hawaii.sqlite`) using SQLAlchemy.

- Performs exploratory analysis:

    - Precipitation trends over the last 12 months.

    - Weather station activity analysis (most active stations, temperature observations).

    - Temperature statistics for the most active station.

    - Histogram of temperature observations over the last year.

- Uses Matplotlib to visualize data.

###🔹 Part 2: Flask API Development (`app.py`)

- Develops a REST API to expose climate data with the following routes:
  
  - `/` → Lists available API endpoints.
  
  - `/api/v1.0/precipitation` → Returns precipitation data for the last 12 months.
  
  - `/api/v1.0/stations` → Lists all weather stations with observation counts.
  
  - `/api/v1.0/tobs` → Returns temperature observations for the most active station.
    
  - `/api/v1.0/<start>` → Returns min, avg, and max temperatures from a given start date.
    
  - `/api/v1.0/<start>/<end>` → Returns min, avg, and max temperatures for a date range.

---
## 📂 File Structure
```
├── Resources/
│   ├── hawaii.sqlite           # SQLite database with climate data
│   ├── hawaii_measurements.csv # Raw temperature & precipitation data
│   ├── hawaii_stations.csv     # Weather station details
│
├── climate.ipynb               # Jupyter Notebook for climate analysis
├── app.py                      # Flask API code
└── README.md                   # Project documentation (this file)
```

---

## 📊 Climate Analysis in Jupyter Notebook (`climate.ipynb`)

#### 🔹 Steps Taken

1.) Database Connection:

- Used SQLAlchemy to connect to hawaii.sqlite database.

- Reflected tables (measurement and station) into ORM models.

2.) Precipitation Analysis:

- Found the most recent date: 2017-08-23.

- Queried the last 12 months of precipitation and plotted the data.

3.) Station Analysis:

- Identified 9 unique weather stations.

- Found the most active station based on temperature observations.

- Calculated min, avg, and max temperature for the most active station.

- Visualized temperature observations using a histogram.
---
## 🌐 Flask API (`app.py`)

####🔹 How to Run the API:

1.) Ensure you have Python installed (Python 3.x recommended).

2.) Install dependencies if needed:
```sh

pip install flask sqlalchemy pandas matplotlib

```

3.) Run the Flask app:
```sh

python app.py

```

4.) Open a webbroser and navigate to:
```sh

https://127.0.0.1:500/

```

---
## 📌 API Endpoints & Examples

### 1️⃣ Homepage
📌 `http://127.0.0.1:5000/`
👉 Lists all available API routes.

### 2️⃣ Precipitation Data
📌 `http://127.0.0.1:5000/api/v1.0/precipitation`
👉 Returns JSON data with date as the key and precipitation as the value:
```json
{
    "2016-08-24": 0.08,
    "2016-08-25": 0.15,
    "2016-08-26": 0.00
}
```

### 3️⃣ Stations List
📌 `http://127.0.0.1:5000/api/v1.0/stations`
👉 Returns a list of all weather stations along with their observation count:
```json
[
    {"station": "USC00519281", "observation_count": 2772},
    {"station": "USC00519397", "observation_count": 2724}
]
```

### 4️⃣ Temperature Observations for Most Active Station
📌 `http://127.0.0.1:5000/api/v1.0/tobs`
👉 Returns temperature observations along with their respective dates:
```json
[
    {"date": "2016-08-24", "temperature": 77},
    {"date": "2016-08-25", "temperature": 78}
]
```

### 5️⃣ Temperature Statistics (Start Date)
📌 `http://127.0.0.1:5000/api/v1.0/2017-01-01`
👉 Returns min, avg, and max temperature starting from `2017-01-01`:
```json
{
    "start_date": "2017-01-01",
    "TMIN": 62,
    "TAVG": 68.92,
    "TMAX": 74
}
```

### 6️⃣ Temperature Statistics (Start & End Date)
📌 `http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-01-10`
👉 Returns min, avg, and max temperature for the range `2017-01-01` to `2017-01-10`:
```json
{
    "start_date": "2017-01-01",
    "end_date": "2017-01-10",
    "TMIN": 62,
    "TAVG": 68.92,
    "TMAX": 74
}
```
---
#### ⚡ Technologies Used:

💠 Python 🐍

💠 Flask 🌍 (API development)

💠 SQLAlchemy 🗄️ (Database connection)

💠 Pandas 📊 (Data manipulation)

💠 Matplotlib 📈 (Data visualization)

💠 SQLite 🗂️ (Database storage)

#### 📌 Summary:

✔️ Performed exploratory climate analysis in Jupyter Notebook.

✔️ Created a Flask API to provide easy access to climate data.

✔️ Implemented multiple endpoints for retrieving precipitation, stations, and temperature statistics.

✔️ Filtered out `NULL` values for precipitation & structured JSON responses effectively.

#### 📌 Future Improvements:

🔹 Add more complex visualizations to the API responses (e.g., plots).

🔹 Allow user-defined date ranges for precipitation analysis.

🔹 Expand the database to include more recent climate data.

---
#### 👨‍💻 Author

Dalton Schmidt

GitHub: [Sharkb8t]

Email: daltonaschmidt@gmail.com

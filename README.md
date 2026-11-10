SmogWatch — Air Quality Monitoring Across Pakistan
SmogWatch is a Flask-based web application that monitors and compares estimated PM2.5 air pollution levels across five major cities in Pakistan using the Open-Meteo Air Quality API.

The application fetches live API data, classifies pollution levels, ranks cities, and presents the results through a responsive web dashboard.
Features
- Fetches current PM2.5 data from a live API.
- Monitors Karachi, Lahore, Islamabad, Peshawar, and Quetta.
- Classifies air quality into different pollution categories.
- Ranks cities from lowest to highest PM2.5 concentration.
- Displays results through a responsive Flask dashboard.
- Includes a refresh button to fetch updated readings.
- Handles API request errors and invalid responses.
Technologies Used
- Python
- Flask
- Requests
- HTML5
- CSS3
- Jinja2
- Open-Meteo Air Quality API
- Git and GitHub
Project Structure
Smog-Watch/
│
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── routes.py
│   ├── utils.py
│   │
│   ├── templates/
│   │   └── smog_watch.html
│   │
│   └── static/
│       └── style.css
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
Installation and Setup
1. Clone the repository
git clone https://github.com/AyeshaGhayour/Smog_Watch.git
2. Navigate to the project directory
cd Smog_Watch
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment
For Windows PowerShell:
.\.venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
6. Run the application
python run.py
7. Open the dashboard
Visit the following address in your browser:
http://127.0.0.1:5000/
API Information
SmogWatch uses the Open-Meteo Air Quality API to retrieve current PM2.5 readings for the selected cities.
- API: https://air-quality-api.open-meteo.com/v1/air-quality
- Parameter: current=pm2_5
- Data unit: μg/m³
- Location: Five major cities in Pakistan.
Note: Open-Meteo provides model-based air quality estimates. These readings should not be interpreted as direct measurements from physical monitoring stations.
Air Quality Classification
The project uses simplified PM2.5 concentration thresholds to categorize pollution levels:
PM2.5 (μg/m³)	Category
0–5	Good
5–15	Moderate
15–35	Unhealthy for Sensitive Groups
35–55	Unhealthy
55–150	Very Unhealthy
Above 150	Hazardous


These thresholds are simplified for this educational project and are not a substitute for official air quality standards.
Sample Output
Example terminal output (illustrative values):
===== SMOGWATCH CITY RANKING =====

1. Quetta | PM2.5: 16.4 μg/m³ | Category: Unhealthy for Sensitive Groups
2. Karachi | PM2.5: 21.8 μg/m³ | Category: Unhealthy for Sensitive Groups
3. Peshawar | PM2.5: 60.3 μg/m³ | Category: Very Unhealthy
4. Islamabad | PM2.5: 89.4 μg/m³ | Category: Very Unhealthy
5. Lahore | PM2.5: 179.7 μg/m³ | Category: Hazardous
The values above are examples only. Actual readings change when the application fetches new API data.
Future Improvements
- Add historical air quality data.
- Introduce interactive charts and visualizations.
- Add more cities across Pakistan.
- Implement additional air quality indicators such as PM10 and nitrogen dioxide.
- Improve pollution category visualization.
Author

Ayesha Ghayour

Developed as a Python and Flask project to explore live API integration, data processing, and web application development.
License
This project is intended for educational and portfolio purposes.
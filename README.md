🧾 Invoicing ROI Simulator

A simple web app that helps businesses calculate cost savings, ROI, and payback period when switching from manual invoicing to automation.
It includes live ROI simulation, scenario saving, and PDF report generation — all in one lightweight Flask project.

🚀 Features

✅ Instant ROI Simulation — Calculates monthly savings, payback, and ROI instantly.
✅ Scenario Management (CRUD) — Save, load, and delete multiple simulations.
✅ Email-Gated Report Download — Generate and download a summary PDF after entering email.
✅ SQLite Database — Persistent local storage, no setup needed.
✅ Simple UI — Clean HTML/Bootstrap frontend with live feedback.

🧱 Tech Stack
Layer	Technology	Purpose
Frontend	HTML, CSS (Bootstrap), JavaScript	Simple UI
Backend	Flask (Python)	REST API & calculations
Database	SQLite	Store saved scenarios
PDF Generation	reportlab	Create downloadable reports
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/<your-username>/invoicing-roi-simulator.git
cd invoicing-roi-simulator

2. Create a Virtual Environment (optional)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
python app.py

5. Open in Browser
http://127.0.0.1:5000

📂 Project Structure
invoicing-roi-simulator/
│
├── app.py                 # Flask backend logic & API routes
├── database.db            # SQLite database file
├── templates/             # HTML frontend (index.html, etc.)
├── static/                # CSS & JS files
├── requirements.txt       # Python dependencies
├── README.md              # Setup guide
└── DOCUMENTATION.md       # Architecture & approach details

🧩 API Endpoints
Method	Endpoint	Description
POST	/simulate	Run ROI calculation
POST	/scenarios	Save a scenario
GET	/scenarios	List all saved scenarios
GET	/scenarios/<id>	Retrieve one scenario
DELETE	/scenarios/<id>	Delete scenario
POST	/report/generate	Generate PDF report (requires email)

All endpoints return JSON.

🧮 Example Calculation

Inputs:

monthly_invoice_volume: 2000
num_ap_staff: 3
avg_hours_per_invoice: 0.17
hourly_wage: 30
error_rate_manual: 0.5
error_cost: 100
time_horizon_months: 36
one_time_implementation_cost: 50000


Output Example:

{
  "monthly_savings": 8200,
  "payback_months": 6.1,
  "roi_percentage": 420.5,
  "net_savings": 160000
}

📄 Example Usage
Run Simulation
curl -X POST http://127.0.0.1:5000/simulate \
     -H "Content-Type: application/json" \
     -d '{
           "monthly_invoice_volume": 2000,
           "num_ap_staff": 3,
           "avg_hours_per_invoice": 0.17,
           "hourly_wage": 30,
           "error_rate_manual": 0.5,
           "error_cost": 100,
           "time_horizon_months": 36,
           "one_time_implementation_cost": 50000
         }'

Response
{
  "monthly_savings": 8200,
  "payback_months": 6.1,
  "roi_percentage": 420.5
}

📦 Requirements

Dependencies listed in requirements.txt:

Flask
Flask-Cors
reportlab


Install with:

pip install -r requirements.txt

📧 Report Generation

User must enter a valid email before generating PDF.

Backend verifies format (basic regex).

Report includes:

Input parameters

Calculated results

ROI chart or table

🧠 Future Enhancements

Add visual charts for ROI trends.

Cloud deployment (Render / Vercel).

Authentication for multiple users.

Enhanced report styling and analytics.

🧾 License

This project is open-source and free to use for educational and demonstration purposes.

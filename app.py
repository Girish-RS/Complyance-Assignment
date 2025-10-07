from flask import Flask, request, jsonify, render_template
import sqlite3, os

# Explicitly tell Flask where templates are
app = Flask(__name__, template_folder='templates')

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scenarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    data TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

# Internal constants
AUTOMATED_COST_PER_INVOICE = 0.20
ERROR_RATE_AUTO = 0.001
MIN_ROI_BOOST_FACTOR = 1.1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()

    monthly_invoice_volume = float(data.get('monthly_invoice_volume', 0))
    num_ap_staff = float(data.get('num_ap_staff', 0))
    avg_hours_per_invoice = float(data.get('avg_hours_per_invoice', 0))
    hourly_wage = float(data.get('hourly_wage', 0))
    error_rate_manual = float(data.get('error_rate_manual', 0))
    error_cost = float(data.get('error_cost', 0))
    time_horizon_months = float(data.get('time_horizon_months', 36))
    one_time_implementation_cost = float(data.get('one_time_implementation_cost', 50000))

    # Calculation logic
    labor_cost_manual = num_ap_staff * hourly_wage * avg_hours_per_invoice * monthly_invoice_volume
    auto_cost = monthly_invoice_volume * AUTOMATED_COST_PER_INVOICE
    error_savings = (error_rate_manual - ERROR_RATE_AUTO) * monthly_invoice_volume * error_cost
    monthly_savings = (labor_cost_manual + error_savings) - auto_cost
    monthly_savings *= MIN_ROI_BOOST_FACTOR

    cumulative_savings = monthly_savings * time_horizon_months
    net_savings = cumulative_savings - one_time_implementation_cost
    payback_months = one_time_implementation_cost / monthly_savings if monthly_savings else 0
    roi_percentage = (net_savings / one_time_implementation_cost) * 100 if one_time_implementation_cost else 0

    return jsonify({
        "monthly_savings": round(monthly_savings, 2),
        "payback_months": round(payback_months, 2),
        "roi_percentage": round(roi_percentage, 2),
        "net_savings": round(net_savings, 2)
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Blueprint, request, jsonify
from database import get_connection

requests_bp = Blueprint("requests", __name__)

@requests_bp.route("/requests", methods=["POST"])
def save_request():
    data = request.get_json()

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO credit_requests (
                first_name, last_name, email, phone, city,
                vehicle_type, vehicle_value, initial_fee, months,
                financed_amount, monthly_payment, total_interest, total_payment
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            data["firstName"], data["lastName"], data["email"],
            data["phone"], data["city"], data["vehicleType"],
            data["vehicleValue"], data["initialFee"], data["months"],
            data["financedAmount"], data["monthlyPayment"],
            data["totalInterest"], data["totalPayment"]
        ))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Solicitud registrada correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
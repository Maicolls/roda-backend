from flask import Blueprint, request, jsonify

simulate_bp = Blueprint("simulate", __name__)

def calculate_credit(vehicle_type, vehicle_value, initial_fee, months):
    financed_amount = vehicle_value - initial_fee
    interest_rate = 0.015 if vehicle_type == "bike" else 0.02

    monthly_payment = (
        financed_amount *
        (interest_rate * (1 + interest_rate) ** months)
    ) / ((1 + interest_rate) ** months - 1)

    total_payment = monthly_payment * months
    total_interest = total_payment - financed_amount

    schedule = []
    remaining = financed_amount

    for month in range(1, months + 1):
        interest = remaining * interest_rate
        capital = monthly_payment - interest
        remaining -= capital
        schedule.append({
            "month": month,
            "payment": round(monthly_payment, 2),
            "interest": round(interest, 2),
            "capital": round(capital, 2),
            "balance": round(max(remaining, 0), 2)
        })

    return {
        "financedAmount": round(financed_amount, 2),
        "monthlyPayment": round(monthly_payment, 2),
        "totalInterest": round(total_interest, 2),
        "totalPayment": round(total_payment, 2),
        "schedule": schedule
    }

@simulate_bp.route("/simulate", methods=["POST"])
def simulate():
    data = request.get_json()

    vehicle_type = data.get("vehicleType")
    vehicle_value = float(data.get("vehicleValue", 0))
    initial_fee = float(data.get("initialFee", 0))
    months = int(data.get("months", 0))

    if not vehicle_type:
        return jsonify({"error": "Tipo de vehículo requerido"}), 400
    if vehicle_value < 500000:
        return jsonify({"error": "El vehículo debe costar mínimo $500.000"}), 400
    if initial_fee > vehicle_value:
        return jsonify({"error": "La cuota inicial no puede ser mayor al vehículo"}), 400
    if months <= 0:
        return jsonify({"error": "El plazo debe ser mayor a 0"}), 400

    result = calculate_credit(vehicle_type, vehicle_value, initial_fee, months)
    return jsonify(result), 200
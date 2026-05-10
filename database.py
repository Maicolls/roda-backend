import psycopg2
from config import DATABASE_URL

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS credit_requests (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(150) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            city VARCHAR(100) NOT NULL,
            vehicle_type VARCHAR(50) NOT NULL,
            vehicle_value NUMERIC NOT NULL,
            initial_fee NUMERIC NOT NULL,
            months INTEGER NOT NULL,
            financed_amount NUMERIC NOT NULL,
            monthly_payment NUMERIC NOT NULL,
            total_interest NUMERIC NOT NULL,
            total_payment NUMERIC NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
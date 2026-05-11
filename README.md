# Roda Backend

API REST desarrollada en Flask para simular créditos de vehículos eléctricos y registrar solicitudes de financiación en PostgreSQL.

## Tecnologías utilizadas

* Python 3.12
* Flask 3.1
* Flask-CORS
* psycopg2-binary
* python-dotenv
* Gunicorn
* PostgreSQL

## Funcionalidades

* Simulación de créditos para:

  * Bicicletas eléctricas
  * Motos eléctricas
* Cálculo automático de:

  * Valor financiado
  * Cuota mensual
  * Total de intereses
  * Total pagado
  * Tabla de amortización
* Registro de solicitudes de crédito
* Persistencia de datos en PostgreSQL
* Validaciones de negocio desde backend

## Estructura del proyecto

```bash
roda-backend/
│
├── app.py
├── database.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .env
│
├── routes/
│   ├── simulate.py
│   └── requests.py
│
└── utils/
```

## Requisitos previos

* Python 3.12 o superior
* PostgreSQL 14 o superior
* pip

## Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Maicolls/roda-backend.git
cd roda-backend
```

### 2. Crear entorno virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/roda_db
PORT=5000
FLASK_ENV=development
```

### Variables

| Variable     | Descripción                |
| ------------ | -------------------------- |
| DATABASE_URL | URL de conexión PostgreSQL |
| PORT         | Puerto del servidor        |
| FLASK_ENV    | Ambiente de ejecución      |

## Configuración de PostgreSQL

Crear la base de datos:

```sql
CREATE DATABASE roda_db;
```

El backend crea automáticamente la tabla principal al iniciar mediante:

```python
create_tables()
```

## Ejecutar el proyecto

```bash
python app.py
```

Servidor local:

```bash
http://localhost:5000
```

## Endpoints

### Simular crédito

```http
POST /simulate
```

Body ejemplo:

```json
{
  "vehicleType": "bike",
  "vehicleValue": 8000000,
  "initialFee": 1000000,
  "months": 24
}
```

Respuesta ejemplo:

```json
{
  "monthlyPayment": 350000,
  "financedAmount": 7000000,
  "totalInterest": 1400000,
  "totalPayment": 8400000,
  "schedule": []
}
```

---

### Registrar solicitud

```http
POST /requests
```

Body ejemplo:

```json
{
  "firstName": "Juan",
  "lastName": "Perez",
  "email": "juan@example.com",
  "phone": "3001234567",
  "city": "Bogotá"
}
```

## Despliegue

El proyecto está preparado para desplegarse en Render usando:

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

## Decisiones técnicas

* Se utilizó Flask por simplicidad y rapidez de desarrollo.
* PostgreSQL fue elegido por estabilidad y compatibilidad con Render.
* La tabla se crea automáticamente para simplificar la prueba técnica.
* Se habilitó CORS para permitir comunicación con el frontend desplegado.
* Gunicorn se usa como servidor WSGI en producción.
* La lógica financiera se centraliza en backend para evitar inconsistencias.

## Flujo general

1. El frontend envía datos al endpoint `/simulate`
2. El backend valida y calcula el crédito
3. El frontend muestra resumen y amortización
4. El usuario registra la solicitud
5. El backend almacena la información en PostgreSQL

## Producción

Backend desplegado en Render.

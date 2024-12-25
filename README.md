## Wi-Fi Ticketing System

### Overview
The Wi-Fi Ticketing System is a web-based solution designed to manage and provide internet access via ticket-based authentication. It integrates with a payment gateway to streamline user access and track usage. Built using **FastAPI** for performance and scalability, this system supports user authentication, ticket generation, and validation.

### Features
- **User Registration and Authentication**  
  Secure user sign-up and login functionality using encrypted password storage.
- **Ticket Generation**  
  Users can purchase access tickets, granting them internet access for a specified duration.
- **Payment Gateway Integration**  
  Seamless integration with payment gateways to handle ticket purchases.
- **Ticket Validation**  
  Authentication and validation of tickets through a secure API.
- **Database Integration**  
  Uses SQLAlchemy for database management, allowing persistence of user and ticket information.

### Prerequisites
Before running the Wi-Fi Ticketing System, ensure you have the following installed:
- **Python 3.11+**  
- **FastAPI**  
- **SQLAlchemy**  
- **Uvicorn** (for development server)
- **Passlib** (for password hashing)
- **Database**: SQLite (or any database of your choice, like PostgreSQL or MySQL)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/WIFI_TICKETING_SYSTEM.git
   cd WIFI_TICKETING_SYSTEM
   ```

2. Set up and activate your virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Migrate database (if needed):
   ```bash
   alembic upgrade head
   ```

### Configuration
1. Update the database URL in `database.py`:
   ```python
   DATABASE_URL = "sqlite:///./test.db"  # Replace with your database URL
   ```

2. Set up your payment gateway API credentials in a configuration file or environment variables.

### Running the Application
To run the development server, use:
```bash
uvicorn main:app --reload
```

Your application will be accessible at `http://127.0.0.1:8000`.

### API Endpoints
- **User Signup**: `POST /auth/signup`  
  Endpoint for user registration with validation.
  
- **Ticket Purchase**: `POST /tickets/buy`  
  Endpoint to purchase internet access tickets via the payment gateway.

- **Ticket Validation**: `GET /tickets/validate/{ticket_id}`  
  Endpoint to validate and check ticket status.

### Contributing
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

### License
This project is licensed under the MIT License.

 

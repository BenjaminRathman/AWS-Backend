# AWS Backend - FastAPI Bar Management System

A robust RESTful API backend built with FastAPI for managing bars, locations, and user data. This project demonstrates modern Python backend development practices with PostgreSQL database integration, Docker containerization, and comprehensive testing.

## 🚀 Features

- **User Management**: Complete CRUD operations for user accounts with email validation
- **Location Management**: Handle multiple bar locations with full CRUD support
- **Bar Management**: Comprehensive bar information system with weekly specials
- **Authentication**: JWT token-based authentication system (placeholder implementation)
- **Database**: PostgreSQL with SQLAlchemy ORM and proper foreign key relationships
- **Testing**: Comprehensive test suite with pytest
- **Containerization**: Docker and Docker Compose setup for easy deployment
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.104.1
- **Database**: PostgreSQL with SQLAlchemy 2.0.23
- **Authentication**: JWT tokens with placeholder verification
- **Testing**: pytest with async support
- **Containerization**: Docker & Docker Compose
- **Code Quality**: Black, Flake8, MyPy for code formatting and linting
- **AWS Integration**: Boto3 for AWS services (ready for deployment)

## 📁 Project Structure

```
AWS-Backend/
├── API/
│   ├── Endpoint.py              # Authentication endpoints
│   ├── PydanticModels/          # Request/Response models
│   │   ├── BarsModels.py
│   │   ├── LocationModels.py
│   │   └── UserModels.py
│   └── Routers/                 # API route handlers
│       ├── Bars.py
│       ├── Health.py
│       ├── Locations.py
│       └── Users.py
├── DATABASE/
│   ├── dbConnection.py          # Database connection setup
│   ├── Queries.py              # Custom database queries
│   └── SqlaModels/             # SQLAlchemy ORM models
│       ├── BarsDb.py
│       ├── LocationsDb.py
│       └── UsersDb.py
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container configuration
├── docker-compose.yml         # Multi-container setup
└── test_tests.py              # Comprehensive test suite
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 12+
- Docker & Docker Compose (optional)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd AWS-Backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/database_name
   ```

5. **Set up PostgreSQL database**
   ```bash
   # Create database
   createdb your_database_name
   
   # Run migrations (when available)
   # alembic upgrade head
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

7. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc
   - Health Check: http://localhost:8000/health/

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs

## 📚 API Endpoints

### Authentication
- `GET /health/protected` - Protected route (requires Bearer token)

### Users
- `POST /users/createUser` - Create new user
- `GET /users/getUser/{UserId}` - Get user by ID
- `PUT /users/updateUserLastLogin/{UserId}` - Update last login time
- `DELETE /users/deleteUser/{UserId}` - Delete user

### Locations
- `POST /locations/createLocation` - Create new location
- `GET /locations/getLocation/{LocationId}` - Get location by ID
- `GET /locations/allLocations` - Get all locations
- `PUT /locations/updateLocation/{LocationId}` - Update location
- `DELETE /locations/deleteLocation/{LocationId}` - Delete location

### Bars
- `POST /bars/createBar` - Create new bar
- `GET /bars/getBar/{BarId}` - Get bar by ID
- `GET /bars/allBars` - Get all bars
- `DELETE /bars/deleteBar/{BarId}` - Delete bar

### Bar Information
- `POST /bars/createBarInfo` - Create bar information
- `GET /bars/getBarInfo/{BarId}` - Get bar information
- `GET /bars/allBarInfo` - Get all bar information
- `PUT /bars/updateBarInfo/{BarId}` - Update bar information
- `DELETE /bars/deleteBarInfo/{BarId}` - Delete bar information

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest test_tests.py -v

# Run with coverage
pytest test_tests.py --cov=. --cov-report=html

# Run specific test categories
pytest test_tests.py::test_create_user_success -v
```

## 🗄️ Database Schema

### Users Table
- `UserId` (UUID, Primary Key)
- `Email` (String, Unique)
- `FirstName` (String)
- `LastName` (String)
- `DateOfBirth` (Date)
- `TimeOfLastLogin` (Timestamp)

### Locations Table
- `LocationId` (Integer, Primary Key, Auto-increment)
- `LocationName` (String)

### AllBars Table
- `BarId` (UUID, Primary Key)
- `LocationId` (Integer, Foreign Key → Locations.LocationId)
- `BarName` (String)

### AllBarsInfo Table
- `BarId` (UUID, Primary Key, Foreign Key → AllBars.BarId)
- `LocationId` (Integer, Foreign Key → Locations.LocationId)
- `BarName` (String)
- `Description` (String, Optional)
- `WeeklySpecials` (JSONB, Optional)

## 🔧 Development

### Code Quality
```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

### Database Migrations
```bash
# Generate migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head
```

## 🚀 Deployment

### AWS Deployment (Ready)
The project is configured with AWS dependencies and can be deployed to:
- AWS ECS with Fargate
- AWS Lambda with API Gateway
- AWS EC2 with Application Load Balancer

### Environment Variables for Production
```env
DATABASE_URL=postgresql://user:pass@host:5432/db
SECRET_KEY=your-secret-key
DEBUG=False
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- SQLAlchemy for robust ORM capabilities
- PostgreSQL community for the reliable database
- Docker team for containerization tools

---

**Note**: This project demonstrates modern Python backend development practices and is ready for production deployment with proper environment configuration.

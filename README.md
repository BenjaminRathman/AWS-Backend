# AWS Backend - FastAPI Bar Management System

A robust RESTful API backend built with FastAPI for a vendor IOS APP. This project demonstrates modern Python backend development practices with PostgreSQL database integration, Docker containerization, and comprehensive testing.

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


### Prerequisites

- Python 3.11+
- PostgreSQL 12+
- Docker & Docker Compose (optional)


   ```




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






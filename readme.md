# Simple Distributed System

This is an simple web-based system implemented using Docker containers. The system consists of customer-facing web servers, admin web servers, a load balancer (HAProxy), web frameworks, admin web frameworks, and a MySQL database.

## Getting Started

These instructions will help you set up and run this simple distributed system on your local machine.

### Prerequisites

To run this project, you need to have the following installed on your system:

- Docker
- Docker Compose

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Mueem-Nahid/simple-distributed-system.git
cd simple-distributed-system
```

2. Build and start the containers:

```bash
docker-compose up --build
```

3. Database Initialization

   The system uses a MySQL database to store product information. The database is initialized with sample data from the initialize.sql file in the database directory.

4. Once the containers are up and running, you can access the following services:

   - Customer-Facing Web Servers: http://localhost:8083 and http://localhost:8084
   - Admin Web Servers: http://localhost:8081 and http://localhost:8082
   - Web Framework: http://localhost:5003 (This service queries the database and provides JSON data)
   - Admin Web Framework: http://localhost:5002 (Similar to the Web Framework but with write access to the database)
   - Load Balancer: http://localhost/ (Round-robin load balancing between customer-facing web servers)
   - Database (MySQL): Not directly accessible from the host machine

5. Some usefull docker cmd:
   1. To kill all running docker container

```bash
docker stop $(docker ps -q)
```

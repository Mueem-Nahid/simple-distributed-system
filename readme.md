# Simple Distributed System

This is an simple web-based system implemented using Docker containers. The system consists of customer-facing web
servers, admin web servers, a load balancer (HAProxy), web frameworks, admin web frameworks, and a MySQL database.

#### The system layout can be seen in the diagram below:

![Simple Distributed System Layout](https://i.ibb.co/X5W54Mp/Screenshot-2024-02-18-000008.png)

### The system components:

Each of the components shown in above diagram should be instances of docker containers.
The whole system should be able to be started from a docker-compose.yml file with a
docker- compose up command. Most of the individual containers should be built using the
Dockerfile and docker-compose.yml file where applicable. The ports that each container
will be required to use are provided in the diagram above.

### Load balancer:

The load balancer should be a HAProxy based image that performs round robin load
balancing between running instances of the web servers. This is to avoid overloading any
single instance of a web-server. Load balancer would serve any requests made to
http://localhost address and load balance (using round robin method) between the 2-front
facing web-servers. Any requests made to http://localhost/admin should be load balanced
(using round robin method) between the 2-back facing admin web-servers instead.

### Web servers:

There should be 2 instances of the customer facing web server that run identical code but
on different ports. Their purpose is to present items for sale in an easy to read and
professional manner (Item name, item quantity and item price). The servers should be
based on the php:apache image. The web-servers should also display their unique
hostname at the top left corner.

### Admin web server:

There should be 2 instances of the admin web server that run identical code but on different
ports. These are based on the same container as the normal web servers but in addition to
displacing current items being sold, they should also have an ability to insert new items into
the database. They should present a form that allows users to enter all the details required
to add the new items. If the items are new, it should insert it for sale and if it is not a new
item it should update its quantity on the system. The web-servers should also display their
unique hostname at the top left corner.

### Web-framework:

The web-framework is based on a python 3 image running the Flask web-framework. This
framework is meant to query the database (read only) and provide the data as a JSON to the
web-servers. Data received from the database should be validated. The web-framework
should not be able to be accessed externally and should only be accessed by containers in
the system.

### Admin web-framework:

The admin web-framework is based on normal web-framework with the additional
functionality of being able to write into the database to allow for insertion of new items to
be sold on the store front and allow to update quantity of the currently sold items. Data
received from the user should be correctly validated before written into the database.

### Database:

The database should be based on the mysql image and store the following data:

- Item name
- Items quantity
- Item price

The database should not be able to be accessed externally and should only be accessed by
containers in the system.

### Database caching:

Database caching service. Any requests that have been already made to the database should be cached and presented for
any new access.
Database should only be accessed directly if the query made is not in the database cache.

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

   The system uses a MySQL database to store product information. The database is initialized with sample data from the
   initialize.sql file in the database directory.

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

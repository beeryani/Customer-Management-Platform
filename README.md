# Customer Management Application

## Getting Started

### Prerequisites

1. Python 3.x
2. PostgreSQL
3. pip (Python package installer)

## Installation

1. Clone the repository to your local machine using `git clone https://github.com/pratyzsh/Customer-Management-Platform.git`
2. Create a virtual environment for the project using `python -m venv env`
3. Activate the virtual environment using `source env/bin/activate`(on Linux or Mac) or `env\Scripts\activate` (on Windows)
4. Install the required Python packages using `pip install -r requirements.txt`
5. Create a new PostgreSQL database for the project
6. Create a `.env` file and update the database credentials required in `settings/base.py`

## Usage

1. Once you have completed the installation steps, run the server using the command `python manage.py runserver`
2. Navigate to `http://localhost:8000` in your web browser to access the Customer Management Platform
3. You can create a new customer by clicking the "Add New Customer" button on the homepage and filling out the form.
4. You can view the list of customers and their details by clicking the "View Customers" button on the homepage.
5. You can search for customers by their name, email or phone number using the search bar on the homepage.
6. You can edit or delete a customer by clicking on the corresponding buttons on the customer details page.

## Functional Requirements:

1. User Registration: The platform should allow users to register and create an account.
2. User Authentication: The platform should authenticate users when they log in to ensure they are authorized to access the system.
3. Customer Creation: The platform should allow users to create new customers with their details like name, contact details, and other relevant information.
4. Customer Management: Users should be able to view, update, and delete existing customers.
5. Search: Users should be able to search for specific customers based on their name, contact details, or other criteria.
6. Reporting: Users should be able to generate reports on customer data, such as the number of customers, sales, and revenue generated.

## Non-Functional Requirements:

1. Security: The platform should be secure, protecting user data and customer data from unauthorized access.
2. Scalability: The platform should be scalable and able to handle a large number of users and customer data.
3. Performance: The platform should be fast and responsive, ensuring a smooth user experience even when dealing with large amounts of data.
4. Usability: The platform should be easy to use, with an intuitive interface and clear navigation.

## User Stories:

1. As a user, I want to be able to create an account on the platform so that I can access the customer management functionality.
2. As a user, I want to be able to log in to the platform securely so that I can access my customer data.
3. As a user, I want to be able to add new customers to the system with their name, contact details, and other relevant information so that I can keep track of my customer base.
4. As a user, I want to be able to view, update, and delete existing customers so that I can keep my customer data up-to-date.
5. As a user, I want to be able to search for specific customers based on their name, contact details, or other criteria so that I can find the information I need quickly and easily.
6. As a user, I want to be able to generate reports on customer data so that I can analyze my customer base and identify opportunities for growth.

## Architecture:

The Customer Management Platform in the mentioned repository is a web application built using a two-tier architecture, consisting of the following layers:

1. Presentation Layer: This layer is responsible for providing a user-friendly interface to the users. It will consist of a web-based user interface that allows users to interact with the platform.

2. Data Layer: This layer will manage the persistence of customer data. It will consist of a database that stores customer data in a structured way.

### Technologies:

The Customer Management Platform in the mentioned repository is built using the following technologies:

1. Python programming language
2. Django web framework
3. HTML, CSS, and JavaScript for front-end development
4. Bootstrap CSS framework for styling
5. PostgreSQL database for data storage
6. Django's built-in authentication system for user management
7. Docker for virtualisation and container management

### Security:

To ensure the security of the platform, the following measures should be taken:

1. User Authentication: Users should be required to provide a valid username and password to access the platform.

2. Encryption: User data and customer data should be encrypted to prevent unauthorized access.

3. Access Control: Different levels of access should be granted to different types of users based on their roles and permissions.

## #TO DO

1. ~~Add authentication as next step~~
2. Add production docker compose file with neccessary attachments for production environment
3. Add Signals for email notification

# DataFabricator: SQL Schema and Data Generator

## Overview

DataFabricator is a Python-based project that automates the process of generating SQL schemas and synthetic data for testing and development purposes. The project is designed to create random but realistic SQL schema definitions and insert statements, allowing users to quickly set up and populate a database for testing and experimentation.

The project includes functionality for generating SQL schema definitions, generating data that conforms to the schema, and executing the generated SQL statements to create tables and insert data into an SQLite database. It uses the openai completions api.

## Features
- **Schema Generation**: The project includes a schema generation module that creates random SQL schema definitions. The generated schema may include multiple tables with various data types, primary keys, foreign keys, and constraints.
- **Data Generation**: The data generation module generates random, synthetic data that conforms to the schema definition. The generated data includes insert statements that can be executed to populate the tables defined in the schema.
- **Database Connection and Execution**: The project includes a database connection module that allows users to connect to an SQLite database, execute SQL statements, and retrieve query results. The module supports executing multiple SQL statements, including creating tables and inserting data.
- **In-Memory Database Support**: The project supports working with in-memory SQLite databases, allowing users to quickly set up and experiment with databases without the need for file-based storage.

## Usage
The project includes a main script that demonstrates the usage of the schema and data generation modules, as well as the database connection and execution module. The code here can be extened to other use-cases.

To run the main script, use the following commands:
git clone rorarij/DataFabricator
pip install requirements.txt
python3 main.py
The script will output the generated schema and data, as well as the results of executing the SQL statements.

## Use Cases
- **Testing Database Applications**: The project can be used to generate test data for database applications, allowing developers to test their applications with a variety of data scenarios.
- **Learning SQL**: The project can be used as a learning tool for individuals who are new to SQL and want to practice writing and executing SQL queries.
- **Benchmarking Database Performance**: The project can be used to generate large volumes of data for benchmarking the performance of database systems.

## Disclaimer
The generated SQL schema and data are intended for testing and development purposes only. The project is not intended for use with production databases or sensitive data. Users are responsible for ensuring the security and integrity of their databases when using the generated SQL statements.

## License
This project is open-source and available under the MIT License.

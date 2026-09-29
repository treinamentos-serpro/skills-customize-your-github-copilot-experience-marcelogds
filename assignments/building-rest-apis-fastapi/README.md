# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn the basics of building a REST API with FastAPI by creating endpoints, returning JSON data, and handling request parameters and validation in a small web application.

## 📝 Tasks

### 🛠️ Create a FastAPI application

#### Description
Set up a minimal FastAPI app and define a root endpoint that confirms the service is running.

#### Requisitos
The program completed must:

- import FastAPI and create an app instance
- define a route such as `/` or `/health`
- return a JSON response with a status message
- run the app with a local development server

### 🛠️ Build a simple resource API

#### Description
Create an API for managing a list of items such as books, tasks, or products.

#### Requisitos
The program completed must:

- define a collection of sample data in memory
- create a route to list all items
- create a route to retrieve one item by id
- return JSON objects in a clean structure

### 🛠️ Add create and update operations

#### Description
Extend the API with endpoints to add new items and update existing ones.

#### Requisitos
The program completed must:

- add a POST route to create a new item
- accept JSON payloads with fields such as id and name
- add a PUT or PATCH route to update an existing item
- validate missing or invalid input before saving changes

### 🛠️ Test the API

#### Description
Run the application locally and verify the endpoints using requests or browser testing.

#### Requisitos
The program completed must:

- start the FastAPI server with uvicorn
- test at least three endpoints with valid requests
- confirm that responses include correct status codes and JSON payloads
- document one example request and response for the API

# 📘 Assignment: To-Do App with SQLite

## 🎯 Objective

Build a small to-do application that stores tasks in a database and supports adding, listing, updating, and deleting items while practicing file persistence and working with structured data in Python.

## 📝 Tasks

### 🛠️ Create the database and task table

#### Descrição
Set up a SQLite database and create a table to store tasks with a unique identifier, title, and completion status.

#### Requisitos
O programa concluído deve:

- import the `sqlite3` module
- connect to a SQLite database file
- create a table named `tasks`
- store at least the columns `id`, `title`, and `completed`

### 🛠️ Add tasks to the list

#### Descrição
Implement a function that allows the user to add a new task and save it in the database.

#### Requisitos
O programa concluído deve:

- ask the user for a task title
- insert the new task into the database
- confirm that the task was saved successfully
- display the updated task list

### 🛠️ List and update tasks

#### Descrição
Allow the user to view all saved tasks and mark a task as completed.

#### Requisitos
O programa concluído deve:

- fetch all tasks from the database
- print each task with a readable format
- update the status of a selected task
- persist the change in the database

### 🛠️ Delete tasks and finish the app

#### Descrição
Add the ability to remove tasks and make the program user-friendly for repeated use.

#### Requisitos
O programa concluído deve:

- provide an option to delete a task by id
- remove the task from the database permanently
- handle invalid ids gracefully
- present a simple menu for add, list, update, and delete actions

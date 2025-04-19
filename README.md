# Railway Registration System

This project is a simple railway registration system built using Flask. It allows users to register for railway tickets, store their registration data in a database, and view or cancel their tickets through a web interface.

## Features

- **User Registration:** Users can register for railway tickets through a web form.
- **Confirmation:** After filling out the registration form, a confirmation message is displayed, asking users to cross-check their information and either take a screenshot or print it out for their records.
- **Data Storage:** Registered user data is stored in a database.
- **View Registrations:** Users can view all stored entries through `view.html`.
- **Ticket Cancellation:** Users can cancel their tickets using the `delete.html` file.

## How to Use

### 1. Start the Confirmation Process

First, you need to start the confirmation process by running the `connecttrain.py` file. This script will collect all necessary information for registration.

```bash
python connecttrain.py
```

After you fill out all the required information, you will receive a confirmation message. Please cross-check the details carefully. You are advised to take a screenshot or print out this confirmation message for your records.

### 2. Register for the Railway Ticket

Once you have confirmed your details, run the `connect.py` file to load the registration form.

```bash
python connect.py
```

Fill out the registration form with the required information. Upon successful registration, your data will be stored in the database.

### 3. View Stored Entries

You can view all stored entries by accessing `view.html`. This page will display all the registrations that have been stored in the database.

### 4. Cancel a Ticket

If you need to cancel a ticket, you can do so using the `delete.html` file. This form allows you to delete your registration from the database.

## File Descriptions

- **`connecttrain.py`**: Handles the initial confirmation process, collecting user information.
- **`connect.py`**: Runs the registration form and stores data in the database.
- **`view.html`**: Displays all stored registrations in the database.
- **`delete.html`**: Allows users to cancel their tickets by deleting their registration from the database.

# SQLite Database Connection and Basic CRUD Operations

## Objective

Implement and understand SQLite database connection and basic SQL CRUD operations using Python.

CRUD stands for:

- **C - Create:** Insert new records into the database.
- **R - Read:** Retrieve records from the database.
- **U - Update:** Modify existing records.
- **D - Delete:** Remove records from the database.

---

## Requirements

- Python 3.x
- SQLite3

> `sqlite3` is included with Python, so no separate installation is required.

---

## Project Structure

```text
SQLite-CRUD/
│
├── sqlite_crud.py
├── college.db
└── README.md
```

---

## Step 1: Import SQLite

```python
import sqlite3
```

The `sqlite3` module is used to connect Python with an SQLite database.

---

## Step 2: Create Database Connection

```python
conn = sqlite3.connect("college.db")
cursor = conn.cursor()
```

- `college.db` is the SQLite database file.
- If the file does not exist, SQLite creates it automatically.
- `cursor` is used to execute SQL commands.

---

## Step 3: Create Table

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
course TEXT
)
""")
```

The `students` table contains:

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary key, automatically increases |
| name | TEXT | Student name |
| age | INTEGER | Student age |
| course | TEXT | Student course |

---

## Step 4: CREATE - Insert Data

```python
cursor.execute("""
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
""", ("Kevin", 18, "Computer Engineering"))

conn.commit()
```

This inserts a new student:

- Name: Kevin
- Age: 18
- Course: Computer Engineering

`commit()` permanently saves the changes to the database.

### Output

```text
Data Inserted Successfully
```

---

## Step 5: READ - Display Data

```python
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\nStudent Records:")

for student in students:
    print(student)
```

`SELECT *` retrieves all records from the `students` table.

`fetchall()` returns all retrieved records.

### Example Output

```text
Student Records:
(1, 'Kevin', 18, 'Computer Engineering')
```

---

## Step 6: UPDATE - Modify Data

```python
cursor.execute("""
UPDATE students
SET course = ?
WHERE id = ?
""", ("Information Technology", 1))

conn.commit()
```

This changes the course of student ID `1` from:

```text
Computer Engineering
```

to:

```text
Information Technology
```

### Output

```text
Data Updated Successfully
```

---

## Step 7: DELETE - Remove Data

```python
cursor.execute("""
DELETE FROM students
WHERE id = ?
""", (1,))

conn.commit()
```

This deletes the student whose ID is `1`.

### Output

```text
Data Deleted Successfully
```

---

## Step 8: Close Database Connection

```python
conn.close()

print("\nDatabase Connection Closed")
```

Closing the connection releases database resources.

### Output

```text
Database Connection Closed
```

---

## Complete Python Program

```python
import sqlite3

# Database connection
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
course TEXT
)
""")

# CREATE
cursor.execute("""
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
""", ("Kevin", 18, "Computer Engineering"))

conn.commit()

print("Data Inserted Successfully")

# READ
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\nStudent Records:")

for student in students:
    print(student)

# UPDATE
cursor.execute("""
UPDATE students
SET course = ?
WHERE id = ?
""", ("Information Technology", 1))

conn.commit()

print("\nData Updated Successfully")

# DELETE
cursor.execute("""
DELETE FROM students
WHERE id = ?
""", (1,))

conn.commit()

print("Data Deleted Successfully")

# Close connection
conn.close()

print("\nDatabase Connection Closed")
```

---

## Expected Output

```text
Data Inserted Successfully

Student Records:
(1, 'Kevin', 18, 'Computer Engineering')

Data Updated Successfully
Data Deleted Successfully

Database Connection Closed
```

> Note: If you run the program multiple times, new student records will be inserted each time. The `UPDATE` and `DELETE` statements specifically target `id = 1`.

---

## How to Run

### 1. Open the project folder in VS Code

### 2. Create a Python file

Create:

```text
sqlite_crud.py
```

### 3. Paste the Python code

Save the file.

### 4. Open VS Code Terminal

Go to:

```text
Terminal → New Terminal
```

### 5. Run the program

```bash
python sqlite_crud.py
```

If `python` does not work on Windows, try:

```bash
py sqlite_crud.py
```

---

## Database File

After running the program, SQLite creates:

```text
college.db
```

This file stores the `students` table and its data.

---

## CRUD Summary

| Operation | SQL Command | Purpose |
|---|---|---|
| Create | `INSERT` | Add new data |
| Read | `SELECT` | View data |
| Update | `UPDATE` | Modify data |
| Delete | `DELETE` | Remove data |

---

## Conclusion

This project demonstrates how to:

1. Connect Python to an SQLite database.
2. Create a database table.
3. Insert student records.
4. Read student records.
5. Update student records.
6. Delete student records.
7. Close the database connection.

This is a basic example of using **SQLite with Python for CRUD operations**.

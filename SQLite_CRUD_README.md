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

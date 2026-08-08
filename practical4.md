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
""", ("Kevin", 21, "Computer Science & Engineering"))

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
(1, 'Kevin', 21, 'Computer Science & Engineering')

Data Updated Successfully
Data Deleted Successfully

Database Connection Closed
```


## Conclusion

This project demonstrates how to:

1. Connect Python to an SQLite database.
2. Create a database table.
3. Insert student records.
4. Read student records.
5. Update student records.
6. Delete student records.
7. Close the database connection.

<img width="1600" height="863" alt="image" src="https://github.com/user-attachments/assets/b3b04531-baee-4638-a94d-f7f509f04bd4" />



<img width="1600" height="863" alt="image" src="https://github.com/user-attachments/assets/c178adcb-d71c-40d1-8dc2-56789b2c33a5" />



<img width="1600" height="863" alt="image" src="https://github.com/user-attachments/assets/62f533c4-ff7d-4031-b26b-5f33f5411d7c" />






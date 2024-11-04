import sqlite3

# Connects to SQLite3 and creates the database if it does not already exist
conn = sqlite3.connect("intervals.db")

# Creates a cursor object
cursor = conn.cursor()

# Creates the table if it does not already exist
cursor.execute("""CREATE TABLE IF NOT EXISTS intervals (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               numerical_symbol TEXT,
               degree TEXT,
               interval_distance INTEGER,
               interval_name TEXT,
               sound_characteristic TEXT)
               """)

intervals_data = [

    ("I", "tonic", 0, "unison", "open_consonance"),
    ("ii", "supertonic", 1, "minor_second", "sharp_dissonance"),
    ("II", "supertonic", 2, "major_second", "mild_dissonance"),
    ("iii", "mediant", 3, "minor_third", "soft_consonance"),
    ("III", "mediant", 4, "major_third", "soft_consonance"),
    ("IV", "subdominant", 5, "perfect_fourth", "consonance_or_dissonance"),
    ("IV+", "tritone", 6, "augmented_fourth", "neutral_or_restless"),
    ("V°", "tritone", 6, "diminished_fifth", "neutral_or_restless"),
    ("V", "dominant", 7, "perfect_fifth", "open_consonance"),
    ("V+", "submediant", 8, "augmented_fifth", "soft_consonance"),
    ("vi", "submediant", 8, "minor_sixth", "soft_consonance"),
    ("VI", "submediant", 9, "major_sixth", "soft_consonance"),
    ("vii°", "submediant", 9, "diminished_seventh", "soft_consonance"),
    ("vii", "subtonic", 10, "minor_seventh", "mild_dissonance"),
    ("VII", "leading_note", 11, "major_seventh", "sharp_dissonance")

]

# Inserts the data into the table
cursor.executemany("""
                   INSERT INTO intervals (numerical_symbol, degree, interval_distance, interval_name, sound_characteristic)
                   VALUES (?, ?, ?, ?, ?)
                   """, intervals_data)

# Commits the changes
conn.commit()

# Verifies the insertion by selecting all data from the table
cursor.execute("SELECT * FROM intervals")
rows = cursor.fetchall()

# Prints the data to confirm the insertion
for row in rows:
    
    print(row)

# Closes the connection
conn.close()

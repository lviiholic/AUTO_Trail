import csv
import sqlite3
import pandas as pd
import numpy as np

# Create a database connection
conn = sqlite3.connect('data/hiking.db')
cursor = conn.cursor()

# Create the Park table
cursor.execute('''CREATE TABLE IF NOT EXISTS Park (
    park_id TEXT PRIMARY KEY NOT NULL,
    park_name TEXT NOT NULL,
    area INTEGER NOT NULL
)''')

# Create the Trail table
cursor.execute('''CREATE TABLE IF NOT EXISTS Trail (
    trail_id TEXT PRIMARY KEY NOT NULL,
    park_id TEXT NOT NULL,
    trail_name TEXT NOT NULL,
    region TEXT NOT NULL,
    difficulty INTEGER NOT NULL,
    star INTEGER NOT NULL,
    surface INTEGER NOT NULL,
    gradient INTEGER NOT NULL,
    length REAL NOT NULL,
    time REAL NOT NULL,
    summary TEXT NOT NULL,
    FOREIGN KEY (park_id) REFERENCES Park(park_id)
)''')

# Create the Rescue table
cursor.execute('''CREATE TABLE IF NOT EXISTS Rescue (
    rescue_id TEXT PRIMARY KEY NOT NULL,
    park_id TEXT NOT NULL,
    year INTEGER NOT NULL,
    rescue_count INTEGER NOT NULL,
    injury_count INTEGER NOT NULL,
    death_count INTEGER NOT NULL,
    FOREIGN KEY (park_id) REFERENCES Park(park_id)
)''')

# Create the Template table
cursor.execute('''CREATE TABLE IF NOT EXISTS Template (
    template_id TEXT PRIMARY KEY NOT NULL,
    template TEXT NOT NULL,
    sql_text TEXT NOT NULL
)''')

# Commit the changes and close the connection
conn.commit()
conn.close()

# Insert data into table 

conn = sqlite3.connect('data/hiking.db')
cursor = conn.cursor()

with open('csv/park.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

    # Prepare the data for insertion
    data = [(row[0], row[1], int(row[2])) for row in csv_reader]

    # Insert the rows into the table
    cursor.executemany('''INSERT INTO Park (park_id, park_name, area)
                          VALUES (?, ?, ?)''', data)

with open('csv/rescue.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

    # Prepare the data for insertion
    data = []
    for row in csv_reader:
        rescue_id = row[0]
        park_id = row[1]
        year = int(row[2])
        rescue_count = int(row[3])
        injury_count = int(row[4])
        death_count = int(row[5])

        data.append((rescue_id, park_id, year, rescue_count, injury_count, death_count))

    # Insert the rows into the table
    cursor.executemany('''INSERT INTO Rescue (rescue_id, park_id, year, rescue_count, injury_count, death_count)
                          VALUES (?, ?, ?, ?, ?, ?)''', data)

with open('csv/trail.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

    # Prepare the data for insertion
    data = []
    for row in csv_reader:
        trail_id = row[0]
        park_id = row[1]
        trail_name = row[2]
        region = row[3]
        difficulty = int(row[4])
        star = int(row[5])
        surface = int(row[6])
        gradient = int(row[7])
        length = float(row[8])
        time = float(row[9])
        summary = row[10]

        data.append((trail_id, park_id, trail_name, region, difficulty, star, surface, gradient, length, time, summary))

    # Insert the rows into the table
    cursor.executemany('''INSERT INTO Trail (trail_id, park_id, trail_name, region, difficulty, star, surface, gradient, length, time, summary)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)

with open('csv/template.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

    # Prepare the data for insertion
    data = [(row[0], row[1], row[2]) for row in csv_reader]

    # Insert the rows into the table
    cursor.executemany('''INSERT INTO Template (template_id, template, sql_text)
                          VALUES (?, ?, ?)''', data)

conn.commit()
conn.close()



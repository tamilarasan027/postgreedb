-- schema.sql

-- Create the students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    mark INTEGER
);

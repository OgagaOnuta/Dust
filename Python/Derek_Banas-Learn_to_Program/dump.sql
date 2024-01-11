BEGIN TRANSACTION;
CREATE TABLE Employees(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        FName TEXT NOT NULL,
        LName TEXT NOT NULL,
        Age INTEGER NOT NULL,
        Address TEXT,
        Salary REAL,
        HireDate TEXT, 'Image' BLOB DEFAULT NULL);
INSERT INTO "Employees" VALUES(1,'David','Onuta',26,'121 Main St',500000.0,'2023-11-10',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('Employees',1);
COMMIT;

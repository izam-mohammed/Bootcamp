# Postgres

## Basic Theories

### What is database
It's a structured collection of data that is organized , stored and managed to do CRUD operations

### What is DBMS
It stands for Data Base Management System. It's the software that allows CRUD operations.
Eg :- mySQL , postgreSQL

### Difference between DBMS and RDBMS
In DBMS, the data is stored as a file, whereas in RDBMS , the data stored in the form of tables

### Benefits of postgres
- Open source and community driven
- SQL database
- Have advanced features
- Extensibility - allowes you to create your own things
- It follows ACID complaints
- Scalabiliy and data integrity

### Transactions
A group of tasks like insert, update, etc

```sql
BEGIN TRANSACTION

UPDATE account SET balance = balance -100 WHERE no = '123';
UPDATE account SET balance = balance -200 WHERE no = '321';

COMMIT;

```

### ACID properties
It's a 4 properties of a robust (well designed and reliable for CRUD)  database

1. **Atomacity** : All operations in a transaction either compleated or none of them applied at all.
2. **Consistancy** : DB should follow a predefined rules like `this column should be int`
3. **Isolation** : Each transacton is isolated from others like scope of a variable
4. **Durability** : Once the transaction committed, then changes are permanent sucurely



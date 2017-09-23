/*
    FIT9132 2017 Semester 2 Assignment 2 SOLUTIONS SCRIPT
    
    Student Name:
    
    Student ID:
    
	Studio Class:
	
	Tutor:
	
	Comments for your marker:
	
	

*/


-- Task 1 Data Definition
-- ======================

-- Task 1.1
CREATE TABLE fs_diner (
    diner_no        NUMBER(8) NOT NULL,
    food_item_no    NUMBER(4) NOT NULL,
    food_serve_size CHAR(2 BYTE) NOT NULL,
    bev_alcohol_level   NUMBER(3,1) NOT NULL,
    fs_diner_no_serves  NUMBER(1) NOT NULL,
    fs_diner_item_served CHAR(1 BYTE) NOT NULL
);


ALTER TABLE fs_diner
    ADD CONSTRAINT food_serve_size_chk CHECK (
        food_serve_size IN (
            'LG','SM','ST'
        )
    );

ALTER TABLE fs_diner
    ADD CONSTRAINT fs_diner_item_served_chk CHECK (
        fs_diner_item_served IN (
            'S','O'
        )
    );

COMMENT ON COLUMN fs_diner.diner_no IS
    'Diner identifier';

COMMENT ON COLUMN fs_diner.food_item_no IS
    'Identifier for a particular menu item';

COMMENT ON COLUMN fs_diner.food_serve_size IS
    'Food serve size - must be SM,ST or LG';

COMMENT ON COLUMN fs_diner.bev_alcohol_level IS
    'Alcoholic content of beverage';


COMMENT ON COLUMN fs_diner.fs_diner_no_serves IS
    ' the number of serves diners have ordered';

COMMENT ON COLUMN fs_diner.fs_diner_item_served IS
    'The status of the food item';


-- ADD PK CONSTRAINT
ALTER TABLE fs_diner ADD CONSTRAINT fs_diner_pk PRIMARY KEY ( 
    dinerr_no, 
    food_item_no,
    food_serve_size 
);

-- ADD FK CONSTRAINT
ALTER TABLE fs_diner
    ADD CONSTRAINT fs_diner_diner_fk FOREIGN KEY ( dinner_no )
        REFERENCES diner ( dinner_no )
    NOT DEFERRABLE; 


ALTER TABLE fs_diner
    ADD CONSTRAINT fs_diner_food_serve_fk FOREIGN KEY ( food_item_no, food_serve_size )
        REFERENCES food_serve ( food_item_no, food_serve_size )
    NOT DEFERRABLE; 





    
-- Task 1.2
-- drop table statements
-- here you must NOT use CASCADE constraints
-- TODO
DROP TABLE dessert;
DROP TABLE main;
DROP TABLE entree;
DROP TABLE beverage;
DROP TABLE fs_diner;
DROP TABLE diner;
DROP TABLE table_details;
DROP TABLE food_serve;
DROP TABLE fooditem



-- Task 2 Data Manipulation
-- ========================

-- Task 2.1
-- Add to your database four DINER records and their associated FS_DINER records
-- table no: 1 2 3 4 
-- value： diner, diner_payment_due, seat_no,completed, table no 
INSERT INTO DINER VALUES (1, 24.00, 1, "01-May-1995", "01-May-1995", 1);
INSERT INTO DINER VALUES (2, 57.00, 2, "02-May-1995", "02-May-1995", 1);
INSERT INTO DINER VALUES (3, 56.00, 3, "03-May-1995", "03-May-1995", 1);
INSERT INTO DINER VALUES (4, 22.00, 1, "04-May-1995", "04-May-1995", 1);

-- value： diner_no, food_item_no, food_serve_size, fs_diner_no_serve, fs_diner_item_served
INSERT INTO FS_DINER VALUES (1, 2, "ST", 1, "S");
INSERT INTO FS_DINER VALUES (1, 3, "ST", 1, "S");

INSERT INTO FS_DINER VALUES (2, 4, "LG", 1, "S");
INSERT INTO FS_DINER VALUES (2, 10, "ST", 1, "S");

INSERT INTO FS_DINER VALUES (3, 4, "SM", 1, "S");
INSERT INTO FS_DINER VALUES (3, 5, "ST", 1, "S");

INSERT INTO FS_DINER VALUES (4, 8, "ST", 1, "S");
INSERT INTO FS_DINER VALUES (4, 9, "ST", 1, "S");


-- Task 2.2
-- Provide the create sequence commands to be used for primary key vales when adding 
-- food items and diners to the system. 
-- - the food item sequence should start at 11 and increment by 1
-- - the diner sequence should start at 10 and increment by 1
CREATE SEQUENCE food_item__seq START WITH 11 INCREMENT BY 1;
CREATE SEQUENCE diner_seq START WITH 10 INCREMENT BY 1;



-- Task 2.3    
--  Provide the drop sequence statements for the two sequences you created in  Q2.1 
DROP SEQUENCE food_item__seq;
DROP SEQUENCE diner_seq;



-- Task 3 Database Insert/Updates
-- ==============================

-- SEQUENCES created in task 2.2 must be used in this task for the adding primary keys.

-- Task 3.1
--  Add a new DESSERT to the Monash food menu - you will need to research some
-- meaningful data to be able to add this item.  DESSERT's are food_type 'D' and are 
-- only served in standard 'ST' serve sizes.




-- Task 3.2
-- Monash food has decided to increase the price charged for all standard serve  
-- ('ST') main food items ('M' food type) by 15%, make this change in the database




-- Task 3.3 Diner Activity

-- Task 3.3 (a) A new diner has just arrived and been seated at Table 1 seat 3. Update the  
-- database to seat this diner




-- Task 3.3 (b) This new diner calls the waiter over and proceeds to order two 'Bruschetta' 
-- entrees. Entrees are only available in a standard 'ST' size. Add this data to the 
-- Monash Food System for this diner. The food item has not been served as yet, this is 
-- an order only




-- Task 3.3 (c) Some time after this order has been recorded the 'Bruschetta' are served to 
-- this diner - update the database to record this service. 




-- Task 4 Database Structure
-- =========================
-- Task 4.1 Collection of Diner information




-- Task 4.2 End of financial year DINER and FS_DINER archive




--========================= END OF ASS2-SOLUTION.SQL ==================================

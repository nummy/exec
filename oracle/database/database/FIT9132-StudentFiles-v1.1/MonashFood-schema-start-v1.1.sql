-- Monash Food Schema Partial

CREATE TABLE beverage (
    food_item_no        NUMBER(4) NOT NULL,
    bev_alcohol_level   NUMBER(3,1) NOT NULL
);

COMMENT ON COLUMN beverage.food_item_no IS
    'Identifier for a particular menu item';

COMMENT ON COLUMN beverage.bev_alcohol_level IS
    'Alcoholic content of beverage';

ALTER TABLE beverage ADD CONSTRAINT beverage_pk PRIMARY KEY ( food_item_no );

CREATE TABLE dessert (
    food_item_no           NUMBER(4) NOT NULL,
    dessert_lactose_free   CHAR(1 BYTE) NOT NULL
);

ALTER TABLE dessert
    ADD CONSTRAINT chk_dessert_lactose_free CHECK (
        dessert_lactose_free IN (
            'N','Y'
        )
    );

COMMENT ON COLUMN dessert.food_item_no IS
    'Identifier for a particular menu item';

COMMENT ON COLUMN dessert.dessert_lactose_free IS
    'Is dessert lactose free';

ALTER TABLE dessert ADD CONSTRAINT dessert_pk PRIMARY KEY ( food_item_no );

CREATE TABLE diner (
    diner_no            NUMBER(8) NOT NULL,
    diner_payment_due   NUMBER(6,2) NOT NULL,
    diner_seat_no       NUMBER(2) NOT NULL,
    diner_seated        DATE NOT NULL,
    diner_completed     DATE,
    table_no            NUMBER(2) NOT NULL
);

COMMENT ON COLUMN diner.diner_no IS
    'Diner identifier';

COMMENT ON COLUMN diner.diner_payment_due IS
    'Total amount owing for this diner';

COMMENT ON COLUMN diner.diner_seat_no IS
    'Seat occupied by this diner';

COMMENT ON COLUMN diner.diner_seated IS
    'The date and time the diner is seated (begins the dining experience)';

COMMENT ON COLUMN diner.diner_completed IS
    'The date and time the diner pays for their meal (completed the dining experience)';

COMMENT ON COLUMN diner.table_no IS
    'Table number';

ALTER TABLE diner ADD CONSTRAINT diner_pk PRIMARY KEY ( diner_no );

CREATE TABLE entree (
    food_item_no   NUMBER(4) NOT NULL,
    entree_hot     CHAR(1) NOT NULL
);

ALTER TABLE entree
    ADD CONSTRAINT chk_entree_hot CHECK (
        entree_hot IN (
            'N','Y'
        )
    );

COMMENT ON COLUMN entree.food_item_no IS
    'Identifier for a particular menu item';

COMMENT ON COLUMN entree.entree_hot IS
    'Is entree hot (Y/N)';

ALTER TABLE entree ADD CONSTRAINT entree_pk PRIMARY KEY ( food_item_no );

CREATE TABLE food_serve (
    food_item_no           NUMBER(4) NOT NULL,
    food_serve_size        CHAR(2) NOT NULL,
    food_serve_kilojoules  NUMBER(4) NOT NULL,
    food_serve_cost        NUMBER(5,2) NOT NULL
);

ALTER TABLE food_serve
    ADD CONSTRAINT food_serve_size_chk CHECK (
        food_serve_size IN (
            'LG','SM','ST'
        )
    );

COMMENT ON COLUMN food_serve.food_item_no IS
    'Identifier for a particular menu item';

COMMENT ON COLUMN food_serve.food_serve_size IS
    'Food serve size - must be SM,ST or LG';

COMMENT ON COLUMN food_serve.food_serve_kilojoules IS
    'Number of kilojoules in this food item of this serve size';

COMMENT ON COLUMN food_serve.food_serve_cost IS
    'Cost of this food serve';

ALTER TABLE food_serve ADD CONSTRAINT food_serve_pk PRIMARY KEY ( food_item_no,food_serve_size );

CREATE TABLE fooditem (
    food_item_no       NUMBER(4) NOT NULL,
    food_name          VARCHAR2(50) NOT NULL,
    food_description   VARCHAR2(100) NOT NULL,
    food_type          CHAR(1) NOT NULL
);

ALTER TABLE fooditem
    ADD CONSTRAINT chk_food_type CHECK (
        food_type IN (
            'B','D','E','M'
        )
    );

COMMENT ON COLUMN fooditem.food_item_no IS
    'Identifier for a particular menu item';

COMMENT ON COLUMN fooditem.food_name IS
    'Name of menu item';

COMMENT ON COLUMN fooditem.food_description IS
    'Description of menu item';

COMMENT ON COLUMN fooditem.food_type IS
    'Which type of food - must be B, E, M or D';

ALTER TABLE fooditem ADD CONSTRAINT fooditem_pk PRIMARY KEY ( food_item_no );

ALTER TABLE fooditem ADD CONSTRAINT foodname_un UNIQUE ( food_name );

CREATE TABLE main (
    food_item_no       NUMBER(4) NOT NULL,
    main_vegetarian    CHAR(1) NOT NULL,
    main_gluten_free   CHAR(1) NOT NULL
);

ALTER TABLE main
    ADD CONSTRAINT chk_main_vegetarian CHECK (
        main_vegetarian IN (
            'N','Y'
        )
    );

ALTER TABLE main
    ADD CONSTRAINT chk_main_gluten_free CHECK (
        main_gluten_free IN (
            'N','Y'
        )
    );

COMMENT ON COLUMN main.food_item_no IS
    'Identifier for a particular menu item';

COMMENT ON COLUMN main.main_vegetarian IS
    'Is main vegetarian (Y/N)';

COMMENT ON COLUMN main.main_gluten_free IS
    'Is main gluten free (Y/N)';

ALTER TABLE main ADD CONSTRAINT main_pk PRIMARY KEY ( food_item_no );

CREATE TABLE table_details (
    table_no                 NUMBER(2) NOT NULL,
    table_seating_capacity   NUMBER(2) NOT NULL,
    table_location           VARCHAR2(50) NOT NULL
);

COMMENT ON COLUMN table_details.table_no IS
    'Table number';

COMMENT ON COLUMN table_details.table_seating_capacity IS
    'Maximum number of diners which can be seated at  table';

COMMENT ON COLUMN table_details.table_location IS
    'Location of table';

ALTER TABLE table_details ADD CONSTRAINT table_details_pk PRIMARY KEY ( table_no );

ALTER TABLE beverage
    ADD CONSTRAINT beverage_fooditem_fk FOREIGN KEY ( food_item_no )
        REFERENCES fooditem ( food_item_no )
    NOT DEFERRABLE;

ALTER TABLE dessert
    ADD CONSTRAINT dessert_fooditem_fk FOREIGN KEY ( food_item_no )
        REFERENCES fooditem ( food_item_no )
    NOT DEFERRABLE;

ALTER TABLE entree
    ADD CONSTRAINT entree_fooditem_fk FOREIGN KEY ( food_item_no )
        REFERENCES fooditem ( food_item_no )
    NOT DEFERRABLE;

ALTER TABLE food_serve
    ADD CONSTRAINT food_serve_fooditem_fk FOREIGN KEY ( food_item_no )
        REFERENCES fooditem ( food_item_no )
    NOT DEFERRABLE;

ALTER TABLE main
    ADD CONSTRAINT main_fooditem_fk FOREIGN KEY ( food_item_no )
        REFERENCES fooditem ( food_item_no )
    NOT DEFERRABLE;

ALTER TABLE diner
    ADD CONSTRAINT diner_table_details_fk FOREIGN KEY ( table_no )
        REFERENCES table_details ( table_no )
    NOT DEFERRABLE;

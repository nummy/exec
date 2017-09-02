
CREATE TABLE carnival (
    "date"     VARCHAR2(25 CHAR) NOT NULL,
    director   VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE carnival ADD CONSTRAINT carnival_pk PRIMARY KEY ( "date" );

CREATE TABLE competitor (
    competitor_number         VARCHAR2(5 CHAR) NOT NULL,
    firstname                 VARCHAR2(25 CHAR) NOT NULL,
    lastname                  VARCHAR2(25 CHAR) NOT NULL,
    gender                    CHAR(1) NOT NULL,
    birthday                  DATE NOT NULL,
    email                     VARCHAR2(30 CHAR) NOT NULL,
    isstudent                 CHAR(1) NOT NULL,
    mobile                    VARCHAR2(20 CHAR) NOT NULL,
    medical_condition         CHAR(1) NOT NULL,
    medical_areas             mdsys.sdo_geometry,
    ec_firstname              VARCHAR2(20),
    ec_lastname               VARCHAR2(20) NOT NULL,
    ec_phone                  VARCHAR2(20) NOT NULL,
    ec_relationship           VARCHAR2(20) NOT NULL,
    g_firstname               VARCHAR2(20) NOT NULL,
    g_lastname                VARCHAR2(20) NOT NULL,
    g_phone                   VARCHAR2(20) NOT NULL,
    entry_competitor_number   VARCHAR2(5) NOT NULL
);

CREATE UNIQUE INDEX competitor__idx ON
    competitor ( entry_competitor_number ASC );

ALTER TABLE competitor ADD CONSTRAINT competitor_pk PRIMARY KEY ( competitor_number );

CREATE TABLE entry (
    competitor_number   VARCHAR2(5) NOT NULL,
    teamname            VARCHAR2(20),
    event_event_name    VARCHAR2(30 CHAR) NOT NULL
);

ALTER TABLE entry ADD CONSTRAINT entry_pk PRIMARY KEY ( competitor_number );

CREATE TABLE event (
    event_name      VARCHAR2(30 CHAR) NOT NULL,
    carnival_date   VARCHAR2(25 CHAR) NOT NULL
);

ALTER TABLE event ADD CONSTRAINT event_pk PRIMARY KEY ( event_name );

CREATE TABLE location (
    name            VARCHAR2(20 CHAR) NOT NULL,
    carnival_date   VARCHAR2(25 CHAR) NOT NULL
);

ALTER TABLE location ADD CONSTRAINT location_pk PRIMARY KEY ( name );

CREATE TABLE merchandise (
    order_number       VARCHAR2(25) NOT NULL,
    item_code          VARCHAR2(20 CHAR) NOT NULL,
    item_description   VARCHAR2(30 BYTE) NOT NULL,
    cost               FLOAT NOT NULL,
    qty                INTEGER NOT NULL,
    line_cost          FLOAT NOT NULL
);

ALTER TABLE merchandise ADD CONSTRAINT merchandise_pk PRIMARY KEY ( item_code );

CREATE TABLE "Order" (
    order_number                   VARCHAR2(5 CHAR) NOT NULL,
    order_date                     DATE NOT NULL,
    carnival_date                  VARCHAR2(20 CHAR) NOT NULL,
    order_number_2                 VARCHAR2(20 CHAR) NOT NULL,
    competitor_competitor_number   VARCHAR2(5 CHAR) NOT NULL,
    volunteer_volunteer_number     VARCHAR2(5 CHAR) NOT NULL
);

ALTER TABLE "Order" ADD CONSTRAINT order_pk PRIMARY KEY ( order_number );

CREATE TABLE sponsor (
    sponsor_name    VARCHAR2(25 CHAR) NOT NULL,
    isnaming        CHAR(1) NOT NULL,
    amount          FLOAT NOT NULL,
    contact         VARCHAR2(25 CHAR) NOT NULL,
    phone           VARCHAR2(20 CHAR) NOT NULL,
    carnival_date   VARCHAR2(25 CHAR) NOT NULL
);

ALTER TABLE sponsor ADD CONSTRAINT sponsor_pk PRIMARY KEY ( sponsor_name );

CREATE TABLE volunteer (
    volunteer_number   VARCHAR2(5 CHAR) NOT NULL,
    volunteer_name     VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE volunteer ADD CONSTRAINT volunteer_pk PRIMARY KEY ( volunteer_number );

ALTER TABLE competitor
    ADD CONSTRAINT competitor_entry_fk FOREIGN KEY ( entry_competitor_number )
        REFERENCES entry ( competitor_number );

ALTER TABLE entry
    ADD CONSTRAINT entry_event_fk FOREIGN KEY ( event_event_name )
        REFERENCES event ( event_name );

ALTER TABLE event
    ADD CONSTRAINT event_carnival_fk FOREIGN KEY ( carnival_date )
        REFERENCES carnival ( "date" );

ALTER TABLE location
    ADD CONSTRAINT location_carnival_fk FOREIGN KEY ( carnival_date )
        REFERENCES carnival ( "date" );

ALTER TABLE "Order"
    ADD CONSTRAINT order_competitor_fk FOREIGN KEY ( competitor_competitor_number )
        REFERENCES competitor ( competitor_number );

ALTER TABLE "Order"
    ADD CONSTRAINT order_volunteer_fk FOREIGN KEY ( volunteer_volunteer_number )
        REFERENCES volunteer ( volunteer_number );

ALTER TABLE sponsor
    ADD CONSTRAINT sponsor_carnival_fk FOREIGN KEY ( carnival_date )
        REFERENCES carnival ( "date" );


CREATE TABLE carnival (
    carnival_date   VARCHAR2(25 CHAR) NOT NULL,
    director        VARCHAR2(20 CHAR) NOT NULL,
    location        VARCHAR2(40 CHAR) NOT NULL
);

COMMENT ON COLUMN carnival.carnival_date IS
    'carnival date,primary key';

COMMENT ON COLUMN carnival.director IS
    'carnival director';

COMMENT ON COLUMN carnival.location IS
    'carnival location';

ALTER TABLE carnival ADD CONSTRAINT carnival_pk PRIMARY KEY ( carnival_date );

CREATE TABLE competitor (
    competitor_number         VARCHAR2(5 CHAR) NOT NULL,
    firstname                 VARCHAR2(25 CHAR) NOT NULL,
    cname                     VARCHAR2(25 CHAR) NOT NULL,
    gender                    CHAR(1) NOT NULL,
    birthday                  DATE NOT NULL,
    email                     VARCHAR2(30 CHAR) NOT NULL,
    isstudent                 CHAR(1) NOT NULL,
    mobile                    VARCHAR2(20 CHAR) NOT NULL,
    medical_condition         CHAR(1) NOT NULL,
    medical_areas             mdsys.sdo_geometry,
    ename                     VARCHAR2(20),
    ec_lastname               VARCHAR2(20) NOT NULL,
    ephone                    VARCHAR2(20) NOT NULL,
    relationship              VARCHAR2(20) NOT NULL,
    gname                     VARCHAR2(20) NOT NULL,
    g_lastname                VARCHAR2(20) NOT NULL,
    gphone                    VARCHAR2(20) NOT NULL,
    entry_competitor_number   VARCHAR2(5) NOT NULL,
    enumber                   VARCHAR2(20 CHAR) NOT NULL
);

COMMENT ON COLUMN competitor.competitor_number IS
    'competitor gender';

COMMENT ON COLUMN competitor.cname IS
    'competitor Name';

COMMENT ON COLUMN competitor.birthday IS
    'competitor''s birthday';

COMMENT ON COLUMN competitor.email IS
    'competitor''s email';

COMMENT ON COLUMN competitor.isstudent IS
    'Is competitor a university student';

COMMENT ON COLUMN competitor.mobile IS
    'competitor''s mobile';

COMMENT ON COLUMN competitor.medical_condition IS
    'medical condition';

COMMENT ON COLUMN competitor.medical_areas IS
    'medical areas';

COMMENT ON COLUMN competitor.ename IS
    'emergency contact name';

COMMENT ON COLUMN competitor.ephone IS
    'emergency contact phone';

COMMENT ON COLUMN competitor.relationship IS
    'emergency contact relationship';

COMMENT ON COLUMN competitor.gname IS
    'guardian name';

COMMENT ON COLUMN competitor.gphone IS
    'guardian phone';

COMMENT ON COLUMN competitor.enumber IS
    'entry number';

CREATE UNIQUE INDEX competitor__idx ON
    competitor ( entry_competitor_number ASC );

CREATE UNIQUE INDEX competitor__idx ON
    competitor ( enumber ASC );

ALTER TABLE competitor ADD CONSTRAINT competitor_pk PRIMARY KEY ( competitor_number );

CREATE TABLE entry (
    competitor_number   VARCHAR2(5) NOT NULL,
    teamname            VARCHAR2(20),
    event_event_name    VARCHAR2(30 CHAR) NOT NULL,
    enumber             VARCHAR2(20 CHAR) NOT NULL
);

COMMENT ON COLUMN entry.competitor_number IS
    'competitor number';

COMMENT ON COLUMN entry.teamname IS
    'team name';

COMMENT ON COLUMN entry.event_event_name IS
    'event name';

COMMENT ON COLUMN entry.enumber IS
    'entry number';

ALTER TABLE entry ADD CONSTRAINT entry_pk PRIMARY KEY ( enumber );

CREATE TABLE event (
    event_name      VARCHAR2(30 CHAR) NOT NULL,
    carnival_date   VARCHAR2(25 CHAR) NOT NULL
);

COMMENT ON COLUMN event.event_name IS
    'event_name';

COMMENT ON COLUMN event.carnival_date IS
    'carnival date,foreign key';

ALTER TABLE event ADD CONSTRAINT event_pk PRIMARY KEY ( event_name );

CREATE TABLE item (
    item_code          VARCHAR2(20 CHAR) NOT NULL,
    item_description   VARCHAR2(40) NOT NULL,
    cost               FLOAT NOT NULL
);

COMMENT ON COLUMN item.item_code IS
    'item code';

COMMENT ON COLUMN item.item_description IS
    'item description';

COMMENT ON COLUMN item.cost IS
    'item cost';

ALTER TABLE item ADD CONSTRAINT item_pk PRIMARY KEY ( item_code );

CREATE TABLE location (
    name            VARCHAR2(20 CHAR) NOT NULL,
    carnival_date   VARCHAR2(25 CHAR) NOT NULL
);

ALTER TABLE location ADD CONSTRAINT location_pk PRIMARY KEY ( name );

CREATE TABLE merchandise (
    order_number          VARCHAR2(25) NOT NULL,
    item_code             VARCHAR2(20 CHAR) NOT NULL,
    item_description      VARCHAR2(30 BYTE) NOT NULL,
    cost                  FLOAT NOT NULL,
    qty                   INTEGER NOT NULL,
    line_cost             FLOAT NOT NULL,
    order_order_number    VARCHAR2(5 CHAR) NOT NULL,
    order_order_number1   VARCHAR2(5 CHAR) NOT NULL,
    item_item_code        VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE merchandise ADD CONSTRAINT merchandise_pk PRIMARY KEY ( order_order_number1,item_item_code );

CREATE TABLE "Order" (
    order_number                   VARCHAR2(5 CHAR) NOT NULL,
    order_date                     DATE NOT NULL,
    carnival_date                  VARCHAR2(20 CHAR) NOT NULL,
    order_number_2                 VARCHAR2(20 CHAR) NOT NULL,
    competitor_competitor_number   VARCHAR2(5 CHAR) NOT NULL,
    volunteer_volunteer_number     VARCHAR2(5 CHAR) NOT NULL
);

COMMENT ON COLUMN "Order".order_number IS
    'order number';

COMMENT ON COLUMN "Order".order_date IS
    'order date';

COMMENT ON COLUMN "Order".carnival_date IS
    'carnival date';

COMMENT ON COLUMN "Order".competitor_competitor_number IS
    'competitor number';

COMMENT ON COLUMN "Order".volunteer_volunteer_number IS
    'volunteer number';

ALTER TABLE "Order" ADD CONSTRAINT order_pk PRIMARY KEY ( order_number );

CREATE TABLE sponsor (
    sponsor_name    VARCHAR2(25 CHAR) NOT NULL,
    isnaming        CHAR(1) NOT NULL,
    amount          FLOAT NOT NULL,
    contact         VARCHAR2(25 CHAR) NOT NULL,
    phone           VARCHAR2(20 CHAR) NOT NULL,
    carnival_date   VARCHAR2(25 CHAR) NOT NULL
);

COMMENT ON COLUMN sponsor.sponsor_name IS
    'sponsor name';

COMMENT ON COLUMN sponsor.isnaming IS
    'Naming Sponsor ';

COMMENT ON COLUMN sponsor.amount IS
    'Amount of Sponsorship';

COMMENT ON COLUMN sponsor.contact IS
    'Sponsor Contact ';

COMMENT ON COLUMN sponsor.phone IS
    'Sponsor Phone Contact ';

COMMENT ON COLUMN sponsor.carnival_date IS
    'carnival date,foreign key';

ALTER TABLE sponsor ADD CONSTRAINT sponsor_pk PRIMARY KEY ( sponsor_name );

CREATE TABLE volunteer (
    volunteer_number   VARCHAR2(5 CHAR) NOT NULL,
    volunteer_name     VARCHAR2(20 CHAR) NOT NULL
);

COMMENT ON COLUMN volunteer.volunteer_number IS
    'volunteer number';

COMMENT ON COLUMN volunteer.volunteer_name IS
    'volunteer name';

ALTER TABLE volunteer ADD CONSTRAINT volunteer_pk PRIMARY KEY ( volunteer_number );

ALTER TABLE competitor
    ADD CONSTRAINT competitor_entry_fk FOREIGN KEY ( enumber )
        REFERENCES entry ( enumber );

ALTER TABLE entry
    ADD CONSTRAINT entry_event_fk FOREIGN KEY ( event_event_name )
        REFERENCES event ( event_name );

ALTER TABLE event
    ADD CONSTRAINT event_carnival_fk FOREIGN KEY ( carnival_date )
        REFERENCES carnival ( carnival_date );

ALTER TABLE location
    ADD CONSTRAINT location_carnival_fk FOREIGN KEY ( carnival_date )
        REFERENCES carnival ( carnival_date );

ALTER TABLE merchandise
    ADD CONSTRAINT merchandise_item_fk FOREIGN KEY ( item_item_code )
        REFERENCES item ( item_code );

ALTER TABLE merchandise
    ADD CONSTRAINT merchandise_order_fk FOREIGN KEY ( order_order_number )
        REFERENCES "Order" ( order_number );

ALTER TABLE merchandise
    ADD CONSTRAINT merchandise_order_fkv2 FOREIGN KEY ( order_order_number1 )
        REFERENCES "Order" ( order_number );

ALTER TABLE "Order"
    ADD CONSTRAINT order_competitor_fk FOREIGN KEY ( competitor_competitor_number )
        REFERENCES competitor ( competitor_number );

ALTER TABLE "Order"
    ADD CONSTRAINT order_volunteer_fk FOREIGN KEY ( volunteer_volunteer_number )
        REFERENCES volunteer ( volunteer_number );

ALTER TABLE sponsor
    ADD CONSTRAINT sponsor_carnival_fk FOREIGN KEY ( carnival_date )
        REFERENCES carnival ( carnival_date );

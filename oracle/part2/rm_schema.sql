CREATE TABLE carnival (
    "date"     DATE NOT NULL,
    director   VARCHAR2(20 CHAR) NOT NULL,
    location   mdsys.sdo_geometry NOT NULL,
    event      mdsys.sdo_geometry NOT NULL
);

ALTER TABLE carnival ADD CONSTRAINT carnival_pk PRIMARY KEY ( "date" );

CREATE TABLE COMPETITOR 
    ( 
     cnumber         VARCHAR2 (6 CHAR)  NOT NULL , 
     cfirstname      VARCHAR2 (20 CHAR)  NOT NULL , 
     clastname       VARCHAR2 (20 CHAR)  NOT NULL , 
     cname           VARCHAR2 (30 CHAR)  NOT NULL , 
     cgender         CHAR (1)  NOT NULL , 
     cbirthday       DATE  NOT NULL , 
     cemail          VARCHAR2 (30 CHAR)  NOT NULL , 
     cIsStu          CHAR (1)  NOT NULL , 
     cMobile         VARCHAR2 (30 CHAR)  NOT NULL , 
     cIsAnyCondition CHAR (1)  NOT NULL , 
     cArea           MDSYS.SDO_GEOMETRY , 
     ecfirstname     VARCHAR2 (20 CHAR)  NOT NULL , 
     eclastname      VARCHAR2 (20 CHAR)  NOT NULL , 
     ecname          VARCHAR2 (30 CHAR)  NOT NULL , 
     ecphone         VARCHAR2 (20 CHAR)  NOT NULL , 
     ecrelation      VARCHAR2 (20 CHAR)  NOT NULL , 
     gfistname       VARCHAR2 (20 CHAR)  NOT NULL , 
     glastname       VARCHAR2 (20 CHAR)  NOT NULL , 
     gname           VARCHAR2 (30 CHAR) , 
     gphone          VARCHAR2 (gphone CHAR)  NOT NULL , 
     ENTRY_enumber   VARCHAR2 (10 CHAR)  NOT NULL 
    ) 
;

CREATE UNIQUE INDEX COMPETITOR__IDX ON COMPETITOR 
    ( 
     ENTRY_enumber ASC 
    ) 
;

ALTER TABLE competitor ADD CONSTRAINT competitor_pk PRIMARY KEY ( cnumber );

CREATE TABLE entry (
    enumber         VARCHAR2(10 CHAR) NOT NULL,
    event           VARCHAR2(20 CHAR) NOT NULL,
    teamname        VARCHAR2(20 CHAR),
    carnival_date   DATE NOT NULL
);

ALTER TABLE entry ADD CONSTRAINT entry_pk PRIMARY KEY ( enumber );

CREATE TABLE item (
    itemcode          VARCHAR2(20 CHAR) NOT NULL,
    itemdescription   VARCHAR2(30 CHAR) NOT NULL,
    itemcost          FLOAT NOT NULL
);

ALTER TABLE item ADD CONSTRAINT item_pk PRIMARY KEY ( itemcode );

CREATE TABLE merchandiise (
    itemcode            VARCHAR2(20 CHAR) NOT NULL,
    qtn                 INTEGER NOT NULL,
    linecost            FLOAT NOT NULL,
    order_ordernumber   VARCHAR2(8 CHAR) NOT NULL,
    item_itemcode       VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE merchandiise ADD CONSTRAINT merchandiise_pk PRIMARY KEY ( itemcode,order_ordernumber );

CREATE TABLE "ORDER" (
    ordernumber          VARCHAR2(8 CHAR) NOT NULL,
    orderdate            DATE,
    cvnumber             VARCHAR2(10 CHAR),
    delivery             FLOAT(2) NOT NULL,
    totalcost            FLOAT NOT NULL,
    competitor_cnumber   VARCHAR2(6 CHAR) NOT NULL,
    volunteer_vnumber    VARCHAR2(10 CHAR) NOT NULL
);

ALTER TABLE "ORDER" ADD CONSTRAINT order_pk PRIMARY KEY ( ordernumber );

CREATE TABLE sponsor (
    sponsorname       VARCHAR2(20 CHAR) NOT NULL,
    isnaming          CHAR(1) NOT NULL,
    sponsoramount     FLOAT NOT NULL,
    sponsoracontact   VARCHAR2(30 CHAR) NOT NULL,
    sponsorphone      VARCHAR2(20 CHAR) NOT NULL,
    carnival_date     DATE NOT NULL
);

ALTER TABLE sponsor ADD CONSTRAINT sponsor_pk PRIMARY KEY ( sponsorname );

CREATE TABLE volunteer (
    vnumber   VARCHAR2(10 CHAR) NOT NULL,
    vname     VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE volunteer ADD CONSTRAINT volunteer_pk PRIMARY KEY ( vnumber );

ALTER TABLE competitor
    ADD CONSTRAINT competitor_entry_fk FOREIGN KEY ( entry_enumber )
        REFERENCES entry ( enumber );

ALTER TABLE entry
    ADD CONSTRAINT entry_carnival_fk FOREIGN KEY ( carnival_date )
        REFERENCES carnival ( "date" );

ALTER TABLE merchandiise
    ADD CONSTRAINT merchandiise_item_fk FOREIGN KEY ( item_itemcode )
        REFERENCES item ( itemcode );

ALTER TABLE merchandiise
    ADD CONSTRAINT merchandiise_order_fk FOREIGN KEY ( order_ordernumber )
        REFERENCES "ORDER" ( ordernumber );

ALTER TABLE "ORDER"
    ADD CONSTRAINT order_competitor_fk FOREIGN KEY ( competitor_cnumber )
        REFERENCES competitor ( cnumber );

ALTER TABLE "ORDER"
    ADD CONSTRAINT order_volunteer_fk FOREIGN KEY ( volunteer_vnumber )
        REFERENCES volunteer ( vnumber );

ALTER TABLE sponsor
    ADD CONSTRAINT sponsor_carnival_fk FOREIGN KEY ( carnival_date )
        REFERENCES carnival ( "date" );

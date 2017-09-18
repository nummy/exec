
INSERT INTO TABLE_DETAILS VALUES (1,3,'North side near window');
INSERT INTO TABLE_DETAILS VALUES (2,4,'North side near window');
INSERT INTO TABLE_DETAILS VALUES (3,6,'Central near kitchen');
INSERT INTO TABLE_DETAILS VALUES (4,4,'South side in alcove');

INSERT INTO FOODITEM VALUES (1,'Bruschetta','Tomato, spring onion, olive oil, parmesan - four pieces','E');
INSERT INTO ENTREE VALUES (1,'Y');
INSERT INTO FOOD_SERVE VALUES (1,'ST',426,12);
INSERT INTO FOODITEM VALUES (2,'Arancini Balls','Pork, peas and gorgonzola rice balls - four pieces','E');
INSERT INTO ENTREE VALUES (2,'Y');
INSERT INTO FOOD_SERVE values (2,'ST',1403,12);
INSERT INTO FOODITEM VALUES (3,'Beef Carpaccio','Pork, peas and gorgonzola rice balls - four pieces','E');
INSERT INTO ENTREE VALUES (3,'N');
INSERT INTO FOOD_SERVE VALUES (3,'ST',1054,12);

INSERT INTO FOODITEM VALUES (4,'Braised Beef Brisket','Braised beef brisket, herb polenta, baby onions, parsnip puree','M');
INSERT INTO MAIN VALUES (4,'N','N');
INSERT INTO FOOD_SERVE VALUES (4,'ST',4600,38);
INSERT INTO FOOD_SERVE VALUES (4,'SM',3500,28);
INSERT INTO FOOD_SERVE VALUES (4,'LG',6300,45);
INSERT INTO FOODITEM VALUES (5,'Ravioli Ricotta','Ricotta and spinach ravioli, sun-dried tomato, fresh basil, red onion, Napoletana, cream, pesto','M');
INSERT INTO MAIN VALUES (5,'Y','N');
INSERT INTO FOOD_SERVE VALUES (5,'ST',2400,28);
INSERT INTO FOOD_SERVE VALUES (5,'SM',1200,18);
INSERT INTO FOODITEM VALUES (6,'Spaghetti Marinara','Spaghetti, garlic, tiger prawns, mussels, diced fish, cockles, calamari, spinach, olive oil','M');
INSERT INTO MAIN VALUES (6,'N','N');
INSERT INTO FOOD_SERVE VALUES (6,'ST',3380,33);

INSERT INTO FOODITEM VALUES (7,'Sticky Date Pudding','Caramel sauce, double cream, ice-cream','D');
INSERT INTO DESSERT VALUES (7,'N');
INSERT INTO FOOD_SERVE VALUES (7,'ST',1764,14);
INSERT INTO FOODITEM VALUES (8,'Classic Chocolate Mousse','Rich chocolate mousse with cream','D');
INSERT INTO DESSERT VALUES (8,'N');
INSERT INTO FOOD_SERVE VALUES (8,'ST',1564,10);

INSERT INTO FOODITEM VALUES (9,'House White (Glass)','South Australian Dry white wine','B');
INSERT INTO BEVERAGE VALUES (9,12.5);
INSERT INTO FOOD_SERVE VALUES (9,'ST',270,12);
INSERT INTO FOODITEM VALUES (10,'Corona Beer','Ice cold imported beer','B');
INSERT INTO BEVERAGE VALUES (10,4.6);
INSERT INTO FOOD_SERVE VALUES (10,'ST',244,12);

COMMIT;


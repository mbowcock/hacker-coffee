CREATE TABLE coffeeshops
(
   id serial NOT NULL, 
   name text, 
   address text, 
   city text, 
   state text, 
   zip text, 
   country text DEFAULT 'US', 
   description text, 
   CONSTRAINT pkid PRIMARY KEY (id)
) 
WITH (
  OIDS = FALSE
)
;

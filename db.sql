-- according to postgresql docs there is no performance gain when 
-- specifying size of text data. So I'm leaving these as plain text
-- until I have a reason to change.
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

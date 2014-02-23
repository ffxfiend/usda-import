DROP TABLE IF EXISTS `food_description`;
CREATE TABLE `food_description` (
  id text PRIMARY KEY NOT NULL,
  food_group_id text REFERENCES food_group(id) NOT NULL,
  long_desc text NOT NULL DEFAULT '',
  short_desc text NOT NULL DEFAULT '',
  common_names text NULL DEFAULT '',
  manufac_name text NULL DEFAULT '',
  survey text NULL DEFAULT '',
  ref_desc text NULL DEFAULT '',
  refuse int NULL,
  sci_name text NULL DEFAULT '',
  nitrogen_factor float NULL,
  protein_factor float NULL,
  fat_factor float NULL,
  calorie_factor float NULL
);
CREATE INDEX food_short_desc_search_index ON food_description(short_desc);
CREATE INDEX food_long_desc_search_index ON food_description(long_desc);

DROP TABLE IF EXISTS `food_group`;
CREATE TABLE `food_group` (
  id text PRIMARY KEY NOT NULL,
  name text NOT NULL
);

DROP TABLE IF EXISTS `nutrition`;
CREATE TABLE `nutrition` (
  food_id text REFERENCES food(id) NOT NULL,
  nutrient_id text REFERENCES nutrient(id) NOT NULL,
  amount float NOT NULL,
  num_data_points int NOT NULL,
  std_error float,
  source_code text NOT NULL,
  derivation_code text,
  reference_food_id REFERENCES food(id),
  added_nutrient text,
  num_studients int,
  min float,
  max float,
  degrees_freedom int,
  lower_error_bound float,
  upper_error_bound float,
  comments text,
  modification_date text,
  confidence_code text,
  PRIMARY KEY(food_id, nutrient_id)
);

DROP TABLE IF EXISTS `nutrient`;
CREATE TABLE `nutrient` (
  id text PRIMARY KEY NOT NULL,
  units text NOT NULL,
  tagname text NOT NULL DEFAULT '',
  name text NOT NULL,
  num_decimal_places text NOT NULL,
  sr_order int NOT NULL
);
CREATE INDEX nutrient_name_search_index ON nutrient(name);
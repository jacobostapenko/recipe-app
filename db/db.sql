\c master


Create table recipe(
    recipe_id int Primary key
    name varchar(255) not null

    --there seems to be a better data type otpions for uri but non-trivial
    url varchar(255) not null
)
insert into recipe (recipe_id, name, url) values (1, 'in', 'erat');
insert into recipe (recipe_id, name, url) values (2, 'erat', 'potenti');
insert into recipe (recipe_id, name, url) values (3, 'pulvinar', 'donec');
insert into recipe (recipe_id, name, url) values (4, 'vitae', 'et');
insert into recipe (recipe_id, name, url) values (5, 'eu', 'justo');
insert into recipe (recipe_id, name, url) values (6, 'eros', 'nunc');
insert into recipe (recipe_id, name, url) values (7, 'non', 'potenti');
insert into recipe (recipe_id, name, url) values (8, 'suscipit', 'turpis');
insert into recipe (recipe_id, name, url) values (9, 'ipsum', 'velit');
insert into recipe (recipe_id, name, url) values (10, 'consequat', 'in');
insert into recipe (recipe_id, name, url) values (11, 'lacus', 'curabitur');
insert into recipe (recipe_id, name, url) values (12, 'nunc', 'consequat');
insert into recipe (recipe_id, name, url) values (13, 'interdum', 'curabitur');
insert into recipe (recipe_id, name, url) values (14, 'eleifend', 'amet');
insert into recipe (recipe_id, name, url) values (15, 'quis', 'mi');


create table ingredient(
    ing_id primary key
    name varchar(255) not null
    recipe_id int not null
)
insert into ingredient (ing_id, name, recipe_id) values (1, 'non', 1);
insert into ingredient (ing_id, name, recipe_id) values (2, 'imperdiet', 11);
insert into ingredient (ing_id, name, recipe_id) values (3, 'sit', 15);
insert into ingredient (ing_id, name, recipe_id) values (4, 'tellus', 6);
insert into ingredient (ing_id, name, recipe_id) values (5, 'primis', 8);
insert into ingredient (ing_id, name, recipe_id) values (6, 'tempus', 15);
insert into ingredient (ing_id, name, recipe_id) values (7, 'nec', 9);
insert into ingredient (ing_id, name, recipe_id) values (8, 'neque', 14);
insert into ingredient (ing_id, name, recipe_id) values (9, 'sapien', 3);
insert into ingredient (ing_id, name, recipe_id) values (10, 'congue', 5);
insert into ingredient (ing_id, name, recipe_id) values (11, 'proin', 3);
insert into ingredient (ing_id, name, recipe_id) values (12, 'quam', 14);
insert into ingredient (ing_id, name, recipe_id) values (13, 'sed', 4);
insert into ingredient (ing_id, name, recipe_id) values (14, 'dui', 11);
insert into ingredient (ing_id, name, recipe_id) values (15, 'tellus', 1);

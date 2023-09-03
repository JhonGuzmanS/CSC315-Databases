USE CSC315Final2022;
select * from genre;
select * from sub_genre;
select * from bands;
select * from country;
select * from band_origins;
select * from band_styles;

create table user(
	uid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    uname CHAR(20),
    home_country CHAR(20)
);

insert into user (uname, home_country) values ('Mike', 'United States');
insert into user (uname, home_country) values ('Bob', 'Canada');
insert into user (uname, home_country) values ('Tom', 'England');


create table favorites(
	uid INT,
    bid INT,
    bname CHAR(20),
    FOREIGN KEY (uid) REFERENCES user(uid),
    FOREIGN KEY (bid) REFERENCES bands(bid)
);

insert into favorites (uid, bid, bname) values (1, 1, 'Seputura');
insert into favorites (uid, bid, bname) values (1, 4, 'Led Zeppelin');
insert into favorites (uid, bid, bname) values (1, 15, 'Tengger Cavalry');
insert into favorites (uid, bid, bname) values (2, 6, 'The Hu');
insert into favorites (uid, bid, bname) values (2, 7, 'Huun-Huur-Tu');
insert into favorites (uid, bid, bname) values (2, 3, 'Muddy Waters');
insert into favorites (uid, bid, bname) values (3, 9, 'Battuvshin');
insert into favorites (uid, bid, bname) values (3, 10, 'Sade');
insert into favorites (uid, bid, bname) values (3, 11, 'Tchaikovsky');

--

select * from favorites;
select * from band_styles;

select distinct N.bname from band_styles N where N.sgname in
(select S.sgname from band_styles S, favorites F where F.bname = S.bname);

--
select * from favorites;
select * from band_styles;
select * from sub_genre;


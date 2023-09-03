-- initialize database
-- create database CSC315Lab2;
use CSC315Lab2;

create table Suppliers(
	sid INTEGER,
    sname CHAR(30),
    address CHAR(30),
    PRIMARY KEY (sid)
);

create table Parts(
	pid INTEGER,
    pname CHAR(30),
    color CHAR(30),
	PRIMARY KEY (pid)

);

create table Catalog(
	sid INTEGER,
    pid INTEGER,
    cost DOUBLE(10, 2),
    FOREIGN KEY (sid) REFERENCES Suppliers(sid),
	FOREIGN KEY (pid) REFERENCES Parts(pid)
);

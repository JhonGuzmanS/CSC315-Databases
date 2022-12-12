create database StudentInfo;
use StudentInfo;

create table Students(
	sid INTEGER AUTO_INCREMENT,
    sfirst CHAR(30) NOT NULL,
    slast CHAR(30) NOT NULL,
    syear ENUM('FRES', 'SOPH', 'JUN', 'SEN') NOT NULL,
    sgrade INTEGER NOT NULL,
    PRIMARY KEY (sid)
) AUTO_INCREMENT=1000;

create table Advisors(
	aid INTEGER AUTO_INCREMENT,
    afirst CHAR(30) NOT NULL,
    alast CHAR(30) NOT NULL,
    PRIMARY KEY (aid)
) AUTO_INCREMENT=1;

create table Classes(
	cid INTEGER AUTO_INCREMENT,
    cname CHAR(30) NOT NULL,
    csubject CHAR(30) NOT NULL,
    PRIMARY KEY (cid)
) AUTO_INCREMENT=100;

create table Advises(
	sid INTEGER,
    aid INTEGER,
    FOREIGN KEY (sid) REFERENCES Students(sid),
    FOREIGN KEY (aid) REFERENCES Advisors(aid)
);

create table ClassTaken(
	sid INTEGER,
    cid INTEGER,
    grade INTEGER,
    FOREIGN KEY (sid) REFERENCES Students(sid),
    FOREIGN KEY (cid) REFERENCES Classes(cid)
);

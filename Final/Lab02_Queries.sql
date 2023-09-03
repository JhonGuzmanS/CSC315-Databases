-- sample data
insert into suppliers (sid, sname, address) values (001, 'Supplier_01', 'Address 123');
insert into suppliers (sid, sname, address) values (002, 'Supplier_02', 'Address 535');
insert into suppliers (sid, sname, address) values (003, 'Supplier_03', 'Address 952');
insert into suppliers (sid, sname, address) values (004, 'Acme Widget Suppliers', 'Address 164');

insert into parts (pid, pname, color) values (81, 'Part_01', 'red');
insert into parts (pid, pname, color) values (73, 'Part_04', 'red');
insert into parts (pid, pname, color) values (49, 'Part_05', 'red');
insert into parts (pid, pname, color) values (50, 'Part_06', 'yellow');


insert into catalog (sid, pid, cost) values (001, 49, 85);
insert into catalog (sid, pid, cost) values (001, 73, 70);
insert into catalog (sid, pid, cost) values (001, 81, 59);
insert into catalog (sid, pid, cost) values (001, 50, 67);
insert into catalog (sid, pid, cost) values (002, 81, 65);
insert into catalog (sid, pid, cost) values (003, 50, 89);
insert into catalog (sid, pid, cost) values (003, 81, 59);



insert into parts (pid, pname, color) values (65, 'Part_02', 'blue');
insert into parts (pid, pname, color) values (55, 'Part_03', 'green');

insert into catalog (sid, pid, cost) values (003, 65, 59);
insert into catalog (sid, pid, cost) values (002, 65, 55);
insert into catalog (sid, pid, cost) values (003, 49, 88);
insert into catalog (sid, pid, cost) values (004, 55, 59);
insert into catalog (sid, pid, cost) values (004, 81, 64);

-- 1
select distinct pname from parts cross join catalog where catalog.pid = parts.pid;

-- 2
select S.sname from suppliers S where not exists(
select P.pid from parts P where not exists(
select C.pid from catalog C where C.pid=P.pid and C.sid=S.sid));

-- 3? - unsure how to search whether a part is unique
select S.sname from suppliers S where S.sid in(
select C.sid from catalog C where C.pid in(
select P.pid from parts P where P.color='red' having count(C.pid) >= 1));

-- 4? - unsure how to check whether said part is in other suppliers
select P.pid from parts P where P.pid in(
select C.pid from catalog C where C.sid in(
select S.sid from suppliers S where S.sname='Acme Widget Suppliers' and C.pid not in(
select S1.sid from suppliers S1 where S1.sid=C.sid and C.pid=P.pid))) ;

-- 7 
select S.sname from suppliers S where S.sid not in(
select C.sid from catalog C where C.pid not in(
select P.pid from parts P where P.color = all (select P1.color from parts P1 where P1.color='red')));

-- 8 
select S.sname from suppliers S, catalog C1, parts P1, catalog C2, parts P2 where 
S.sid=C1.sid and C1.pid=P1.pid and S.sid=C2.sid and C2.pid=P2.pid and P1.color='red' and P2.color='green';

-- 9
select distinct S.sname from suppliers S, catalog C, parts P where 
S.sid=C.sid and C.pid=P.pid and (P.color='red' or P.color='green');

-- 10
select S.sname from catalog C, suppliers S, parts P where S.sid=C.sid and P.pid=C.pid and P.color='green' union 
select count(C1.sid) from catalog C1, suppliers S1, parts P1 where S1.sid=C1.sid and P1.pid=C1.pid;

-- 11

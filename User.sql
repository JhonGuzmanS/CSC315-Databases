use StudentInfo;

create role 'principal', 'advisor', 'staff';
-- grant SELECT on ViewStudent to 'staff';
grant select on studentinfo to 'staff';
grant all on studentinfo to 'principal';
grant insert, update on studentinfo.students to 'advisor';

create user 'John'@'localhost';
grant 'staff' to 'John'@'localhost';

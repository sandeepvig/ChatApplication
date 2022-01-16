create schema chatapp;

create user chatapp_user_rw password 'chatapp_user_rw_pwd';
create role chatapp_role_rw;
grant chatapp_role_rw to chatapp_user_rw;

grant all on schema chatapp to chatapp_role_rw;

---drop table chatapp.users;

create table chatapp.users
(
	login varchar(250),
	fname varchar(250),
	lname varchar(250),
	passwd varchar(250)
);
grant select, insert, update, delete on chatapp.users to chatapp_role_rw;


insert into chatapp.users
(login, fname, lname, passwd)
values
('svig', 'Sandeep', 'Vig', 'vig');

insert into chatapp.users
(login, fname, lname, passwd)
values
('atiwari', 'Abhishek', 'Tiwari', 'tiwari');

insert into chatapp.users
(login, fname, lname, passwd)
values
('vvirmani', 'Vineet', 'Virmani', 'virmani');

insert into chatapp.users
(login, fname, lname, passwd)
values
('achaudhary', 'Ajay', 'Chaudhary', 'chaudhary');

insert into chatapp.users
(login, fname, lname, passwd)
values
('agupta', 'Amit', 'Gupta', 'gupta');


commit;

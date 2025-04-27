create table user (
    id integer primary key autoincrement,
    first_name varchar(255) default 'John',
    last_name varchar(255) default 'Doe',
    email text not null,
    phone varchar(50),
    password varchar(50),
    date_created timestamp default current_timestamp,
    date_modified timestamp default current_timestamp
);

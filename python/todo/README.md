This is just a simple script to play around with.  I was watching a udemy course (The Python Mega Course: Learn Python in 60 Days with 20 Apps) starting at the beginning and found that part very basic.  So I started to create my own version.  

I could imagin this being a simple cli script which stores information in a DB (initially sqlite).  In the future posibly have a simple API and web interface running in a docker container with the cli connecting to the api to pull/push informaiton. 


1. todo cli
  * Argument based
  * Storage - Database
  * Don't think I'll do it as a class yet
  * May end up using a `.todo` file for settings later on.
  * Will leave arguments as they are for now.  May try adding named arguments with the positional arguments later.


This version of the script will use a sqlite3 database named `todo.db` and a table named `todo_list`.  

`todo_list` definition:
```
create table todo_list (
    _id integer primary key autoincrement,
    todo text not null,
    date_added datatime default current_timestamp
);```

"""
This is just a simple script that I started after starting to watch the first
few days in the udemy course "The Python Mega Course: Learn Python in 60 Days
with 20 Apps".

I decided to try creating a todo list app myself first rather
than watching what the course instructor does.  Also didn't want to do a menu
based script and rather an argument based script.

This will run off of a sqlite database todo.db.  The table definition is:

create table todo_list (
    _id integer primary key autoincrement,
    todo text not null,
    date_added datatime default current_timestamp
);

"""

import sqlite3
from   argparse import ArgumentParser, REMAINDER

# Global constants
DBFILE = 'todo.db'

def db_query(query: str, query_data: list = []):
    dbcon = sqlite3.connect(DBFILE)

    results = dbcon.execute(query, query_data)
    return_data = results.fetchall()

    dbcon.commit()
    dbcon.close()

    return return_data[0]

def todo_add(todo_item: str):
    list_query = f"INSERT INTO todo_list('todo') VALUES('{todo_item}')"
    db_query(list_query)

def todo_remove(todo_item: str):
    print(f"remove: {todo_item}")

def todo_list(todo_item: str):
    list_query = "SELECT todo from todo_list"
    todo_items = db_query(list_query)
    print(todo_items)

def main():
    actions = {"add": todo_add,
               "remove": todo_remove,
               "list": todo_list}

    parser = ArgumentParser()
    parser.add_argument("action", 
                        choices=["add", "remove", "list"], 
                        nargs='?',
                        default="list",
                        help="Default is 'list'")
    parser.add_argument("todo_item", 
                        nargs=REMAINDER,
                        help="Item to add or remove")
    args = parser.parse_args()

    actions[args.action](" ".join(args.todo_item))


if __name__ == '__main__':
    main()

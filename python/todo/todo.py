from argparse import ArgumentParser, REMAINDER

def todo_add(todo_item: str):
    print(f"add: {todo_item}")

def todo_remove(todo_item: str):
    print(f"remove: {todo_item}")

def todo_list(todo_item: str):
    print(f"list: {todo_item}")

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

class TodoList:
    """This is a basic class for a todo list"""
    def __init__(self):
        self.todo_items = list()

    def add_item(self, item: str):
        self.todo_items.append(item)

    def remove_item(self, item_index: int):
        if item_index > len(self.todo_items) or item_index < 1:
            return

        self.todo_items.remove(item_index - 1)
        return true

    def __str__(self):
        return "\n".join([ f"{i[0] + 1}. {i[1]}" for i in enumerate(self.todo_items) ])


def main():
    my_todo_list = TodoList()
    prompt_user = "Add, remove, list or exit. What do to: "
    prompt_user_item = "Which todo item: "
    user_answer = ""
    user_item_answer = ""

    while (user_answer.lower() != "exit"):
        user_answer = input(prompt_user)
        if user_answer.lower() == "add":
            my_todo_list.add_item(input(prompt_user_item))
        elif user_answer.lower() == "remove":
            my_todo_list.remove_item(int(input(prompt_user_item)))
        elif user_answer.lower() == "list":
            print(my_todo_list)
        elif user_answer.lower() == "exit":
            print("Exiting...")
        else:
            print("Invalid option...")

if __name__ == "__main__":
    main()

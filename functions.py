FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a file containing a todos list
    and returning it"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes an element to a txt file list
    containing of todos"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "main":
    print(__name__)
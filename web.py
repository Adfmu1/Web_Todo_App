import streamlit as sl
import functions

todos = functions.get_todos()

def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


sl.title("To-do App")
sl.subheader("Oh boy its a todo app again")
sl.write("Todos:")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.rerun()


sl.text_input("", placeholder="Enter a todo", on_change=add_todo, key="new_todo")

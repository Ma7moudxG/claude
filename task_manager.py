tasks = []

def add_task(name):
    # BUG: This doesn't actually add the task to the list
    new_task = {"id": len(tasks), "name": name, "status": "pending"}
    print(f"Added {name}")

def list_tasks():
    for t in tasks:
        print(t)

def complete_task(id):
    # BUG: This will crash if the ID doesn't exist
    tasks[id]["status"] = "done"

add_task("Buy Milk")
list_tasks()

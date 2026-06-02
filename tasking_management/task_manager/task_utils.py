from .validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        task = {"title": title, "description": description, "due_date": due_date, "completed": False}
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Error: Invalid task details.")
    
def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Error: Invalid task index.")
    
def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks currently.")
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i}: {task['title']} (Due: {task['due_date']})")

def calculate_progress():
    if not tasks:
        return 0.0
    completed = len([t for t in tasks if t["completed"]])
    return (completed / len(tasks)) * 100
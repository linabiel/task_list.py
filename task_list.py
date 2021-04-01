tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# def list of uncompleted tasks

# input a list of tasks

# loop thorugh tasks and print uncompleted tasks

# Print a list of uncompleted tasks

# Print a list of completed tasks

# Print a list of all task descriptions

# Print a list of tasks where time_taken is at least a given time

# Print any task with a given description

def print_uncompleted_tasks(list_of_tasks): 
    uncompleted_tasks = []
    for task in list_of_tasks:
        if task['completed'] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

print(print_uncompleted_tasks(tasks))

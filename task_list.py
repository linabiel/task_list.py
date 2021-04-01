tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# Print a list of uncompleted tasks

# Print a list of completed tasks

# Print a list of all task descriptions

# Print a list of tasks where time_taken is at least a given time

# Print any task with a given description

# def print_uncompleted_tasks(list_of_tasks): 
#     uncompleted_tasks = []
#     for task in list_of_tasks:
#         if task['completed'] == False:
#             uncompleted_tasks.append(task)
#     return uncompleted_tasks

# print(print_uncompleted_tasks(tasks))


def print_completed_tasks(list_of_tasks): 
    completed_tasks = []
    for task in list_of_tasks:
        if task['completed'] == True:
            completed_tasks.append(task)
    return completed_tasks

print(print_completed_tasks(tasks))

def task_description_list(list_of_tasks):
    task_descriptions = []
    for tasks in list_of_tasks:
        task_descriptions.append(tasks['description'])
        
    return task_descriptions

print(task_description_list(tasks))

def print_task_within_time(list_of_tasks):
    task_description_list = []
    for task in list_of_tasks:
        if task['time_taken'] >= 10:
            task_description_list.append(task)
    return task_description_list

print(task_description_list(tasks))

def print_task_with_description(list_of_tasks):
    for task in list_of_tasks:
        if task['description'] == "Wash Dishes":
            return task

print(task_description_list(tasks))
        
    

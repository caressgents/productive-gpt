# ai/scheduler.py

from datetime import datetime, timedelta

def schedule_tasks(tasks):
    # This is a very basic scheduling algorithm that schedules tasks based on their priority and deadline.
    # More advanced scheduling could involve machine learning algorithms to predict the best times for different types of tasks.
    tasks.sort(key=lambda task: (task['priority'], task['deadline']))
    now = datetime.now()
    schedule = []
    for task in tasks:
        start_time = now
        end_time = now + timedelta(hours=task['duration'])
        schedule.append({
            'task': task['name'],
            'start_time': start_time,
            'end_time': end_time,
        })
        now = end_time
    return schedule

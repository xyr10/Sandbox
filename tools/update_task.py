import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

TASK_UPDATES = [
    {
        "summary": "Wash dishes",
        "description": "Don't go to bed without doing this first"
    },
    {
        "summary": "Brush teeth",
        "description": "Do this before going to bed"
    }
]
def update_task(summary, description):
    task_data = {
        "summary": summary,
        "description": description
    }
response = requests.put(BACKEND_URL, json=task_data)
    if response.status_code == 200:
        print("Task updated successfully")
    else:
        print("Something went wrong while updating task")

if __name__ == "__main__":
    for task in TASK_UPDATES:
        update_task(
                task.get("summary"),
                task.get("description")
        )
    print ("Task update complete.")


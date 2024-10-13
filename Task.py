from datetime import datetime, timedelta

class Task:
    def __init__(self, name: str, duration_in_hours: int):
        self.name = name
        self.duration = timedelta(hours=duration_in_hours)

    def can_complete_by(self, deadline: str) -> bool:
        """
        Check if the task can be completed before the deadline.
        """
        deadline_date = datetime.strptime(deadline, "%d/%m/%Y %H:%M")
        current_time = datetime.now()

        # Calculate the task completion time
        completion_time = current_time + self.duration

        # Compare completion time with the deadline
        return completion_time <= deadline_date

    def time_remaining(self, deadline: str) -> timedelta:
        """
        Calculate the time remaining until the deadline.
        """
        deadline_date = datetime.strptime(deadline, "%d/%m/%Y %H:%M")
        current_time = datetime.now()

        return deadline_date - current_time

    def completion_time(self) -> datetime:
        """
        Calculate when the task will be completed.
        """
        current_time = datetime.now()
        return current_time + self.duration

def main():
    task_name = input("Enter the task name: ")
    duration = int(input("Enter the duration of the task in hours: "))
    deadline = input("Enter the deadline (DD/MM/YYYY HH:MM): ")

    task = Task(task_name, duration)

    # Check if the task can be completed on time
    if task.can_complete_by(deadline):
        print(f"The task '{task_name}' can be completed before the deadline.")
        print(f"Completion time: {task.completion_time().strftime('%d/%m/%Y %H:%M')}")
    else:
        print(f"The task '{task_name}' cannot be completed before the deadline.")
        print(f"Time remaining: {task.time_remaining(deadline)}")

if __name__ == "__main__":
    main()

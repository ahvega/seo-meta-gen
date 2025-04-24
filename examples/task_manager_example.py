from seo_meta_gen.task_manager import UBOSTaskManager

def main():
    # Initialize the task manager
    task_manager = UBOSTaskManager()

    # Create a new task
    task = task_manager.create_task(
        title="Implement Database Write-Back",
        description="Add functionality to write generated metadata back to WordPress",
        priority="high",
        category="development"
    )
    print(f"Created task: {task['title']}")

    # Add a comment to the task
    comment = task_manager.add_comment(
        task_id=task['id'],
        comment="Starting implementation of database write-back functionality"
    )
    print(f"Added comment: {comment['comment']}")

    # Update task status
    updated_task = task_manager.update_task(
        task_id=task['id'],
        updates={"status": "in_progress"}
    )
    print(f"Updated task status to: {updated_task['status']}")

    # List all tasks
    tasks = task_manager.list_tasks()
    print("\nAll tasks:")
    for t in tasks:
        print(f"- {t['title']} ({t['status']})")

if __name__ == "__main__":
    main() 
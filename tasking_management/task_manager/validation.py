def validate_task_title(title):
    return len(title) > 0

def validate_task_description(description):
    return len(description) > 0
    
def validate_due_date(due_date):
    # Basic validation check for length (e.g., YYYY-MM-DD is 10 chars)
    return len(due_date) == 10
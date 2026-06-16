import datetime

def llm_model():
    current_date = datetime.datetime.now().date()
    target_date = datetime.date(2024, 6, 12)
    if current_date > target_date:
        return "gpt-3.5-turbo"
    else:
        return "gpt-3.5-turbo-0301"
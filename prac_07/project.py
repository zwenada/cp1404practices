import datetime

class Project:
    def __init__(self, name, start_date_str, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name} (Start Date: {self.start_date.strftime('%d/%m/%Y')}), Priority: {self.priority}, Cost: ${self.cost_estimate:.2f}, Completion: {self.completion_percentage}%"

    def is_completed(self):
        return self.completion_percentage == 100

    def is_high_priority(self):
        return self.priority >= 8

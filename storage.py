'''import csv
from datetime import datetime

def save_to_csv(name, role, questions, answers, scores):
    filename = "candidate_results.csv"
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        for q, a, s in zip(questions, answers, scores):
            writer.writerow([datetime.now(), name, role, q, a, s])'''

import csv
from datetime import datetime

def save_to_csv(name, role, questions, answers, scores):
    filename = "candidate_results.csv"
    try:
        file_exists = os.path.isfile(filename)
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Timestamp", "Candidate", "Role", "Question", "Answer", "Score"])
            for q, a, s in zip(questions, answers, scores):
                writer.writerow([datetime.now(), name, role, q, a, s])
    except PermissionError:
        print("❌ Cannot write to CSV. Please close the file if it's open.")

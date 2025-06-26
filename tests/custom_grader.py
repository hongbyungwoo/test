import json

# Your custom grading logic
results = [
    {
        "name": "Functionality Test",
        "output": "Passed all edge cases",
        "score": 0.75,
        "max_score": 1.0
    },
    {
        "name": "Style Check",
        "output": "Minor formatting issues",
        "score": 0.5,
        "max_score": 1.0
    },
    {
        "name": "Bonus Question",
        "output": "Excellent work!",
        "score": 1.0,
        "max_score": 1.0
    }
]

# Save the results
with open("results.json", "w") as f:
    json.dump(results, f, indent=2)

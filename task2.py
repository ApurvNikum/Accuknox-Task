import requests
import numpy as np
import matplotlib.pyplot as plt

#We Fetch the data from an API
response = requests.get('http://live-test-scores.herokuapp.com/scores')
test_scores_data = response.json()

# Scores are extracted from data which was in JSON Format
scores = [student['score'] for student in test_scores_data]

# Calculating average score
average_score = np.mean(scores)*100

# Visualization
plt.bar(range(len(scores)), scores)
plt.xlabel('Student')
plt.ylabel('Score')
plt.title('Test Scores Distribution')
plt.show()

print(f'Average score: {average_score}')

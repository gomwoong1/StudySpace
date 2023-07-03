file = open("data/answers.csv", "r")
lines = file.readlines()
file.close()

def get_summary():
  num_questions = 0
  num_students = 0
  avg_score = 0
  best_score = 0

  lines.reverse()
  answer = str(lines.pop()).replace(",", "").rstrip().lower()
  num_questions = len(answer)

  while len(lines) != 0:
    val = str(lines.pop()).replace(",", "").rstrip().lower()
    num_students += 1
    score = 0

    for i, j in zip(answer, val):
      if i == j:
        score += 4

    avg_score += score

    if score > best_score:
      best_score = score

  avg_score /= num_students
  return (num_questions, num_students, avg_score, best_score)

print(get_summary())
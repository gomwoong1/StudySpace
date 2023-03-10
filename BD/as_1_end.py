def get_summary(filename):
  num_questions = 0
  num_students = 0
  total_score = 0
  best_score = 0

  file = open(filename, "r")
  lines = file.readlines()
  file.close()
  
  lines = [ res.rstrip().lower().split(",") for res in lines ]

  lines.reverse()
  answer = lines.pop()
  num_questions = len(answer)
  num_students = len(lines)

  for res in lines:
    sum = 0
    for i, j in zip(answer, res):
      if i == j:
        sum +=4

    total_score += sum
    
    if sum > best_score:
      best_score = sum

  return (num_questions, num_students, total_score, best_score)
  
num_q, num_s, total, best = get_summary("data/answers.csv")

print(f"# of questions: {num_q}")
print(f"# of students: {num_s}")
print(f"total score: {total}")
print(f"best score: {best}")
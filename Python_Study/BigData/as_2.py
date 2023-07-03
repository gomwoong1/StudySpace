def get_score_board(filename):
  file = open(filename, "r")
  lines = file.readlines()
  file.close()

  # 2D answer list of students
  answers = []

  # Preprocessing input data
  for line in lines:
    answers.append([i.strip() for i in line.lower().split(',')])

  # Pop the correct answers
  c_answers = answers.pop(0)

  # 2D score list of students
  score_board = []

  # using index-based for loop
  for i in range(len(answers)):
    score_board.append([])
    for j in range(len(c_answers)):
      if answers[i][j] == c_answers[j]:
        score_board[i].append(1)
      else:
        score_board[i].append(0)

  return score_board

def get_question_scores(score_board):
  results = []

  results = [ 0 for i in range(len(s_board[0])) ]
  for res in score_board:
    for i in range(len(s_board[0])):
      results[i] += res[i]

  return results

s_board = get_score_board("data/answers.csv")
q_scores = get_question_scores(s_board)

if s_board:
  print(f"# of questions: {len(s_board[0])}")
  print(f"# of students: {len(s_board)}")
  print(f"total score: {sum([sum(s) for s in s_board]) * 4}")
  print(f"best score: {max([sum(s) for s in s_board]) * 4}")

for i, score in enumerate(q_scores):
    print(f"Q.{i:02d} : {score}")
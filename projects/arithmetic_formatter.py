# format the math problems, return the answer if true is passed as an optional argument


def arithmetic_arranger(problems, displayedAnswer=False):
  array_probs = [problem.split(" ") for problem in problems]
  return array_probs

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# format the math problems, return the answer if true is passed as an optional argument
import operator
ops = {"+": operator.add, "-": operator.sub}

def arithmetic_arranger(problems, solver=False):
  top = ""
  bottom = ""
  lines = ""
  totals = ""
  for n in problems:
    fnumber = n.split()[0]
    operator = n.split()[1]
    snumber = n.split()[2]

    # get function total
    total = ops[operator](int(fnumber), int(snumber))
    #  get distance of longeset operator
    operator_distance = max(len(fnumber), len(snumber)) + 2

    # organizing line lengths
    snumber = operator + snumber.rjust(operator_distance - 1)
    top = top + fnumber.rjust(operator_distance) + (4 * " ")
    bottom = bottom + snumber + (4 * " ")
    lines = lines + len(snumber) * "_" + (4 * " ")
    totals = totals + str(total).rjust(operator_distance) + (4 * " ")

  print(top)
  print(bottom)
  print(lines)
  if solver:
    print(totals)

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

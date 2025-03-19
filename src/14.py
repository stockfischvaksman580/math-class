  import random
  
  def get_random_code():
      numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      operators = ["+", "-", "*", "/"]
      variables = ["x", "y", "z"]
      
      code = ""
      
      for i in range(random.randint(2, 3)):
          code += variables[random.randint(0, 2)] + " "
          
          if random.randint(0, 1) == 0:
              code += operators[random.randint(0, 3)] + " "
          
          code += str(numbers[random.randint(0, 9)]) + "\n"
      
      return code
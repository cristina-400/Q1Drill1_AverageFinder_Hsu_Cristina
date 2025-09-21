from pyscript import document, display

def adding_numbers(e): #e for event handling
  #Getting the values from the input fields
  num1 = float(document.getElementById("input1").value)
  num2 = float(document.getElementById("input2").value)
  result = (num1 + num2)/2
#Calculating the sum and displaying it in the output field
  display(result, target="output2") 
  if result > 75:
    display ("You passed!", target="output2")
  else:
    display ("You failed!", target="output2")

import re

alpha = "A9BC0DEF1GHI2JKL3MN4OPQ5RS6TUV7WXY8Z"


def input_sent(help_text):
  
  """
  this function prompt the user and do input validation by making sure the input only contain letters and number.
  """
  
  sent = str(input(help_text)).upper()
  check = re.findall("[^A9BC0DEF 1GHI2JKL3MN4OPQ5RS6TUV7WXY8Z]", sent)
  if check:
    print("\ninput can only contain number and letter\n")
    input_sent(help_text)
  else:
    return sent
    


def input_step(help_text):
  
  """
  this function prompt the user and do input validation by making sure the input is an integer.
  """
  
  step = input(help_text)
  try:
    step = int(step)
    return step
  except:
    print("\nonly numbers are allow\n")
    input_step(help_text)





def encrypt():
  
  """
  this function encrypt the input text using the ceaser cipher
  """
  
  sent = input_sent("what do you want to encrypt: ")
  step = input_step("Enter your caeser step: ")
  secret_sent = "" 
  
  
  for x in sent:
    if x != " ":
      old_index = alpha.find(x)
      new_index = (old_index + step) % len(alpha)
      y = alpha[new_index]
      secret_sent += y
    else:
      secret_sent += x
    
  print("\n", secret_sent, "\n")





def decrypt():
  
  """
  this function decrypt the secret_text using the ceaser cipher
  """
  
  sent = input_sent("what do you want to decrypt: ")
  step = input_step("Enter your caeser step: ")
  text = ""
  
  for x in sent:
    if x != " ":
      old_index = alpha.find(x)
      new_index = (old_index - step) % len(alpha)
      y = alpha[new_index]
      text += y
    else:
      text += x

  print("\n", text, "\n")


encrypt()
decrypt()
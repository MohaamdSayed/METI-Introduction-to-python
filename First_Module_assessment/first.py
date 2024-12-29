def write_introduction():
  name = "Mohamed Sayed"
  age = 27
  learning_goal = "to improve my pytghon programming skills and apply them effectively in testing and automation."

  #Create the introduction
  intro = f"""My Introduction:\n
  Hello, my name is {name}.
  I am {age} years old.
  In this course, I aim to learn: {learning_goal}.
  """

  #Print the introduction
  print(intro)


if __name__ == "__main__":
  write_introduction()

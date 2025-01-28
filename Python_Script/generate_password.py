import random
import string

def generate_password(length=16):
  """Generates a random password of the specified length.

  Args:
    length: The desired length of the password.

  Returns:
    A randomly generated string of characters.
  """

  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password

if __name__ == "__main__":
  password = generate_password()
  print(password)


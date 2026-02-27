from array_stack_student import ArrayStack

def reverse_file(input_filename, output_filename):
  """Overwrite given file with its contents line-by-line reversed.
     Use with open(.) construct to read and write files as provided.
     Think about how to use ArrayStack to help you.
     You cannot use other data structures like Python List to complete this question.
  """
  stack = ArrayStack()

  with open(input_filename, 'r') as F:
    for line in F:
      stack.push(line)

  # now we overwrite with contents in LIFO order
  with open(output_filename, 'w') as F:
    while not stack.is_empty():
        line = stack.pop()
        F.write(line)

if __name__ == '__main__':
  reverse_file('/Users/erdem/Documents/ds/lec5/DSSyllabus.txt', 'DSSyllabus_reverse.txt')

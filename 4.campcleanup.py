''' Initialize global variable'''
OUTPUT = 0

''' Functions '''
def checkContain(pairs):

  elf1a, elf1b = map(int, pairs[0].split('-'))
  elf2a, elf2b = map(int, pairs[1].split('-'))

  if (elf1a >= elf2a and elf1b <= elf2b) or (elf2a >= elf1a and elf2b <= elf1b): # if either elf is within range
    print(OUTPUT)
    return 1
  
  return 0

def checkStop(line):

  if line == 'stop':
    print(OUTPUT)
    return True
  
  return False

''' MAIN FUNCTION '''
while True:
  try:
    line = input()

    if checkStop(line) == False:

      pairs = line.split(',')
      
      OUTPUT += checkContain(pairs)
    
    else:
      break

  except EOFError:
    break
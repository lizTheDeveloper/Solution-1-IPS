def k_backspace(inputString):
	stack = []
	
	for element in inputString:
	  if element == "<":
	    # remove the last element from the stack
	    stack.pop(-1) ## for the stretch:
	    # pull element out of stack
	    # capitalize
	    # append element to stack 
	  else: 
	    stack.append(element)
	
	return "".join(stack)

# don't forget to actually call your answer's function!
testInput = 'a^bc^'
actualOutput = k_backspace(testInput)
print(actualOutput)
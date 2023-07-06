def isValid(s):

        stack = []
        
        p = {'(': ')', '[': ']', '{': '}'}
        
        for i in s:
            if i in '([{':
                stack.append(i)

                print(stack, 's')
                print(stack.pop(), 'pop')
                print(stack, 's2')

                stack.append(i)
                print (p[stack.pop()], 'p')

                print(i, 'i')
                stack.append(i)
                
            elif len(stack) ==0 or i != p[stack.pop()]:
                
                return False

        return len(stack)==0

s = "()[]{}[{}]"
print(isValid(s))
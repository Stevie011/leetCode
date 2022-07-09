class Solution:
    def isValid(self, s: str) -> bool:
        #dict lookup style
        stack = []
        lookup = {")":"(","}":"{","]":"["}
        #loop thru input str
        for i in s:
            #we know s is only paren chars, so if its not in values it must be in keys
            if i in lookup.values():
                stack.append(i)
            # if there's something on the stack (if stack) and the current iteration matches whatevers on top of the stack
            elif stack and lookup[i] == stack[-1]:
                #take off whatevers on top
                stack.pop()
            else:
                #if it can't be matched its def false
                return False
        #check if stack is empty (if not, some things haven't been matched)
        return stack == []
        
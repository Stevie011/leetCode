class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #name for answer list specced in question
        answer =[]
        #don't forget to shift range right by 1
        for i in range(1,n+1):
            #if i divis by both, append FizzBuzz
            if i%3==0 and i%5==0:
                answer.append("FizzBuzz")
            #if only divis by 3, just append fizz
            elif i%3==0:
                answer.append("Fizz")
            #only divis by 5, just append buzz
            elif i%5==0:
                answer.append("Buzz")
            #else just add i, but convert it to string
            else:
                answer.append(str(i))
        #spit it out
        return answer
                    
            
        
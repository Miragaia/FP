def reverseAux(partValue, partReversed):
   if partValue == 0:
      return partReversed   
      
   partValue=int(partValue)
   partReversed=str(partReversed)
   partReversed +=str(partValue%10)
   partValue = partValue//10
   return (reverseAux(partValue, partReversed))

def reverseDigits(value):
   return reverseAux(value, "")

print(reverseDigits(1234))
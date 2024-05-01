def check(string): 
  count=0
  for i in string: 
    if i in 'AEIOUaeiou': 
      count+=1
    if count>=5: 
      return 'accepted'
  return 'not accepted'

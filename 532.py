def check_permutation(str1, str2):
  n1=len(str1)
  n2=len(str2)
  if(n1!=n2):
    return False
  a=sorted(str1)
  str1=" ".join(a)
  b=sorted(str2)
  str2=" ".join(b)
  for i in range(0, n1, 1):
    if(str1[i] != str2[i]):
      return False
  return True

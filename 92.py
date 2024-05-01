def is_undulating(n):
  if len(n) < 3:
    return False
  for i in range(2, len(n)):
    if n[i-2] != n[i]:
      return False
  return True

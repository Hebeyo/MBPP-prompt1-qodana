def n_common_words(text,n):
  from collections import Counter
  words = text.split()
  n_common_words= Counter(words).most_common(n)
  return list(n_common_words)

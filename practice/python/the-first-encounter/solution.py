def string_to_number_mapping(s: str) -> dict:
  d={}
  for i,v in enumerate(s):
    if v in d:
      continue
    else:
      d[v]=i
  return d

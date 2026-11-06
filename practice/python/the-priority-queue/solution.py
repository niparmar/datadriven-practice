def sort_by_multiple_keys(records: list, keys: list) -> list:
  sorted_list = sorted(records, key = lambda x : (x[keys[0]],x[keys[-1]]))
  return sorted_list

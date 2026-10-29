def max_depth(root) -> int:
  if root is None:
    return 0
  left_depth = max_depth(root.get("left"))
  right_depth = max_depth(root.get("right"))
  return max(left_depth,right_depth) + 1


  #return

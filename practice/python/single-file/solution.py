def flatten(feed: list) -> list:
   res = []
   for i in feed:
     if isinstance(i,list):
       res.extend(flatten(i))
     else:
        res.append(i)
   return res   

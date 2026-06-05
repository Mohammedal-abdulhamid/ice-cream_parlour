
def classify_tub(tub):
  tub["status"] = ""
  capacity= tub["capacity"]
  exixting_litres= tub["litres"]
  percentage = (exixting_litres / capacity) * 100
  percentage_form = f'{percentage}%'

  if percentage > 70 :
   tub["status"] = "ok"
  
  return tub


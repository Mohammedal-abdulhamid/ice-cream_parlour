
def classify_tub(tub):
  modified_tub = tub.copy()
  modified_tub["status"] = ""
  capacity= modified_tub["capacity"]
  exixting_litres= modified_tub["litres"]
  percentage = (exixting_litres / capacity) * 100
  percentage_form = f'{percentage}%'

  if percentage > 70 :
   modified_tub["status"] = "ok"
  elif 70 >= percentage > 25:
   modified_tub["status"] = "low"
  else:
    modified_tub["status"] = "reorder"
  
  return modified_tub


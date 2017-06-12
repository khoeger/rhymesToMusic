"""
  Given a dictionary as input, how do we calculate the percentages
  of incidence of each key?
  - Add up the key values
  - Percentage is value/sum of values
"""

def sumDictValues(dictionary):
  """
    Total sum of the values in the dictionary
  """
  result = 0
  for key in dictionary.keys():
      # Leaves out the rests when run through dictionary
      if key != None:
           result += dictionary[key]
  return(result)

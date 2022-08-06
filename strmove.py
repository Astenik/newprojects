def strmove(name:str, count:int):
          ''' this function returns name 
          string moved count units to the rigth.
          name is  string and is the first argument of the function.
          count is the integer ang is the second argument 
          of the function.'''
          if count >= len(name):
                return name 
          string = ''
          n = len(name) - count
          for ind in range(n, len(name)):
                 string += name[ind]
          for ind1 in range(n):
                  string += name[ind1]
          return string
print(strmove('tenikas', 2))

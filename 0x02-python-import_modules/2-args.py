#!/usr/bin/python3
import sys
if __name__ == "__main__":
  arg_c =len(sys.argv) -1
  if arg_c == 0:
    print("0 arguments.")
  elif arg_c == 1:
    print("1 argument:")
  else:
    print("{}:{}".format(i+1, sys.argv[i + 1]))
  for i in range(arg_c):
      print("{}: {}".format(i + 1, sys.argv[i + 1]))  
  

#!/usr/bin/python3
 # Daneil Ben


 def multiple_returns(sentence):
     """Returns the length of a string and its first character."""
     first = "None" if len( sentence) == 0 else sentence[0]
     new_tuple = (len(sentence), first)
     return new_tuple


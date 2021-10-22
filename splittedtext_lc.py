# using list comprehensions for texts

mysentence = 'Random fact I am a fan of jam'
words = mysentence.split()

print(words)

ending_m = [word for word in words if word[-1] == 'm']

print(ending_m)

def palindrome(n):
  flag=True
  for i in range(len(n)):
    if n[i]==n[len(n)-1-i]:
      flag=True
    else:
      flag=False
      break
  if flag == True:
    print("True")
  else:
    print("Flase")
n=input()
palindrome(n)

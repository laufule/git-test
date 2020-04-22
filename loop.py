# loops
# 1.while()
print("--- first loop begin ---")
num = 1
while num <= 5:
    print(num)
    num += 1

print("--- second loop begin ---")
active = True
while active:
    message = input("say something: ")
    if message == 'quit':
        active = False
    else:
        print("What you input is:\n\t" + message)


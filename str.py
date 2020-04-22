# str
str1 = "123654"
list1 = list(str1)
print("list1:")
print(list1)

str2 = "ab cd ef"
list2 = str2.split()
print("list2:")
print(list2)

str3 = "www.github.com"
list3 = str3.split('.')
print("list3:")
print(list3)

message = "wellcome to Beijing."
print(message.upper())
print(message.title())
print(message.lower())

first_name = "liu"
last_name = "fule"
age = 24
full_name = first_name + " " + last_name
message = " Hello "+full_name.title() + ". You are " + str(age) + "years old"
print(message)
print("rm spect:")
print(message.strip())

#lint feed
print("Language: \n\tPython\n\tC++\n\tJava")


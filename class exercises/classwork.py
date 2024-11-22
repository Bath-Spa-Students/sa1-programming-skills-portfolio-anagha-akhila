print("welcome to code-lab1")

print("my name is Anagha")
print("I am 18 years old")
print("My mother's name is Akhila")
print("my father's name is rajeev")
print("my favourite cartoon is bob l'eponge")
print("the name of my university is bath spa")
print("i like my university")
print("i like fries")
print("i study cc")
# i study creative computing
print("i am now in code lab")
# i am now in code lab class
print("i was in gis")
# i was in a school named global indian school
print("i enjoy coding")
print("my favourite color is blue")
#blue is my favourite color
""" blue is a beautiful color
it has many different shades """
print ("i enjoy playing valorant")
print(""" valorant has many characters""")
print("""my favourite characters are neon
      and deadlock""")
print("""i also enjoy playing roblox and 
      mortal kombat""")
#videogames i enjoy playing
print("""johnny johnny yes papa
      eating sugar no papa""")
print("""telling lies no papa
      open your mouth hahaha""")
#nursery rhyme

#VARIABLES
a = 9
b = ("anagha")
c = ("bathspa")
d = ("""hannah 
     banana""")
e=("music")
f=("roblox")
g=("game")
h=("valorant")
i=("game")
print(a)
print(b)

l = "anagha"
m = "hannah"
print (l,m)

color="pink"
print(type(color))

ab= str(3)
cd= float(3)
ef=int(3)

#Overwriting variables

#String Concatenation through variable
sign = "bathspa" + "university"
print (sign)

name = "TVR" + "Hospital"
print (name)

brand = "Apple " + "IPhone"
print (brand)

#String concat through print statement
print ("Hello" + "World")

#String concat through diff variables
a = "Hello"
b = "World"
c = a + " " + b
print (c)

#To get input from user
name = input ("Enter class_name : ")
print (name )

club = input ("Enter football club_name: ")
print (club )

color = input ("Enter color_name : ")
print (color )

#we have to mention (Type cast ) to get an integer/float value
age = int (input("Enter age"))
print (age)

#performing calculations
arya = 5
bran = 6
rob = (5+6)
print (rob)
#performing calculations

arya = 5
bran = 6
rob = (5+6)
print (rob)

print(50/2)
print(70*4) #for float
print(90//3) #for integer

# precedence BODMAS (Bracket, order, divison, multiplication, addition, subtraction)

print((4*6)/8 +(23+5))

#To write formula in multiple line we need back slash \

result = 6 * 2 + 4 * 6 + 7 \
         3 * 5 + 9 + 6 * 4

# end delimitter to remove new line, by default print will switch to another statement

name = "aNAGHA aKHILA"
print (name,end = " ")
print ("New Print Line message")

# \n and \t these are also known as escape sequences
print("\n will print on the next line")
print("\t this is tabbed in")


# displaying formatted output with f-string

name = "anagha"
print(f'my name is (anagha)')

word1 = "coding"
word2 = "is"
word3 = "cool"
print (word1, word2, 3)
#nested if
earning = int(input("Enter your earning per year"))
Work_experience = float (input("Enter your work experience"))

if earning >= 45000:
    if Work_Experience >= 2:
         print ("Eligible for loan")
    else :
         print("Sorry your work experience is less than 5 years")
else :
     print ("Sorry your earning is less than 50 K")

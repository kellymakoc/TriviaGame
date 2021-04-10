print("How well do you know about the NBA star (based on 2019 NBA)?")
print("You are only allowed to get 3 questions wrong. \nAre you ready?!!!!")
ready = input("Press enter to start the quiz. ")

count_right = 0
count_wrong = 0
limited_wrong = 3
out_of_limit = False

while count_wrong < limited_wrong:
    one = input("Who is well known for his 3 pointers? ")
    one.lower()
    if one.lower() == "stephen curry":
        print("Correct! Correct answer: Stephen Curry. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: Stephen Curry")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break   
                        
    two = input("Who is the centre for the Thunder?  ")
    two.lower()
    if two.lower() == "steven adams":
        print("Correct! Correct answer: Steven Adams. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: Steven Adams.")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break   
        
    three = input("Who is the power forward for the Raptors? ")
    three.lower() 
    if three.lower() == "serge ibaka":
        print("Correct! Correct answer: Serge Ibaka. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: Serge Ibaka.")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break
        
    four = input("Who got traded to the Raptors from the Spurs? ")
    four.lower()
    if four.lower() == "kawhi leonard":
        print("Correct! Correct answer: Kawhi Lenoard. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: Kawhi Lenoard.")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break
        
    five = input("Who is the first place in the west bound conference? ")
    five.lower()
    if five.lower() == "golden state warriors":
        print("Correct! Correct answer: Golden State Warriors. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: Golden State Warriors.")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break
        
    six = input("What is the name of the exciting rookie in the Utah Jazz? ")
    six.lower()
    if six.lower() == "donovan mitchell":
        print("Correct! Correct answer: Donovan Mitchell. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: Donovan Mitchell.")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break   
    seven = input("Who is the former Laker in Net? ")
    seven.lower()
    if seven.lower() == "d'angelo russell":
        print("Correct! Correct answer: D'Angelo Russell. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: D'Angelo Russell.")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break
        
    eight = input("How many years have Lebron James been playing in the NBA? ")
    if eight == "16":
        print("Correct! Correct answer: 16 years. Lebron James started playing in 2003. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: 16 years. Lebron James started playing in 2003.")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break   
    nine = input("Who is the head coach in Golden State Warrior? ")
    nine.lower()
    if nine.lower() == "steve kerr":
        print("Correct! Correct answer: Steve Kerr. Keep up the good work!")
        count_right += 1
    else:
        print("Incorrect!")
        count_wrong += 1
        print("This is wrong.Correct answer: Steve Kerr.")
        if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break   
    ten = input("Who is the point guard in Raptors? ")
    ten.lower()
    if ten.lower() == "kyle lowry":
        print("Correct! Correct answer: Kyle Lowry. Keep up the good work!")
        count_right += 1
        break
    else:
         print("Incorrect!")
         count_wrong += 1
         print("This is wrong.Correct answer: Kyle Lowery.")
         if count_wrong == 3:
            print("You fail the quiz :(. You got 3 questions wrong alredy.")
            break
list = [
        ('    /|  ***   *'),
        ('   / |  *    ***'),
        ('  /  |  ***   * '),
        (' /_| |    *   * '),
        ('   | |  ***     '),
        ('   | |          '),
        ('   | |          '),
        (' __| |__        '),
        ('|_______|       '),
        ]
def score ():
    print("You score ",(count_right/10)*100,"%")
score ()
score = (count_right/10)*100
if score < 50:
    print("You got ",count_right," right. You got ",count_wrong,"wrong.")
    print("It's ok. Try again next time.")
if score > 49 and score < 70:
    print("You got ",count_right," right. You got ",count_wrong,"wrong.")
    print("You did a good job.")
elif score < 90 and score > 70:
    print("You got ",count_right," right. You got ",count_wrong,"wrong.")
    print("You are amazing!! You know a lot about the NBA stars.")
elif score >= 90:
    print("You got ",count_right," right. You got ",count_wrong,"wrong.")
    print("OMGGG!!! You are fantastic. You know everything about the NBA stars.")
    for row in list:
        print(row)



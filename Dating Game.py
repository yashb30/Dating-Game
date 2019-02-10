all=()
short=()
funny=()
serious=()
LaVar=[]
Sharquisha=[]
LaVar=0
Sharquisha=0
q=input("what is your name")
qwerty={'LaVar':'funny','Sharquisha':'serious'} 
z=[LaVar,Sharquisha]
class attributes(object):
    def __init__(self, height):
        self.height=height
class funny(attributes):
    LaVar=attributes(funny)
class serious(attributes):
    Sharquisha=attributes(serious)
print(q,", there are many options, now we will go through a series of questions, and the first candidate to reach 4 is your match!")
lil=input(q + " do you like tall people or short people?")
if lil=="tall":
    LaVar+=1
if lil=="short":
    Sharquisha+=1
print(str(Sharquisha) + " is Sharquisha's score!")
print(str(LaVar) + " is LaVar's score!")
lili=input(q + " do you like dogs or cats?")
if lili=="dogs":
    LaVar=+1
if lili=="cats":
    Sharquisha+=1
print(str(Sharquisha) + " is Sharquisha's score!")
print(str(LaVar) + " is LaVar's score!")
lilil=input(q + " are you athletic or non-athletic?")
if lilil=="athletic":
    LaVar+=1
if lilil=="non-athletic":
    Sharquisha+=1
print(str(Sharquisha) + " is Sharquisha's score!")
print(str(LaVar) + " is LaVar's score!")
lilili=input(q + " do you beleive in love at first sight?")
if lilili=="yes":
    Sharquisha+=1
if lilili=="no":
    LaVar+=1
print(str(Sharquisha) + " is Sharquisha's score!")
print(str(LaVar) + " is LaVar's score!")
lilili=input(q + " are you extroverted or introverted?")
if lilili=="introverted":
    Sharquisha+=1
if lilili=="extroverted":
    LaVar+=1
print(str(Sharquisha) + " is Sharquisha's score!")
print(str(LaVar) + " is LaVar's score!")
lol=input(q + " do you like serious people or funny people?")
if lol=="serious":
    LaVar+=1
if lol=="funny":
    Sharquisha+=1
print(str(Sharquisha) + " is Sharquisha's score!")
print(str(LaVar) + " is LaVar's score!")
lolo=input(q + " do you like sports?")
if lolo=="yes":
    LaVar+=1
if lolo=="no":
    Sharquisha+=1
print(str(Sharquisha) + " is Sharquisha's score!")
print(str(LaVar) + " is LaVar's score!")
if LaVar>=4:
    print(q + " your match is LaVar! Have Fun!")
if Sharquisha>=4:
    print(q + " your match is Sharquisha! Have Fun!")
    

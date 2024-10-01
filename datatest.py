from logic import *
import logic

rain = Symbol("Rain")
heavyTraffic = Symbol("HeavyTraffic")
earlyMeeting = Symbol("EarlyMeeting")
strike = Symbol("Strike")
wfh = Symbol("WFH")
drive = Symbol("Drive")
publicTransport = Symbol("PublicTransport")

knowledge = {(Implication(Or(rain,earlyMeeting),wfh)), (Implication(And(Not(rain),Not(heavyTraffic)),drive)), Implication(And(Not(strike),Not(rain)),publicTransport)}

#this function create a model using your conditions and knowledge then suggest what you should do
def model(knowledge,conditions):
    #print("How should i prepare to work ?")
    for x in knowledge:
        mod = And(x,conditions)
        #print(conditions)
        if model_check(mod, wfh):
            print("You should work from home")
        if model_check(mod, drive):
            print("You should drive to work")    
        if model_check(mod, publicTransport):
            print("You should take public transports")
    
model(knowledge,And(Not(rain),Not(strike)))
print('\n Scenario 1 : \n')
model(knowledge,And((rain),(heavyTraffic)))

print('\n Scenario 2 : \n')
model(knowledge,And((strike),Not((rain))))
#We miss trafic knowledge to know the answer
#As priority is not defined even working from is not suggested

print('\n Scenario 3 : \n')
model(knowledge,And(Not((rain)),Not((heavyTraffic)),Not(strike)))
#Both option respects conditions, so they are both given.

#print(knowledge.formula())
"""
    Scenario 1: It’s raining, and there’s heavy traffic. Check if the assistant suggests working from home or driving.
    Scenario 2: There’s a public transport strike, and it’s not raining. Check if the assistant still suggests taking public transport.
    Scenario 3: There’s no rain, traffic is light, and there’s no strike. Check if the assistant suggests driving or taking public transport.
"""
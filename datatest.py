from logic import *
import logic

rain = Symbol("Rain")
heavyTraffic = Symbol("HeavyTraffic")
earlyMeeting = Symbol("EarlyMeeting")
strike = Symbol("Strike")
wfh = Symbol("WFH")
drive = Symbol("Drive")
publicTransport = Symbol("PublicTransport")
appointment = Symbol("Appointment")
roadConstruction = Symbol("RoadConstruction")

#Give the good way of moving depending on conditions
knowledge = {(Implication(Or(rain,earlyMeeting),wfh)),
            (Implication(And(Not(rain),Not(heavyTraffic)),drive)),
            Implication(And(Not(strike),Not(rain)),publicTransport),
            Implication(appointment,drive),
            Implication(roadConstruction,Not(drive))}

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

print('\n Scenario 4 : \n')
model(knowledge,And(rain,heavyTraffic,appointment))
#To make something really logic we should make a priority depending on the customer needs
#This version of the program is easy to adapt according to priority, we could also focus on time/comfort/envirronment/mixe

print('\n Scenario 5 : \n')
model(knowledge,roadConstruction)
#We could make deduction using hypothesis

#print(knowledge.formula())

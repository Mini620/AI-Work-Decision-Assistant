from logic import *
import logic

rain = Symbol("Rain")
heavyTraffic = Symbol("HeavyTraffic")
earlyMeeting = Symbol("EarlyMeeting")
strike = Symbol("Strike")
wfh = Symbol("WFH")
drive = Symbol("Drive")
publicTransport = Symbol("PublicTransport")

#knowledge = (Or(Implication(Or(rain,earlyMeeting)),wfh),(Implication(And(not(rain),not(earlyMeeting))),drive))
# If it's raining or there’s an early meeting, you should work from home.
# If it’s not raining and there’s no heavy traffic, you should drive.
# If there’s no strike and it’s not raining, you should take public transport.
knowledge = {(Implication(Or(rain,earlyMeeting),wfh)), (Implication(And(Not(rain),Not(heavyTraffic)),drive)), Implication(And(Not(strike),Not(rain)),publicTransport)}

def model(knowledge,conditions):
    return And(knowledge,conditions)


for x in knowledge:
    #test = model(x,And(Not(rain),earlyMeeting))
    #test = model(x,And(Not(rain),Not(heavyTraffic)))
    test = model(x,And(Not(rain),Not(strike)))
    print(test.formula())
    print("Should I work from home ? :",model_check(test, wfh))
    print("Should I drive ? :",model_check(test, drive))    
    print("Should I take public transports ? :",model_check(test, publicTransport))
    
#print(knowledge.formula())
#print(model_check(knowledge, rain))

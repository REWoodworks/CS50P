#talking about side effects, having seen that functions take inputs and produce outputs
#one output is a return value, but another output can be a side effect
#for example, printing to the console is a side effect 
#side effect is anything changed that is not a return value

emoticon = "v.v"
#definin a GLOBAL variable here


def main ():
    global emoticon
    # line 9 will allow us to modify global as a side effect of the function
    # global has to be declared before modifying the variable so python will actually mod it
    say("Is anyone there?")
    emoticon = ":D" 
    say("Oh, hi")
    

def say(phrase):
    print(phrase + " " + emoticon)
#function say has the side effect of printing to the console


# we see 2 side effects here
#1. printing to the console from the say function
#2. modifying the global variable emoticon  

# modifying a global var may not always be a good idea because it can lead to unexpected side effects, especially in larger programs where 
# it can be difficult to track changes to the global state.




main()


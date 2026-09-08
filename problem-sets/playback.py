#takes a fast talker and splits their words with ...

user_input=input("Whats the lesson today? ")

fast_talk = user_input.split()
normal_talk = "...".join(fast_talk)

print (normal_talk)
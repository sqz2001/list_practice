"""practice problem on page 42 says to make a list with at least three people I would want to
invite to dinner. Then use the list to print a message to each persson, inviting them to dinner
"""

#guestlist done with print statements and variables
guestlist = ["Catherine", "Adam Driver", "God"]
first_guest = guestlist[0]
print(f"{first_guest}, join me at our local Hooters")

second_guest = guestlist[1]
print(f"{second_guest}, my best friend and I are going to Hooters and u are 'the little guy in (her) mind'"
      f" so please come through")

third_guest = guestlist[2]
print(f"{third_guest}, I have so much beef with you. Let's duel it out at my local Hooters.")

#guestlist for generic invites, done with a For Loop
generic_list = ["Adam", "Eve", "Steve"]
for name in generic_list:
    print(f"{name}, Hi do you want to see something? Come to your local Hooters")


"""The next practice problem says to modify the list, replacing the name of the guest who can't make it with the name
of the new person you are inviting,
We will assume that God didn't want to show up because he knows me, Adam, Eve, and Steve all got beef with him
 and together we are too powerful and will fight him"""

#Modify list to replace God with Dog (this is a Behemoth reference)
guestlist[2] = "Dog"
third_guest = guestlist[2]
print(f"{third_guest}, you are such a dawg, join us at Hooters")


"""The next practice problem says to use a print statement to inform my guests that Hooters upgraded us to a larger table"""
for name in guestlist:
    print(f"{name}, Hooters has upgraded our table to the mega-milker station!")
for name in generic_list:
    print(f"{name}, Hooters has upgraded our table to the mega-milker station!")


"""The next practice problem says to add one new guest to the beginning of the list, one to the middle, and one to the end,
and then to resend invites out"""
#join guestlist with generic_list
joinedlist = guestlist + generic_list
joinedlist.insert(0, "Bill Nye")
joinedlist.insert(3, "Stacy's mom")
joinedlist.append("Joe Mama")

for name in joinedlist:
    print(f"{name}, last and final call for Hooters")
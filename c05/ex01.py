name = 'gsj'
age = 30
height = 187
weight = 160
eyes = 'brown'
teeth = 'white'
hair = 'black'

print("Let's talk about %s." % name)
print("He's %d cm tall." % height)
print("He's %d jin" % weight)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

print(round(1.7333))
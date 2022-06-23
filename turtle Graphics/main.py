# import turtle
#
# timmy = turtle.Turtle()
#
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
# print(timmy)
#
#
# my_screen= turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon",["pikachu","Squirte", "charmander"])
table.add_column("type",["Electric","Water", "Fire"])
print(table)


cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_a_car
avarage_passenger_per_car = passengers / cars_driven

# -------- Printing Calculated Values ---------
print ("There are", cars, "cars available")
print ("There are only ", drivers, " drivers available")
print ("There are ", cars_not_driven, " empty cars today")
print ('We can transport', car_pool_capacity, " passengers today")
print ('We can transport ', passengers, ' passengers today')
print ('We need to put about ',avarage_passenger_per_car)
print ("Author's height = ",74 * 2.54)
# Mistake to type variable names causes NameError: name 'car_pool_capacity' is not defined

####################################################
#  	PRINTING STRING WITH FORMAT SPECIFIER		   #
####################################################
print ("\n#########	PRINTING STRING WITH FORMAT SPECIFIER	##########")
my_age = 25 # not a lie
my_name = 'Sauvik Dolui'
my_weight = 65 # Kg
my_height = 174 # cm
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print ("Let's talk about %s.",my_name)
print ("He is %d cm tall.")
print ("He is %d kg heavy")
print ("Actually that is not too much heavy")
print ("He's got %s eyes and %s hair" %(my_eyes, my_hair))
print ("His %s teeth usually depende on the coffee")
print ("If I add %d, %d and %d, I get %d."% (my_age, my_height, my_weight,my_age + my_height + my_weight))

x = "There are 10 types of people, who knows binary and those who don't."
print ("I said that ",x)
print ("I also said that ",x)


####################################################
# 		 	MORE PRINTING OPOTIONS		     	   #
####################################################
print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
print ("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print ((end1 + end2 + end3 + end4 + end5 + end6), (end7 + end8 + end9 + end10 + end11 + end12))


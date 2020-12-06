# -*- coding: utf-8 -*-
#Assign the number of car that I have :D, I am a billionaire so that I have a lot of cars
cars = 100
# Mỗi xe chỉ chở được 4 người (có kể cả tài xế không?)
space_in_a_car = 4.0
# Số lượng tài xế hiện có
drivers = 30
# Số lượng hành khách cần chở hôm nay
passengers = 90
# Số lượng xe không ai lái = số lượng xe - số tài xế hiện có
cars_not_driven = cars - drivers
# Số lượng xe được sử dụng = số tài xế
cars_driven = drivers
# Số lượng hành khách tối đa được chở = số xe * số ghế trên xe
carpool_capacity = cars_driven * space_in_a_car
# Số hành khách trung bình trên 1 xe = số hành khách chia cho số xe được lái
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print 'We need to put about', average_passengers_per_car, "passenger in each car."
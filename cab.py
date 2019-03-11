#case 1: when driver has nobody in the cab
from haversine import haversine
start_lat=float(input())
start_long=float(input())
driver_lat=float(input())
driver_long=float(input())
dest_lat=float(input())
dest_long=float(input())
start=(start_lat,start_long)
driver=(driver_lat,driver_long)
dest=(dest_lat,dest_long)
distance=haversine(start,driver)

if(distance<3):
    print("Pick up")
else:
	print("Look for another ride")



#case2: when one person is already in the cab
from haversine import haversine
current_lat=float(input())
current_long=float(input())

start_lat1=float(input())
start_long1=float(input())
start_lat2=float(input())
start_long2=float(input())

dest_lat1=float(input())
dest_long1=float(input())
dest_lat2=float(input())
dest_long2=float(input())

start1=(start_lat1,start_long1)
start2=(start_lat2,start_long2)
dest1=(dest_lat1,dest_long1)
dest2=(dest_lat2,dest_long2)

current=(current_lat,current_long)
distance_start=haversine(current,start2)
distance_dest=haversine(dest1,dest2)

if(distance_start<3):
    if(distance_dest<3):
        print("Pick up")
else:
	print("Look for another ride")
   

#considering cab capacity as 3
#case 3:when two are already in the cab
from haversine import haversine
current_lat=float(input())
current_long=float(input())
current=(current_lat,current_long)

dest_lat1=float(input())
dest_long1=float(input())
dest_lat2=float(input())
dest_long2=float(input())
dest_lat3=float(input())
dest_long3=float(input())
dest1=(dest_lat1,dest_long1)
dest2=(dest_lat2,dest_long2)
dest3=(dest_lat3,dest_long3)

mid_point=(dest_lat1-dest_lat2,dest_long1-dest_long2)
distance=haversine(dest3,mid_point)

if(distance<3):
    print("Pick up")
else:
		print("Look for another ride")

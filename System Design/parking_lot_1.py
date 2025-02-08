"""

1. Design a Parking Lot - Multi-Threaded

Write code for low level design of a parking lot system.
The parking lot has two kinds of parking spaces: type = 2, for 2 wheeler vehicles and type = 4, for 4 wheeler vehicles.

There are multiple floors in the parking lot. On each floor, vehicles are parked in parking spots arranged in rows and columns.
For simplicity, lets assume that each floor will have same number of rows and each row will have same number of columns.

Some of the parking spots are inactive. You can't park your vehicle in those spots.

For Java, your code will be tested in a multi-threaded environment.
So make sure that you take care of thread safety and synchronization.
For Python, your code will be tested in a single-threaded environment.

Implement the below methods in Solution class:

init(Helper helper, String [][][] parking) :
- helper has methods like, helper.print("") and helper.println("") which you can use for printing logs
- parking[i][j][k] : parking spot on i-th floor, j-th row and k-th column.
- each item in parking is of the following type.
"4-1" : an active 4 wheeler parking spot,
"2-1" : an active 2 wheeler parking spot,
"4-0" and "2-0" are inactive parking spots, you can't park there.

park(int vehicleType, String vehicleNumber, String ticketId);
- This function assigns an empty parking spot to vehicle and maps vehicleNumber and ticketId to the assigned spotId
- spotId is floor+"-"+row+"-"+column
e.g. parking[2][0][15] = parking spot at 2nd floor , 0th row and 15th column (0 based index),
its spotId will be: "2-0-15"
- For Java, return ParkingResult: (status,spotId, vehicleNumber, ticketId)
- For Python, return the assigned spotId string or
return an empty string "" , in case not spot can be assigned to vehicle.

removeVehicle(String spotId, String vehicleNumber, String ticketId)
- Unparks or removes vehicle from parking spot.
- Exactly one of spotId, vehicleNumber and ticketId will be non-blank.
- vehicleId and ticketId are from the ones assigned in park() above.
- return 201 for success and 404 for failure to remove vehicle

ParkingResult searchVehicle( String spotId, String vehicleNumber, String ticketId)
- search the vehicle parked in one of park() method calls.
- Exactly one of spotId, vehicleNumber and ticketId will be non-blank.
- If the vehicle is already removed, then also you should be able to get its last spotId using either vehicleNumber or ticketId.
- For Java, return ParkingResult: (status,spotId, vehicleNumber, ticketId)
- For Python, return the assigned spotId string or empty string "" if vehicle was never parked in this parking lot.


int getFreeSpotsCount(int floor, int vehicleType)
At any point of time get the number of free spots of vehicle type (2 or 4 wheeler). 0>= floor < parking from init() method.


Constraints:
- type = 2 for two-wheeler vehicle, type = 4 for 4 wheeler vehicle
- 1<=floors<=5, 1<=rows<=10,000, 1<=columns<=10,000, 1<=rows*columns<=10,000
- Java variables follow camel case while python variables in default code follow snake case.

Input Example
parking = [[
["4-1","4-1","2-1","2-0"],
["2-1","4-1","2-1","2-1"],
["4-0","2-1","4-0","2-1"],
["4-1","4-1","4-1","2-1"]]]

Above input has 1 floor.
It has 4 rows and 4 columns on floor 0.
Total 7 active 2-wheeler vehicles and 6 active 4-wheeler vehicles are there.

e.g park(4, "bh234", "tkt4534") will return below ParkingResult object
  {
      status: 201,
      spotId: "0-3-1",
      vehicleNumber: "bh234",
      ticketId:"tkt4534"
   }

It assigns spot id 0-3-1 i.e parking spot from floor 0, row 3 and column 1 is assigned.
The spotId can be different depending on how you have implemented your solution.

- search("","bh234","") or search("","","tkt4534") at this point should return the above ParkingResult object with spotId = "0-3-1"
we can use vehicleNumber: "bh234" or ticketId:"tkt4534" to find the parking spot id where vehicle is parked.

- getFreeSpotsCount(0, 4) : will return 5.

- removeVehicle("0-3-1","","") or removeVehicle("","bh234","") or removeVehicle("","","tkt4534") :
should unpark the parked vehicle and getFreeSpotsCount(0, 4) after unparking will return 6.


parking = [[
["2-1","4-1","2-1","4-1"],
["2-1","2-1","4-1","4-1"]
],
[
["2-1","2-1","4-1","2-1"],
["4-1","4-1","2-1","2-1"]
]]

Above input has 2 floors.
Each floor has 2 rows and 4 columns.
ParkingFloor 0 has 4 active 2-wheeler and 4 active 4-wheeler vehicle parking spots.
ParkingFloor 1 has 5 active 2-wheeler and 3 active 4-wheeler vehicle parking spots.
"""

from collections import defaultdict
from threading import Lock


class Solution:
    def __init__(self):
        self.helper = None
        self.parking_lot = []
        self.lock = Lock()
        self.free_spots = defaultdict(int)
        self.vehicle_map = {}
        self.ticket_map = {}
        self.spot_map = {}

    def init(self, helper, parking):
        self.helper = helper
        self.parking_lot = parking
        self.free_spots.clear()
        self.vehicle_map.clear()
        self.ticket_map.clear()
        self.spot_map.clear()

        for floor in range(len(parking)):
            for row in range(len(parking[floor])):
                for col in range(len(parking[floor][row])):
                    spot_info = parking[floor][row][col]
                    vehicle_type, active = map(int, spot_info.split('-'))
                    if active:
                        self.free_spots[(floor, vehicle_type)] += 1

    def park(self, vehicle_type, vehicle_number, ticket_id):
        with self.lock:
            for floor in range(len(self.parking_lot)):
                for row in range(len(self.parking_lot[floor])):
                    for col in range(len(self.parking_lot[floor][row])):
                        spot_info = self.parking_lot[floor][row][col]
                        v_type, active = map(int, spot_info.split('-'))
                        if v_type == vehicle_type and active:
                            spot_id = f"{floor}-{row}-{col}"
                            if spot_id not in self.spot_map:
                                self.spot_map[spot_id] = (vehicle_number, ticket_id)
                                self.vehicle_map[vehicle_number] = spot_id
                                self.ticket_map[ticket_id] = spot_id
                                self.free_spots[(floor, vehicle_type)] -= 1
                                return spot_id
        return ""

    def removeVehicle(self, spot_id, vehicle_number, ticket_id):
        with self.lock:
            if spot_id:
                if spot_id in self.spot_map:
                    vehicle_number, ticket_id = self.spot_map.pop(spot_id)
                else:
                    return 404
            elif vehicle_number:
                if vehicle_number in self.vehicle_map:
                    spot_id = self.vehicle_map.pop(vehicle_number)
                else:
                    return 404
            elif ticket_id:
                if ticket_id in self.ticket_map:
                    spot_id = self.ticket_map.pop(ticket_id)
                else:
                    return 404
            else:
                return 404

            floor = int(spot_id.split('-')[0])
            vehicle_type = int(self.parking_lot[floor][0][0].split('-')[0])
            self.free_spots[(floor, vehicle_type)] += 1
            return 201

    def searchVehicle(self, spot_id, vehicle_number, ticket_id):
        with self.lock:
            if spot_id and spot_id in self.spot_map:
                return spot_id
            if vehicle_number and vehicle_number in self.vehicle_map:
                return self.vehicle_map[vehicle_number]
            if ticket_id and ticket_id in self.ticket_map:
                return self.ticket_map[ticket_id]
        return ""

    def getFreeSpotsCount(self, floor, vehicle_type):
        return self.free_spots.get((floor, vehicle_type), 0)


class Helper:
    def print(self, msg):
        print(msg)

    def println(self, msg):
        print(msg)


# Initialize the parking lot
parking = [[
    ["4-1", "4-1", "2-1", "2-0"],
    ["2-1", "4-1", "2-1", "2-1"],
    ["4-0", "2-1", "4-0", "2-1"],
    ["4-1", "4-1", "4-1", "2-1"]
]]

helper = Helper()
solution = Solution()
solution.init(helper, parking)

# Park a vehicle
spot_id = solution.park(4, "bh234", "tkt4534")
print("Parked at:", spot_id)

# Search for a vehicle
search_result = solution.searchVehicle("", "bh234", "")
print("Found at:", search_result)

# Check free spots
free_spots = solution.getFreeSpotsCount(0, 4)
print("Free 4-wheeler spots:", free_spots)

# Remove the vehicle
remove_status = solution.removeVehicle("0-3-1", "", "")
print("Remove Status:", remove_status)

# Check free spots again
free_spots_after = solution.getFreeSpotsCount(0, 4)
print("Free 4-wheeler spots after removal:", free_spots)

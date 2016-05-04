\* Oil Distribution Problem *\
Minimize
Sum_of_Transporting_Costs: 8 Route_A_1 + 6 Route_A_2 + 3 Route_A_3
 + 2 Route_B_1 + 4 Route_B_2 + 9 Route_B_3
Subject To
Sum_of_Products_into_TruckStops1: Route_A_1 + Route_B_1 >= 40
Sum_of_Products_into_TruckStops2: Route_A_2 + Route_B_2 >= 35
Sum_of_Products_into_TruckStops3: Route_A_3 + Route_B_3 >= 25
Sum_of_Products_out_of_Warehouse_A: Route_A_1 + Route_A_2 + Route_A_3 <= 70
Sum_of_Products_out_of_Warehouse_B: Route_B_1 + Route_B_2 + Route_B_3 <= 40
Bounds
0 <= Route_A_1
0 <= Route_A_2
0 <= Route_A_3
0 <= Route_B_1
0 <= Route_B_2
0 <= Route_B_3
Generals
Route_A_1
Route_A_2
Route_A_3
Route_B_1
Route_B_2
Route_B_3
End

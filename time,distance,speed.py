while True:
    time=float(input("Time(h)="))
    distance=float(input("Distance(km)="))
    speed=float(input("Speed(km/h)="))
    
    # 0 == empty
    
    zero_count = [time, distance, speed].count(0)

    if zero_count > 1:
        print("You must set one value as 0 to find that or else its IMPOSSIBLE")
    elif zero_count == 0:
        print(" All values are filled you need to leave one as 0 to find it")

    if time == 0:
        tans=distance/speed
        question = input("Do you want answer in minutes or hrs")
        if question == "hrs":
            print(tans,"hrs")
        else:
            print(tans*60,"minutes")
    elif distance == 0:
        dans=time*speed
        print(dans,"km")
    elif speed == 0:
        sans=distance/time
        print(sans,"km/h")
    
    again = input("Do you want to calculate again, yes/no:")
    
    if again != 'yes':
        print("Goodbye")
        break
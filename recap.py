time = 19
place_of_work = "Manchester"
town_you_live_in = "Sale"

if time < 8:
    print(f"The time is before 8am so I am at {town_you_live_in}")
elif time == 8:
    print(f"It is 8am so I am communting to {place_of_work}")
elif time >= 9 and time <= 17:
    print(f"I am at work in {place_of_work}")
elif time == 18:
    print(f"I am going back home to {town_you_live_in}")
else:
    print(f"I am at home in {town_you_live_in}")
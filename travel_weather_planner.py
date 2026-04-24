distance_km = 15
is_raining = True
has_bike = False
has_car = True
has_bolt = True  # Bolt ride-share app (SA)

if distance_km <= 0:
    print(False)

elif distance_km <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_km <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    if has_car or has_bolt:
        print(True)
    else:
        print(False)

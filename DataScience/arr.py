import numpy as np
temp_data=np.array([
    [342,342,2423,2342,234],
    [342,324324,4234,332,322],
    [42343,324324,32432,32432,3242],
    [3423,234234,42,334,34],
])

daily_avg=np.mean(temp_data,axis=1)
print("daily avg temp for each city in india",daily_avg)

city_highest=np.argmax(daily_avg)
cities=["mumbai","nabg","dsadff","sfsg","dsfg"]
print("city with highest avg temprature is:",cities[city_highest])

temp_anamolie=temp_data-daily_avg[:,np.newaxis]
print(temp_anamolie)
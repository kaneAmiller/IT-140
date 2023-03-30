age_years = float(int(input()))
weight_pounds = float(int(input()))
heartrate_bpm = float(int(input()))
time_minutes = float(int(input()))

Calories = ((age_years * 0.2757) + (weight_pounds * 0.03295) +
            (heartrate_bpm * 1.0781) - 75.4991) * time_minutes / 8.368

print('Calories: {:.2f} calories'.format(Calories))

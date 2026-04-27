# ==========================================
# EDIT THESE NUMBERS BELOW TO TEST A DAY!
# ==========================================

cape = 3000               # Atmospheric lift/energy (usually 0 to 5000)
shear = 45                # Wind shear in knots (usually 0 to 60+)
tornado_param = 4.0       # Tornado parameter rating (usually 0 to 10+)
hail_size = 2.5           # Max predicted hail size in inches (e.g., 2.5 = tennis ball)
wind_speed = 65           # Max predicted straight-line wind gusts in mph
coverage = 0.8            # Percent of your area affected (use 0.0 to 1.0)
population_density = 0.7  # How crowded the target area is (use 0.0 to 1.0)
nighttime = True          # Type True if it's a dangerous nighttime setup, False if daytime

# ==========================================
# THE SCORER ENGINE (Do not edit below)
# ==========================================

# 1. Atmospheric Fuel (Max 25)
score_cape = min(10.0, cape / 400.0)
score_shear = min(10.0, shear / 5.0)
score_fuel = score_cape + score_shear + 5.0

# 2. Specific Hazard Threats (Max 40)
score_tor = min(15.0, tornado_param * 3.0)
score_hail = min(10.0, hail_size * 3.0)
score_wind = min(10.0, wind_speed / 7.0)
score_hazards = score_tor + score_hail + score_wind + 5.0

# 3. Coverage & Timing (Max 20)
score_cov = coverage * 10.0
score_time = 10.0 if nighttime else 5.0
score_timing = score_cov + score_time

# 4. Societal Vulnerability (Max 15)
score_pop = population_density * 10.0
score_soc = score_pop + 5.0

# Calculate Total
total = score_fuel + score_hazards + score_timing + score_soc
final_score = min(100.0, round(total, 1))

# Determine the risk category
if final_score <= 20:
    category = "QUIET DAY (Standard rain or storms)"
elif final_score <= 40:
    category = "LOW RISK (Be aware of isolated strong storms)"
elif final_score <= 60:
    category = "MODERATE RISK (Multiple severe storms likely)"
elif final_score <= 80:
    category = "HIGH RISK (Widespread damage expected)"
else:
    category = "HISTORIC EVENT (Extreme, destructive outbreak)"

print("==========================================")
print("THE SEVERE WEATHER SCORE IS: " + str(final_score) + " / 100")
print("RISK LEVEL: " + category)
print("==========================================")

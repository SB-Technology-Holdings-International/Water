#watering system check for amount of rain.
Forever
    check watering parameters
        if <10cm then
            no action
        if >10cm then
            initiate watering system

# this data should be from nws.
import pyeto
latitude_deg = 38.01
latitude = pyeto.deg2rad(latitude_deg)
day_of_year = 206
tmin = 37
tmax = 53
coastal = True
altitude = 147
rh_min = 13
rh_max = 88
ws = 1.3

tmean = pyeto.daily_mean_t(tmin, tmax)
atmos_pres = pyeto.atm_pressure(altitude)
psy = pyeto.psy_const(atmos_pres)

# Humidity
svp_tmin = pyeto.svp_from_t(tmin)
svp_tmax = pyeto.svp_from_t(tmax)
delta_svp = pyeto.delta_svp(tmean)
svp = pyeto.mean_svp(tmin, tmax)
avp = pyeto.avp_from_rhmin_rhmax(svp_tmin, svp_tmax, rh_min, rh_max)

# Radiation
sol_dec = pyeto.sol_dec(day_of_year)
sha = pyeto.sunset_hour_angle(latitude, sol_dec)
ird = pyeto.inv_rel_dist_earth_sun(day_of_year)
et_rad = pyeto.et_rad(latitude, sol_dec, sha, ird)
cs_rad = pyeto.cs_rad(altitude, et_rad)
sol_rad = pyeto.sol_rad_from_t(et_rad, cs_rad, tmin, tmax, coastal)
ni_sw_rad = pyeto.net_in_sol_rad(sol_rad)
no_lw_rad = pyeto.net_out_lw_rad(pyeto.celsius2kelvin(tmin), pyeto.celsius2kelvin(tmax), sol_rad, cs_rad, avp)
net_rad = pyeto.net_rad(ni_sw_rad, no_lw_rad)

eto = pyeto.fao56_penman_monteith(net_rad, pyeto.celsius2kelvin(tmean), ws, svp, avp, delta_svp, psy)
print eto

Forever
    check the time
    if not running
        if eto is <0 then
            turn on water
            var ontime = time.time()
    else
        time running = ontime - time.time()
        if time running > eto then
            turn off water

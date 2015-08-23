import pyeto
latitude_deg = 38
latitude = pyeto.deg2rad(latitude_deg)
day_of_year = 235
tmin = 13
tmax = 24
coastal = True
altitude = 300
rh_min = 20
rh_max = 66
ws = 2

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

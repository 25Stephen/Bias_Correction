library(hyfo)
obs_file <-'/media/kenz/1B8D1A637BBA134B/bcsd-final/data2/Era_5_obs.nc'
obs_var <- getNcdfVar(obs_file)
obs_data <- loadNcdf(obs_file, obs_var)

mod_file <-'/media/kenz/1B8D1A637BBA134B/bcsd-final/data2/mod_d.nc'
mod_var <- getNcdfVar(mod_file)
mod_data <- loadNcdf(mod_file, obs_var)

frc_file <-'/media/kenz/1B8D1A637BBA134B/bcsd-final/data2/mod_rcp.nc'
frc_var <- getNcdfVar(frc_file)
frc_data <- loadNcdf(frc_file, obs_var)

newFrc <- biasCorrect(frc_data, mod_data, obs_data, method = 'eqm')
writeNcdf(newFrc, '/media/kenz/1B8D1A637BBA134B/bcsd-final/data2/bias_corrected_with_hyfo')

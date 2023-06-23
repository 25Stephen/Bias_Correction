# Bias_Correction
This script is used to bias correct two dataset using the quantile mapping approach.
Cordex_preocessing.ipynb is used to processes the outputs of cordex to suite the bias correction model.
bbias.ipynb bias correct the historical modelled data using the observed data and also has a posrtion to bias correct the future data using the bias corrected data. They are twi distinct scripts and undependant on one another.
bias.R is a sample R script used to bias correct the scenario data using the Hyfo Package in R. I used that to cross check the Python Script.
biash.sh is a sample bash script I am using to automate the bias correcting processes.
The scripts here are imperfect as in not well arranged. Depending on the results I may want to get I will have to rearrange the scripts to suite my needs.

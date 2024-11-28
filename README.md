# FUTHLI
Find Users That Haven't Logged In (Entra ID .csv user finder)

Small program that finds the users that haven't logged in over the last two months.

Program takes three input files, 2 .csv files containing the last months worth of user logins, and an xlsx file that contains the current users registered in the AD.
The program then saves the output as either .txt or .csv
Since Entra ID only logs 1 month, this program is intended to be used after 2 months of logs.
It uses TkInter, so you don't have to place any of the files in the same folder.

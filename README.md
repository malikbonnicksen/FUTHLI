# FUTHLI
Find Users That Haven't Logged In (Entra ID .csv user finder)

Small program that finds the users that haven't logged in over the last two months.

Program takes a .csv file containing users extracted from AD and two .csv files from Entra ID.
Since Entra ID only logs 1 month, this program is intended to be used after gathering 2 months of logs.
It finds the unique users in the Entra ID files and compares it to the AD list of users and finds users that haven't logged in.

# Define the OUs
$OU1 = ""
$OU2 = ""

# Get enabled users from both OUs
$users1 = Get-ADUser -Filter {Enabled -eq $true} -SearchBase $OU1 -Property GivenName,Surname
$users2 = Get-ADUser -Filter {Enabled -eq $true} -SearchBase $OU2 -Property GivenName,Surname

# Combine the users
$allUsers = $users1 + $users2

# Select only GivenName and Surname
$selectedUsers = $allUsers | Select-Object GivenName, Surname

# Export to CSV
$selectedUsers | Export-Csv -Path "C:\Users\Public\enabled_users.csv" -NoTypeInformation -Encoding UTF8

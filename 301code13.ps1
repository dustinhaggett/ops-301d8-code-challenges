# Import the Active Directory module
Import-Module ActiveDirectory

# Define user properties
$userParams = @{
    'SamAccountName'       = 'f.ferdinand'
    'UserPrincipalName'    = 'ferdi@GlobeXpower.com'
    'Name'                 = 'Franz Ferdinand'
    'GivenName'            = 'Franz'
    'Surname'              = 'Ferdinand'
    'Enabled'              = $true
    'DisplayName'          = 'Franz Ferdinand'
    'Description'          = 'TPS Reporting Lead'
    'Title'                = 'TPS Reporting Lead'
    'Department'           = 'TPS Department'
    'Company'              = 'GlobeX USA'
    'StreetAddress'        = 'Springfield'
    'State'                = 'OR'
    'EmailAddress'         = 'ferdi@GlobeXpower.com'
    'AccountPassword'      = (ConvertTo-SecureString -AsPlainText "P@ssw0rd" -Force)
    'PassThru'             = $true
    'ChangePasswordAtLogon'= $true
}

# Create the new user
New-ADUser @userParams

---
title: Quick Start Web API with PowerShell Option 2
description: Describes how to use the Dataverse Web API from PowerShell
ms.date: 12/05/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Quick Start: Web API with PowerShell Option 2

In this quick start, you'll learn how to:

- Use PowerShell and Visual Studio Code to use reusable functions for ad-hoc testing of Web API operations.
- Authenticate to Dataverse using PowerShell without registering your own application.
- Compose requests to the Dataverse Web API using the PowerShell [Invoke-RestMethod](/powershell/module/microsoft.powershell.utility/invoke-restmethod).
- Create reusable functions that you can save in a .ps1 file.
- Write and run a script using the functions you created.

> [!NOTE]
> - This should work for Windows, Linux, and macOS, but these steps have only been tested on Windows. If changes are needed, please let us know using the **Feedback** section at the bottom of this article.

## Prerequisites

- Install PowerShell 7.4 or higher. See [Install PowerShell on Windows, Linux, and macOS](/powershell/scripting/install/installing-powershell)
   
   - In a PowerShell terminal, run `$PSVersionTable.PSVersion` to check.

- Install Azure CLI version 2.54.0 or higher. See [How to install the Azure CLI](/cli/azure/install-azure-cli)
   
   - In a PowerShell terminal, run `az version` to check.

- The Azure CLI `account` extension.
   
   - In a PowerShell terminal, run `az extension add --name account`
   - [Learn more about Azure CLI extensions](/cli/azure/azure-cli-extensions-overview)

- Install Visual Studio Code. See [Download Visual Studio Code](https://code.visualstudio.com/download)
- Install the PowerShell extension for Visual Studio Code. See [PowerShell for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)
- Internet connection
- Valid user account for a Dataverse environment
- Url to the Dataverse environment you want to connect to. See [View developer resources](../view-download-developer-resources.md)
- Basic understanding of the PowerShell scripting language

## Creating reusable functions

The following script contains definitions of re-usable PowerShell functions that you can use with Dataverse Web API.

```powershell
<#
   .SYNOPSIS
   Connects to a Dataverse environment using the device code authentication.

   .DESCRIPTION
   The Connect-Device-Code function uses the Azure CLI to obtain an access token for the specified Dataverse environment. 
   It sets the global variables $environmentUrl and $accessToken with the values of the uri parameter and the token respectively. 
   It also displays the expiration time of the token.

   .PARAMETER uri 
   The url for the Dataverse environment you want to connect to. 
   For example, 'https://contoso.crm.dynamics.com'.

   .EXAMPLE
   PS> Connect-Device-Code -uri 'https://yourorg.crm.dynamics.com/'
   ERROR: Please run 'az login' to setup account.
   To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code FVF55NNWF to authenticate.
   Connected to https://yourorg.crm.dynamics.com/
   Token will expire in 30 minutes.

   .EXAMPLE
   PS> Connect-Device-Code -uri 'https://yourorg.crm.dynamics.com/'
   Connected to https://yourorg.crm.dynamics.com/
   Token will expire in 30 minutes.
    #>
function Connect-Device-Code {
   param (
      [Parameter(Mandatory)] 
      [String] 
      # Specifies the url for the environment you want to connect to
      $uri
   )

   # Set environment URL
   $global:environmentUrl = $uri

   ## Login if not already logged in
   if ($null -eq (az account tenant list  --only-show-errors)) {
      az login --allow-no-subscriptions --use-device-code | Out-Null
   }
   # Get token
   $token = az account get-access-token --resource=$environmentUrl --output json
   $tokenObj = $token | ConvertFrom-Json
   # Set accessToken
   $global:accessToken = $tokenObj.accessToken
   # Get minutes to token expiration
   $minutesToTokenExpire = (New-TimeSpan -End ([DateTime]$tokenObj.expiresOn)).Minutes
   # Show information
   Write-Output "Connected to $environmentUrl"
   Write-Output "Token will expire in $minutesToTokenExpire minutes."
}

# Define common set of headers
$baseHeaders = @{
   'Authorization'    = "Bearer $accessToken"
   'Accept'           = 'application/json'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}

<#
   .SYNOPSIS
   Gets the information about the current user, organization, and business unit.

   .DESCRIPTION
   The Get-WhoAmI function uses the Invoke-RestMethod cmdlet to send a GET request to the Dataverse Web API. 
   It retrieves the information about the current user, organization, and business unit from the WhoAmI function. 
   It returns the user ID, business unit ID, and organization ID as properties.

   .PARAMETER 
   None This function does not take any parameters.

   .OUTPUTS
   Microsoft.Dynamics.CRM.WhoAmIResponse ComplexType 

   .EXAMPLE
   PS> Get-WhoAmI | Format-List -Property BusinessUnitId,UserId,OrganizationId
#>
function Get-WhoAmI {
   $WhoAmIRequest = @{
      Uri     = $environmentUrl + 'api/data/v9.2/WhoAmI'
      Method  = 'Get'
      Headers = $baseHeaders
   }
   Invoke-RestMethod @WhoAmIRequest
}

<#
   .SYNOPSIS
   Returns a collection of records from a table that match a query

   .DESCRIPTION
   The Get-Records function returns a collection of records from the table with the matching -setName parameter
   filtered by the -query parameter

   .PARAMETER setName 
   The table set name (EntityMetadata.EntitySetName property) of the records to retrieve. For example, 'accounts' or 'contacts'.

   .PARAMETER query 
   The ODATA query to select properties, expand navigation properties, and filter results. 
   For example, '?$select=name,address1_city&$filter=address1_city eq ''Seattle''&$top=10'.

   .OUTPUTS
   Collection of table records 

   .EXAMPLE 
   Get-Records -setName 'accounts' -query '?$select=name,address1_city&$filter=address1_city eq ''Seattle''&$top=10'

   .EXAMPLE
   PS> Get-Records accounts '?$select=name&$top=3'

   @odata.context                                        : https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#accounts(name)
   @Microsoft.Dynamics.CRM.totalrecordcount              : -1
   @Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded : False
   @Microsoft.Dynamics.CRM.globalmetadataversion         : 103348253
   value                                                 : {@{@odata.etag=W/"102872096"; name=Adatum Corporation;
                                                         accountid=4b757ff7-9c85-ee11-8179-000d3a9933c9}, @{@odata.etag=W/"103323309";
                                                         name=Adventure Works Cycles; accountid=2ada33e7-ef8b-ee11-8179-000d3a9933c9},
                                                         @{@odata.etag=W/"103323312"; name=Alpine Ski House;
                                                         accountid=2eda33e7-ef8b-ee11-8179-000d3a9933c9}}

   .EXAMPLE
   PS> (Get-Records accounts '?$select=name&$top=3').value
      
   @odata.etag   name                   accountid
   -----------   ----                   ---------
   W/"102872096" Adatum Corporation     4b757ff7-9c85-ee11-8179-000d3a9933c9
   W/"103323309" Adventure Works Cycles 2ada33e7-ef8b-ee11-8179-000d3a9933c9
   W/"103323312" Alpine Ski House       2eda33e7-ef8b-ee11-8179-000d3a9933c9


   .EXAMPLE
   PS> (Get-Records accounts '?$select=name&$top=3').value | Format-Table -Property name,accountid

   name                   accountid
   ----                   ---------
   Adatum Corporation     4b757ff7-9c85-ee11-8179-000d3a9933c9
   Adventure Works Cycles 2ada33e7-ef8b-ee11-8179-000d3a9933c9
   Alpine Ski House       2eda33e7-ef8b-ee11-8179-000d3a9933c9
#>
function Get-Records {
   param (
      [Parameter(Mandatory)] 
      [String] 
      # The table set name (EntityMetadata.EntitySetName property)
      $setName,
      [Parameter(Mandatory)] 
      [String] 
      # The ODATA query to select properties, expand navigation properties, and filter results
      $query
   )
   $uri = $environmentUrl + 'api/data/v9.2/' + $setName + $query

   # Header for GET operations that have annotations
   $getHeaders = $baseHeaders.Clone()
   $getHeaders.Add('If-None-Match', $null)
   $getHeaders.Add('Prefer', 'odata.include-annotations="*"')

   $RetrieveMultipleRequest = @{
      Uri     = $uri
      Method  = 'Get'
      Headers = $getHeaders
   }
   Invoke-RestMethod @RetrieveMultipleRequest
}

<# 
.SYNOPSIS 
Creates a record in a table.

.DESCRIPTION 
The New-Record function uses the Invoke-RestMethod cmdlet to send a POST request to the Dataverse Web API. 
It creates a new record in the specified table set with the properties and values provided in the body parameter. 
It returns the GUID of the created record.

.PARAMETER 
setName The table set name (EntityMetadata.EntitySetName property) of the record to create. 
For example, 'accounts' or 'contacts'.

.PARAMETER 
body 
A hashtable that contains the properties and values of the record to create. 
For example, @{name = 'Contoso'; address1_city = 'Seattle'}.

.EXAMPLE 
New-Record -setName 'accounts' -body @{name = 'Contoso'; address1_city = 'Seattle'}

This example creates a new account record with the name 'Contoso' and the city 'Seattle'. It returns the GUID of the created record. 
#>
function New-Record {
   param (
      [Parameter(Mandatory)] 
      [String] 
      # The table set name (EntityMetadata.EntitySetName property)
      $setName,
      [Parameter(Mandatory)] 
      [hashtable]
      # Contains the properties and values of the record to change.
      $body
   )
   $postHeaders = $baseHeaders.Clone()
   $postHeaders.Add('Content-Type', 'application/json')
   $CreateRequest = @{
      Uri     = $environmentUrl + 'api/data/v9.2/' + $setName
      Method  = 'Post'
      Headers = $postHeaders
      Body    = ConvertTo-Json $body
   }
   Invoke-RestMethod @CreateRequest  -ResponseHeadersVariable rh
   $url = $rh['OData-EntityId']
   $selectedString = Select-String -InputObject $url -Pattern '(?<=\().*?(?=\))'
   return [System.Guid]::New($selectedString.Matches.Value.ToString())
}

<# 
.SYNOPSIS 
Retrieves a record from a table set using the primary key.

.DESCRIPTION 
The Get-Record function uses the Invoke-RestMethod cmdlet to send a GET request to the Dataverse Web API. 
It retrieves a record from the specified table set using the GUID primary key value provided in the id parameter. 
It optionally accepts an ODATA query parameter to select properties, filter results and expand navigation properties. 
It returns the record as a PowerShell object.

.PARAMETER 
setName 
The table set name (EntityMetadata.EntitySetName property) of the record to retrieve. For example, 'accounts' or 'contacts'.

.PARAMETER 
id 
The GUID primary key value of the record to retrieve. For example, '00000000-0000-0000-0000-000000000000'.

.PARAMETER 
query 
The ODATA query to select properties, filter results and expand navigation properties. 
For example, '?$select=name,address1_city&$expand=primarycontactid($select=fullname)'.

.EXAMPLE 
Get-Record -setName 'accounts' -id '00000000-0000-0000-0000-000000000000'

This example retrieves the account record with the specified GUID and returns all the properties.

.EXAMPLE 
Get-Record -setName 'accounts' -id '00000000-0000-0000-0000-000000000000' -query '?$select=name,address1_city&$expand=primarycontactid($select=fullname)'

This example retrieves the account record with the specified GUID and returns only the name and city properties, as well as the full name of the primary contact. 

.EXAMPLE
Get-Record `
-setName  accounts `
-id $newAccountID.Guid '?$select=name,accountcategorycode' |
Format-List -Property name,
accountid,
accountcategorycode,
accountcategorycode@OData.Community.Display.V1.FormattedValue

This example retrieves the account record with the specified GUID and returns only the name, 
accountid, accountcategorycode, and the formatted value for the account category code.

name                                                          : Example Account
accountid                                                     : f20412c1-1592-ee11-be37-000d3a993550
accountcategorycode                                           : 1
accountcategorycode@OData.Community.Display.V1.FormattedValue : Preferred Customer

#>
function Get-Record {
   param (
      [Parameter(Mandatory)] 
      [String] 
      # The table set name (EntityMetadata.EntitySetName property)
      $setName,
      [Parameter(Mandatory)] 
      [Guid] 
      # The GUID primary key value of the record to retrieve
      $id,
      [String] 
      # The ODATA query to select properties, filter results and expand navigation properties
      $query
   )

   $uri = $environmentUrl + 'api/data/v9.2/' + $setName
   $uri = $uri + '(' + $id.Guid + ')' + $query

   $getHeaders = $baseHeaders.Clone()
   $getHeaders.Add('If-None-Match', $null)
   $getHeaders.Add('Prefer', 'odata.include-annotations="*"')

   $RetrieveRequest = @{
      Uri     = $uri
      Method  = 'Get'
      Headers = $getHeaders
   }
   Invoke-RestMethod @RetrieveRequest
}

<# .SYNOPSIS 
Updates a record in a table using the primary key.

.DESCRIPTION 
The Update-Record function uses the Invoke-RestMethod cmdlet to send a PATCH request to the Dataverse Web API. 
It updates an existing record in the specified table using the GUID primary key value provided in the id parameter. 
It accepts a hashtable that contains the values to update in the body parameter.

.PARAMETER 
setName The table set name (EntityMetadata.EntitySetName property) of the record to update. For example, 'accounts' or 'contacts'.

.PARAMETER 
id The GUID primary key value of the record to update. For example, '00000000-0000-0000-0000-000000000000'.

.PARAMETER 
body A hashtable that contains the values to update in the record. For example, @{name = 'Contoso'; address1_city = 'Seattle'}.

.EXAMPLE 
Update-Record -setName 'accounts' -id '00000000-0000-0000-0000-000000000000' -body @{name = 'Contoso'; address1_city = 'Seattle'}

This example updates the account record with the specified GUID and changes the name to 'Contoso' and the city to 'Seattle'. 

.EXAMPLE
$updateAccountData = @{
   name                = 'Contoso';
   accountcategorycode = 2; #Standard
}
Update-Record `
-setName accounts `
-id $newAccountID.Guid `
-body $updateAccountData

This example updates the account record with the specified GUID and changes the name to 'Contoso' and the accountcategorycode to 2 (Standard). 

#>
function Update-Record {
   param (
      [Parameter(Mandatory)] 
      [String] 
      # The table set name (EntityMetadata.EntitySetName property)
      $setName,
      [Parameter(Mandatory)] 
      [Guid] 
      # The GUID primary key value of the record to update
      $id,
      [Parameter(Mandatory)] 
      [hashtable]
      # A hashtable containing the values to update
      $body
   )
   $uri = $environmentUrl + 'api/data/v9.2/' + $setName
   $uri = $uri + '(' + $id.Guid + ')'

   # Header for Update operations
   $updateHeaders = $baseHeaders.Clone()
   $updateHeaders.Add('Content-Type', 'application/json')
   $updateHeaders.Add('If-Match', '*') # Prevent Create

   $UpdateRequest = @{
      Uri     = $uri
      Method  = 'Patch'
      Headers = $updateHeaders
      Body    = ConvertTo-Json $body
   }
   Invoke-RestMethod @UpdateRequest
}

<# 

.SYNOPSIS 
Deletes a record from a table using the primary key.

.DESCRIPTION 
The Remove-Record function uses the Invoke-RestMethod cmdlet to send a DELETE request to the Dataverse Web API. 
It deletes an existing record from the specified table using the GUID primary key value provided in the id parameter.

.PARAMETER 
setName The table set name (EntityMetadata.EntitySetName property) of the record to delete. For example, 'accounts' or 'contacts'.

.PARAMETER 
id The GUID primary key value of the record to delete. For example, '00000000-0000-0000-0000-000000000000'.

.EXAMPLE 
Remove-Record -setName 'accounts' -id '00000000-0000-0000-0000-000000000000'

This example deletes the account record with the specified GUID. 

#>
function Remove-Record {
   param (
      [Parameter(Mandatory)] 
      [String]
      # The table set name (EntityMetadata.EntitySetName property)
      $setName,
      [Parameter(Mandatory)] 
      [Guid] 
      # The GUID primary key value of the record to delete
      $id
   )
   $uri = $environmentUrl + 'api/data/v9.2/' + $setName
   $uri = $uri + '(' + $id.Guid + ')'

   $DeleteRequest = @{
      Uri     = $uri
      Method  = 'Delete'
      Headers = $baseHeaders
   }
   Invoke-RestMethod @DeleteRequest
}

<# 
.SYNOPSIS 
Gets the error details from a Dataverse Web API HTTP response exception.

.DESCRIPTION 
The Get-Error-Details function takes an exception object from the pipeline and extracts the status code, error code, and error message from it. 
It assumes that the exception object is of type Microsoft.PowerShell.Commands.HttpResponseException and that the error details are in JSON format. 
It returns a custom object with the status code, error code, and error message as properties.

.PARAMETER 
Exception The exception object from the pipeline. 
It should be of type Microsoft.PowerShell.Commands.HttpResponseException and have the ErrorDetails property populated with a JSON string.

.EXAMPLE 
Connect-Device-Code -uri 'https://yourorg.crm.dynamics.com/'
try {
   (Get-Records `
   -setName accounts `
   -query '?$select=names&$top=3').value | 
Format-Table -Property name, accountid
}
catch [Microsoft.PowerShell.Commands.HttpResponseException] {
   Get-Error-Details | Format-List 
} 

Connected to https://yourorg.crm.dynamics.com/
Token will expire in 30 minutes.
                                                                                                                        
statuscode : BadRequest
code       : 0x0
message    : Could not find a property named 'names' on type 'Microsoft.Dynamics.CRM.account'.
#>
function Get-Error-Details {
   try {
      $statuscode = $_.Exception.StatusCode
      $code = $null
      $message = $null
      if ((!$null -eq $_.ErrorDetails.Message) -and (Test-Json $_.ErrorDetails.Message) ) {
         $json = $_.ErrorDetails.Message | ConvertFrom-Json
         $code = $json.error.code
         $message = $json.error.message
      }
      return [PSCustomObject]@{
         statuscode = $statuscode
         code       = $code
         message    = $message
      }
   }
   catch {
      throw $_
   }
}
```

1. Copy this script into a file named `myDVWebAPIFunctions.ps1` and save it.
1. Open the `myDVWebAPIFunctions.ps1` file using Visual Studio Code.
1. Press <kbd>F5</kbd> to save and run the script.

## Create a script file for testing

1. In the Visual Studio Code menu, select **File** > **New Text File**, or use the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>N</kbd>.

   By default, this file is **Plain Text** file.

1. Select the **Select a Language** prompt to select a language, or use the **Language Mode Selector** on the right hand of the **Status Bar** to select **PowerShell (powershell)**.
1. Copy the following script and paste it into the new file.

   ```powershell
   Connect-Device-Code -uri 'https://yourorg.crm.dynamics.com/'
   try {
      # Try WhoAmI
      Write-Host 'Call WhoAmI:'
      Get-WhoAmI | Format-List -Property BusinessUnitId, UserId, OrganizationId

      # Retrieve Records
      Write-Host 'Retrieve first three account records:'
      (Get-Records `
         -setName accounts `
         -query '?$select=name&$top=3').value | 
      Format-Table -Property name, accountid

      # Create a record
      Write-Host 'Create an account record:'
      $newAccountID = New-Record `
      -setName accounts `
      -body @{
         name                = 'Example Account'; 
         accountcategorycode = 1 # Preferred
      }
      Write-Host "Account with ID $newAccountID created"

      # Retrieve a record
      Write-Host 'Retrieve the created record:'
      Get-Record `
      -setName  accounts `
      -id $newAccountID.Guid '?$select=name,accountcategorycode' |
      Format-List -Property name,
      accountid,
      accountcategorycode,
      accountcategorycode@OData.Community.Display.V1.FormattedValue

      # Update a record
      Write-Host 'Update the record'
      $updateAccountData = @{
         name                = 'Updated Example account';
         accountcategorycode = 2; #Standard
      }
      Update-Record `
      -setName accounts `
      -id $newAccountID.Guid `
      -body $updateAccountData
      Write-Host 'Retrieve the updated the record:'
      Get-Record `
      -setName accounts `
      -id  $newAccountID.Guid `
      -query '?$select=name,accountcategorycode' |
      Format-List -Property name,
      accountid,
      accountcategorycode,
      accountcategorycode@OData.Community.Display.V1.FormattedValue

      # Delete a record
      Write-Host 'Delete the record:'
      Remove-Record `
      -setName accounts `
      -id $newAccountID.Guid
      Write-Host "The account with ID $newAccountID was deleted"
   }
   catch [Microsoft.PowerShell.Commands.HttpResponseException] {

      Write-Host "An error occurred calling Dataverse:" -ForegroundColor Red
      Get-Error-Details | Format-List 

   }
   catch {
      
      Write-Host "An error occurred in the script:" -ForegroundColor Red
      Write-Host $_
   }
   ```

## Run the script

1. Change the first line to use the URL for your environment instead of 'https://yourorg.crm.dynamics.com/'.
1. Press <kbd>F5</kbd> to debug your script file.

   > [!NOTE]
   > This will not save your script. It isn't necessary to save this file to use it for ad-hoc testing.

1. The first time you run the script, you need to sign in using a web browser. You see output like the following:

   ```powershell
   To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code A57834N7J to authenticate.
   ```

1. Copy the code value, in this example `A57834N7J`, and then select the [https://microsoft.com/devicelogin](https://microsoft.com/devicelogin) link to open the page.

   The page displays a series of dialogs to capture the information necessary to authenticate. You have options to sign in different ways. For example, your organization might require multifactor authentication.

1. At the final page, you can close the window

   :::image type="content" source="media/web-api-ps-final-5.png" alt-text="Sign-in complete page":::

1. After you authenticate, the script will complete. You should see output like the following:

   ```powershell
   Call WhoAmI:

   BusinessUnitId : 946986fe-ae36-4b86-a17e-b7815e3c881b
   UserId         : 2979a124-067d-4e7e-ada2-e7df09549908
   OrganizationId : 9e43d5ea-a042-41c0-bb44-a630fb0dd021

   Retrieve first three account records:

   name                   accountid
   ----                   ---------
   Adatum Corporation     4b757ff7-9c85-ee11-8179-000d3a9933c9
   Adventure Works Cycles 2ada33e7-ef8b-ee11-8179-000d3a9933c9
   Alpine Ski House       2eda33e7-ef8b-ee11-8179-000d3a9933c9

   Create an account record:
   Account with ID  3a1cb908-af90-ee11-8179-000d3a993550 created
   Retrieve the created record:

   name                                                          : Example Account
   accountid                                                     : 3a1cb908-af90-ee11-8179-000d3a993550
   accountcategorycode                                           : 1
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Preferred Customer

   Update the record

   Retrieve the updated the record:

   name                                                          : Updated Example account
   accountid                                                     : 3a1cb908-af90-ee11-8179-000d3a993550
   accountcategorycode                                           : 2
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Standard

   Delete the record:

   The account with ID 3a1cb908-af90-ee11-8179-000d3a993550 was deleted
   ```

1. Press <kbd>F5</kbd> to debug your script file again.

   This time, you don't need to sign in because you already signed in.

## How does it work?

TODO: Explain how it works

## Troubleshooting

This section contains some guidance for issues you might encounter.

### Error: "az : The term 'az' is not recognized as the name of a cmdlet, function, script file, or operable program."

You need to install the [Azure CLI](/cli/azure/install-azure-cli).

### Nothing happens when I press <kbd>F5</kbd> to debug the script

Press the <kbd>F Lock</kbd> key to toggle function on your keyboard.

### The login script hangs

The script in [Run the script](#run-the-script) doesn't respond. There is no error.

This will happen if you haven't installed the Azure CLI `account` extension.
   
In a PowerShell terminal, run `az extension add --name account`, then try again.

Or, in the terminal enter `az account tenant list`. This will prompt you to consent to install the extension. [Learn more about dynamic installation of Azure CLI extensions](/cli/azure/azure-cli-extensions-overview#install-extensions-automatically)

### Error: Invoke-RestMethod : Object reference not set to an instance of an object.

In the [Retrieve Records](#retrieve-records) section you may encounter this error:

```powershell
PS C:\Users\you.Domain> Get-Records accounts '?$select=name&$top=3'
PS C:\Users\you.Domain> 
Invoke-RestMethod : Object reference not set to an instance of an object.
At C:\test\myDVWebAPICommands.ps1:54 char:4
+    Invoke-RestMethod @RetrieveMultipleRequest
+    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Invoke-RestMethod], NullReferenceException
    + FullyQualifiedErrorId : System.NullReferenceException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
```

This is because earlier versions of PowerShell didn't support [splatting](/powershell/module/microsoft.powershell.core/about/about_splatting) parameters to the `Invoke-RestMethod` command. To resolve this, [install PowerShell 7.4 or higher](/powershell/scripting/install/installing-powershell)

### Error: Get-Record: Cannot process argument transformation on parameter 'id'. Cannot convert null to type "System.Guid".

You can get this error for the functions that accept an `id` parameter when the value of the parameter is null.

### Error dialog: connect ENOENT\\\\.\\pipe\\&lt;RANDOM_text&gt; with Open 'launch.json' button

This error might occur at times when debugging using Visual Studio code. To resolve, press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>, type `restart` and select `Powershell: Restart session`. See [PowerShell/vscode-powershell GitHub Issue 4332](https://github.com/PowerShell/vscode-powershell/issues/4332) for more information.


## Next steps

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)

### Related articles

[Use the Microsoft Dataverse Web API](overview.md)   
[PowerShell in Visual Studio Code](https://code.visualstudio.com/docs/languages/powershell)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

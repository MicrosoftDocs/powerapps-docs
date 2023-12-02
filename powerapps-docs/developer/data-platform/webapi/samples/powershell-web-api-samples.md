---
title: "Sample: PowerShell functions using Dataverse Web API"
description: "This sample demonstrates how to authenticate to Dataverse and perform data operations using PowerShell with the Dataverse Web API."
ms.date: 12/01/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---
# Sample: PowerShell functions using Dataverse Web API

The following PowerShell script contains the functions defined in [Quick Start: Web API with PowerShell](../quick-start-ps.md). See this article for details about the functions.

## Prereqisites

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
- Url to the Dataverse environment you want to connect to. See [View developer resources](../../view-download-developer-resources.md)
- Basic understanding of the PowerShell scripting language

## Functions

This file contains a set of reusable functions you can use in your scripts to perform data operations using Dataverse Web API.

```powershell
$environmentUrl = 'https://yourorg.crm.dynamics.com/' # change this

## login if not already logged in
if ($null -eq (az account tenant list  --only-show-errors)) {
   az login --allow-no-subscriptions --use-device-code | Out-Null
}
# get token
$token = az account get-access-token --resource=$environmentUrl --output json
$tokenObj = $token | ConvertFrom-Json
# get minutes to token expiration
$minutesToTokenExpire = (New-TimeSpan -End ([DateTime]$tokenObj.expiresOn)).Minutes
Write-Host "Token will expire in $minutesToTokenExpire minutes."
# get accessToken
$accessToken = $tokenObj.accessToken

Write-Host "Connected to $environmentUrl"

# Define common set of headers
$baseHeaders = @{
   'Authorization'    = "Bearer $accessToken"
   'Accept'           = 'application/json'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}

# WhoAmI message
function Get-WhoAmI {
   $WhoAmIRequest = @{
      Uri     = $environmentUrl + 'api/data/v9.2/WhoAmI'
      Method  = 'Get'
      Headers = $baseHeaders
   }
   Invoke-RestMethod @WhoAmIRequest
}

# Retrieve records that match a query
function Get-Records {
   param (
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] [String] $query
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

# Create a record
function New-Record {
   param (
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] $body
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

# Retrieve a record using the primary key
function Get-Record {
   param (
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] [Guid] $id,
      [String] $query
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

# Update a record
function Update-Record {
   param (
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] [Guid] $id,
      [Parameter(Mandatory)] $body
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

# Delete a record
function Remove-Record {
   param (
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] [Guid] $id
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

# Captures relevant Dataverse Web API error information
function Get-Error-Details {
   try {
      $statuscode = $_.Exception.StatusCode
      $json = $_.ErrorDetails.Message | ConvertFrom-Json
      return [PSCustomObject]@{
         statuscode = $statuscode
         code       = $json.error.code
         message    = $json.error.message
      }
   }
   catch {
      throw $_
   }
}
```

## Using the functions

The following PowerShell script demonstrates using the functions defined in [Functions](#functions).

```powershell
try {
   # Try WhoAmI
   Write-Output 'Call WhoAmI:'
   Get-WhoAmI | Format-List -Property BusinessUnitId, UserId, OrganizationId

   # Retrieve Records
   Write-Output 'Retrieve first three account records:'
   (Get-Records -setName accounts -query '?$select=name&$top=3').value | Format-Table -Property name, accountid

   # Create a record
   Write-Output 'Create an account record:'
   $newAccountID = New-Record -setName accounts -body @{
      name                = 'Example Account'; 
      accountcategorycode = 1 # Preferred
   }
   Write-Output "Account with ID $newAccountID created"

   # Retrieve a record
   Write-Output 'Retrieve the created record:'
   Get-Record -setName  accounts -id $newAccountID.Guid '?$select=name,accountcategorycode' |
   Format-List -Property name,
   accountid,
   accountcategorycode,
   accountcategorycode@OData.Community.Display.V1.FormattedValue

   # Update a record
   Write-Output 'Update the record'
   $updateAccountData = @{
      name                = 'Updated Example account';
      accountcategorycode = 2; #Standard
   }
   Update-Record -setName accounts -id $newAccountID.Guid -body $updateAccountData
   Write-Output 'Retrieve the updated the record:'
   Get-Record -setName accounts -id  $newAccountID.Guid -query '?$select=name,accountcategorycode' |
   Format-List -Property name,
   accountid,
   accountcategorycode,
   accountcategorycode@OData.Community.Display.V1.FormattedValue

   # Delete a record
   Write-Output 'Delete the record:'
   Remove-Record -setName accounts -id $newAccountID.Guid
   Write-Output "The account with ID $newAccountID was deleted"
}
catch [Microsoft.PowerShell.Commands.HttpResponseException] {

   Write-Host "An error occurred calling Dataverse:" -ForegroundColor Red
   Get-Error-Details | Format-List 

}
catch {
   
   Write-Host "An error occurred in the script:" -ForegroundColor Red
   Write-Output $_
}
```

The expected output to the terminal for this script is something like this:

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

### Related articles

[Quick Start: Web API with PowerShell](../quick-start-ps.md)   
[Perform operations using the Web API](../perform-operations-web-api.md)   
[PowerShell in Visual Studio Code](https://code.visualstudio.com/docs/languages/powershell)
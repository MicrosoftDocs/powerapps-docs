---
title: Quick Start Web API with PowerShell
description: Decribes how to use Web API from PowerShell
ms.date: 11/17/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Quick Start: Web API with PowerShell

In this quick start you will run a PowerShell script that uses Dataverse Web API to invoke the [WhoAmI Function](xref:Microsoft.Dynamics.CRM.WhoAmI). This function retrieves information about the logged on Dataverse user. Once you understand the basic functionality described here, you can move onto other Web API operations such as create, retrieve, update, and deletion of Dataverse table rows.

This script uses an access token generated using the Azure CLI [az account get-access-token command](/cli/azure/account?view=azure-cli-latest#az-account-get-access-token) based on the Azure account credentials you use with the [az login command](/cli/azure/reference-index?view=azure-cli-latest#az-login). This access token has the necessary delegated permissions to connect to Dataverse. You don't need to register an application to use the Web API with PowerShell.

## Prerequisites

- PowerShell 6.x or higher. See [Install PowerShell on Windows, Linux, and macOS](/powershell/scripting/install/installing-powershell)
- Azure CLI installed. See [How to install the Azure CLI](/cli/azure/install-azure-cli)
- Internet connection
- Valid user account for a Dataverse environment
- Url to the Dataverse environment you want to connect with
- Basic understanding of the PowerShell scripting language.

## Try WhoAmI

1. Copy this snippet in to VS Code, or the text editor of your choice

   ```powershell
   $environmentUrl = "https://yourorg.crm.dynamics.com/" # change this
   $userName = "you@yourorg.onmicrosoft.com"             # change this
   $password = "password"                                # change this
   # Login to Azure
   az login -u $userName -p $password | Out-Null
   # Get an access token
   $token = (az account get-access-token --resource=$environmentUrl --query accessToken --output tsv)
   
   # Define a function to call the WhoAmI message
   function Get-WhoAmI {
      param (
         [Parameter(Mandatory)] [String] $token
      )
   $headers = @{
      "Authorization" = "Bearer $token"
      "OData-MaxVersion" = "4.0"
      "OData-Version" = "4.0"
      }
   $WhoAmIRequest = @{
      Uri = "${environmentUrl}"+"api/data/v9.2/WhoAmI"
      Method = 'GET'
      Headers = $headers
      }
   return Invoke-RestMethod @WhoAmIRequest
   }
   
   # Invoke the GetWhoAmI function
   Get-WhoAmI $token | ConvertTo-Json
   ```

1. Edit the `$environmentUrl`, `$userName` and `$password` variables to match the Dataverse environment you want to connect with and the credentials to use.
1. Open a PowerShell 7 terminal window. You may want to use the Visual Studio Code terminal window.
1. Paste the edited code snippet into the terminal window and press enter.

   You can expect output like the following:

   ```
   PS C:\Users\you.Domain> Get-WhoAmI $token | ConvertTo-Json
   {
      "@odata.context":  "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
      "BusinessUnitId":  "38e0dbe4-131b-e111-ba7e-78e7d1620f5e",
      "UserId":  "4026be43-6b69-e111-8f65-78e7d1620f5e",
      "OrganizationId":  "883278f5-07af-45eb-a0bc-3fea67caa544"
   }
   PS C:\Users\you.Domain>
   ```

## Create a record

```powershell
function New-Record {
   param (
      [Parameter(Mandatory)] [String] $token,
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] $body
   )
   $headers = @{
      "Authorization"    = "Bearer $token"
      "OData-MaxVersion" = "4.0"
      "OData-Version"    = "4.0"
      "Content-Type"     = "application/json"
   }
   $CreateRequest = @{
      Uri     = "${environmentUrl}" + "api/data/v9.2/" + $setName
      Method  = 'POST'
      Headers = $headers
      Body    = ConvertTo-Json $body
   }
   Invoke-RestMethod @CreateRequest  -ResponseHeadersVariable rh
   $url = $rh["OData-EntityId"]
   $selectedString = Select-String -InputObject $url -Pattern "(?<=\().*?(?=\))"
   return $selectedString.Matches.Value.ToString()
}
```

## Retrieve a record

```powershell
function Get-Record {
   param (
      [Parameter(Mandatory)] [String] $token,
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] [String] $id,
      [String] $query
   )
   $headers = @{
      "Authorization"    = "Bearer $token"
      "OData-MaxVersion" = "4.0"
      "OData-Version"    = "4.0"
   }
   $RetrieveRequest = @{
      Uri     = "${environmentUrl}" + "api/data/v9.2/" + $setName + "(" + $id + ")" + $query
      Method  = 'GET'
      Headers = $headers
   }
   Invoke-RestMethod @RetrieveRequest 
}
```

## Update a record

```powershell
function Update-Record {
   param (
      [Parameter(Mandatory)] [String] $token,
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] [guid] $id,
      [Parameter(Mandatory)] $body
   )
   $headers = @{
      "Authorization"    = "Bearer $token"
      "OData-MaxVersion" = "4.0"
      "OData-Version"    = "4.0"
      "Content-Type"     = "application/json"
      "If-Match"         = "*" # Prevent Create
   }
   $UpdateRequest = @{
      Uri     = "${environmentUrl}" + "api/data/v9.2/" + $setName
      Method  = 'PATCH'
      Headers = $headers
      Body    = ConvertTo-Json $body
   }
   Invoke-RestMethod @UpdateRequest 
}
```

## Delete a record






## Next steps


Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

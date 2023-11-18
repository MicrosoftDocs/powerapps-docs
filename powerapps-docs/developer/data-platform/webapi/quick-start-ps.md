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

- PowerShell 6.x or higher
- Internet connection
- Valid user account for a Dataverse environment
- Url to the Dataverse environment you want to connect with
- Basic understanding of the PowerShell scripting language.

## Try it

In this interactive snippet you need to edit the `$environmentUrl` variable to match the Dataverse environment you want to connect with.

```azurepowershell-interactive
$environmentUrl = "https://yourorg.crm.dynamics.com/"
az login | Out-Null
$token = (az account get-access-token --resource=$environmentUrl --query accessToken --output tsv)
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
```


## Next steps


Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

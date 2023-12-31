---
title: Quick Start Web API with PowerShell
description: Describes how to interactively authenticate and use the Dataverse Web API from PowerShell
ms.date: 01/05/2024
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---
# Quick Start Web API with PowerShell

In this quick start, learn how to:

- Use Visual Studio Code with PowerShell to interactively authenticate with Dataverse without registering an application.
- Compose requests to the Dataverse Web API using the PowerShell [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod).

> [!NOTE]
> This Quick Start article provides only an introduction of the basic concepts. This should be enough for basic testing. [Use PowerShell and Visual Studio Code with the Dataverse Web API](use-ps-and-vscode-web-api.md) builds on this introduction to describe more advanced capabilities to be more productive:
> 
> - Interactive auto-login
> - Handling exceptions
> - Patterns to create reusable functions
> - Manage Dataverse Service protection limits
>
> The instructions below should work for Windows, Linux, and macOS, but these steps have only been tested on Windows. If changes are needed, please let us know using the **Feedback** section at the bottom of this article.

## Prerequisites

Do not proceed without confirming each of the following prerequisites have been met.

### Install or verify that the following are installed

- Install Visual Studio Code. See [Download Visual Studio Code](https://code.visualstudio.com/download)
- Install the PowerShell extension for Visual Studio Code. See [PowerShell for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)
- Install PowerShell 7.4 or higher. See [Install PowerShell on Windows, Linux, and macOS](/powershell/scripting/install/installing-powershell)
- Install Azure CLI version 2.54.0 or higher. See [How to install the Azure CLI](/cli/azure/install-azure-cli)
- Install the Azure Powershell AZ module. [How to install Azure PowerShell](/powershell/azure/install-azure-powershell)

### Verify installation

1. Open Visual Studio Code.
1. In the **Terminal** menu, select **New Terminal**.
1. In Visual Studio Code navigation pane, select the :::image type="icon" source="media/visual-studio-code-powershell-extension-icon.png" border="false"::: icon for the PowerShell extension.
1. Copy and paste the following in the Visual Studio Code terminal:

   ```powershell
   Write-Host 'PowerShell Version:'
   $PSVersionTable.PSVersion.ToString()
   Write-Host 'Azure CLI Version:'
   az version --output table
   Write-Host 'PowerShell Az version:'
   (Get-InstalledModule Az).Version
   ```

1. Press <kbd>Enter</kbd>. The output should resemble the following:

   ```powershell
   PowerShell Version:
   7.4.0
   Azure CLI Version:
   Azure-cli    Azure-cli-core    Azure-cli-telemetry
   -----------  ----------------  ---------------------
   2.55.0       2.55.0            1.1.0
   PowerShell Az version:
   11.1.0
   ```


### You will also need the following

- Valid user account for a Dataverse environment
- Url to the Dataverse environment you want to connect to. See [View developer resources](../view-download-developer-resources.md) to learn how to find it. It looks something like this: `https://yourorg.crm.dynamics.com/`
- Basic understanding of the PowerShell scripting language

## Try it

For this quick start, you can use either the **Azure CLI** or **Powershell AZ**  PowerShell scripts below. The details for both scripts are described in the [How it works](#how-it-works) section.

### [Azure CLI](#tab/azurecli)

```powershell
$environmentUrl = 'https://yourorg.crm.dynamics.com/' # change this
# Login to Azure
az login --allow-no-subscriptions | Out-Null
# Get an access token
$token = (az account get-access-token --resource $environmentUrl --query accessToken --output tsv)
# Common headers
$headers = @{
   'Authorization'    = 'Bearer ' + $token
   'Accept'           = 'application/json'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}
# Invoke WhoAmI Function
Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Method Get -Headers $headers
| ConvertTo-Json
```

### [Powershell AZ](#tab/powershellaz)

```powershell
$environmentUrl = 'https://yourorg.crm.dynamics.com/' # change this
# Login to Azure
Connect-AzAccount | Out-Null
# Get an access token
$token = (Get-AzAccessToken -ResourceUrl $environmentUrl).Token
# Common headers
$headers = @{
   'Authorization'    = 'Bearer ' + $token
   'Accept'           = 'application/json'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}
# Invoke WhoAmI Function
Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Method Get -Headers $headers
| ConvertTo-Json
```

---

1. In Visual Studio Code, select **File** > **New Text File**, or <kbd>Ctrl</kbd>+<kbd>N</kbd> to open a new file.

   You don't need to save the file.

1. Copy and paste either the **Azure CLI** or **Powershell AZ**  PowerShell scripts above in the new file.

   Visual Studio Code should automatically recognize it is a PowerShell script.

1. Edit the `$environmentUrl` variable to match your Dataverse environment URL.
1. Press <kbd>F5</kbd>, or use the Visual Studio Code **Run** > **Start Debugging** menu command instead.

   A browser window will open. Enter or select the credentials you want to use to authenticate.

1. Verify the output in the Visual Studio Code terminal window

   Some of the output is different depending on the script you use.

   The **Azure CLI** script will have this warning:

   ```powershell
   WARNING: A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
   ```

   The **Powershell AZ** script may have this warning:

   ```powershell
   WARNING: TenantId '<your tenant id>' contains more than one active subscription. First one will be selected for further use. To select another subscription, use Set-AzContext. 
   To override which subscription Connect-AzAccount selects by default, use `Update-AzConfig -DefaultSubscriptionForLogin 00000000-0000-0000-0000-000000000000`. Go to https://go.microsoft.com/fwlink/?linkid=2200610 for more information.
   ```
   
   Both scripts should return the [WhoAmIResponse complex type](xref:Microsoft.Dynamics.CRM.WhoAmIResponse) expected for the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI). It should look something like this:

   ```json
   {
   "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
   "BusinessUnitId": "639dea3c-505c-4c3a-b8b5-d916cb507e1e",
   "UserId": "d2159662-498a-406b-83cd-f515b7e561d6",
   "OrganizationId": "83e197ed-ede1-4886-81f2-f41fe9395297"
   }
   ```

## How it works

This section describes the details of the **Azure CLI** and **Powershell AZ**  PowerShell scripts included in the [Try it section](#try-it).

### Authentication

You can authenticate with Dataverse using either Azure CLI or the Powershell AZ module. For this quick start, we are presenting both ways so you can compare. Use whichever shortens your learning curve. [Learn more about choosing the right Azure command-line tool](/cli/azure/choose-the-right-azure-command-line-tool)

The differences are in the following table:

|Azure CLI|Powershell AZ|Description|
|---------|---------|---------|
|[az login](/cli/azure/reference-index#az-login)|[Connect-AzAccount](/powershell/module/az.accounts/connect-azaccount)|Opens a browser to accept credentials to login to Azure.|
|[az account get-access-token](/cli/azure/account#az-account-get-access-token)|[Get-AzAccessToken](/powershell/module/az.accounts/get-azaccesstoken)|Generates an access token you can use to perform Dataverse operations.|


Either of the scripts above will set the `$token` variable with an access token you can use to authenticate with the Dataverse Web API.

### Use `Invoke-RestMethod` with the WhoAmI function

Once you have an access token set to the `$token` variable, you need to compose the request to Dataverse Web API and send it using the [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod)

#### Set headers

All Dataverse Web API requests must include a set of common HTTP request headers, including a `Authorization` header that includes the access token value. Some operations require additional headers, but the following are the minimum. [Learn more about Dataverse Web API request headers](/power-apps/developer/data-platform/webapi/compose-http-requests-handle-errors#http-headers)

```powershell
# Common headers
$headers = @{
   'Authorization'    = 'Bearer ' + $token
   'Accept'           = 'application/json'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}
```

#### Send the Request

The [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) is one of the simplest Dataverse operations you can perform. Because it is an OData *function* rather than an *action*, it requires the `GET` HTTP method. [Learn more about Web API functions](/power-apps/developer/data-platform/webapi/use-web-api-functions)

Use the [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod) `Uri`, `Method`, and `Headers` parameters to send this request.

```powershell
# Invoke WhoAmI Function
Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Method Get -Headers $headers
| ConvertTo-Json
```

For operations that use `POST` or `PATCH` HTTP methods, set use the `Body` parameter to send the JSON payload.

The [ConvertTo-Json cmdlet](/powershell/module/microsoft.powershell.utility/convertto-json) converts the object to a JSON-formatted string that is easy to see in the terminal.

## Troubleshooting

Make sure you have verified all the required programs are installed as described in [Verify installation](#verify-installation).

The following are situations that can cause this to fail:

### Nothing happens when I press <kbd>F5</kbd>

Make sure that your function keys are enabled on your keyboard by pressing the <kbd>F-Lock</kbd>,<kbd>Fn Lock</kbd>, or <kbd>Function Lock</kbd> key on your keyboard.

You can also use the Visual Studio Code **Run** > **Start Debugging** menu command instead.

### No such host is known

If you see this error after running the script:

   ```powershell
   Invoke-RestMethod: untitled:Untitled-1:14:1
   Line |
   14 |  Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Me …
      |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      | No such host is known.
   ```

Check that the `$environmentUrl` represents an environment you have access to.

### The user is not a member of the organization

If you see this error after running the script:

   ```powershell
   Invoke-RestMethod: untitled:Untitled-1:14:1                                                                             
   Line |
   14 |  Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Me …
      |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |  {   "error": {     "code": "0x80072560",     "message": "The user is not a member of the organization."   } }
   ```

Make sure that the account you select in the browser window is that account that has access to the Dataverse environment.

## Next steps

Now that you have the ability to authenticate and send Dataverse Web API requests using PowerShell, you can try other Web API operations.

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)

Learn more advanced capabilities to be more productive using PowerShell and Visual Studio Code with the Dataverse Web API, such as:

- Interactive auto-login
- Handling exceptions
- Patterns to create reusable functions
- Manage Dataverse Service protection limits

> [!div class="nextstepaction"]
> [Use PowerShell and Visual Studio Code with the Dataverse Web API](use-ps-and-vscode-web-api.md)

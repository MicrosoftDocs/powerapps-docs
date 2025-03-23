---
title: Quick Start Web API with PowerShell and Visual Studio Code
description: Describes how to interactively authenticate and use the Dataverse Web API from PowerShell with Visual Studio Code
ms.topic: quickstart
ms.date: 03/22/2025
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
---
# Quick Start Web API with PowerShell and Visual Studio Code

PowerShell is a powerful scripting language that can automate repetitive tasks and streamline workflows, making it an ideal tool for integrating with Dataverse. This quick start focuses on helping you get started using PowerShell with the Dataverse Web API in Visual Studio Code. Visual Studio Code with PowerShell provides an alternative to using API clients like Postman or [Insomnia](insomnia.md).

In this quick start, learn how to:

- Use Visual Studio Code with PowerShell to interactively authenticate with Dataverse without registering an application.
- Compose requests to the Dataverse Web API using the PowerShell [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod).

> [!NOTE]
> This Quick Start article only introduces basic concepts. This should be enough for basic testing. After your complete the steps in this article, go to  [Use PowerShell and Visual Studio Code with the Dataverse Web API](use-ps-and-vscode-web-api.md) to learn more advanced capabilities that will make you more productive, such as how to:
> 
> - [Create reusable functions](use-ps-and-vscode-web-api.md#create-reusable-functions)
> - [Handle exceptions](use-ps-and-vscode-web-api.md#handle-exceptions)
> - [Manage Dataverse service protection limits](use-ps-and-vscode-web-api.md#manage-dataverse-service-protection-limits)
> - [Debug using Fiddler](use-ps-and-vscode-web-api.md#debug-using-fiddler)
> - [Download the Dataverse Web API CSDL $metadata document](use-ps-and-vscode-web-api.md#download-the-dataverse-web-api-csdl-metadata-document)
>
> The instructions in this article should work for Windows, Linux, and macOS, but these steps have only been tested on Windows. If changes are needed, please let us know using the **Feedback** section at the bottom of this article.

## Prerequisites

Don't proceed without confirming each of the following prerequisites are met.

[!INCLUDE [cc-visual-studio-code-powershell-prerequisites](../includes/cc-visual-studio-code-powershell-prerequisites.md)]

## Try it

1. In Visual Studio Code, select **File** > **New Text File**, or <kbd>Ctrl</kbd>+<kbd>N</kbd> to open a new file.

   You don't need to save the file.

1. Copy and paste the following script into the new file.

   ```powershell
   $environmentUrl = 'https://yourorg.crm.dynamics.com/' # change this
   ## Login if not already logged in
   if ($null -eq (Get-AzTenant -ErrorAction SilentlyContinue)) {
      Connect-AzAccount | Out-Null
   }

   # Get an access token
   $secureToken = (Get-AzAccessToken `
      -ResourceUrl $environmentUrl `
      -AsSecureString).Token

   # Convert the secure token to a string
   $token = ConvertFrom-SecureString `
      -SecureString $secureToken `
      -AsPlainText


   # Common headers
   $baseHeaders = @{
      'Authorization'    = 'Bearer ' + $token
      'Accept'           = 'application/json'
      'OData-MaxVersion' = '4.0'
      'OData-Version'    = '4.0'
   }
   # Invoke WhoAmI Function
   Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Method Get -Headers $baseHeaders
   | ConvertTo-Json
   ```

   Visual Studio Code should automatically detect it's a PowerShell script.

1. Edit the `$environmentUrl` variable value (`https://yourorg.crm.dynamics.com/`) to match your Dataverse environment URL.
1. Press <kbd>F5</kbd>, or use the Visual Studio Code **Run** > **Start Debugging** menu command.

   A browser window opens. In the browser window, enter or select the credentials you want to use to authenticate.

1. Verify the output in the Visual Studio Code terminal window.

   At the bottom of the terminal, find the [WhoAmIResponse complex type](xref:Microsoft.Dynamics.CRM.WhoAmIResponse) value expected for the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI). It should look something like this:

   ```json
   {
   "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
   "BusinessUnitId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
   "UserId": "22cc22cc-dd33-ee44-ff55-66aa66aa66aa",
   "OrganizationId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
   }
   ```

1. In the terminal window, type `cls` to clear the terminal content.
1. Press <kbd>F5</kbd>, or use the Visual Studio Code **Run** > **Start Debugging** menu command to run the script again.

   Because you're already logged in, the browser window doesn't open. You can continue to edit and run your script to try different requests.

## How it works

This section describes the details of the PowerShell script included in the [Try it section](#try-it).

### Authentication

The script uses the Az PowerShell module [Get-AzTenant](/powershell/module/az.accounts/get-aztenant) command to get tenants authorized for the current user. When you aren't logged in, this command returns an error. This script uses the `-ErrorAction SilentlyContinue` parameter to ignore the error and nothing is returned.

When the `Get-AzTenant` command doesn't return anything, the script uses the [Connect-AzAccount](/powershell/module/az.accounts/connect-azaccount) 
to open an interactive browser window where you can enter or select your credentials to sign in. [Learn more about signing into Azure PowerShell interactively](/powershell/azure/authenticate-interactive) or [noninteractively with a service principal](/powershell/azure/authenticate-noninteractive).

Finally, the script uses the [Get-AzAccessToken](/powershell/module/az.accounts/get-azaccesstoken) command with the `-ResourceUrl $environmentUrl` to get a 
[PSAccessToken](/dotnet/api/microsoft.azure.commands.profile.models.psaccesstoken) instance, which contains a SecureString [Token](/dotnet/api/microsoft.azure.commands.profile.models.psaccesstoken.token#microsoft-azure-commands-profile-models-psaccesstoken-token) property that you can convert into an access token you can use to authenticate with Dataverse.

When you want to connect with a different set of credentials, you need to use the [Disconnect-AzAccount](/powershell/module/az.accounts/disconnect-azaccount) command.

### Use `Invoke-RestMethod` with the WhoAmI function

Once you have an access token set to the `$token` variable, you need to compose the request to Dataverse Web API and send it using the [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod)

#### Set headers

All Dataverse Web API requests must include a set of common HTTP request headers, including a `Authorization` header that includes the access token value. Some operations require more headers. [Learn more about Dataverse Web API request headers](/power-apps/developer/data-platform/webapi/compose-http-requests-handle-errors#http-headers)

```powershell
# Common headers
$baseHeaders = @{
   'Authorization'    = 'Bearer ' + $token
   'Accept'           = 'application/json'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}
```

#### Send the Request

The [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) is one of the simplest Dataverse operations you can perform. Because it's an OData *function* rather than an *action*, it requires the `GET` HTTP method. [Learn more about Web API functions](/power-apps/developer/data-platform/webapi/use-web-api-functions)

Use the [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod) `Uri`, `Method`, and `Headers` parameters to send this request.

```powershell
# Invoke WhoAmI Function
Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Method Get -Headers $baseHeaders
| ConvertTo-Json
```

For operations that use `POST` or `PATCH` HTTP methods, set use the `Body` parameter to send the JSON payload.

The [ConvertTo-Json cmdlet](/powershell/module/microsoft.powershell.utility/convertto-json) converts the object returned to a JSON-formatted string that is easy to see in the terminal.

If you want to capture only the `UserId` property of the response, you can use the following script instead:

```powershell
# Get UserId
$userId = (
   Invoke-RestMethod `
   -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') `
   -Method 'Get' `
   -Headers $baseHeaders
   ).UserId
Write-Host $userId
```

## Troubleshooting

Make sure you verify all the required programs are installed as described in [Verify installation](#verify-installation).

The following are situations that can cause the instructions in this quick start to fail:

### Nothing happens when I press <kbd>F5</kbd>

Make sure that your function keys are enabled on your keyboard by pressing the <kbd>F-Lock</kbd>, <kbd>Fn Lock</kbd>, or <kbd>Function Lock</kbd> key on your keyboard.

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

Check that the `$environmentUrl` represents an environment you have access to. Make sure you changed it from the default value (`https://yourorg.crm.dynamics.com/`).

### The user is not a member of the organization

If you see this error after running the script:

   ```powershell
   Invoke-RestMethod: untitled:Untitled-1:14:1                                                                             
   Line |
   14 |  Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Me …
      |  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |  {   "error": {     "code": "0x80072560",     "message": "The user is not a member of the organization."   } }
   ```

Make sure that the account you select in the browser window is that account that has access to the Dataverse environment specified by the `$environmentUrl` parameter.

If you're using a different set of credentials than you used before, use the [Disconnect-AzAccount](/powershell/module/az.accounts/disconnect-azaccount) command in the terminal window.

### WARNING: TenantId '&lt;your tenant id&gt;' contains more than one active subscription

When you run the script for the first time and login using the browser, you might get this warning:
 
 ```powershell
 WARNING: TenantId '<your tenant id>' contains more than one active subscription. First one will be selected for further use. 
 To select another subscription, use Set-AzContext. 
 To override which subscription Connect-AzAccount selects by default, use `Update-AzConfig -DefaultSubscriptionForLogin 00000000-0000-0000-0000-000000000000`. 
 Go to https://go.microsoft.com/fwlink/?linkid=2200610 for more information.
 ```

You can ignore this warning if you see it. These requests don't require a subscription.

## Next steps

Learn more advanced capabilities to be more productive using PowerShell and Visual Studio Code with the Dataverse Web API, such as how to:

- [Create reusable functions](use-ps-and-vscode-web-api.md#create-reusable-functions)
- [Handle exceptions](use-ps-and-vscode-web-api.md#handle-exceptions)
- [Manage Dataverse service protection limits](use-ps-and-vscode-web-api.md#manage-dataverse-service-protection-limits)
- [Debug using Fiddler](use-ps-and-vscode-web-api.md#debug-using-fiddler)
- [Download the Dataverse Web API CSDL $metadata document](use-ps-and-vscode-web-api.md#download-the-dataverse-web-api-csdl-metadata-document)

> [!div class="nextstepaction"]
> [Use PowerShell and Visual Studio Code with the Dataverse Web API](use-ps-and-vscode-web-api.md)

Now that you have the ability to authenticate and send Dataverse Web API requests using PowerShell, you can try other Web API operations.

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)

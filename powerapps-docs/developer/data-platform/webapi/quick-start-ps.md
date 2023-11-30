---
title: Quick Start Web API with PowerShell
description: Describes how to use the Dataverse Web API from PowerShell
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

In this quick start you will learn:

- How to authenticate to Dataverse using PowerShell without registering your own application.
- How to compose requests to the Dataverse Web API using [Invoke-RestMethod](/powershell/module/microsoft.powershell.utility/invoke-restmethod)
- How to create reusable functions that you can save in a .ps1 file.
- How to write and run a script using the functions you created.

> [!NOTE]
> This should work for Windows, Linux, and macOS, but these steps have only been tested on Windows.

## Prerequisites

- PowerShell 7.4 or higher. See [Install PowerShell on Windows, Linux, and macOS](/powershell/scripting/install/installing-powershell)
- Azure CLI version 2.54.0 or higher. See [How to install the Azure CLI](/cli/azure/install-azure-cli)
- Visual Studio Code. See [Download Visual Studio Code](https://code.visualstudio.com/download)
- Powershell extension for Visual Studio Code. See [PowerShell for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)
- Internet connection
- Valid user account for a Dataverse environment
- Url to the Dataverse environment you want to connect to. See [View developer resources](../view-download-developer-resources.md)
- Basic understanding of the PowerShell scripting language

## Authenticate to Dataverse

The first step is to authenticate and get an access token you will need to send with your requests.

You can use an access token generated using the Azure CLI [az account get-access-token command](/cli/azure/account?view=azure-cli-latest#az-account-get-access-token) based on the Azure account credentials you use with the [az login command](/cli/azure/reference-index?view=azure-cli-latest#az-login). This access token has the necessary delegated permissions to connect to Dataverse. You don't need to register an application to use the Web API with PowerShell.

1. Open Visual Studio Code.
1. In the menu, select the ellipses (...) and then select **Terminal** > **New Terminal**. Or use <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>`</kbd>.
1. Copy the following and paste it in the terminal, replacing `https://your.crm.dynamics.com/` with the url to the Dataverse environment you want to connect to.

   ```powershell
   $environmentUrl = 'https://your.crm.dynamics.com/' # change this
   az login --use-device-code --allow-no-subscriptions  | Out-Null
   $token = (az account get-access-token --resource=$environmentUrl --query accessToken --output tsv)
   ```

   > [!NOTE]
   > This example uses the device code flow as a security best practice. We don't recommend setting the user name and password, but this also works unless your organization requires multi-factor authentication. More information: [Username and Password flow](/entra/identity-platform/scenario-desktop-acquire-token-username-password)
   > 
   >    ```powershell
   >    az login -u you@yourorg.com -p yourPassword | Out-Null
   >    ```

1. Press <kbd>Enter</kbd> to run the command. You can expect an output like this:

   ```powershell
   To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code A57834N7J to authenticate.
   ```

   The `az login` command is configured to use a device code and to not require an Azure subscription. You need to login using a web browser.

1. Copy the code value, in this example `A57834N7J`, and then click the `https://microsoft.com/devicelogin` link to open the page.

   You will see a series of dialog windows. These dialogs might change over time, but the purpose is to capture the account credentials you will use to connect. This example uses a password, but you have options to sign in different ways. Your organization may require 2FA (two factor authentication) which will make your experience different.

   1. Paste the code into the **Enter code** dialog.
   
      :::image type="content" source="media/web-api-ps-enter-code-1.png" alt-text="Dialog to enter the device code":::
   
   1. Enter the account you want to use to connect in the **Sign in** dialog.
   
      :::image type="content" source="media/web-api-ps-sign-in-2.png" alt-text="Dialog to Sign-in":::
   
   1. Enter your password in the **Enter password** dialog.
   
      :::image type="content" source="media/web-api-ps-enter-password-3.png" alt-text="Dialog to enter password":::
   
   1. Select **Continue** in the **Are you trying to sign in to Microsoft Azure CLI?** dialog
   
      :::image type="content" source="media/web-api-ps-continue-4.png" alt-text="Confirm you are trying to sign in dialog":::
   
   At the final page, you can close the window
   
   :::image type="content" source="media/web-api-ps-final-5.png" alt-text="Sign-in complete page":::

1. At this point, you can type `Write-Host $token` in the terminal to see the access token value.

### Simplifying Sign in

To avoid completing the device sign-on process every time you debug your script, you can create a script that will prompt you to sign in only if you are not already signed in.

1. In Visual Studio Code, click **File** > **New Text File**, or use the <kbd>Ctrl</kbd>+<kbd>N</kbd> keyboard shortcut.
1. Paste the following into the new file, replacing `https://your.crm.dynamics.com/` with the Url to the Dataverse environment you want to connect to.

   ```powershell
   $environmentUrl = 'https://your.crm.dynamics.com/' # change this

   ## login if not already logged in
   if($null -eq (az account tenant list --only-show-errors))
   {
      az login --allow-no-subscriptions --use-device-code | Out-Null
   }
   # get token
   $token = az account get-access-token --resource=$environmentUrl --output json
   $tokenObj = $token | ConvertFrom-Json
   # get minutes to token expiration
   $minutesToTokenExpire =  (New-TimeSpan -End ([DateTime]$tokenObj.expiresOn)).Minutes
   Write-Host "Token will expire in $minutesToTokenExpire minutes."
   # get accessToken
   $accessToken = $tokenObj.accessToken

   Write-Host "Connected to $environmentUrl"
   ```

1. Save the file with the extension `.ps1`. In this example we will save it to: `C:\test\myDVWebAPICommands.ps1`.
1. Press <kbd>F5</kbd> to run the script, or select the **Run** button.
   You can expect the following:

   If you have already completed the steps above to sign in, you should see something like the following:

   ```powershell
   PS C:\Users\you.Domain> . 'C:\test\myDVWebAPICommands.ps1'
   Token will expire in 29 minutes.
   Connected to https://your.crm.dynamics.com/
   PS C:\Users\you.Domain> 
   ```

   Otherwise, you will be prompted to sign in again with the device code dialogs.

   ```powershell
   PS C:\Users\you.Domain> . 'C:\test\myDVWebAPICommands.ps1'
   ERROR: No subscription found. Run 'az account set' to select a subscription.
   To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code F6NDGHEM7 to authenticate.
   ```

   You can ignore the `No subscription found` error, that is expected as part of checking whether you are already signed in or not.

   After you are signed in, you can confirm the access token by entering `Write-Host $accessToken` in the terminal.


## Try WhoAmI

Now that you are logged in and have an access token, let's try a simple Web API function. The [WhoAmI Function](xref:Microsoft.Dynamics.CRM.WhoAmI) is a simple function to start with.

1. Edit your file to add the following:

   ```powershell
   # Define common set of headers
   $baseHeaders = @{
      'Authorization'    = "Bearer $accessToken"
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
      return Invoke-RestMethod @WhoAmIRequest
   }
   ```

   Note that the `$baseHeaders` variable includes the `$accessToken` value in the `Authorization` header, together with other headers you should use with Web API. [Learn more about headers to use with Dataverse Web API](compose-http-requests-handle-errors.md#http-headers)

   This script passes parameters to the [Invoke-RestMethod](xref:Microsoft.PowerShell.Utility.Invoke-RestMethod) with a [hashtable](/powershell/module/microsoft.powershell.core/about/about_hash_tables) using a technique known as [splatting](/powershell/module/microsoft.powershell.core/about/about_splatting).


1. Save the file and press <kbd>F5</kbd> to run the script. You can expect the following output:

   ```powershell
   PS C:\Users\you.DOMAIN> . 'C:\test\myDVWebAPICommands.ps1'
   Token will expire in 17 minutes.
   Connected to https://yourorg.crm.dynamics.com/
   PS C:\Users\you.DOMAIN> 
   ```
   
   Nothing happened because you have simply defined the `Get-WhoAmI` function. Now you can use it in the terminal.

1. Enter `Get-WhoAmI` in the terminal. You can expect raw output like the following:

   ```powershell
   PS C:\Users\you.DOMAIN> Get-WhoAmI

   @odata.context                                                                               BusinessUnitId
   --------------                                                                               --------------
   https://your.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse 38e0dbe4-131b-e111-ba7e-…

   PS C:\Users\you.DOMAIN> 
   ```

   Unfortunately, only the `@odata.context` property is fully visible. This is the least useful property returned. You can generally ignore it.

   You can get a better view of the data by converting it to JSON by piping the output to [ConvertTo-Json](xref:Microsoft.PowerShell.Utility.ConvertTo-Json).

1. Enter `Get-WhoAmI | ConvertTo-Json` in the terminal.

   ```powershell
   PS C:\Users\you.DOMAIN> Get-WhoAmI | ConvertTo-Json
   {
   "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
   "BusinessUnitId": "38e0dbe4-131b-e111-ba7e-78e7d1620f5e",
   "UserId": "4026be43-6b69-e111-8f65-78e7d1620f5e",
   "OrganizationId": "883278f5-07af-45eb-a0bc-3fea67caa544"
   }
   PS C:\Users\you.DOMAIN> 
   ```

   You can get a better view of the most important data, and exclude the `@odata.context`, when you pipe the output using [Format-List](/powershell/module/microsoft.powershell.utility/format-list).

1. Enter `Get-WhoAmI | Format-List -Property BusinessUnitId,UserId,OrganizationId` in the terminal.

   ```powershell
   PS C:\Users\you.DOMAIN> Get-WhoAmI | Format-List -Property BusinessUnitId,UserId,OrganizationId

   BusinessUnitId : 38e0dbe4-131b-e111-ba7e-78e7d1620f5e
   UserId         : 4026be43-6b69-e111-8f65-78e7d1620f5e
   OrganizationId : 883278f5-07af-45eb-a0bc-3fea67caa544

   PS C:\Users\you.DOMAIN> 
   ```

   > [!TIP]
   > Functions you create should generally return the raw data and allow consumers to apply available options to transform or format the data as they need to.

## Retrieve Records

## Create a record


## Retrieve a record


## Update a record



## Delete a record






## Next steps


Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

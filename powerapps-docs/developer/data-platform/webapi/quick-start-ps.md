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
   > ```powershell
   > az login -u you@yourorg.com -p yourPassword | Out-Null
   > ```

1. Press <kbd>Enter</kbd> to run the command. Because we are using the device flow, you will see output like the following:

   ```powershell
   To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code A57834N7J to authenticate.
   ```

   The `az login` command is configured to use a device code and to not require an Azure subscription. You need to login using a web browser.

1. Copy the code value, in this example `A57834N7J`, and then click the `https://microsoft.com/devicelogin` link to open the page.

   You will see a series of dialog windows. These dialogs might change over time, but the purpose is to capture the account credentials you will use to connect. This example uses a password, but you have options to sign in different ways. Your organization may require multi factor authentication which will make your experience different.

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

To avoid completing the device sign-in process every time you debug your script, you can create a script that will prompt you to sign in only if you are not already signed in.

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

   This code adds logic to extract the `expiresOn` property of the token to get an estimate for when the current token will expire.

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

   This script passes parameters to the [Invoke-RestMethod](/powershell/module/microsoft.powershell.utility/invoke-restmethod) with a [hashtable](/powershell/module/microsoft.powershell.core/about/about_hash_tables) using a technique known as [splatting](/powershell/module/microsoft.powershell.core/about/about_splatting).

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

   You can get a better view of the data by converting it to JSON by piping the output to [ConvertTo-Json](/powershell/module/microsoft.powershell.utility/convertto-json) that will convert the output into JSON-formatted string.

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

1. Add this function to your file

```powershell
# Retrieve records that match a query
function Get-Records {
   param (
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] [String] $query
   )
   $uri = $environmentUrl + 'api/data/v9.2/' + $setName + $query

   $RetrieveMultipleRequest = @{
      Uri     = $uri
      Method  = 'Get'
      Headers = $getHeaders
   }
   Invoke-RestMethod @RetrieveMultipleRequest
}
```

1. Press <kbd>F5</kbd> to save and run the script.

1. Now you can use the `Get-Records` function from the terminal. You need to specify the table entity set name and provide a query to filter the results. [Learn more about querying data using Dataverse Web API](query-data-web-api.md)

```powershell
Get-Records accounts '?$select=name&$top=3'
```

You will get results like the following:

```powershell
PS C:\Users\you.Domain> Get-Records accounts '?$select=name&$top=3'
PS C:\Users\you.Domain>

@odata.context                                        : https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#accounts(name)
@Microsoft.Dynamics.CRM.totalrecordcount              : -1
@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded : False
@Microsoft.Dynamics.CRM.globalmetadataversion         : 103348253
value                                                 : {@{@odata.etag=W/"102872096"; name=Adatum Corporation;
                                                        accountid=4b757ff7-9c85-ee11-8179-000d3a9933c9}, @{@odata.etag=W/"103323309";
                                                        name=Adventure Works Cycles; accountid=2ada33e7-ef8b-ee11-8179-000d3a9933c9},
                                                        @{@odata.etag=W/"103323312"; name=Alpine Ski House;
                                                        accountid=2eda33e7-ef8b-ee11-8179-000d3a9933c9}}

PS C:\Users\you.Domain>
```

The value returned is a collection that can provide very useful information, especially when you are retrieving paged results, but in this case, you are probably only interested in the `value` property. To access only this property, use the following command in the terminal:

```powershell
(Get-Records accounts '?$select=name&$top=3').value`
```

Now the results are more readable, but still not ideal.

```powershell
PS C:\Users\you.DOMAIN> (Get-Records accounts '?$select=name&$top=3').value

@odata.etag   name                   accountid
-----------   ----                   ---------
W/"102872096" Adatum Corporation     4b757ff7-9c85-ee11-8179-000d3a9933c9
W/"103323309" Adventure Works Cycles 2ada33e7-ef8b-ee11-8179-000d3a9933c9
W/"103323312" Alpine Ski House       2eda33e7-ef8b-ee11-8179-000d3a9933c9

PS C:\Users\you.DOMAIN>
```

The `@odata.etag` value is always returned, but not really useful unless you are performing [specific conditional operations](perform-conditional-operations-using-web-api.md), which is a more advanced scenario.

You can take this a step further and remove the `@odata.etag` property with the following command in the terminal using the [Format-Table](/powershell/module/microsoft.powershell.utility/format-table)

```powershell
(Get-Records accounts '?$select=name&$top=3').value | Format-Table -Property name,accountid
```

This results in a table with the data you are interested in:

```powershell
PS C:\Users\you.DOMAIN> (Get-Records accounts '?$select=name&$top=3').value | Format-Table -Property name,accountid

name                   accountid
----                   ---------
Adatum Corporation     4b757ff7-9c85-ee11-8179-000d3a9933c9
Adventure Works Cycles 2ada33e7-ef8b-ee11-8179-000d3a9933c9
Alpine Ski House       2eda33e7-ef8b-ee11-8179-000d3a9933c9

PS C:\Users\you.DOMAIN>
```

## Create a record

Add the following function to your file:

```powershell
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
```

This function breaks the rule of returning the raw values to the user. Dataverse Web API returns the full URL of the created record in the `OData-EntityId` response header, along with many other response headers. The only value that is generally useful is the ID of the created record, which is a [System.Guid](xref:System.Guid). For simplicity, this function parses out that ID and returns it as a `Guid` value. [Learn more about creating records using Dataverse Web API](create-entity-web-api.md)

This function requires the table set name, but it also requires data about the record to create. Pass this data using a [hashtable](/powershell/module/microsoft.powershell.core/about/about_hash_tables).

Enter the following command into the terminal:

```powershell
New-Record accounts @{name='Example Account'; accountcategorycode=1}
```

You will get results like the following:

```powershell
PS C:\Users\you.DOMAIN> New-Record accounts @{name='Example Account'; accountcategorycode=1}

Guid
----
73600f9a-d48f-ee11-8179-000d3a993550

PS C:\Users\you.DOMAIN>
```

Generally, you will want to capture and use the ID values of the records you create. It is difficult to continue to do this using only the terminal. Let's create a script file that will use the functions we have created.

### Create a script file

1. In the Visual Studio Code menu, select **File** > **New Text File**, or use the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>N</kbd>.
1. By default, this file will be Plain Text file. Click the **Select a Language** prompt to select a language, or use the **Language Mode Selector** on the right hand of the Status Bar to select **PowerShell (powershell)**
1. Enter the following into the file:

   ```powershell
   $newAccountID = New-Record accounts @{name='Example Account'; accountcategorycode=1}
   ```

1. Press <kbd>F5</kbd> to debug your script.

   > [!NOTE]
   > This will not save your script

   The terminal output should look like this:

   ```powershell
   PS C:\Users\you.DOMAIN>
   PS C:\Users\you.DOMAIN> . $args[0] $newAccountID = New-Record accounts @{name='Example Account'; accountcategorycode=1}
   PS C:\Users\you.DOMAIN>
   ```

1. Since you have set the ID value to a variable, to see the value of the record created, enter `$newAccountID` in the terminal. The terminal output should look like this:

   ```powershell
   PS C:\Users\you.DOMAIN> $newAccountID


   Guid
   ----
   6b7c5c5e-d88f-ee11-8179-000d3a993550

   PS C:\Users\you.DOMAIN>
   ```

1. To get the GUID value of the `$newAccountID` variable, use `$newAccountID.Guid`.

```powershell
PS C:\Users\you.DOMAIN> $newAccountID.Guid
6b7c5c5e-d88f-ee11-8179-000d3a993550
PS C:\Users\you.DOMAIN>
```

## Retrieve a record

Now let's retrieve the record you created.

1. Add the following function to the functions file:

   ```powershell
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
   ```

1. With the functions definition file open, press <kbd>F5</kbd> to debug and save your file.
1. In your script file, add the following lines:

   ```powershell
   Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode'
   ```

1. Press <kbd>F5</kbd> to debug your script

   The terminal output should look like this:

   ```powershell
   PS C:\Users\you.DOMAIN> . $args[0] Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode'

   @odata.context                                                : https://crmue.crm.dynamics.com/api/data/v9.2/$metadata#accounts(name,accountcategorycode)/$entity
   @odata.etag                                                   : W/"103351278"
   name                                                          : Example Account
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Preferred Customer
   accountcategorycode                                           : 1
   accountid                                                     : 51c8091c-df8f-ee11-8179-000d3a9933c9

   PS C:\Users\you.DOMAIN> 
   ```

   Notice that the `accountcategorycode@OData.Community.Display.V1.FormattedValue` property contains the string value representing the value of the `accountcategorycode` choice column integer value. This is an example of [formatted values](query-data-web-api.md#formatted-values) that are returned because of the `Prefer:odata.include-annotations="*"` header included in this request.

   Let's clean this up by formatting the properties.

1. Replace the call to `Get-Record` with the following:

   ```powershell
   Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode' |
   Format-List -Property name,
      accountid,
      accountcategorycode,
      accountcategorycode@OData.Community.Display.V1.FormattedValue
   ```

1. Press <kbd>F5</kbd> to debug your script. Now the response looks like this:

   ```powershell
   PS C:\Users\you.DOMAIN>
   PS C:\Users\you.DOMAIN> . $args[0] Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode' |
   Format-List -Property name,
      accountid,
      accountcategorycode,
      accountcategorycode@OData.Community.Display.V1.FormattedValue

   name                                                          : Example Account
   accountid                                                     : 51c8091c-df8f-ee11-8179-000d3a9933c9
   accountcategorycode                                           : 1
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Preferred Customer

   PS C:\Users\you.DOMAIN>
   ```


## Update a record

Now let's update the record you created.

1. Add the following function to your functions file:

   ```powershell
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
   ```

   Like the `New-Record` function, this request needs to include the `Content-Type:application/json` request header. The `If-Match: *` header makes sure this will not create a new record if the record you intended to update doesn't exist. The `Patch` method is also used for *upsert* operations. [Learn more about updating and upserting table rows](update-delete-entities-using-web-api.md)

1. With the functions definition file open, press <kbd>F5</kbd> to debug and save your file.
1. The `Update-Record` returns the response properties from the request, but there isn't anything interesting returned as long as the operation succeeds. In your script file, add the following *above* the query currently there. The query will demonstrate that the data actually changed because you updated it.

   ```powershell
   $updateAccountData = @{
      name='Updated Example account';
      accountcategorycode=2; #Standard
      }
   Update-Record accounts $newAccountID.Guid $updateAccountData
   ```

   > [!NOTE]
   > The `$newAccountID` variable is still in memory so you can continue to access it

1. Press <kbd>F5</kbd> to debug your script. Now the response looks like this:

   ```powershell
   PS C:\Users\you.DOMAIN>
   PS C:\Users\you.DOMAIN> . $args[0] $updateAccountData = @{
      name='Updated Example account';
      accountcategorycode=2; #Standard
      }
   Update-Record accounts $newAccountID.Guid $updateAccountData
   Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode' |
      Format-List -Property name,
         accountid,
         accountcategorycode,
         accountcategorycode@OData.Community.Display.V1.FormattedValue


   name                                                          : Updated Example account
   accountid                                                     : 51c8091c-df8f-ee11-8179-000d3a9933c9
   accountcategorycode                                           : 2
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Standard

   PS C:\Users\you.DOMAIN> 
   ```

   This demonstrates how the `name` and `accountcategorycode` properties of the account with ID `51c8091c-df8f-ee11-8179-000d3a9933c9` were updated.

## Delete a record

Finally, let's delete the record you created.

1. Add the following function to your functions file:

```powershell
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
```

1. With the functions definition file open, press <kbd>F5</kbd> to debug and save your file.
1. In your script file, replace the contents with the following:

```powershell
Remove-Record accounts $newAccountID.Guid
```

1. Press <kbd>F5</kbd> to debug your script. Now the response looks like this:

```powershell
PS C:\Users\you.DOMAIN>
PS C:\Users\you.DOMAIN> . $args[0] Remove-Record accounts $newAccountID.Guid

PS C:\Users\you.DOMAIN>
```

1. To verify that the account record was deleted, try deleting it again. Press <kbd>F5</kbd> to debug your script again. Now the response looks like this:

```powershell
PS C:\Users\you.DOMAIN>
PS C:\Users\you.DOMAIN> . $args[0] Remove-Record accounts $newAccountID.Guid
Invoke-RestMethod: C:\test\myDVWebAPICommands.ps1:143:4
Line |
 143 |     Invoke-RestMethod @DeleteRequest
     |     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     |  {   "error": {     "code": "0x80040217",     "message": "Entity \u0027account\u0027 With Id =
     | 51c8091c-df8f-ee11-8179-000d3a9933c9 Does Not Exist"   } }
PS C:\Users\you.DOMAIN> 
```

This shows the kind of error you can expect.

## Parsing errors

TODO: Using Try/Catch and parsing errors

## Function Definitions file

This is the complete file with all the logic you have by following the steps in this article. You can add additional functions and re-use these function definitions to work with the Dataverse Web API using PowerShell.

```powershell
$environmentUrl = 'https://yourorg.crm.dynamics.com/' # change this

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

# Define common set of headers
$baseHeaders = @{
   'Authorization'    = "Bearer $accessToken"
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}
# Header for POST operations
$postHeaders = $baseHeaders.Clone()
$postHeaders.Add('Content-Type', 'application/json')

# Header for GET operations that have annotations
$getHeaders = $baseHeaders.Clone()
$getHeaders.Add('If-None-Match', $null)
$getHeaders.Add('Prefer', 'odata.include-annotations="*"')

# WhoAmI message
function Get-WhoAmI {
   $WhoAmIRequest = @{
      Uri     = $environmentUrl + 'api/data/v9.2/WhoAmI'
      Method  = 'Get'
      Headers = $baseHeaders
   }
   return Invoke-RestMethod @WhoAmIRequest
}

# Retrieve records that match a query
function Get-Records {
   param (
      [Parameter(Mandatory)] [String] $setName,
      [Parameter(Mandatory)] [String] $query
   )
   $uri = $environmentUrl + 'api/data/v9.2/' + $setName + $query

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
```

## Troubleshooting

This section contains some guidance for issues you might encounter.

TBD Add issues found during testing

## Next steps

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"] > [Web API types and operations](web-api-types-operations.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

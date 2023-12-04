---
title: Quick Start Web API with PowerShell Option 1
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

# Quick Start: Web API with PowerShell Option 1

In this quick start, you'll learn how to:

- Authenticate to Dataverse using PowerShell without registering your own application.
- Compose requests to the Dataverse Web API using the PowerShell [Invoke-RestMethod](/powershell/module/microsoft.powershell.utility/invoke-restmethod).
- Create reusable functions that you can save in a .ps1 file.
- Write and run a script using the functions you created.

> [!NOTE]
> - This should work for Windows, Linux, and macOS, but these steps have only been tested on Windows. If changes are needed, please let us know using the **Feedback** section at the bottom of this article.
> - If you want to skip the step-by-step instructions and explanations, you can find the scripts representing the completed steps for this quick start in [Sample: PowerShell functions using Dataverse Web API](samples/powershell-web-api-samples.md).

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

## Authenticate to Dataverse

The first step is to authenticate and get an access token you need to send with your requests.

You can use an access token generated using the Azure CLI [az account get-access-token command](/cli/azure/account#az-account-get-access-token) based on the Azure account credentials you use with the [az login command](/cli/azure/reference-index#az-login). This access token has the necessary delegated permissions to connect to Dataverse. You don't need to register an application to use the Dataverse Web API with PowerShell.

1. Open Visual Studio Code.
1. In the menu, select **Terminal** > **New Terminal**. Or use the <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>`</kbd> keyboard shortcut.
1. Copy the following and paste it in the terminal, replacing `https://yourorg.crm.dynamics.com/` with the url to the Dataverse environment you want to connect to.

   ```powershell
   $environmentUrl = 'https://yourorg.crm.dynamics.com/' # change this
   az login --allow-no-subscriptions  | Out-Null
   $token = (az account get-access-token --resource=$environmentUrl --query accessToken --output tsv)
   ```
   
1. Press <kbd>Enter</kbd> to run the command.

   ```powershell
      WARNING: A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
   ```

1. In the browser that opened, enter the credentials you need to authenticate.

At this point, you can enter `Write-Host $token` in the terminal to see the access token value.

### Simplifying Sign in

To avoid completing the device sign-in process every time you debug your script, you can create a script that prompts you to sign in only if you aren't already signed in.

> [!IMPORTANT]
> This is the first step in creating a file containing reusable functions. We will use this *functions file* through the rest of this article.

1. In Visual Studio Code menu, select **File** > **New Text File**, or use the <kbd>Ctrl</kbd>+<kbd>N</kbd> keyboard shortcut.
1. Copy and paste the following script into the new file, replacing `https://yourorg.crm.dynamics.com/` with the Url to the Dataverse environment you want to connect to.

   ```powershell
   $environmentUrl = 'https://yourorg.crm.dynamics.com/' # change this

   ## login if not already logged in
   if($null -eq (az account tenant list --only-show-errors))
   {
      az login --allow-no-subscriptions | Out-Null
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

   This code uses the [az account tenant list](/cli/azure/account/tenant#az-account-tenant-list) Azure CLI extension to get a list of tenants associated with the signed-in user. If it returns null, you need to sign in. [If nothing happens, you need to install the extension](#the-login-script-hangs).
   
   This code also adds logic to extract the `expiresOn` property of the token to get an estimate for when the current token expires. If the token expires and you get `401 Unauthorized` error, try running this script again.

1. Save the file with the extension `.ps1`. In this example, we'll save it to: `C:\test\myDVWebAPICommands.ps1`.
1. Press <kbd>F5</kbd> to run the script, or select the **Run** button. There are two possible results:

   - If you have already completed the steps in [Authenticate to Dataverse](#authenticate-to-dataverse) to sign in, you should see something like the following:

      ```powershell
      PS C:\Users\you.Domain> . 'C:\test\myDVWebAPICommands.ps1'
      Token will expire in 49 minutes.
      Connected to https://yourorg.crm.dynamics.com/
      ```

   - Otherwise, you are prompted to sign in again with the device code dialogs.

      ```powershell
      PS C:\Users\you.Domain> . 'C:\test\myDVWebAPICommands.ps1'
      ERROR: Please run 'az login' to setup account.
      WARNING: A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
      ```

      You can ignore the `No subscription found` error. That error is an expected as part of checking whether you're already signed in or not. In the browser that opened, enter the credentials you need to authenticate.

   When you're signed in, you can confirm the access token by entering `Write-Host $accessToken` in the terminal.

## Try WhoAmI

Now that you're logged in and have an access token, let's try a simple Web API function. The [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) requires no input parameters and returns data in the form of a [WhoAmIResponse complex type](xref:Microsoft.Dynamics.CRM.WhoAmIResponse).

1. Edit your functions file to add this `Get-WhoAmI` function below the line `Write-Host "Connected to $environmentUrl"`.

   ```powershell
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
      return Invoke-RestMethod @WhoAmIRequest
   }
   ```

   The `$baseHeaders` variable includes the `$accessToken` value in the `Authorization` header, together with other headers you should always use with Web API. [Learn more about headers to use with Dataverse Web API](compose-http-requests-handle-errors.md#http-headers)

   This script passes the `Uri`, `Method`, and `Headers` parameters to the [Invoke-RestMethod](/powershell/module/microsoft.powershell.utility/invoke-restmethod) with a [hashtable](/powershell/module/microsoft.powershell.core/about/about_hash_tables) using a technique known as [splatting](/powershell/module/microsoft.powershell.core/about/about_splatting).

   PowerShell has specific requirements about the names of functions. That is why this function is named `Get-WhoAmI` rather than simply `WhoAmI`. [Learn more about approved verbs for PowerShell commands](/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands)

1. Save the file and press <kbd>F5</kbd> to run the script. You can expect the following output:

   ```powershell
   PS C:\Users\you.DOMAIN> . 'C:\test\myDVWebAPICommands.ps1'
   Token will expire in 40 minutes.
   Connected to https://yourorg.crm.dynamics.com/
   PS C:\Users\you.DOMAIN>
   ```

   Nothing happened because you have only defined the `Get-WhoAmI` function. Now you can use it in the terminal.

1. Enter `Get-WhoAmI` in the terminal. You can expect raw output like the following:

   ```powershell
   PS C:\Users\you.DOMAIN> Get-WhoAmI

   @odata.context                                                                               BusinessUnitId
   --------------                                                                               --------------
   https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse 38e0dbe4-131b-e111-ba7e-…
   ```

   Unfortunately, only the `@odata.context` property is fully visible. This property is the least useful property returned. You can generally ignore it.

   You can get a better view of the data by converting it to JSON by piping the output to [ConvertTo-Json](/powershell/module/microsoft.powershell.utility/convertto-json) that converts the output into a JSON-formatted string.

1. Enter `Get-WhoAmI | ConvertTo-Json` in the terminal. You can expect the following:

   ```powershell
   PS C:\Users\you.DOMAIN> Get-WhoAmI | ConvertTo-Json
   {
   "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
   "BusinessUnitId": "946986fe-ae36-4b86-a17e-b7815e3c881b",
   "UserId": "2979a124-067d-4e7e-ada2-e7df09549908",
   "OrganizationId": "9e43d5ea-a042-41c0-bb44-a630fb0dd021"
   }
   ```

   That's better. But you can get an even better view of the most important data, and exclude the `@odata.context`, when you pipe the output using [Format-List](/powershell/module/microsoft.powershell.utility/format-list).

1. Enter `Get-WhoAmI | Format-List -Property BusinessUnitId,UserId,OrganizationId` in the terminal. You can expect the following:

   ```powershell
   PS C:\Users\you.DOMAIN> Get-WhoAmI | Format-List -Property BusinessUnitId,UserId,OrganizationId

   BusinessUnitId : 946986fe-ae36-4b86-a17e-b7815e3c881b
   UserId         : 2979a124-067d-4e7e-ada2-e7df09549908
   OrganizationId : 9e43d5ea-a042-41c0-bb44-a630fb0dd021
   ```

> [!TIP]
> Functions you create should generally return the raw data and allow consumers to apply available options to transform or format the data as they need to.

## Retrieve Records

Let's start working with business data. We'll add a function to let you query Dataverse tables.

1. Edit your functions file to add this `Get-Records` function below the `Get-WhoAmI` function.

   ```powershell
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
   ```
   ### Retrieve headers

   This function adds two more headers to the base headers:

   - `If-None-Match : null` is to make sure that related record collections you might include using `$expand` are retrieved from the server and don't use cached data in the browser that doesn't reflect recent changes.
   - `Prefer : odata.include-annotations="*"` requests all available annotations that can be returned. You can also choose to retrieve specific types of annotations. [Learn how to request annotations](compose-http-requests-handle-errors.md#request-annotations)

1. Press <kbd>F5</kbd> to save and run the script.

   Now you can use the `Get-Records` function from the terminal. You need to specify the [table entity set name](web-api-service-documents.md#entity-set-name) and provide a query to filter the results. [Learn more about querying data using Dataverse Web API](query-data-web-api.md)

1. Enter the following into the terminal. This query retrieves the `name` property for the first three [account](xref:Microsoft.Dynamics.CRM.account) records in Dataverse.

   ```powershell
   Get-Records accounts '?$select=name&$top=3'
   ```

   You'll get results like the following:

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
   ```

   The value returned is a collection that can provide useful information, especially when you're retrieving [paged results](query-data-web-api.md#page-results), but in this case, you're probably only interested in the `value` property.

1. To access only the `value` property, use the following command in the terminal:

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
   ```

   The `@odata.etag` value is always returned, but not useful unless you're performing [specific conditional operations](perform-conditional-operations-using-web-api.md), which is a more advanced scenario.

   You can take this a step further and remove the `@odata.etag` property with the using the [Format-Table](/powershell/module/microsoft.powershell.utility/format-table)

1. Enter the following command using `Format-Table` in the terminal:

   ```powershell
   (Get-Records accounts '?$select=name&$top=3').value | Format-Table -Property name,accountid
   ```

   This results in a table with the data you're interested in:

   ```powershell
   PS C:\Users\you.DOMAIN> (Get-Records accounts '?$select=name&$top=3').value | Format-Table -Property name,accountid

   name                   accountid
   ----                   ---------
   Adatum Corporation     4b757ff7-9c85-ee11-8179-000d3a9933c9
   Adventure Works Cycles 2ada33e7-ef8b-ee11-8179-000d3a9933c9
   Alpine Ski House       2eda33e7-ef8b-ee11-8179-000d3a9933c9
   ```

## Create a record

Now, let's create a record.

1. Edit your functions file to add this `New-Record` function below the `Get-Records` function.

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

   The `New-Record` function breaks the rule of returning the raw values to the user. Dataverse Web API returns the full URL of the created record in the `OData-EntityId` response header, along with many other response headers. The only value that is useful is the ID of the created record, which is a [System.Guid](xref:System.Guid). For simplicity, this function parses out that ID and returns it as a `Guid` value. [Learn more about creating records using Dataverse Web API](create-entity-web-api.md)

   The `New-Record` function requires the [table entity set name](web-api-service-documents.md#entity-set-name) and data about the record to create. Pass this data using a [hashtable](/powershell/module/microsoft.powershell.core/about/about_hash_tables).

1. Press <kbd>F5</kbd> to save and run the script.
1. To create an account record, enter the following command into the terminal:

   ```powershell
   New-Record accounts @{name='Example Account'; accountcategorycode=1}
   ```

   You'll get results like the following:

   ```powershell
   PS C:\Users\you.DOMAIN> New-Record accounts @{name='Example Account'; accountcategorycode=1}

   Guid
   ----
   73600f9a-d48f-ee11-8179-000d3a993550
   ```

   Generally, you want to capture and use the ID values of the records you create. It's difficult to continue to do this using only the terminal. Let's create a *script file* that uses the functions you create in your *functions file*.

   > [!NOTE]
   > Going forward, we will have two documents open in Visual Studio Code. The *functions file* just for function definitions, the *script file* for testing out the scripts.

### Create a script file

1. In the Visual Studio Code menu, select **File** > **New Text File**, or use the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>N</kbd>.

   By default, this file is **Plain Text** file.

1. Select the **Select a Language** prompt to select a language, or use the **Language Mode Selector** on the right hand of the **Status Bar** to select **PowerShell (powershell)**.
1. Copy and paste the following line into the file:

   ```powershell
   $newAccountID = New-Record accounts @{name='Example Account'; accountcategorycode=1}
   ```
   
   This command creates an account record and assignes the ID value to the `$newAccountID` variable. Later steps will use this variable.

   > [!NOTE]
   >You can find information about the [account entity type](xref:Microsoft.Dynamics.CRM.account) in our reference documentation. For tables not included by default in Dataverse, the definitive information is found in the service documents. [Learn about Dataverse Web API entity types](web-api-entitytypes.md).

1. Press <kbd>F5</kbd> to debug your script file.

   > [!NOTE]
   > This will not save your script. It isn't necessary to save this file to use it for ad-hoc testing.

   The terminal output should look like this:

   ```powershell
   PS C:\Users\you.DOMAIN>
   PS C:\Users\you.DOMAIN> . $args[0] $newAccountID = New-Record accounts @{name='Example Account'; accountcategorycode=1}
   ```

1. Since you set the ID value to the `$newAccountID` variable, to see the value of the record created, enter `$newAccountID` in the terminal. The terminal output should look like this:

   ```powershell
   PS C:\Users\you.DOMAIN> $newAccountID


   Guid
   ----
   6b7c5c5e-d88f-ee11-8179-000d3a993550
   ```

   > [!NOTE]
   > The `$newAccountID` variable is defined with global scope. You can continue to access this value for as long as your session lasts. [Learn more about variable scopes in PowerShell](/powershell/module/microsoft.powershell.core/about/about_scopes)

1. To get the GUID value of the `$newAccountID` variable, enter `$newAccountID.Guid` in the terminal. The output is simpler. 

   ```powershell
   PS C:\Users\you.DOMAIN> $newAccountID.Guid
   6b7c5c5e-d88f-ee11-8179-000d3a993550
   ```

   You need to use the `$newAccountID.Guid` property as the parameter in other functions.

## Retrieve a record

Now let's retrieve the account record you created.

1. Edit your functions file to add this `Get-Record` function below the `New-Record` function

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
   
   This function sets the ID of the record to retrieve and adds the same two request [retrieve headers](#retrieve-headers) found in the `Get-Records` function.

1. With your *functions file* open, press <kbd>F5</kbd> to debug and save your file.
1. In your *script file*, add the following line:

   ```powershell
   Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode'
   ```

1. Press <kbd>F5</kbd> to debug your script file.

   The terminal output should look like this:

   ```powershell
   PS C:\Users\you.DOMAIN> . $args[0] Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode'

   @odata.context                                                : https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#accounts(name,accountcategorycode)/$entity
   @odata.etag                                                   : W/"103351278"
   name                                                          : Example Account
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Preferred Customer
   accountcategorycode                                           : 1
   accountid                                                     : 51c8091c-df8f-ee11-8179-000d3a9933c9
   ```

   Notice that the `accountcategorycode@OData.Community.Display.V1.FormattedValue` property contains the string value representing the value of the `accountcategorycode` choice column integer value. This property is an example of [formatted values](query-data-web-api.md#formatted-values) that are returned because of the `Prefer:odata.include-annotations="*"` header included in this request.

   Let's clean up this output by formatting the properties using [Format-List](/powershell/module/microsoft.powershell.utility/format-list).

1. In your script file, *replace* the call to `Get-Record` with the following script:

   ```powershell
   Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode' |
   Format-List -Property name,
      accountid,
      accountcategorycode,
      accountcategorycode@OData.Community.Display.V1.FormattedValue
   ```

1. Press <kbd>F5</kbd> to debug your script file. Now the terminal has the following output:

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
   ```


## Update a record

Now let's update the record you created.

1. Edit your functions file to add this `Update-Record` function below the `Get-Record` function.

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

   Like the `New-Record` function, this request needs to include the `Content-Type:application/json` request header because it includes data in the body of the request. The `If-Match: *` header makes sure this function doesn't create a new record if the record you intended to update doesn't exist. The `Patch` method is also used for *upsert* operations. [Learn more about updating and upserting table rows](update-delete-entities-using-web-api.md)

1. With the functions file open, press <kbd>F5</kbd> to debug and save your file.

   The `Update-Record` function returns the response properties from the request, but there isn't anything interesting returned as long as the operation succeeds. We will explain handing errors in [Parsing errors](#parsing-errors).

1. In your script file, add the following code using `Update-Record` above the code that is using `Get-Record` currently there. The query demonstrates that the data changed because you updated it.

   ```powershell
   $updateAccountData = @{
      name='Updated Example account';
      accountcategorycode=2; #Standard
      }
   Update-Record accounts $newAccountID.Guid $updateAccountData
   Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode' |
      Format-List -Property name,
         accountid,
         accountcategorycode,
         accountcategorycode@OData.Community.Display.V1.FormattedValue
   ```

   > [!NOTE]
   > If the `$newAccountID` variable is still in memory so you can continue to access it. Otherwise, [you will get an error like this](#error-get-record-cannot-process-argument-transformation-on-parameter-id-cannot-convert-null-to-type-systemguid). Repeat the steps in [Create a record](#create-a-record) to set it.

1. Press <kbd>F5</kbd> to debug your script. Now the terminal has the following output:

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
   ```

   This demonstrates how the `name` and `accountcategorycode` properties of the account with ID `51c8091c-df8f-ee11-8179-000d3a9933c9` were updated.

## Delete a record

Let's delete the record you created.

1. Edit your functions file to add this `Remove-Record` function below the `Update-Record` function.

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

1. With your *functions file* open, press <kbd>F5</kbd> to debug and save your file.
1. In your *script file*, replace the contents with the following line:

   ```powershell
   Remove-Record accounts $newAccountID.Guid
   ```

1. Press <kbd>F5</kbd> to debug your script. Now the terminal has the following output:

   ```powershell
   PS C:\Users\you.DOMAIN>
   PS C:\Users\you.DOMAIN> . $args[0] Remove-Record accounts $newAccountID.Guid
   ```

1. To verify that the account record was deleted, try deleting it again. Press <kbd>F5</kbd> to debug your script again. Now the terminal has the following output:

   ```powershell
   PS C:\Users\you.DOMAIN>
   PS C:\Users\you.DOMAIN> . $args[0] Remove-Record accounts $newAccountID.Guid
   Invoke-RestMethod: C:\test\myDVWebAPICommands.ps1:143:4
   Line |
   143 |     Invoke-RestMethod @DeleteRequest
      |     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |  {   "error": {     "code": "0x80040217",     "message": "Entity \u0027account\u0027 With Id =
      | 51c8091c-df8f-ee11-8179-000d3a9933c9 Does Not Exist"   } }
   ```

   This shows the kind of error you can expect. Next, let's look at how to handle the error returned.

## Parsing errors

Errors occur and your PowerShell script can handle them using [Try/Catch pattern](/powershell/module/microsoft.powershell.core/about/about_try_catch_finally). What we need is a function that enables extracting important information about the error from Dataverse.


1. Edit your functions file to add this `Get-Error-Details` function below the `Remove-Record` function.

   ```powershell
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

   This function extracts information from Dataverse Web API errors when they're invoked using [Invoke-RestMethod](/powershell/module/microsoft.powershell.utility/invoke-restmethod). The errors are <xref:Microsoft.PowerShell.Commands.HttpResponseException?displayProperty=fullName> exceptions.
   But these errors aren't the only kinds of error that might occur in your script.

1. Replace the contents of your script file with the following script:

   ```powershell
   try {
      Get-Records accounts '?$invalidParameter'
      Remove-Record accounts $newAccountID.Guid
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

   This introduces a Try/Catch pattern to capture relevant Dataverse Web API error details from the server. The first `catch` block only responds to [HttpResponseException](xref:Microsoft.PowerShell.Commands.HttpResponseException) errors. The second catch block manages any other kinds of script errors.

1. Press <kbd>F5</kbd> to debug your script. Now the terminal has the following output:

   ```powershell
   PS C:\test> . 'C:\test\test3.ps1'
   An error occurred calling Dataverse:

   statuscode : BadRequest
   code       : 0x80060888
   message    : The query parameter [REDACTED] is not supported
   ```

   This error refers to the use of `?$invalidParameter` as the query parameter to the `Get-Records` function. The specific parameter value is `[REDACTED]` because the string could potentially include personal data that can't be stored in error logs.

1. Remove the line: `Get-Records accounts '?$invalidParameter'` and press <kbd>F5</kbd> to debug your script again.

   This time, if the `$newAccountID` variable is still a global variable, you get this error from Dataverse:

   ```powershell
   An error occurred calling Dataverse:

   statuscode : NotFound
   code       : 0x80040217
   message    : Entity 'account' With Id = 51c8091c-df8f-ee11-8179-000d3a9933c9 Does Not Exist
   ```

   Otherwise, if the `$newAccountID` variable doesn't contain a value you get this error, which is due to an error in the script:

   ```powershell
   An error occurred in the script:
   Remove-Record: untitled:Untitled-1:2:27
   Line |
      2 |     Remove-Record accounts $newAccountID.Guid
      |                            ~~~~~~~~~~~~~~~~~~
      | Cannot process argument transformation on parameter 'id'. Cannot convert null to type "System.Guid".
   ```
   
   See [Error: Get-Record: Cannot process argument transformation on parameter 'id'. Cannot convert null to type "System.Guid".](#error-get-record-cannot-process-argument-transformation-on-parameter-id-cannot-convert-null-to-type-systemguid).

## Bring it all together

In this section we will perform multiple data operations in a single script. This section also shows using the function parameter names, like `-setName`, `-query` and `-body` that will make your script easier to read.

Replace the contents of your script file with the following script:

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

1. Press <kbd>F5</kbd> to debug your script. Now the output in the terminal looks like this:

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

## Troubleshooting

This section contains some guidance for issues you might encounter.

### Error: "az : The term 'az' is not recognized as the name of a cmdlet, function, script file, or operable program."

You need to install the [Azure CLI](/cli/azure/install-azure-cli).

### Nothing happens when I press <kbd>F5</kbd> to debug the script

Press the <kbd>F Lock</kbd> key to toggle function on your keyboard.

### The login script hangs

The script in [Simplifying Sign in](#simplifying-sign-in) doesn't respond. There is no error.

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

You can get this error during the section [Retrieve a record](#retrieve-a-record). The instructions are to run the following command to retrieve a record:

```powershell
Get-Record accounts $newAccountID.Guid '?$select=name,accountcategorycode'
```

This will only work while the `$newAccountID` variable has a value, which was set in the previous [Create a record](#create-a-record) section. If you closed your session, the `$newAccountID` variable will be null if you start at this point. Repeat the steps in the [Create a record](#create-a-record) section to continue.

### Error dialog: connect ENOENT\\\\.\\pipe\\&lt;RANDOM_text&gt; with Open 'launch.json' button

This error might occur at times when debugging using Visual Studio code. To resolve, press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>, type `restart` and select `Powershell: Restart session`. See [PowerShell/vscode-powershell GitHub Issue 4332](https://github.com/PowerShell/vscode-powershell/issues/4332) for more information.


## Next steps

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)

### Related articles

[Sample: PowerShell functions using Dataverse Web API](samples/powershell-web-api-samples.md)   
[PowerShell in Visual Studio Code](https://code.visualstudio.com/docs/languages/powershell)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

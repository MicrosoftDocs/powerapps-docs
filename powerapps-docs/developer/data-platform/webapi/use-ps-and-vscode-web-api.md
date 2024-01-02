---
title: Use PowerShell and Visual Studio Code with the Dataverse Web API
description: Describes how to use PowerShell and Visual Studio Code to create reusable PowerShell functions to interactively test using the Dataverse Web API
ms.date: 01/05/2024
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---
# Use PowerShell and Visual Studio Code with the Dataverse Web API

This article expands on the [Quick Start Web API with PowerShell](quick-start-ps.md) article to describe advanced capabilities using PowerShell and Visual Studio Code with the Dataverse Web API to:

- [Create reusable functions](#create-reusable-functions)
- [Handle exceptions](#handle-exceptions)
- [Manage Dataverse service protection limits](#manage-dataverse-service-protection-limits)

> [!NOTE]
> The instructions in this article should work for Windows, Linux, and macOS, but these steps have only been tested on Windows. If changes are needed, please let us know using the **Feedback** section at the bottom of this article.


## Prerequisites

The content of this article has the same prerequisites as the [Quick Start Web API with PowerShell](quick-start-ps.md) article.

[!INCLUDE [cc-visual-studio-code-powershell-prerequisites](../includes/cc-visual-studio-code-powershell-prerequisites.md)]


## Create reusable functions

[Quick Start Web API with PowerShell](quick-start-ps.md) introduced how to authenticate and call the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) with Visual Studio Code. This might be all you need to for an ad-hoc test of one or more operations. However, as your scripts become more complex, you might find yourself typing the same code again and again. 

In this section, we start creating a set of reusable functions in separate files that we can access using *[dot sourcing](/powershell/module/microsoft.powershell.core/about/about_scripts#script-scope-and-dot-sourcing)*. Use dot sourcing to load a file containing PowerShell scripts that can contain functions and variables that become part of the local script scope.

### Create a Connect function

Let's put the code to authenticate to Dataverse in a function called `Connect` inside a file named `Core.ps1` so we can reuse it in a single line of code.

1. Create a folder. In this example, we create a folder in `C:\scripts`.
1. [Open the scripts folder using Visual Studio Code](https://code.visualstudio.com/docs/editor/workspaces).
1. Create a text file in the scripts folder named `Core.ps1`.
1. Copy and paste the following `Connect` function into the `Core.ps1` file.

   ```powershell
   #Requires -Version 7.4.0
   #Requires -Modules @{ ModuleName="Az"; ModuleVersion="11.1.0" }

   function Connect {
      param (
         [Parameter(Mandatory)] 
         [String] 
         $uri
      )

      ## Login if not already logged in
      if ($null -eq (Get-AzTenant -ErrorAction SilentlyContinue)) {
         Connect-AzAccount | Out-Null
      }

      # Get an access token
      $token = (Get-AzAccessToken -ResourceUrl $uri).Token

      # Define common set of headers
      $global:baseHeaders = @{
         'Authorization'    = 'Bearer ' + $token
         'Accept'           = 'application/json'
         'OData-MaxVersion' = '4.0'
         'OData-Version'    = '4.0'
      }

      # Set baseURI
      $global:baseURI = $uri + 'api/data/v9.2/'
   }
   ```

   > [!NOTE]
   > The script adds the `baseURI` and `baseHeaders` variables to the global context using the `$global` [scope modifier](/powershell/module/microsoft.powershell.core/about/about_scopes#scope-modifiers) so that they are available to other scripts in the same session.

1. Create another text file using Visual Studio Code named `test.ps1` in your `scripts` folder.
1. Copy and paste the following script into the `test.ps1` file:

   ```powershell
   . C:\scripts\Core.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change this
   # Invoke WhoAmI Function
   Invoke-RestMethod -Uri ($baseURI + 'WhoAmI') -Method Get -Headers $baseHeaders
   | ConvertTo-Json
   ```

   `. C:\scripts\Core.ps1` at the top of the file shows using dot sourcing to direct the script to load the contents of that file. Set the path to a different folder if you didn't use `C:\scripts`.

1. Change the `https://yourorg.crm.dynamics.com/` value to match the URL for your environment
1. Press <kbd>F5</kbd> to run the script.

   The output should look something like this:

   ```powershell
   PS C:\scripts> . 'C:\scripts\test.ps1'
   {
   "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
   "BusinessUnitId": "3a277578-5996-ee11-be36-002248227994",
   "UserId": "2c2e7578-5996-ee11-be36-002248227994",
   "OrganizationId": "97bf0e8b-aa99-ee11-be32-000d3a106c3a"
   }
   ```

### Create a WhoAmI function

Let's put the code to invoke the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) in a function called `Get-WhoAmI` inside a file named `CommonFunctions.ps1` so we  can type just 11 characters rather than 100 each time you want to use the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI)

1. Create a new text file named `CommonFunctions.ps1` in your `scripts` folder.
1. Copy and paste the following function definition in the `CommonFunctions.ps1`.

   ```powershell
   function Get-WhoAmI{

      $WhoAmIRequest = @{
         Uri = $baseURI + 'WhoAmI'
         Method = 'Get'
         Headers = $baseHeaders
      }

      Invoke-RestMethod @WhoAmIRequest
   }
   ```

   > [!NOTE]
   > This function definition uses a technique called *[splatting](/powershell/module/microsoft.powershell.core/about/about_splatting)*. Splatting makes your commands shorter and easier to read because it passes a collection of parameter values to a command as a unit.

1. Save the `CommonFunctions.ps1` file.
1. Edit the `test.ps1` file, change the content to look like the following script:

   ```powershell
   . C:\scripts\Core.ps1
   . C:\scripts\CommonFunctions.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change this
   # Invoke WhoAmI Function
   Get-WhoAmI | ConvertTo-Json
   ```

1. Change the `https://yourorg.crm.dynamics.com/` value to match the URL for your environment.
1. Press <kbd>F5</kbd> to run the script.

   The output should look exactly like it did before.

### Create table operations functions

Let's put functions to perform common table operations a file named `TableOperations.ps1` so we can reuse them.

1. Create a new text file named `TableOperations.ps1` in your `scripts` folder.
1. Copy and paste the following function definitions in the `TableOperations.ps1`.

   ```powershell
   # The number of times to re-try a request when re-triable errors occur.
   $maxRetries = 3

   function Get-Records {
      param (
         [Parameter(Mandatory)] 
         [String] 
         $setName,
         [Parameter(Mandatory)] 
         [String] 
         $query
      )
      $uri = $baseURI + $setName + $query
      # Header for GET operations that have annotations
      $getHeaders = $baseHeaders.Clone()
      $getHeaders.Add('If-None-Match', $null)
      $getHeaders.Add('Prefer', 'odata.include-annotations="*"')
      $RetrieveMultipleRequest = @{
         Uri     = $uri
         Method  = 'Get'
         Headers = $getHeaders
      }
      Invoke-RestMethod @RetrieveMultipleRequest -MaximumRetryCount $maxRetries
   }

   function New-Record {
      param (
         [Parameter(Mandatory)] 
         [String] 
         $setName,
         [Parameter(Mandatory)] 
         [hashtable]
         $body
      )
      $postHeaders = $baseHeaders.Clone()
      $postHeaders.Add('Content-Type', 'application/json')
      
      $CreateRequest = @{
         Uri     = $baseURI + $setName
         Method  = 'Post'
         Headers = $postHeaders
         Body    = ConvertTo-Json $body
      }
      Invoke-RestMethod @CreateRequest -ResponseHeadersVariable rh -MaximumRetryCount $maxRetries
      $url = $rh['OData-EntityId']
      $selectedString = Select-String -InputObject $url -Pattern '(?<=\().*?(?=\))'
      return [System.Guid]::New($selectedString.Matches.Value.ToString())
   }

   function Get-Record {
      param (
         [Parameter(Mandatory)] 
         [String] 
         $setName,
         [Parameter(Mandatory)] 
         [Guid] 
         $id,
         [String] 
         $query
      )
      $uri = $baseURI + $setName
      $uri = $uri + '(' + $id.Guid + ')' + $query
      $getHeaders = $baseHeaders.Clone()
      $getHeaders.Add('If-None-Match', $null)
      $getHeaders.Add('Prefer', 'odata.include-annotations="*"')
      $RetrieveRequest = @{
         Uri     = $uri
         Method  = 'Get'
         Headers = $getHeaders
      }
      Invoke-RestMethod @RetrieveRequest  -MaximumRetryCount $maxRetries
   }

   function Update-Record {
      param (
         [Parameter(Mandatory)] 
         [String] 
         $setName,
         [Parameter(Mandatory)] 
         [Guid] 
         $id,
         [Parameter(Mandatory)] 
         [hashtable]
         $body
      )
      $uri = $baseURI + $setName
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
      Invoke-RestMethod @UpdateRequest -MaximumRetryCount $maxRetries
   }

   function Remove-Record {
      param (
         [Parameter(Mandatory)] 
         [String]
         $setName,
         [Parameter(Mandatory)] 
         [Guid] 
         $id
      )
      $uri = $baseURI + $setName
      $uri = $uri + '(' + $id.Guid + ')'
      $DeleteRequest = @{
         Uri     = $uri
         Method  = 'Delete'
         Headers = $baseHeaders
      }
      Invoke-RestMethod @DeleteRequest -MaximumRetryCount $maxRetries
   }

   ```

   For information about how to compose these requests, see the following articles:

   - [Compose HTTP requests and handle errors](compose-http-requests-handle-errors.md)
   - [Query data using the Web API](query-data-web-api.md)
   - [Create a table row using the Web API](create-entity-web-api.md)
   - [Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)
   - [Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)
   - The `MaximumRetryCount` parameter and the `$maxRetries` variable are explained in [Manage Dataverse service protection limits](#manage-dataverse-service-protection-limits)

1. Save the `TableOperations.ps1` file.
1. Copy the following code and paste it into the `test.ps1` file.

   ```powershell
   . C:\scripts\Core.ps1
   . C:\scripts\TableOperations.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change this

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
   Write-Host 'Update the record:'
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
   ```

1. Change the `https://yourorg.crm.dynamics.com/` value to match the URL for your environment.
1. Change the dot source folder references (`. C:\scripts\`) to match the folders you're using.
1. Press <kbd>F5</kbd> to run the script.

   The output should look something like this:

   ```powershell
   PS C:\scripts> . 'C:\scripts\test.ps1'
   Retrieve first three account records:

   name                     accountid
   ----                     ---------
   Fourth Coffee (sample)   d2382248-cd99-ee11-be37-000d3a9b7981
   Litware, Inc. (sample)   d4382248-cd99-ee11-be37-000d3a9b7981
   Adventure Works (sample) d6382248-cd99-ee11-be37-000d3a9b7981

   Create an account record:
   Account with ID  a2c3ebc2-39a8-ee11-be37-000d3a8e8e07 created
   Retrieve the created record:

   name                                                          : Example Account
   accountid                                                     : a2c3ebc2-39a8-ee11-be37-000d3a8e8e07
   accountcategorycode                                           : 1
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Preferred Customer

   Update the record:

   Retrieve the updated the record:

   name                                                          : Updated Example account
   accountid                                                     : a2c3ebc2-39a8-ee11-be37-000d3a8e8e07
   accountcategorycode                                           : 2
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Standard

   Delete the record:

   The account with ID  a2c3ebc2-39a8-ee11-be37-000d3a8e8e07 was deleted
   ```

## Handle exceptions

So far in this article you have been copying and pasting code provided for you. But when you start writing your own functions and using them, you'll encounter errors. When these errors occur, they might be from Dataverse, or they could be from your script.

Let's add helper function that can help detect the source of the errors and extract relevant details from errors returned by Dataverse.

1. Edit the `Core.ps1` file to add the following `Invoke-DataverseCommands` function:

   ```powershell
   function Invoke-DataverseCommands {
      param (
         [Parameter(Mandatory)] 
         $commands
      )
      try {
         Invoke-Command $commands
      }
      catch [Microsoft.PowerShell.Commands.HttpResponseException] {
         Write-Host "An error occurred calling Dataverse:" -ForegroundColor Red
         $statuscode = [int]$_.Exception.StatusCode;
         $statusText = $_.Exception.StatusCode
         Write-Host "StatusCode: $statuscode ($statusText)"
         $_.ErrorDetails.Message
      }
      catch {
         Write-Host "An error occurred in the script:" -ForegroundColor Red
         $_
      }
   }
   ```

   The `Invoke-DataverseCommands` function uses the [Invoke-Command cmdlet](/powershell/module/microsoft.powershell.core/invoke-command) to process a set of commands within a [try/catch block](/powershell/module/microsoft.powershell.core/about/about_try_catch_finally). Any errors returned from Dataverse are <xref:Microsoft.PowerShell.Commands.HttpResponseException> errors, so the first `catch` block writes a `An error occurred calling Dataverse:` message to the terminal with the JSON error data.

   Otherwise, the errors are written back to the terminal window with a message: `An error occurred in the script:`

1. Save the `Core.ps1` file.
1. Edit the `test.ps1` file to use the following script that uses an invalid `setName` parameter value. `account` should be `accounts`. [This is a common error](/troubleshoot/power-platform/power-apps/dataverse/web-api-client-errors#resource-not-found-for-the-segment)

   ```powershell
   . C:\scripts\Core.ps1
   . C:\scripts\TableOperations.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change this

   Invoke-DataverseCommands {

      # Retrieve Records
      Write-Host 'Retrieve first three account records:'
         (Get-Records `
         -setName account `
         -query '?$select=name&$top=3').value | 
      Format-Table -Property name, accountid
      
   }
   ```

   Change the `https://yourorg.crm.dynamics.com/` value to match the URL for your environment.

1. Press <kbd>F5</kbd> to run the script.

   The output should look something like this:

   ```powershell
   PS C:\scripts> . 'C:\scripts\test.ps1'
   Retrieve first three account records:
   An error occurred calling Dataverse:
   StatusCode: 404 (NotFound)

   {
   "error": {
      "code": "0x80060888",
      "message": "Resource not found for the segment \u0027account\u0027."
      }
   }
   ```

1. Edit the `test.ps1` file to throw a script error within the `Invoke-DataverseCommands` block:

   ```powershell
   Invoke-DataverseCommands {

      throw 'A script error'

   }
   ```

1. Press <kbd>F5</kbd> to run the script.

   The output should be almost the same as if it wasn't included in the `Invoke-DataverseCommands` block:

   ```powershell
   PS C:\scripts> . 'C:\scripts\test.ps1'
   An error occurred in the script:
   Exception: C:\scripts\test.ps1:8:4
   Line |
      8 |     throw 'A script error'
        |     ~~~~~~~~~~~~~~~~~~~~~~
        | A script error
   ```

## Manage Dataverse service protection limits

We recommend that you specify a value for the PowerShell [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod) [MaximumRetryCount parameter](/powershell/module/microsoft.powershell.utility/invoke-restmethod#-maximumretrycount) for any functions you create that might be used to send large volume of requests to Dataverse. The functions defined for the `TableOperations.ps1` in the [Create table operations functions](#create-table-operations-functions) section of this article demonstrate this best practice.

[Dataverse Service protection API limits](../api-limits.md) help ensure that Dataverse provides consistent availability and performance. When client applications make extraordinary demands on server resources using the Web API, Dataverse returns [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) errors and client application must pause operations for the duration specified in the [Retry-After header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After).

You might never encounter a service protection limit error while you're learning how to use the Dataverse Web API with PowerShell. Scripts you write might be used to send the large number of requests necessary to encounter these errors, so you should know they can occur and how you can manage them using PowerShell.

The `MaximumRetryCount` parameter specifies how many times PowerShell retries a request when a failure code is between 400 and 599, inclusive or 304 is received. This means PowerShell retries Dataverse service protection 429 errors when you include a value for this parameter. The `MaximumRetryCount` parameter can be used with the [RetryIntervalSec](/powershell/module/microsoft.powershell.utility/invoke-restmethod#-retryintervalsec) to specify the number of seconds to wait. The default is 5 seconds. If the error response includes a `Retry-After` header for a 429 error, as Dataverse service protection errors do, that value is used instead.

## Troubleshooting

This section contains some guidance for issues you might encounter.

### Error dialog: connect ENOENT\\\\.\\pipe\\&lt;RANDOM_text&gt; with Open 'launch.json' button

This error might occur at times when debugging using Visual Studio Code. To resolve:

1. Select **View** > **Command Palette...** from the Visual Studio Code menu, or press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>.
1. Type `restart` and select `Powershell: Restart session`. See [PowerShell/vscode-powershell GitHub Issue 4332](https://github.com/PowerShell/vscode-powershell/issues/4332) for more information.


## Next steps

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)
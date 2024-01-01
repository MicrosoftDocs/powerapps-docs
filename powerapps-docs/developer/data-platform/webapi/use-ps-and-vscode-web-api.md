---
title: Use PowerShell and Visual Studio Code with the Dataverse Web API
description: Describes how to use Powershell and Visual Studio Code to create reusable PowerShell functions to interactively test using the Dataverse Web API
ms.date: 12/30/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---
# Use PowerShell and Visual Studio Code with the Dataverse Web API

This article expands on the [Quick Start Web API with PowerShell](quick-start-ps.md) article to describe advanced capabilities using PowerShell and Visual Studio Code with the Dataverse Web API:

- Patterns to create reusable functions
- Handling exceptions
- Manage Dataverse Service protection limits


## Prerequisites

The content of this article has the same prerequisites as the [Quick Start Web API with PowerShell](quick-start-ps.md) article.

[!INCLUDE [cc-visual-studio-code-powershell-prerequisites](../includes/cc-visual-studio-code-powershell-prerequisites.md)]


## Patterns to create reusable functions

[Quick Start Web API with PowerShell](quick-start-ps.md) introduced how to authenticate and call the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) with Visual Studio code, but none of the code was saved and it isn't reusable. 

In this section we will start creating a set of reusable libraries that we can access using *[dot sourcing](/powershell/module/microsoft.powershell.core/about/about_scripts#script-scope-and-dot-sourcing)*. Use dot sourcing to load a file containing PowerShell scripts that can contain functions and variables that become part of the local script scope.

### Create a Connect function

Let's put the code to authenticate to Dataverse in a function called `Connect` inside a file named `Core.ps1` so we can reuse it.

1. Create a folder. In this example, we will create a folder in `C:\scripts`.
1. Open the scripts folder using Visual Studio Code.
1. Create a text file in the scripts folder named `Core.ps1`.
1. Copy and paste the following `Connect` function into the `Core.ps1` file.

   ```powershell
   function Connect {
      param (
         [Parameter(Mandatory)] 
         [String] 
         $uri
      )
      # Set environment URL
      $global:environmentUrl = $uri
      ## Login if not already logged in
      if ($null -eq (Get-AzTenant -ErrorAction SilentlyContinue)) {
         Connect-AzAccount | Out-Null
      }
      # Get an access token
      $token = (Get-AzAccessToken -ResourceUrl $environmentUrl).Token
      # Define common set of headers
      $global:baseHeaders = @{
         'Authorization'    = 'Bearer ' + $token
         'Accept'           = 'application/json'
         'OData-MaxVersion' = '4.0'
         'OData-Version'    = '4.0'
      }
   }
   ```

   > [!NOTE]
   > The script adds the `environmentUrl` and `baseHeaders` variables to the global context using the `$global` [scope modifier](/powershell/module/microsoft.powershell.core/about/about_scopes#scope-modifiers) so that they are available to other scripts in the same session.

1. Create another text file using Visual Studio Code named `test.ps1` in your `scripts` folder.
1. Copy and paste the following script into the `test.ps1` file:

   ```powershell
   . C:\scripts\Core.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change this
   # Invoke WhoAmI Function
   Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') -Method Get -Headers $baseHeaders
   | ConvertTo-Json
   ```

   `. C:\scripts\Core.ps1` at the top of the file shows using dot sourcing to direct the script to load the contents of that file, so you don't need to repeat it here.

1. Change the 'https://yourorg.crm.dynamics.com/' value to match the URL for your environment
1. Press <kbd>F5</kbd> to run the script.

   The output should look something like this:

   ```powershell
   . 'C:\scripts\test.ps1'
   {
   "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
   "BusinessUnitId": "3a277578-5996-ee11-be36-002248227994",
   "UserId": "2c2e7578-5996-ee11-be36-002248227994",
   "OrganizationId": "97bf0e8b-aa99-ee11-be32-000d3a106c3a"
   }
   ```

### Create a WhoAmI function

Let's put the code to invoke the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) in a function called `Get-WhoAmI` inside a file named `CommonFunctions.ps1` so we can reuse it.

1. Create a new text file named `CommonFunctions.ps1` in your `scripts` folder.
1. Copy and paste the following function definition in the `CommonFunctions.ps1`.

   ```powershell
   function Get-WhoAmI{

      $WhoAmIRequest = @{
         Uri = $environmentUrl + 'api/data/v9.2/WhoAmI'
         Method = 'Get'
         Headers = $baseHeaders
      }

      Invoke-RestMethod @WhoAmIRequest
   }
   ```

   > [!NOTE]
   > This function definition uses a technique called *[splatting](/powershell/module/microsoft.powershell.core/about/about_splatting)*. Splatting makes your commands shorter and easier to read because it passes a collection of parameter values to a command as a unit.

1. Save the `CommonFunctions.ps1` file.
1. Edit the `test.ps1` file, change the content to look like the following:

   ```powershell
   . C:\scripts\Core.ps1
   . C:\scripts\CommonFunctions.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change this
   # Invoke WhoAmI Function
   Get-WhoAmI | ConvertTo-Json
   ```

1. Change the 'https://yourorg.crm.dynamics.com/' value to match the URL for your environment.
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

### Create table operations functions

Let's put functions to perform table operations a file named `TableOperations.ps1` so we can reuse them.

1. Create a new text file named `TableOperations.ps1` in your `scripts` folder.
1. Copy and paste the following function definitions in the `TableOperations.ps1`.

   ```powershell
   function Get-Records {
      param (
         [Parameter(Mandatory)] 
         [String] 
         $setName,
         [Parameter(Mandatory)] 
         [String] 
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
         Uri     = $environmentUrl + 'api/data/v9.2/' + $setName
         Method  = 'Post'
         Headers = $postHeaders
         Body    = ConvertTo-Json $body
      }
      Invoke-RestMethod @CreateRequest -ResponseHeadersVariable rh
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

   function Remove-Record {
      param (
         [Parameter(Mandatory)] 
         [String]
         $setName,
         [Parameter(Mandatory)] 
         [Guid] 
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
   ```

   For information about how to compose these requests, see the following articles:

   - [Compose HTTP requests and handle errors](compose-http-requests-handle-errors.md)
   - [Query data using the Web API](query-data-web-api.md)
   - [Create a table row using the Web API](create-entity-web-api.md)
   - [Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)
   - [Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)

1. Save the `TableOperations.ps1` file.
1. Edit the `test.ps1` file, change the content to look like the following:

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
   ```

1. Change the 'https://yourorg.crm.dynamics.com/' value to match the URL for your environment.
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

   Update the record

   Retrieve the updated the record:

   name                                                          : Updated Example account
   accountid                                                     : a2c3ebc2-39a8-ee11-be37-000d3a8e8e07
   accountcategorycode                                           : 2
   accountcategorycode@OData.Community.Display.V1.FormattedValue : Standard

   Delete the record:

   The account with ID  a2c3ebc2-39a8-ee11-be37-000d3a8e8e07 was deleted
   ```

## Handling exceptions

So far in this article you have been copying and pasting code provided for you. But when you start writing your own functions and using them, you will encounter errors. When these errors occur, they might be from Dataverse or they could be from your script.

Let's add a pair of helper functions that can help detect the source of the errors and extract relevant details from errors returned by Dataverse.

1. Edit the `Core.ps1` file to add the following functions:

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
         Get-ErrorDetails | Format-List 
      }
      catch {
         Write-Host "An error occurred in the script:" -ForegroundColor Red
         Write-Host $_
      }
   }

   function Get-ErrorDetails {
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
         # throw $_
         $_.Exception
      }
   }
   ```

   The `Invoke-DataverseCommands` function uses the [Invoke-Command cmdlet](/powershell/module/microsoft.powershell.core/invoke-command) to process a set of commands within a [try/catch block](/powershell/module/microsoft.powershell.core/about/about_try_catch_finally). Any errors returned from Dataverse will be <xref:Microsoft.PowerShell.Commands.HttpResponseException> errors, so the first `catch` block writes a `An error occurred calling Dataverse:` message to the terminal and then processes the errors using the `Get-ErrorDetails` function 

   Otherwise, the errors are written back to the terminal window with a message: `An error occurred in the script:`

   The `Get-ErrorDetails` function processes the JSON error returned from Dataverse to extract common error properties: 
   `statuscode`, `code`, and `message`.

1. Save the `Core.ps1` file.
1. Edit the `test.ps1` file ... TODO

## Manage Dataverse Service protection limits

## Troubleshooting

This section contains some guidance for issues you might encounter.

### Error dialog: connect ENOENT\\\\.\\pipe\\&lt;RANDOM_text&gt; with Open 'launch.json' button

This error might occur at times when debugging using Visual Studio Code. To resolve:

1. Select **View** > **Command Palette...** from the Visual Studio Code menu, or press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>.
1. Type `restart` and select `Powershell: Restart session`. See [PowerShell/vscode-powershell GitHub Issue 4332](https://github.com/PowerShell/vscode-powershell/issues/4332) for more information.
---
title: Use PowerShell and Visual Studio Code with the Dataverse Web API
description: Describes how to use PowerShell and Visual Studio Code to create reusable PowerShell functions to interactively test using the Dataverse Web API
ms.date: 10/30/2024
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
---

# Use PowerShell and Visual Studio Code with the Dataverse Web API

This article expands on the [Quick Start Web API with PowerShell](quick-start-ps.md) article to describe advanced capabilities using PowerShell and Visual Studio Code with the Dataverse Web API to:

- [Create reusable functions](#create-reusable-functions)
- [Handle exceptions](#handle-exceptions)
- [Manage Dataverse service protection limits](#manage-dataverse-service-protection-limits)
- [Debug using Fiddler](#debug-using-fiddler)
- [Download the Dataverse Web API CSDL $metadata document](#download-the-dataverse-web-api-csdl-metadata-document)

> [!NOTE]
> The instructions in this article should work for Windows, Linux, and macOS, but these steps have only been tested on Windows. If changes are needed, let us know by using the **Feedback** section at the bottom of this article.

## Prerequisites

The content of this article has the same prerequisites as the [Quick Start Web API with PowerShell](quick-start-ps.md) article.

[!INCLUDE [cc-visual-studio-code-powershell-prerequisites](../includes/cc-visual-studio-code-powershell-prerequisites.md)]

## Create reusable functions

[Quick Start Web API with PowerShell](quick-start-ps.md) introduced how to authenticate and call the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) with Visual Studio Code. This approach might be all you need to for an ad-hoc test of one or more operations. However, as your scripts become more complex, you might find yourself typing the same code again and again.

In this section, we start creating a set of reusable functions in separate files that we can access using *[dot sourcing](/powershell/module/microsoft.powershell.core/about/about_scripts#script-scope-and-dot-sourcing)*. Use dot sourcing to load a file containing PowerShell scripts that can contain functions and variables that become part of the local script scope.

> [!TIP]
> You can find fully documented definitions of these functions and more in our [GitHub PowerApps-Samples repo](https://github.com/microsoft/PowerApps-Samples/) at [PowerApps-Samples/dataverse/webapi/PS/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/PS)

### Create a Connect function

Let's put the code to authenticate to Dataverse in a function called `Connect` inside a file named `Core.ps1` so we can reuse it in a single line of code.

1. Create a folder. In this example, we create a folder in `C:\scripts`.
1. [Open the scripts folder within Visual Studio Code](https://code.visualstudio.com/docs/editor/workspaces).
1. Create a text file in the scripts folder named `Core.ps1`.
1. Copy and paste the following `Connect` function into the `Core.ps1` file.

   ```powershell
   function Connect {
      param (
         [Parameter(Mandatory)] 
         [String] 
         $environmentUrl
      )

      ## Login interactively if not already logged in
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

      # Define common set of headers
      $global:baseHeaders = @{
         'Authorization'    = 'Bearer ' + $token
         'Accept'           = 'application/json'
         'OData-MaxVersion' = '4.0'
         'OData-Version'    = '4.0'
      }

      # Set baseURI
      $global:baseURI = $environmentUrl + 'api/data/v9.2/'
   }
   ```

   > [!NOTE]
   > The script adds the `baseURI` and `baseHeaders` variables to the global context using the `$global` [scope modifier](/powershell/module/microsoft.powershell.core/about/about_scopes#scope-modifiers) so that they are available to other scripts in the same session.

1. Create another text file in Visual Studio Code named `test.ps1` in your `scripts` folder.
1. Copy and paste the following script into the `test.ps1` file:

   ```powershell
   . $PSScriptRoot\Core.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change to your organization
   # Invoke WhoAmI Function
   Invoke-RestMethod -Uri ($baseURI + 'WhoAmI') -Method Get -Headers $baseHeaders
   | ConvertTo-Json
   ```

   `. $PSScriptRoot\Core.ps1` at the top of the file uses [dot sourcing](/powershell/module/microsoft.powershell.core/about/about_scripts#script-scope-and-dot-sourcing) to direct the script to load the contents of that file.

   Remember to change `https://yourorg.crm.dynamics.com/` to match the URL for your environment.

1. To run the script, press <kbd>F5</kbd>.

   The output might look similar to this output:

   ```powershell
   PS C:\scripts> . 'C:\scripts\test.ps1'
   {
   "@odata.context": "https://yourorg.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",
   "BusinessUnitId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
   "UserId": "22cc22cc-dd33-ee44-ff55-66aa66aa66aa",
   "OrganizationId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
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
1. Change the `test.ps1` file to look like the following script:

   ```powershell
   . $PSScriptRoot\Core.ps1
   . $PSScriptRoot\CommonFunctions.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change to your organization
   # Invoke WhoAmI Function
   Get-WhoAmI | ConvertTo-Json
   ```

   Remember to change the `https://yourorg.crm.dynamics.com/` value to match the URL for your environment.

1. To run the script, press <kbd>F5</kbd>.

   The output should look exactly like it did before.

### Create table operations functions

Let's put functions to perform common table operations a file named `TableOperations.ps1` so we can reuse them.

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
         Uri     = $baseURI + $setName
         Method  = 'Post'
         Headers = $postHeaders
         Body    = ConvertTo-Json $body
      }
      Invoke-RestMethod @CreateRequest -ResponseHeadersVariable rh | Out-Null
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
      $uri = $baseURI + $setName
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
   - [Query data using the Web API](query/overview.md)
   - [Create a table row using the Web API](create-entity-web-api.md)
   - [Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)
   - [Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)

1. Save the `TableOperations.ps1` file.
1. Copy the following code and paste it into the `test.ps1` file.

   ```powershell
   . $PSScriptRoot\Core.ps1
   . $PSScriptRoot\CommonFunctions.ps1
   . $PSScriptRoot\TableOperations.ps1

   Connect 'https://yourorg.crm.dynamics.com/' # change to your organization

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

   Remember to change the `https://yourorg.crm.dynamics.com/` value to match the URL for your environment.

1. To run the script, press <kbd>F5</kbd>.

   The output might look similar to this output:

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

So far in this article you copied and pasted code provided for you. But when you start writing and using your own functions, you can encounter errors. When these errors occur, they might be from Dataverse or your script.

Add a helper function that can help detect the source of the errors and extract relevant details from errors returned by Dataverse.

1. Add the following `Invoke-DataverseCommands` function to the `Core.ps1` file:

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
         # Replaces escaped characters in the JSON
         [Regex]::Replace($_.ErrorDetails.Message, "\\[Uu]([0-9A-Fa-f]{4})", 
            {[char]::ToString([Convert]::ToInt32($args[0].Groups[1].Value, 16))} )

      }
      catch {
         Write-Host "An error occurred in the script:" -ForegroundColor Red
         $_
      }
   }
   ```

   The `Invoke-DataverseCommands` function uses the [Invoke-Command cmdlet](/powershell/module/microsoft.powershell.core/invoke-command) to process a set of commands within a [try/catch block](/powershell/module/microsoft.powershell.core/about/about_try_catch_finally). Any errors returned from Dataverse are <xref:Microsoft.PowerShell.Commands.HttpResponseException> errors, so the first `catch` block writes a `An error occurred calling Dataverse:` message to the terminal with the JSON error data.

   The JSON data in `$_.ErrorDetails.Message` contains some escaped unicode characters. For example: `\u0026` instead of `&` and  `\u0027` instead of `'`. This function includes some code that replaces those characters with the unescaped characters so that they exactly match errors you see elsewhere.

   Otherwise, the errors are written back to the terminal window with a message: `An error occurred in the script:`

1. Save the `Core.ps1` file.
1. Edit the `test.ps1` file to add the following script that uses an invalid `setName` parameter value. The `account` parameter should be `accounts`. [This error is common](/troubleshoot/power-platform/power-apps/dataverse/web-api-client-errors#resource-not-found-for-the-segment).

   ```powershell
   . $PSScriptRoot\Core.ps1
   . $PSScriptRoot\CommonFunctions.ps1
   . $PSScriptRoot\TableOperations.ps1

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

   Remember to change the `https://yourorg.crm.dynamics.com/` value to match the URL for your environment.

1. To run the script, press <kbd>F5</kbd>.

   The output might look similar to this output:

   ```powershell
   PS C:\scripts> . 'C:\scripts\test.ps1'
   Retrieve first three account records:
   An error occurred calling Dataverse:
   StatusCode: 404 (NotFound)

   {
   "error": {
      "code": "0x80060888",
      "message": "Resource not found for the segment 'account'."
      }
   }
   ```

1. Edit the `test.ps1` file to throw a script error within the `Invoke-DataverseCommands` block:

   ```powershell
   Invoke-DataverseCommands {

      throw 'A script error'

   }
   ```

1. To run the script, press <kbd>F5</kbd>.

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

[Dataverse Service protection API limits](../api-limits.md) help ensure that Dataverse provides consistent availability and performance. When client applications make extraordinary demands on server resources using the Web API, Dataverse returns [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) errors and client applications must pause operations for the duration specified in the [Retry-After header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After).

The PowerShell [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod) [MaximumRetryCount parameter](/powershell/module/microsoft.powershell.utility/invoke-restmethod#-maximumretrycount) specifies how many times PowerShell retries a request when a failure code is between 400 and 599, inclusive or 304 is received. This means PowerShell retries Dataverse service protection 429 errors when you include a value for this parameter. The `MaximumRetryCount` parameter can be used with the [RetryIntervalSec](/powershell/module/microsoft.powershell.utility/invoke-restmethod#-retryintervalsec) to specify the number of seconds to wait. The default is 5 seconds. If the error response includes a `Retry-After` header for a 429 error, as Dataverse service protection errors do, that value is used instead.

You might never encounter a service protection limit error while you're learning how to use the Dataverse Web API with PowerShell. However, scripts you write might send a large number of requests that produce errors, so learn how you can best manage them using PowerShell.

If you add the `MaximumRetryCount` parameter to every Dataverse call using `Invoke-RestMethod`, PowerShell retries a broad range of errors. Retrying every error makes your scripts slow, especially when developing and testing. You would need to wait 10 to 15 seconds each time an error occurs, depending on how many retries you specify. An alternative approach is to encapsulate the `Invoke-RestMethod` in your own method that manages retries for specific errors.

The following `Invoke-ResilientRestMethod` function takes a `request` hashtable object as a mandatory parameter and a boolean `returnHeader` flag to indicate whether or not to return the response header. When `$returnHeader` is true, it sends the request using the `Invoke-RestMethod` command with the [ResponseHeadersVariable](/powershell/module/microsoft.powershell.utility/invoke-restmethod#-responseheadersvariable) parameter to capture the headers returned. The function uses [Out-Null](/powershell/module/microsoft.powershell.core/out-null) so the output that represents the empty response body isn't returned with the function. Otherwise, the function sends the request using `Invoke-RestMethod` with the `request` object and returns the response body.

If the `Invoke-RestMethod` fails with a 429 error, it checks if the `request` object has a `MaximumRetryCount` property. If the function succeeds, it creates a `MaximumRetryCount` property set to `3`. The `Invoke-RestMethod` is then retried using the request object and the `Retry-After` response header value. If the `returnHeader` flag is true, it returns the response header. If the `Invoke-RestMethod` fails with any other error, it rethrows the exception.

```powershell
function Invoke-ResilientRestMethod {
   param (
      [Parameter(Mandatory)] 
      $request,
      [bool]
      $returnHeader
   )
   try {
      if ($returnHeader) {
         Invoke-RestMethod @request -ResponseHeadersVariable rhv | Out-Null
         return $rhv
      }
      Invoke-RestMethod @request
   }
   catch [Microsoft.PowerShell.Commands.HttpResponseException] {
      $statuscode = $_.Exception.Response.StatusCode
      # 429 errors only
      if ($statuscode -eq 'TooManyRequests') {
         if (!$request.ContainsKey('MaximumRetryCount')) {
            $request.Add('MaximumRetryCount', 3)
            # Don't need - RetryIntervalSec
            # When the failure code is 429 and the response includes the Retry-After property in its headers, 
            # the cmdlet uses that value for the retry interval, even if RetryIntervalSec is specified
         }
         # Will attempt retry up to 3 times
         if ($returnHeader) {
            Invoke-RestMethod @request -ResponseHeadersVariable rhv | Out-Null
            return $rhv
         }
         Invoke-RestMethod @request
      }
      else {
         throw $_
      }
   }
   catch {
      throw $_
   }
}
```

You can use a similar function in your reusable functions. When functions need to return values from the header of the response, they need to set the `returnHeader` value to `$true`. For example, the following `New-Record` function modifies the example function in [Create table operations functions](#create-table-operations-functions) to use `Invoke-ResilientRestMethod` instead of `Invoke-RestMethod` directly.

```powershell
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
   # Before: 
   # Invoke-RestMethod @CreateRequest -ResponseHeadersVariable rh | Out-Null

   # After:
   $rh = Invoke-ResilientRestMethod -request $CreateRequest -returnHeader $true
   $url = $rh['OData-EntityId']
   $selectedString = Select-String -InputObject $url -Pattern '(?<=\().*?(?=\))'
   return [System.Guid]::New($selectedString.Matches.Value.ToString())
}
```

Otherwise, `Invoke-ResilientRestMethod` can replace the `Invoke-RestMethod` as shown in this `Get-Record` example:

```powershell
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
   # Before:
   # Invoke-RestMethod @RetrieveRequest

   # After: 
   Invoke-ResilientRestMethod $RetrieveRequest
}
```

The only difference is that you pass the hashtable (`$RetrieveRequest`) to the method instead of using splatting (`@RetrieveRequest`). Otherwise, you get a script error: `A parameter cannot be found that matches parameter name 'Headers'.`

## Debug using Fiddler

[Fiddler](https://www.telerik.com/fiddler) is a web debugging proxy used to view HTTP traffic on your computer. Viewing this data is useful when debugging scripts. By default, HTTP requests and responses sent using [Invoke-RestMethod cmdlet](/powershell/module/microsoft.powershell.utility/invoke-restmethod) aren't visible when you use Fiddler.

To view HTTP traffic in Fiddler, set the `Invoke-RestMethod` [Proxy parameter](/powershell/module/microsoft.powershell.utility/invoke-restmethod#-proxy) to the URL configured as the Fiddler proxy on your local computer. By default, the URL is `http://127.0.0.1:8888`. Your URL might be different.

For example, if you invoke the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI) with the `-Proxy` parameter set while Fiddler is capturing traffic:

```powershell
Invoke-RestMethod `
   -Uri ($environmentUrl + 'api/data/v9.2/WhoAmI') `
   -Method Get `
   -Headers $baseHeaders `
   -Proxy 'http://127.0.0.1:8888'
```

In Fiddler, you can see all the details:

```http
GET https://yourorg.api.crm.dynamics.com/api/data/v9.2/WhoAmI HTTP/1.1
Host: yourorg.api.crm.dynamics.com
OData-MaxVersion: 4.0
Accept: application/json
Authorization: Bearer [REDACTED]
OData-Version: 4.0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Microsoft Windows 10.0.22631; en-US) PowerShell/7.4.0
Accept-Encoding: gzip, deflate, br


HTTP/1.1 200 OK
Cache-Control: no-cache
Allow: OPTIONS,GET,HEAD,POST
Content-Type: application/json; odata.metadata=minimal
Expires: -1
Vary: Accept-Encoding
x-ms-service-request-id: 7341c0c1-3343-430b-98ea-292567ed4776
Set-Cookie: ARRAffinity=f60cbee43b7af0a5f322e7ce57a018546ed978f67f0c11cbb5e15b02ddb091a915134d20c556b0b34b9b6ae43ec3f5dcdad61788de889ffc592af7aca85fc1c508DC0FC94CB062A12107345846; path=/; secure; HttpOnly
Set-Cookie: ReqClientId=4fc95009-0b3d-4a19-b223-0d80745636ac; expires=Sun, 07-Jan-2074 21:10:42 GMT; path=/; secure; HttpOnly
Set-Cookie: orgId=00aa00aa-bb11-cc22-dd33-44ee44ee44ee; expires=Sun, 07-Jan-2074 21:10:42 GMT; path=/; secure; HttpOnly
x-ms-service-request-id: 1ee13aa7-47f3-4a75-95fa-2916775a1f79
Strict-Transport-Security: max-age=31536000; includeSubDomains
REQ_ID: 1ee13aa7-47f3-4a75-95fa-2916775a1f79
CRM.ServiceId: framework
AuthActivityId: 0b562cc3-56f6-44f0-a26e-4039cfc4be6a
x-ms-dop-hint: 48
x-ms-ratelimit-time-remaining-xrm-requests: 1,200.00
x-ms-ratelimit-burst-remaining-xrm-requests: 5999
OData-Version: 4.0
X-Source: 110212218438874147222728177124203420477168182861012399121919014511175711948418152
Public: OPTIONS,GET,HEAD,POST
Set-Cookie: ARRAffinity=f60cbee43b7af0a5f322e7ce57a018546ed978f67f0c11cbb5e15b02ddb091a915134d20c556b0b34b9b6ae43ec3f5dcdad61788de889ffc592af7aca85fc1c508DC0FC94CB062A12107345846; path=/; secure; HttpOnly
X-Source: 2302101791355821068628523819830862152291172232072372448021147103846182145238216119
Date: Sun, 07 Jan 2024 21:10:42 GMT
Content-Length: 277

{"@odata.context":"https://yourorg.api.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse","BusinessUnitId":"11bb11bb-cc22-dd33-ee44-55ff55ff55ff","UserId":"22cc22cc-dd33-ee44-ff55-66aa66aa66aa","OrganizationId":"00aa00aa-bb11-cc22-dd33-44ee44ee44ee"}
```

If Fiddler isn't running, you get an error:

```powershell
Invoke-RestMethod: C:\scripts\test.ps1:8:1
Line |
   8 |  Invoke-RestMethod `
     |  ~~~~~~~~~~~~~~~~~~~
     | No connection could be made because the target machine actively refused it.
```

If you choose to route all your `Invoke-RestMethod` calls through a single function, such as the `Invoke-ResilientRestMethod` described in [Manage Dataverse service protection limits](#manage-dataverse-service-protection-limits), you might set some variables in the `Core.ps1` file to configure this option in a single location.

```powershell
# Set to true only while debugging with Fiddler
$debug = $true
# Set this value to the Fiddler proxy URL configured on your computer
$proxyUrl = 'http://127.0.0.1:8888'
```

Within your centralized function, you can set the `-Proxy` parameter with splatting and use the `$request` hash table only when debugging with Fiddler.

```powershell
function Invoke-ResilientRestMethod {
   param (
      [Parameter(Mandatory)] 
      $request,
      [bool]
      $returnHeader
   )

   if ($debug) {
      $request.Add('Proxy', $proxyUrl)
   }

   ...
```

[Learn about capturing web traffic with Fiddler](https://docs.telerik.com/fiddler/observe-traffic/tasks/capturewebtraffic)

## Download the Dataverse Web API CSDL $metadata document

The Common Schema Definition Language (CSDL) $metadata is the source of truth about Dataverse Web API capabilities. You can view it in a browser, but you might find it easier to download the file and view it within Visual Studio Code. The following script is a modified version of the script introduced in [Quick Start Web API with PowerShell](quick-start-ps.md). The difference is that it uses the [Invoke-WebRequest cmdlet](/powershell/module/microsoft.powershell.utility/invoke-webrequest), which is more appropriate for downloading an XML document.

```powershell
$environmentUrl = 'https://yourorg.crm.dynamics.com/' # change to your organization
$writeFileTo =  'C:\temp\yourorg.xml' # change to your organization

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
$xmlHeaders = @{
   'Authorization'    = 'Bearer ' + $token
   'Accept'           = 'application/xml'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}

$doc = [xml](Invoke-WebRequest `
      -Uri ($environmentUrl + 'api/data/v9.2/$metadata?annotations=true') `
      -Method 'Get' `
      -Headers $xmlHeaders ).Content

$StringWriter = New-Object System.IO.StringWriter
$XmlWriter = New-Object System.XMl.XmlTextWriter $StringWriter
$xmlWriter.Formatting = 'indented'
$xmlWriter.Indentation = 2
$doc.WriteContentTo($XmlWriter)
$XmlWriter.Flush()
$StringWriter.Flush()
Set-Content -Path $writeFileTo -Value $StringWriter.ToString()
code $writeFileTo
```

1. Copy the script.
1. Edit the `$environmentUrl` and `$writeFileTo` variables to match your need.
1. Run the script in Visual Studio Code.

The Dataverse Web API CSDL $metadata document opens in Visual Studio Code.

You might get a notification saying: *For performance reasons, document symbols are limited to 5,000 items. If a new limit is set, close and reopen this file to recompute document symbols*.

The notification gives the option to change the Visual Studio Code XML extension `xml.symbols.maxItemsComputed` limit. For most Dataverse Web API CSDL $metadata documents, setting the limit to `500000` should be sufficient.

## Troubleshooting

This section contains some guidance for issues you might encounter.

### Error dialog: connect ENOENT\\\\.\\pipe\\&lt;RANDOM_text&gt; with Open 'launch.json' button

This error might occur when debugging with Visual Studio Code. To resolve the error:

1. Select **View** > **Command Palette...** from the Visual Studio Code menu, or press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>.
1. Type `restart` and select `Powershell: Restart session`. See [PowerShell/vscode-powershell GitHub Issue 4332](https://github.com/PowerShell/vscode-powershell/issues/4332) for more information.

## Next steps

Learn more about Dataverse Web API capabilities by understanding the service documents.

> [!div class="nextstepaction"]
> [Web API types and operations](web-api-types-operations.md)

Review and run sample code.

> [!div class="nextstepaction"]
> [Web API Data operations Samples (PowerShell)](web-api-samples-powershell.md)

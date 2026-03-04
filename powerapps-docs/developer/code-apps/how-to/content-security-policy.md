---
title: "How to: Configure Content Security Policy"
description: "Learn how to configure Content Security Policy for code apps"
author: EvanCahill
ms.author: hacahill
ms.reviewer: jdaly
ms.service: powerapps
ms.topic: how-to
ms.date: 02/02/2026
---

# How to: Configure Content Security Policy

This article explains how to configure [Content Security Policy](https://developer.mozilla.org/docs/Web/HTTP/CSP) (CSP) for code apps.
You can set up the individual CSP directives, choose whether to enforce CSP or use reporting only, and specify where to send reports.

Set these settings at the environment level to apply to all code apps in the environment.
By default, CSP is enforced with the following directive configuration.
The `<platform>` value represents values required by the platform.

| Directive                          | Default Value                    |
| ---------------------------------- | -------------------------------- |
| [frame-ancestors][frame-ancestors] | `'self' https://*.powerapps.com` |
| [script-src][script-src]           | `'self' <platform>`              |
| [img-src][img-src]                 | `'self' data: <platform>`        |
| [style-src][style-src]             | `'self' 'unsafe-inline'`         |
| [font-src][font-src]               | `'self'`                         |
| [connect-src][connect-src]         | `'none'`                         |
| [frame-src][frame-src]             | `'self'`                         |
| [form-action][form-action]         | `'none'`                         |
| [base-uri][base-uri]               | `'self'`                         |
| [child-src][child-src]             | `'none'`                         |
| [default-src][default-src]         | `'self'`                         |
| [manifest-src][manifest-src]       | `'none'`                         |
| [media-src][media-src]             | `'self' data:`                   |
| [object-src][object-src]           | `'self' data:`                   |
| [worker-src][worker-src]           | `'none'`                         |

<!-- Find reference-style links at the bottom of this article -->

When you customize a directive, the values you supply are appended to the default value.
If the default value is `'none'`, your custom values replace the default value.

If your environment has a Dataverse instance, you can configure the CSP settings in the [Power Platform admin center](#configure-csp-by-using-power-platform-admin-center).
Otherwise, see the instructions for configuring CSP by using the [REST API](#configure-csp-by-using-rest-api).

## Prerequisites

- You must be an administrator of the environment to configure CSP settings.

## Configure CSP by using Power Platform admin center

To access the CSP settings for code apps:

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. In the navigation pane, select **Manage**. In the **Manage** pane, select **Environments**.
1. On the **Environments** page, select an environment.
1. In the command bar, select **Settings**.
1. Expand **Product**, and then select **Privacy + Security**.
1. Under **Content security policy**, select the **App** tab.

:::image type="content" source="media/content-security-policy-settings-overview.png" alt-text="Image of the Code Apps CSP setting UO in the Power Platform admin center":::

### Enable reporting

The **Enable reporting** toggle controls whether CSP violation reports are sent.
When you enable it, specify a valid endpoint.
The system sends violation reports to this endpoint regardless of whether **Enforce content security policy** is enabled.
For more information about reporting, see the [reporting documentation](https://developer.mozilla.org/docs/Web/HTTP/Guides/CSP#violation_reporting).

:::image type="content" source="media/content-security-policy-reporting-setting.png" alt-text="Screenshot of a toggle labeled Enable reporting turned on and a text box labeled Reporting endpoint containing a url.":::

### Configure directives

Use the **Configure directives** section to control the value of individual directives.
If you leave the defaults toggled on, you use the default values specified earlier.
If you turn off the toggle, you can add custom values for the directive.
Custom values are merged with the default values for the directive.
If you turn off a toggle and leave the Source list blank, you disable the directive.

The following example shows three different directives with different configurations:

- `frame-ancestors` is enabled and set to use its default value. The resulting directive value is: `'self' https://*.powerapps.com`
- `script-src` is enabled and adds another source, which is merged with the default value. The resulting directive value is: `script-src 'self' https://contoso.com`
- `img-src` is disabled. The directive is omitted from the policy.

:::image type="content" source="media/content-security-policy-directive-settings.png" alt-text="Screenshot of CSP directives configured in different states":::

## Configure CSP by using REST API

You can programmatically configure CSP by using the [Microsoft Power Platform API](/rest/api/power-platform/).
Manage settings by using the [Environment Management Settings](/rest/api/power-platform/environmentmanagement/environment-management-settings) API: `https://api.powerplatform.com/environmentmanagement/environments/{environmentId}/settings`

The following settings are available:

- `PowerApps_CSPEnabledCodeApps` controls whether CSP is enforced for code apps.
- `PowerApps_CSPReportingEndpoint` controls the reporting of CSP violations.
  Set this setting to a valid URL where CSP violation reports are sent or `null` if reporting is disabled.
- `PowerApps_CSPConfigCodeApps` is the configuration for directives. Set this setting to a stringified JSON object with the format:
  
  ```jsonc
  {
    "default-src": {
      "sources": [{ "source": "'self'" }]
    },
    "style-src": {
      "sources": [{ "source": "'self'" }, { "source": "https://contoso.com" }]
    }
    // Additional directives
  }
  ```

### PowerShell helper functions

To simplify calling the REST API, use the following PowerShell functions.

#### Get-CodeAppContentSecurityPolicy

Use the `Get-CodeAppContentSecurityPolicy` function to retrieve the current CSP settings for code apps in a specified environment. The function returns the enforcement status, reporting endpoint, and configured directives.

```powershell
  <#
  .SYNOPSIS
    Retrieves the Content Security Policy settings for code apps in a Power Platform environment.

  .DESCRIPTION
    Gets the current CSP configuration for code apps, including enforcement status,
    reporting endpoint, and configured directives from the Power Platform API.

  .PARAMETER Env
    The environment ID of the Power Platform environment.

  .PARAMETER Token
    A secure string containing the authentication token for the Power Platform API.

  .PARAMETER ApiEndpoint
    The base URI of the Power Platform API. Defaults to 'https://api.powerplatform.com/'.

  .OUTPUTS
    A hashtable containing:
    - ReportingEndpoint: The URL where CSP violation reports are sent.
    - Enabled: Whether CSP enforcement is enabled.
    - Directives: A hashtable of CSP directives and their configured sources.

  .EXAMPLE
    Get-CodeAppContentSecurityPolicy -Token $token -Env "00000000-0000-0000-0000-000000000000"
  #>
function Get-CodeAppContentSecurityPolicy {
  [CmdletBinding()]
  param(
    [Parameter(Mandatory = $true)]
    [string]$Env,

    [Parameter(Mandatory = $true)]
    [securestring]$Token,

    [uri]$ApiEndpoint = 'https://api.powerplatform.com/'
  )
  $ErrorActionPreference = 'Stop'

  $escapedEnv = [System.Uri]::EscapeDataString($Env)
  $uri = [Uri]::new($ApiEndpoint, "/environmentmanagement/environments/$escapedEnv/settings?api-version=2022-03-01-preview&`$select=PowerApps_CSPReportingEndpoint,PowerApps_CSPEnabledCodeApps,PowerApps_CSPConfigCodeApps")

  $resp = Invoke-RestMethod -Uri $uri -Method Get -Authentication Bearer -Token $Token
  $data = $resp.objectResult[0];

  if ($null -ne $data.PowerApps_CSPConfigCodeApps) {
    $parsed = $data.PowerApps_CSPConfigCodeApps | ConvertFrom-Json -AsHashtable -Depth 10
    $config = @{}
    foreach ($directive in $parsed.Keys) {
      $sources = $parsed[$directive].sources | Select-Object -ExpandProperty source
      $config[$directive] = $sources
    }
  }

  @{
    ReportingEndpoint = $data.PowerApps_CSPReportingEndpoint
    Enabled           = $data.PowerApps_CSPEnabledCodeApps ?? $true
    Directives        = $config
  }
}
```

#### Set-CodeAppContentSecurityPolicy

Use the `Set-CodeAppContentSecurityPolicy` function to update CSP settings for code apps in a specified environment. You can enable or disable CSP enforcement, configure a reporting endpoint, and update individual directives.

```powershell
<#
.SYNOPSIS
  Updates the Content Security Policy settings for code apps in a Power Platform environment.

.DESCRIPTION
  Configures CSP settings for code apps, including enabling or disabling enforcement,
  setting a reporting endpoint for violation reports, and updating CSP directives.

.PARAMETER Env
  The environment ID of the Power Platform environment.

.PARAMETER Token
  A secure string containing the authentication token for the Power Platform API.

.PARAMETER ApiEndpoint
  The base URI of the Power Platform API. Defaults to 'https://api.powerplatform.com/'.

.PARAMETER ReportingEndpoint
  The URL where CSP violation reports are sent. Pass $null to disable reporting.

.PARAMETER Enabled
  Whether to enable or disable CSP enforcement for code apps.

.PARAMETER Directives
  A hashtable of CSP directives and their source values. Replaces the entire directive collection.

.EXAMPLE
  Set-CodeAppContentSecurityPolicy -Token $token -Env "00000000-0000-0000-0000-000000000000" -Enabled $true

.EXAMPLE
  Set-CodeAppContentSecurityPolicy -Token $token -Env "00000000-0000-0000-0000-000000000000" -ReportingEndpoint "https://contoso.com/report"
#>
function Set-CodeAppContentSecurityPolicy {
  [CmdletBinding(SupportsShouldProcess = $true)]
  param(
    [Parameter(Mandatory = $true)]
    [string]$Env,

    [Parameter(Mandatory = $true)]
    [securestring]$Token,

    [uri]$ApiEndpoint = 'https://api.powerplatform.com/',

    [AllowNull()]
    [string]$ReportingEndpoint,

    [bool]$Enabled,

    [hashtable]$Directives
  )
  $payload = @{}

  if ($PSBoundParameters.ContainsKey('ReportingEndpoint')) {
    $payload['PowerApps_CSPReportingEndpoint'] = $ReportingEndpoint
  }

  if ($PSBoundParameters.ContainsKey('Enabled')) {
    $payload['PowerApps_CSPEnabledCodeApps'] = $Enabled
  }

  if ($PSBoundParameters.ContainsKey('Directives')) {
    $allowed = @(
      'Frame-Ancestors', 'Script-Src', 'Img-Src', 'Style-Src', 'Font-Src',
      'Connect-Src', 'Frame-Src', 'Form-Action', 'Base-Uri', 'Child-Src',
      'Default-Src', 'Manifest-Src', 'Media-Src', 'Object-Src', 'Worker-Src'
    )
    $textInfo = [System.Globalization.CultureInfo]::InvariantCulture.TextInfo
    $config = @{}
    foreach ($key in $Directives.Keys) {
      $directive = $textInfo.ToTitleCase($key)
      if ($allowed -notcontains $directive) {
        throw "Invalid CSP directive: $directive"
      }
      $sources = $Directives[$key] | ForEach-Object { @{ source = $_ } }
      $config[$directive] = @{ sources = @($sources) }
    }
    $payload['PowerApps_CSPConfigCodeApps'] = ($config | ConvertTo-Json -Depth 10 -Compress)
  }

  $escapedEnv = [System.Uri]::EscapeDataString($Env)
  $uri = [Uri]::new($ApiEndpoint, "/environmentmanagement/environments/$escapedEnv/settings?api-version=2022-03-01-preview")
  $body = $payload | ConvertTo-Json -Depth 10

  Invoke-RestMethod -Uri $uri -Method Patch -Authentication Bearer -Token $Token -Body $body -ContentType 'application/json' | Out-Null
}
```

### Authentication

To use the PowerShell functions, supply an authentication token.
Use the [Microsoft Authentication CLI](https://github.com/AzureAD/microsoft-authentication-cli) to generate this token.
Refer to their documentation for installation instructions.
After installing the tool, use the following command to generate an authentication token:

```powershell
$tenantId = "<your-tenant-id>"
$clientId = "9cee029c-6210-4654-90bb-17e6e9d36617" # This is the client id of the Power Platform CLI
$token = azureauth aad --resource "https://api.powerplatform.com/" --tenant $tenantId --client $clientId --output token | ConvertTo-SecureString -AsPlainText -Force
```

### Examples

The following examples show how to use the [PowerShell helper functions](#powershell-helper-functions) to manage CSP settings.

#### Retrieve settings

```powershell
Get-CodeAppContentSecurityPolicy -Token $token -Env "<your-env-id>"
```

```output
Name                           Value
----                           -----
Enabled                        True
ReportingEndpoint              http://constoso.com/report
Directives                     {[Frame-Ancestors, System.Object[]], [Script-Src, 'self']}
```

#### Enable or disable enforcement

Use the `-Enabled` parameter to turn CSP enforcement on or off for code apps.

```powershell
Set-CodeAppContentSecurityPolicy -Token $token -Env "<your-env-id>" -Enabled $true
```

#### Enable or disable reporting

Use the `-ReportingEndpoint` parameter to specify where CSP violation reports are sent, or pass `$null` to disable reporting.

```powershell
Set-CodeAppContentSecurityPolicy -Token $token -Env "<your-env-id>" -ReportingEndpoint "https://contoso.com/report"
```

To disable reporting, pass `$null`:

```powershell
Set-CodeAppContentSecurityPolicy -Token $token -Env "<your-env-id>" -ReportingEndpoint $null
```

#### Update directives

> [!WARNING]
> Updating the directives replaces the entire directive collection.
> To update the existing directives, first retrieve them and then update them in place.

To reset a directive to its default value, omit it from the collection.
To disable a directive entirely, pass an empty array for the directive.

```powershell
$env = "<your-env-id>"
$directives = (Get-CodeAppContentSecurityPolicy -Token $token -Env $env).Directives
# Update existing directives
Set-CodeAppContentSecurityPolicy -Token $token -Env $env -Directives $directives
```

<!--Reference links in article-->

[frame-ancestors]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors
[script-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/script-src
[img-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/img-src
[style-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/style-src
[font-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/font-src
[connect-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src
[frame-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/frame-src
[form-action]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/form-action
[base-uri]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/base-uri
[child-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/child-src
[default-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/default-src
[manifest-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/manifest-src
[media-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/media-src
[object-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/object-src
[worker-src]:  https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Security-Policy/worker-src

---
title: "How to: Configure Content Security Policy (preview)"
description: "Learn how to configure Content Security Policy for code apps"
author: EvanCahill
ms.author: hacahill
ms.reviewer: jdaly
ms.service: powerapps
ms.topic: how-to
ms.date: 01/16/2026
---

# How to: Configure Content Security Policy (preview)

In this article, you will learn how to configure [Content Security Policy](https://developer.mozilla.org/docs/Web/HTTP/CSP) (CSP) for code apps.
You can configure the following settings:

- Whether CSP is enabled
- The values of individual directives
- Whether reporting is enabled and where reports are sent

These settings are configured at the environment level and apply to all code apps in the environment.
CSP is enabled by default with the following directives:

| Directive                          | Default Value                                                                                                                 |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [frame-ancestors][frame-ancestors] | `'self' https://*.powerapps.com`                                                                                              |
| [script-src][script-src]           | `'self' 'unsafe-inline'`                                                                                                      |
| [img-src][img-src]                 | `'self' https://res-dev.cdn.officeppe.net/ https://res-sdf.cdn.office.net/ <https://cdn.hubblecontent.osi.office.net/> data:` |
| [style-src][style-src]             | `'self' 'unsafe-inline'`                                                                                                      |
| [font-src][font-src]               | `'self' 'unsafe-inline'`                                                                                                      |
| [connect-src][connect-src]         | `'none'`                                                                                                                      |
| [frame-src][frame-src]             | `'self'`                                                                                                                      |
| [form-action][form-action]         | `'none'`                                                                                                                      |
| [base-uri][base-uri]               | `'self'`                                                                                                                      |
| [child-src][child-src]             | `'none'`                                                                                                                      |
| [default-src][default-src]         | `'self'`                                                                                                                      |
| [manifest-src][manifest-src]       | `'none'`                                                                                                                      |
| [media-src][media-src]             | `'self' data:`                                                                                                                |
| [object-src][object-src]           | `'self' data:`                                                                                                                |
| [worker-src][worker-src]           | `'none'`                                                                                                                      |

If your environment has a Dataverse instance you can configure the CSP settings in the [Power Platform admin center](#configure-csp-using-power-platform-admin-center).
Otherwise, please see the instructions for configuring CSP using the [REST API](#configure-csp-using-rest-api).

## Prerequisites

- You must be an administrator of the environment to configure CSP settings.

## Configure CSP using Power Platform admin center

To access the CSP settings for code apps:

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. In the navigation pane, select **Manage**, then in the **Manage** pane, select **Environments**.
1. On the **Environments** page, select an environment.
1. In the command bar, select **Settings**.
1. Expand **Product**, then select **Privacy + Security**.
1. Under **Content security policy** select the **App** tab.

:::image type="content" source="media/csp-overview.png" alt-text="Image of the Code Apps CSP setting UO in the Power Platform admin center":::

### Enable reporting

The **Enable reporting** toggle controls whether CSP violation reports are sent.
When enabled you are required to specify a valid endpoint.
Violation reports are sent to this endpoint regardless of whether **Enforce content security policy** is enabled. For more information, please refer to the MDN [documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP#violation_reporting).

:::image type="content" source="media/csp-reporting.png" alt-text="Screenshot of a toggle labeled Enable reporting turned on and a text box labeled Reporting endpoint containing a url.":::

### Configure directives

The **Configure directives** section allows you to control the value of individual directives.
Leaving the defaults toggled on uses the default values specified earlier.
Turning off the toggle allows you to add custom values for the directive.
Custom values are merged with the default values for the directive.
Turning off a toggle and leaving the Source list blank disabled the directive.

The example below shows three different directives with different configurations.

- `frame-ancestors` is enabled and set to use its default value. i.e. `'self' https://*.powerapps.com`
- `script-src` is enabled and adds an additional source which will be merged with the default value. i.e. `script-src 'self' 'unsafe-inline' https://contoso.com`
- `img-src` is disabled. The directive will not be sent.

:::image type="content" source="media/csp-directives.png" alt-text="Screenshot":::

## Configure CSP using REST API

You can programmatically configure CSP using the [Microsoft Power Platform API](https://learn.microsoft.com/en-us/rest/api/power-platform/).
Settings are managed with the Environment Management Settings API i.e. `https://api.powerplatform.com/environmentmanagement/environments/{environmentId}/settings`

The following settings are available:

- `PowerApps_CSPEnabledCodeApps` controls whether CSP is enforced for code apps.
- `PowerApps_CSPReportingEndpoint` controls the reporting of CSP violations.
  This setting should be set to a valid URL where CSP violation report will be sent or `null` if reporting is disabled.
- `PowerApps_CSPConfigCodeApps` is the configuration for directives. This setting is a stringified JSON object with the format:
  
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

As an alternative to directly calling the REST API, we have created the following PowerShell functions you can use to configure CSP.

```powershell
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

```powershell
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

To use the PowerShell functions you will need to supply an authentication token.
We recommend using the [Microsoft Authentication CLI](https://github.com/AzureAD/microsoft-authentication-cli) to generate this token.
Please refer to their documentation for installation instructions.
Once you have installed the tool you can use the following command to generate an authentication token.

```powershell
$tenantId = "<your-tenant-id>"
$clientId = "9cee029c-6210-4654-90bb-17e6e9d36617" # This is the client id of the Power Platform CLI
$token = azureauth aad --resource "https://api.powerplatform.com/" --tenant $tenantId --client $clientId --output token | ConvertTo-SecureString -AsPlainText -Force
```

### Examples

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

#### Enable/Disable enforcement

```powershell
Set-CodeAppContentSecurityPolicy -Token $token -Env "<your-env-id>" -Enabled $true
```

#### Enable/Disable reporting

```powershell
Set-CodeAppContentSecurityPolicy -Token $token -Env "<your-env-id>" -ReportingEndpoint "https://contoso.com/report"
```

To disable reporting, pass `$null`:

```powershell
Set-CodeAppContentSecurityPolicy -Token $token -Env "<your-env-id>" -ReportingEndpoint $null
```

#### Update directives

Updating the directives replaces the entire directive collection.
To avoid overriding existing directives please retrieve the existing settings and edit them.

To reset a directive to its default value, omit it from the collection.
To disable a directive entirely pass an empty array for the directive.

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

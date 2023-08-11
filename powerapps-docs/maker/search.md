---
title: Find it with unified search
description: Use unified search to find apps, flows, templates, and web content.
author: Mattp123
ms.subservice: common
ms.topic: conceptual
ms.date: 05/25/2023
ms.author: matp
search.audienceType: 
  - maker
contributors:
  - mattp123
  - v-aangie
ms.reviewer: angieandrews
---

# Find it with unified search

Unified search helps you quickly discover apps in Power Apps, flows in Power Automate, templates, and external web content. From a single entry point, you can find:

|Item  |Content type  |
|---------|---------|
|(Power Apps) Apps that have been built and published   | Environment        |
|(Power Automate) Flows that have been built and published   | Environment        |
|Templates    | Environment  |
|Documentation and learn content    |  External web     |
|Community content     |  External web       |
|Blog posts     | External web        |
| Video tutorials  | External web  |

> [!NOTE]
> To open the Power Automate documentation, go to the [Power Automate Overview](/power-automate/getting-started).

## Use search

By default, search displays items only from your environment, which are apps, flows, and templates.

1. To display suggestions, type in the **Search** box.

    - For Power Apps, suggestions include apps and templates.
    - For Power Automate, suggestions include flows and templates.

1. To go directly to that item, select any suggestion.

1. (Optional) To expand your search to external web content, select **See web results**.

    :::image type="content" source="data-platform/media/search-see-web-results.png" alt-text="See web results .":::

    > [!WARNING]
    > Don't send personal data or confidential/proprietary information as part of your search when you choose this option.

To prevent users from using the **See web results** option to perform external web content searches for an environment, go to [Manage search providers](#manage-search-providers).

## Manage search providers

The Microsoft.PowerApps.Administration.PowerShell module includes the cmdlets that members of either the Global admins, Azure Active Directory Global admins, or Dynamics 365 admin security groups can use to modify the search providers. More information: [Get started using the Power Apps admin module](/powershell/powerapps/get-started-powerapps-admin).

By default, all search providers are enabled, except for the docs search provider `PowerPlatform.Search.disableDocsSearch`. The following search providers can be enabled or disabled.

|Search provider namespace |Default |Description  |
|---------|---------|---------|
|`PowerPlatform.Search.disableDocsSearch`  |True |  Setting the provider namespace to True disables search for the provider. When this provider is disabled, users in the environment will see a message that Microsoft Learn and Documentation search categories have been turned off by the administrator in the search results page.  <br /><br /> When the provider is enabled, users' keywords might be sent outside their company, region, or cloud. Make sure keywords don't contain sensitive or confidential information. |
|`PowerPlatform.Search.disableCommunitySearch`     |False | Setting the provider namespace to True disables search for the provider. When this provider is disabled, users in the environment will see a message that Community and Blog search categories have been turned off by the administrator in the search results page.   |
| `PowerPlatform.Search.disableBingVideoSearch`    |False |Setting the provider namespace to True disables search for the provider. When this provider is disabled, users in the environment will see a message that Video search categories have been turned off by the administrator in the search results page.   |

To return the current settings including which search providers are enabled or disabled, run this cmdlet:
`Get-TenantSettings`

### Disable a search provider

Members of the Power Platform admin role can disable or enable a search provider by specifying the search provider namespace when running the Set-TenantSettings cmdlet.

For example, to disable the Microsoft Learn and Documentation search provider, run this cmdlet:

```powershell
$requestBody = @{PowerPlatform.Search.disableDocsSearch = $true}
Set-TenantSettings -RequestBody $requestBody
```

To enable the Microsoft Learn and Documentation search provider, run this cmdlet:

```powershell
$requestBody = @{PowerPlatform.Search.disableDocsSearch = $false}
Set-TenantSettings -RequestBody $requestBody
```

Alternatively, run:
```powershell
$settings = Get-TenantSettings 
$settings.PowerPlatform.Search.disableDocsSearch = $false
Set-TenantSettings -RequestBody $settings
```

### See also

[Overview of creating apps in Power Apps](index.md)

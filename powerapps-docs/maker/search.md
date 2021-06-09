---
title: Find the apps, templates, and information you need using Power Apps unified search | Microsoft Docs
description: Use unified search to find what you need.
author: Mattp123
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 02/24/2021
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Find the apps, templates, and information you need

Power Apps unified search helps you quickly discover apps, templates, and external web content. From a single entry point you can find:

|Item  |Content type  |
|---------|---------|
|Apps that have been built and published   | Environment        |
|Templates    | Environment  |
|Documentation and learn content    |  External web     |
|Community content     |  External web       |
|Blog posts     | External web        |
| Video tutorials  | External web  |

## Use search

Type in the **Search** box to see suggestions for apps and templates appear in the drop down below the search box.

Choose any suggestion to go directly to that item.

> [!NOTE]
> By default, search only displays items from your environment, which are apps and templates. Users can select the **See web results** option to expand their search to external web content.
> :::image type="content" source="data-platform/media/search-see-web-results.png" alt-text="See web results ":::

> [!WARNING]
> Do not send personal data or confidential/proprietary information as part of your search when you choose this option.

To prevent users from using the **See web results** option to perform external web content searches for an environment, see [Manage search providers](#manage-search-providers).

## Manage search providers

The Microsoft.PowerApps.Administration.PowerShell module includes the cmdlets that members of either the Global admins, Azure Active Directory Global admins, or Dynamics 365 admin security groups can use to modify the search providers. More information: [Get started using the Power Apps admin module](/powershell/powerapps/get-started-powerapps-admin).

By default, all search providers are enabled. The following search providers can be disabled.

|Search provider namespace |Description  |
|---------|---------|
|`PowerPlatform.UniversalSearch.disableDocsSearch`  |  When this provider is disabled, users in the environment will see a message that Microsoft Learn and Documentation search categories have been turned off by the administrator in the search results page.   |
|`PowerPlatform.UniversalSearch.disableCommunitySearch`     | When this provider is disabled, users in the environment will see a message that Community and Blog search categories have been turned off by the administrator in the search results page.   |
| `PowerPlatform.UniversalSearch.disableBingVideoSearch`    | When this provider is disabled, users in the environment will see a message that Video search categories have been turned off by the administrator in the search results page.   |

To return the current settings including which search providers are enabled or disabled, run this cmdlet:
`Get-TenantSettings`

### Disable a search provider

Members of the Power Platform admin role can disable or enable a search provider by specifying the search provider namespace when running the Set-TenantSettings cmdlet.

For example, to disable the Microsoft Learn and Documentation search provider, run this cmdlet:

```powershell
$requestBody = @{PowerPlatform.UniversalSearch.disableDocsSearch = $true}
Set-TenantSettings -RequestBody $requestBody
```

To enable the Microsoft Learn and Documentation search provider, run this cmdlet:

```powershell
$requestBody = @{PowerPlatform.UniversalSearch.disableDocsSearch = $false}
Set-TenantSettings -RequestBody $requestBody
```

### See also

[Overview of creating apps in Power Apps](index.md)

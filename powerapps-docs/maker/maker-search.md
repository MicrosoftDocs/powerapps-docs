---
title: Find the apps, templates, and information you need using Power Apps unified search | Microsoft Docs
description: Use unified search to find what you need.
author: Mattp123
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 01/26/2021
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Find the apps, templates, and information you need

Power Apps unified search helps you quickly discover apps, templates, and content. From a single entry point you can find:

- Apps that have been built and published in your current environment.
- Templates in your current environment.
- Documentation and learning content.
- Community content.
- Blog posts.
- Video tutorials from the web.

Type in the **Search** box and to see suggestion for apps, templates, and documentation appear in the drop down below the search box. Choose any suggestion to go directly to that app, template, or web page.

:::image type="content" source="media/maker-search-demo.gif" alt-text="Unified search on make.powerapps.com":::

## Use search

Search first displays only items from your environment, which are apps and templates, and articles and learning on docs.microsoft.com. Selecting **Show more results** expands your search to additional web content that includes community subject matter, videos, and blog posts.


## Manage search providers

The Microsoft.PowerApps.Administration.PowerShell module includes the cmdlets that members of either the Global admins, Azure Active Directory Global admins, or Dynamics 365 admin security groups can use to modify the search providers. More information: [Get started using the Power Apps admin module](/powershell/powerapps/get-started-powerapps-admin).

To return the current settings including which search providers are enabled or disabled, run this cmdlet:
`Get-TenantSettings`

To disable all search providers, run this cmdlet:

```powershell
$requestBody = @{disableDocsSearch = $true}
Set-TenantSettings -RequestBody $requestBody
```

### See also

[Overview of creating apps in Power Apps](index.md)
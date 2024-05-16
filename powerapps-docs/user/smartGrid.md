---
title: Filter, sort, and search galleries with Copilot (preview)
description: Learn how to use Copilot to quickly sort, filter, and search canvas app galleries using natural language.
ms.date: 05/15/2024
ms.topic: article
ms.component: pa-user
ms.subservice: end-user
author: jordanchodak
ms.author: jordanchodak
ms.reviewer: sericks
search.audienceType: 
  - enduser
---


# Filter, sort, and search galleries with Copilot (preview)

[This article is prerelease documentation and is subject to change.]

You can use Copilot to quickly sort, filter, and search the items in canvas app galleries. Using Copilot saves time because you won’t have to worry about scrolling through the gallery to find the items you need.  

When trying to quickly find the gallery items you need, you might worry about spending time scrolling without success. With the assistance of Copilot, you can quickly use natural language to sort, filter, and search the gallery to find the items you need.

> [!IMPORTANT]
> - To use this feature, your environment must be in a region with GPU (graphics processing unit) capacity, or your tenant must have the **Move data across regions** checkbox selected.  Learn more: [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot)
> - To use this feature, the browser language must be US English.
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability may be subject to usage limits or capacity throttling.
> - Copilot isn't supported and won't work for environments that have customer-managed key (CMK) or have lockbox.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> -  This feature is currently only available for galleries that use SharePoint as their sole data source.  More data sources will be added to have this capability in the future. 
> - For more information about the preview, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).

## Use this feature

1. Select an item in the gallery. 
2. The option to **Sort, filter, and search with Copilot** should appear. Select that option. 
3. Write your desired sort, filter, or search query into the text box or select one of the suggested queries.  
     > [!Note] 
     > You must enter the text in English. This feature only supports the English language at this time. 
4. Select the **Send** icon. 
5. Copilot updates the gallery for you. Review the filters applied. The following options are available: 
    - If you want to remove any filters you have applied, select the **x** on the tag displaying the filter you want to remove. 
    - To clear all applied filters, select the trash icon button. 
    - If you are satisfied with the filters that are applied to the gallery, select **Keep it**.  You can always go back and remove or add more filters. 
  
## Turn off gallery filtering in web player

You can turn off gallery filtering for an app or an environment using a PowerShell cmdlet.  

> [!NOTE]
> - When using PowerShell cmdlets, you must use the latest Power Apps admin PowerShell module version. More information: [Get started using the Power Apps admin module](/powershell/powerapps/get-started-powerapps-admin).
> - If an admin has turned off this feature at the environment-level, this feature isn't available for any apps in that environment.
> - The PowerShell cmdlets may take up to two hours to take effect.
> - This feature is not yet available and is expected to begin rollout as on-by-default in early June.  However, if you turn it off before release, the feature should be disabled when it rolls out to you.

### Turn off gallery filtering for an app

You can use a PowerShell cmdlet to turn this setting off for an app.

To turn off for an app using PowerShell:

```powershell
Set-PowerAppSettings -AppName 'AppName' -CanvasGalleryFilteringCopilotEnabled $false
```

### Turn off gallery filtering for an environment

To turn off gallery filtering for a specific environment, use the following cmdlet.

```powershell
Set-AdminPowerAppEnvironmentCopilotSettings -EnvironmentName 'EnvironmentName' -CanvasAppGalleryFilterCopilotEnabled $false
```
   
## Known issue

- This feature can't be turned off on a per-tenant basis.  It can only be turned off by following the information in [Turn off gallery filtering in web player](#turn-off-gallery-filtering-in-web-player).

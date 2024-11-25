---
title: Filter, sort, and search galleries with Copilot (preview)
description: Learn how to use Copilot to quickly filter, sort, and search canvas app galleries by using natural language.
ms.date: 11/22/2024
ms.topic: article
ms.component: pa-user
ms.subservice: end-user
author: jordanchodak
ms.author: jordanchodak
ms.reviewer: smurkute
search.audienceType: 
  - enduser
contributors:
- lancedMicrosoft
ms.collection: 
    - bap-ai-copilot 
---

# Filter, sort, and search galleries with Copilot (preview)

[This article is prerelease documentation and is subject to change.]

You can use Copilot to quickly filter, sort, and search the items in canvas app galleries. Copilot uses a natural language expression that you enter to generate a query to the database. This query scopes the current view of records in a gallery or grid so that you can quickly find the records that you need.

This feature supports three main types of commands:

- **Filter** the list of records to a specific set by specifying complex criteria. For example, use _and_ and _or_ statements and relational operators such as _equal_ and _greater than_.
- **Sort** the list of records. For example, records can appear in ascending or descending order.
- **Search** for a specific set of records by using _starts with_.

Copilot doesn't support aggregate queries such as _top_, _min_, _max_, _sum_, and _average_, because the results can't be shown as a list of records.

This feature provides five main benefits:

- **Copilot allows for natural language commands.** Users can express commands (filter, sort, and search) in natural language. The prompt user interface (UI) helps users formulate sentences by showing different examples of natural language sentences that work.
- **Copilot allows for queries over the full query result.** Users can filter, sort, and search on fields even if the application doesn't provide UI controls for these tasks. For example, users can search for records even if the application doesn't have a search bar.
- **Copilot saves development time.** Authors save time when they develop apps, because they don't have to develop all the UI controls that are necessary for the app. Instead, they can rely on Copilot for this functionality.
- **Copilot is query safe.** Copilot generates only queries that can be run on the server. Authors don't have to worry whether their queries can be delegated. 
- **Copilot keeps private data private.** Copilot works only with the data that is normally returned to the application. It doesn't access fields that aren't returned to the app in a gallery/grid or form.

> [!IMPORTANT]
> - This feature isn't yet available, but rollout is expected to begin in late June. When the feature is released, it will be turned on by default. However, you can turn the feature off before the release. In this case, it should remain turned off when it's rolled out to you.
> - To use this feature, your environment must be in a region that has graphics processing unit (GPU) capacity, or the **Move data across regions** checkbox must be selected for your tenant. To learn more, go to [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot).
> - To use this feature, the browser language must be US English.
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability might be subject to usage limits or capacity throttling.
> - Copilot isn't supported and won't work for environments that have a customer-managed key (CMK) or lockbox.
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - This feature is designed for galleries that use SharePoint as their only data source. SharePoint supports only filters, sorts, and searches. We plan to extend this feature to more data sources in the future. However, the feature will still support only filters, sorts, and searches.
> - Filters, sorts, and searches are restricted to actions that can be run on the server. All actions can be delegated. For a complete list of actions that can be delegated for SharePoint, go to [Power Apps delegable functions and operations for SharePoint](/connectors/sharepointonline/#power-apps-delegable-functions-and-operations-for-sharepoint).
> - For more information about the preview, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).

## Use this feature

1. Select an item in the gallery.
1. The **Sort, filter, and search with Copilot** option should appear. Select it.
1. Enter the desired filter, sort, or search query in the text box, or select one of the suggested queries.

     > [!NOTE]
     > You must enter the query text in English. This feature currently supports only the English language.

1. Select the **Send** button.
1. Copilot updates the gallery for you. Review the filters that are applied. The following options are available:

    - To remove any filter that is applied, select the **x** on the tag for it.
    - To clear all applied filters, select the trash can symbol.
    - If you're satisfied with the filters that are applied, select **Keep it**. You can always go back later to remove or add more filters.

## Turn off gallery filtering in the web player

You can turn off gallery filtering for an app or environment by using a PowerShell cmdlet.

> [!NOTE]
> - When you use PowerShell cmdlets, you must use the latest Power Apps admin PowerShell module version. To learn more, go to [Get started using the Power Apps admin module](/powershell/powerapps/get-started-powerapps-admin).
> - If an admin turns this feature off at the environment level, it isn't available for any apps in that environment.
> - The PowerShell cmdlets might take up to two hours to take effect.
> - This feature isn't yet available, but rollout is expected to begin in late June. When the feature is released, it will be turned on by default. However, you can turn the feature off before the release. In this case, it should remain turned off when it's rolled out to you.

### Turn off gallery filtering for an app

To turn off gallery filtering for an app, run the following PowerShell cmdlet.

```powershell
Set-PowerAppSettings -AppName 'AppName' -CanvasGalleryFilteringCopilotEnabled $false
```

### Turn off gallery filtering for an environment

To turn off gallery filtering for a specific environment, run the following PowerShell cmdlet.

```powershell
Set-AdminPowerAppEnvironmentCopilotSettings -EnvironmentName 'EnvironmentName' -CanvasAppGalleryFilterCopilotEnabled $false
```

## Known issue

- This feature can't be turned off on a per-tenant basis. It can be turned off only as described in the [Turn off gallery filtering in the web player](#turn-off-gallery-filtering-in-the-web-player) section.


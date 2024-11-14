---
title: "Set a preferred solution | MicrosoftDocs"
description: "Set your preferred solution in Power Apps."
ms.date: 11/13/2024
ms.topic: conceptual
author: Mattp123
ms.subservice: dataverse-maker
ms.author: matp
ms.reviewer:
search.audienceType:
  - maker
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-desc
  - ai-seo-date:10/17/2023
---
# Set the preferred solution

By default, unless already in the context of an unmanaged solution, all solution components are stored in the solution named Common Data Services Default Solution. Because there's no separation of components between makers and the Common Data Services Default Solution can't be exported for import to other environments, this typically isn't the best model.

Using preferred solutions is a way to set which solution will support each maker's edits that happen anywhere in Power Apps. It enables makers to view and update which solution they're using. After you set your preferred solution, you can create components in the solution you specify and those components will automatically be in that solution so that you control the components within the solution. Then, you can export your preferred solution and import the solution to other Microsoft Dataverse environments.

> [!NOTE]
>
> - When your preferred solution isn't set, by default, the **Common Data Services Default Solution** is your preferred solution. If **Common Data Services Default Solution** isn't available, the solution named **Default Solution** is used as your preferred solution. You can change this to your desired solution by following the steps in this article. For more information about the **Common Data Services Default Solution** and **Default Solution**, go to [Default solutions](solutions-overview.md#default-solutions).
> - The environment setting to enable or disable this feature is no longer available now that preferred solution is generally available.

## Prerequisites

We recommend that admins enable the **Cloud flows** and **Canvas apps** environment setting in Power Platform. Enabling this feature ensures cloud flows are also stored in Dataverse and that they're added to the maker's preferred solution. More information: [Create new canvas apps and cloud flows in a Dataverse solution](/power-platform/admin/settings-features#create-new-canvas-apps-and-cloud-flows-in-a-dataverse-solution)

## Set your preferred solution

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Solutions** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the unmanaged solution that you want to make your preferred solution. Don't have one? More information: [Create a solution](create-solution.md)
1. Select **Set preferred solution** on the command bar.

Once your preferred solution is set, notice the **preferred solution** indicator, which can be viewed from the **Solutions** area or when you hover over the **Environment** switcher.

:::image type="content" source="media/preferred-solution-status.png" alt-text="Preferred solution status displayed in Solutions area":::

## Deleting a preferred solution

You can delete your preferred solution or a preferred solution that other makers have also set as their preferred solution.

> [!WARNING]
> When you delete a preferred solution you receive a warning that includes the fallback default solution and the number of other makers who are using the same solution. Delete an active solution only when you're sure it won't impact your work or the work of other makers.
> 
> :::image type="content" source="media/delete-preferred-solution.png" alt-text="Delete a preferred solution warning":::

## Limitations

- You can't set or view the preferred solution in the classic solution explorer.
- Components that are created in the classic solution explorer won't go into the preferred solution.
- Preferred solution currently doesn't work with Dataverse for Teams,cards, dataflows, AI Builder, chatbots, connections, gateways, custom connectors, Power Automate flows (limited), and canvas apps created from image or a Figma design.
- When a component is already part of an existing unmanaged solution, it will still be added to the preferred solution.

## See also

[Solutions overview](solutions-overview.md)  
[Set the preferred solution with Power Apps (video)](https://youtu.be/WohjakB8OdE?feature=shared)

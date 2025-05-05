---
title: "Set a preferred solution | MicrosoftDocs"
description: "Set your preferred solution in Power Apps."
ms.date: 04/09/2025
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

By default, unless you're already in the context of an unmanaged solution when you create an object, all solution objects are stored in the solution named Common Data Services Default Solution. For most situations, you don't want to create your solution objects in either of the two Dataverse system solutions, which are the Common Data Services Solution and the Default Solution. This article explains why using the system solutions is discouraged and provides step-by-step instructions to set and manage your preferred solution.

## Why not create your objects in the system solutions?

There are a few reasons you *shouldn't* create your solution objects in either the Common Data Services Solution and the Default Solution:

- There's no control over the separation of solution objects between makers. All objects can be viewed from the Default Solution and the Common Data Services Solution is the default solution so other makers can and likely are using it.
- The Default Solution can't be exported for import to other environments.
- You can't change the solution publisher for the Default Solution. Additionally, since the solutions already exist, you can't change the solution publisher prefix for either system solutions. More information: [Solution publisher](create-solution.md#solution-publisher)

Using preferred solutions is a way to determine which solutions contain each maker's edits that occur in Power Apps. Setting the preferred solution enables makers to view and update which solution they're using. After you set your preferred solution, you can create objects in the solution you specify and those objects will automatically be in that solution so that you control the objects within the solution. Then, you can export your preferred solution and import the solution to other Microsoft Dataverse environments.

> [!NOTE]
> When your preferred solution isn't set, by default, the **Common Data Services Default Solution** is your preferred solution. If **Common Data Services Default Solution** isn't available, the solution named **Default Solution** is used as your preferred solution. You can change this to your desired solution by following the steps in this article. For more information about the **Common Data Services Default Solution** and **Default Solution**, go to [Default solutions](solutions-overview.md#default-solutions).

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
> When you delete a preferred solution, you receive a warning that includes the fallback default solution and the number of other makers who are using the same solution. Delete an active solution only when you're sure it won't impact your work or the work of other makers.
> 
> :::image type="content" source="media/delete-preferred-solution.png" alt-text="Delete a preferred solution warning":::

## Limitations

- You can't set or view the preferred solution in the classic solution explorer.
- Components that are created in the classic solution explorer won't go into the preferred solution.
- Preferred solution currently doesn't work with Dataverse for Teams, cards, dataflows, AI Builder, chatbots, connections, gateways, custom connectors, Power Automate flows (limited), and canvas apps created from image or a Figma design.
- When a component is already part of an existing unmanaged solution, it will still be added to the preferred solution.

## See also

[Solutions overview](solutions-overview.md)  
[Set the preferred solution with Power Apps (video)](https://youtu.be/WohjakB8OdE?feature=shared)

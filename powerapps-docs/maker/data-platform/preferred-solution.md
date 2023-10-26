---
title: "Set a preferred solution | MicrosoftDocs"
description: "Set your preferred solution in Power Apps."
ms.date: 10/26/2023
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
# Set the preferred solution (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

By default, unless already in the context of an unmanaged solution, all solution components are stored in the solution named Common Data Services Default Solution. Because there's no separation of components between makers and the Common Data Services Default Solution can't be exported for import to other environments, this typically isn't the best model.

Using preferred solutions is a way to set which solution will support each maker's edits that happen anywhere in Power Apps. It enables makers to view and update which solution they are using. After you set your preferred solution, you can create components in the solution you specify and those components will automatically be in that solution so that you control the components within the solution. Then, you can export your preferred solution and import the solution to other Microsoft Dataverse environments.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Prerequisites

Power Platform admins enable the ability for makers to set their preferred solution by setting **Preferred solution** to **On** for the environment settings in the Power Platform admin center. More information: [Preferred solution](/power-platform/admin/settings-features#preferred-solution)

<!-- Alternatively, Power Platform admins can use Dataverse APIs, so that a maker’s solution components are organized. -->

> [!IMPORTANT]
> We recommend that admins also enable the **Cloud flows** environment setting in Power Platform. Enabling this feature ensures cloud flows are also stored in Dataverse and that they're added to the maker's preferred solution. More information: [Create new canvas apps and cloud flows in a Dataverse solution](/power-platform/admin/settings-features#create-new-canvas-apps-and-cloud-flows-in-a-dataverse-solution)

## Set your preferred solution

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Solutions** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the unmanaged solution that you want to make your preferred solution.
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
- Preferred solution doesn't work with cards, dataflows, AI Builder, chatbots, flows, connections, gateways, custom connectors, Power Pages websites, and canvas apps created from image or a figma design.

### See also

[Solutions overview](solutions-overview.md)

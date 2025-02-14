---
title: "Example functions in Microsoft Dataverse"
description: "View function examples to help you understand how functions work in Dataverse"
ms.custom: ""
ms.date: 02/03/2025
ms.reviewer: "Mattp123"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "paulliew"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "paulliew"
search.audienceType: 
  - maker
---
# Example functions (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The article helps you get started with functions in Microsoft Dataverse by integrating them into your apps. You'll understand that the authoring experience includes authoring Dataverse custom APIs backed by Power Fx expressions, which can trigger actions internal or external to Dataverse.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Return a non-negative value

This example uses the `Abs()` function to return the non-negative value of its argument. If a number is negative, `Abs` returns the positive equivalent.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Functions** from the left navigation. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)] Open the unmanaged solution where you want to add a function.
1. Select **New function**.
1. On the **New function** pane, enter a **Display name**, such as *Return non-negative value*, and **Description** for your function.
1. Create a **New output parameter** to validate expected behavior, such as a string. For example, enter the **Name** of your **New Output parameter** *Out*.
1. Optionally, use input parameters to make testing easier, that makes sense with the formula. <!-- Need a specific example here. E.g. such as... -->
1. In the **Formula** box, wrap the **Out** parameter in curly brackets:

   `{Out: "" }`
1. Select **Save**.

To test the function, select the function and then select **Test** on the command bar.
Then, in the **Input** box enter a formula to test such as the one below, and then select **Play**.

   `{Out: "Abs(-5) = 5: " & Text( Abs(-5) = 5) }`

## Input validation and custom errors

### Send in-app notifications based on an instant action

This and more samples coming soon.

<!-- 
In-app notifications enable makers to configure contextual, actionable notifications for users in model-driven apps.

1. On the **New function** pane, enter this **Display name** and **Description** for your function.

   - **Display name**:*NotifyTechnican1* 
   - **Description**: *This function notifies the app user.*

Create input parameters with these data types: -->
<!-- Waiting on dev to provide code in rest of samples-->

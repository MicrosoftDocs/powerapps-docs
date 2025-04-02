---
title: Control State API  | Microsoft Docs
description: The Power Apps component framework allows you to persist state of component across multiple renderings of the component within the same session.
author: anuitz
ms.author: anuitz
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: sample
ms.subservice: pcf
search.audienceType: 
  - developer
contributors:
 - JimDaly
---

# Implementing control state API component

The Power Apps component framework allows you to persist state of component across multiple renderings of the component within the same session. It provides you with the ability to build components that can maintain user state throughout the user's session as the user navigates to and from the component.

[!INCLUDE[cc-terminology](../../data-platform/includes/cc-terminology.md)]

For example, if your code component is a long list that the user can scroll through, you could leverage the **_SetControlState_** functionality to remember the point in the list the user is looking at when they navigated away from the form. You could then add logic on component initialization to check the stored state and render the component's list at the point where the user was previously reading. 

> [!div class="mx-imgBorder"] 
> ![Control state API.](../media/control-state-api.png "Control state API")

## Available for

Model-driven and canvas apps

## Code

You can download the complete sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ControlStateAPI).


### Related articles

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework manifest schema reference](../manifest-schema-reference/index.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

---
title: "TabStateChange event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the TabStateChange event.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# TabStateChange event (Client API reference)



This event occurs when the **DisplayState** of the tab changes due to user interaction or when the [setDisplayState](../formContext-ui-tabs/setDisplayState.md) method is applied in code. 

Use this event when you want to change the **src** property of an IFRAME within the tab. If you set the IFrame.**src** property in the OnLoad event for an IFRAME within a collapsed tab, the value will be overwritten when the tab is expanded.

Use the [addTabStateChange](../formContext-ui-tabs/addTabStateChange.md) method to add event handlers for this event and the [removeTabStateChange](../formContext-ui-tabs/removeTabStateChange.md) method to remove them.





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
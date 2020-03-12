---
title: "TabStateChange Event (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# TabStateChange Event (Client API reference)



This event occurs when the **DisplayState** of the tab changes due to user interaction or when the [setDisplayState](../formContext-ui-tabs/setDisplayState.md) method is applied in code. 

Use this event when you want to change the **src** property of an IFRAME within the tab. If you set the IFrame.**src** property in the OnLoad event for an IFRAME within a collapsed tab, the value will be overwritten when the tab is expanded.

Use the [addTabStateChange](../formContext-ui-tabs/addTabStateChange.md) method to add event handlers for this event and the [removeTabStateChange](../formContext-ui-tabs/removeTabStateChange.md) method to remove them.




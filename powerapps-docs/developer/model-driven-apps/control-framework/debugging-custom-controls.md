---
title: "Debugging Custom Controls | MicrosoftDocs"
description: "How to debug a custom control using Fiddler and Native debugging"
ms.date: 01/12/2018
ms.service: "crm-online"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
author: "Nkrb"
ms.author: "nabuthuk"
manager: "jdaly"
---
# Debugging Custom Controls

Debugging a custom control is as simple as debugging webresources in the Mode-driven Apps.The following are the two ways to debug a custom control. 

## Browser Debugging

Each browser provides you with a debugging tool to help you debug your code natively in the browser. Typically, you activate debugging in your browser by pressing the **F12** key to display the native developer tool used for debugging.

For example, on Microsoft Edge,

- Go to the **Form/Grid** where the control should be rendered.
- Press **F12** to open inspector. 
- On top bar, go to **Debugger**, and then start searching for the control name described in the Manifest file in the search bar. For example, type your control name like ‘Hello World Control’

[!NOTE]
> It is always a good practice to set breakpoints on the control's lifecycle methods like `init` and `updateView`

## Fiddler AutoResponder

Use the Fiddler AutoResponder to quickly debug your custom controls. Install [Fiddler](https://www.telerik.com/download/fiddler) and follow the steps to configure [AutoResponder](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/streamline-javascript-development-fiddler-autoresponder)

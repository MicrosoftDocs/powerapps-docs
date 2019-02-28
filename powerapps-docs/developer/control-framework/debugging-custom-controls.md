---
title: "Debugging Custom Controls | MicrosoftDocs"
description: "How to debug a custom control using Fiddler and Native debugging"
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
---
# Debugging Custom Controls

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Once you are done implementing your custom control logic, you can use the following command to start the debugging process
`npm start`

Debugging a custom control is as simple as debugging webresources in the Model-driven apps.You can debug custom controls in two ways.

## Browser Debugging

Each browser provides you with a debugging tool to help you debug your code natively in the browser. Typically, you activate debugging in your browser by pressing the **F12** key to display the native developer tool used for debugging.

For example, on **Microsoft Edge**,

- Go to the **Form/Grid** where the control should be rendered.
- Press **F12** to open inspector.
- On top bar, go to **Debugger**, and then start searching for the control name described in the Manifest file in the search bar. For example, type your control name like ‘Hello World Control’

> [!NOTE]
> It is always a good practice to set breakpoints on the control's life cycle methods like `init` and `updateView`

## Fiddler AutoResponder

Use the Fiddler AutoResponder to quickly debug your custom controls. Install [Fiddler](https://www.telerik.com/download/fiddler) and follow the steps to configure [AutoResponder](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/streamline-javascript-development-fiddler-autoresponder)

### Related Topics

[PowerApps Control Framework API Reference](index.md)<br />
[PowerApps Control Framework Overview](overview.md)

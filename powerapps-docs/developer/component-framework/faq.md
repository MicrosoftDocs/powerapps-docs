---
title: "FAQ | MicrosoftDocs"
description: "Frequently asked questions about component framework"
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 9f940264-d7d5-4930-8052-1bd582445d37
ms.author: "nabuthuk"
author: Nkrb
---

# FAQ

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

## Component changes are not reflected after the updated solution import?

Update the control version (minor) in control manifest. eg. 1.0.0 to 1.0.1. Every update in the control needs a control version bump to be reflected on the CDS server.

## What are the things to be considered from a performance perspective?

1. Be mindful of the data you are trying to load into your component. If your user will truly need access to hundreds or thousands of data items, implement methods of filtering and paging to limit how much data is being loaded at any one time.
2. Batch your network calls. Rather than making a call for each data item you want to show, either get all that information in a single call, or design your component such that the user has to do something (such as clicking on a button) to initiate loading of one item's detail data.
3. If a component is likely to have more than one instance of itself on a single screen or form, try to have your code be aware of that and not repeat work that can be shared across all instances.

## Where can I find some good examples of PCF controls?
Lots of great examples from the community are available on the [Power Apps Community Forums](https://powerusers.microsoft.com/t5/Power-Apps-Component-Framework/Community-content-sample-components-blogs-etc-Link-to-this-page/td-p/280710).

## How to use rich data types in PCF controls such as Collections?
Currently this feature is unsupported. However, there is a [JSON function](https://docs.microsoft.com/powerapps/maker/canvas-apps/functions/function-json) in Canvas-based Power Apps that allows app makers to stringify their data.

1. Pass your collection into that function
2. Pass the string representation of your collection data that is returned from the JSON function into one of your component's string properties
3. Use [JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) in your component code to convert it back into a javascript Object.

## How can I define multiple components in single manifest file?

It is not possible to define multiple components in a single manifest file. 

## How can I define behavior properties?

This is not supported at this time. Currently, you can only call dialog boxes using the [Navigation](reference/navigation.md) method in Model-based Power Apps.

## How can I calling other components from within another component?

This is not supported natively by the framework.

## Can I bundle font resources?

Currently font resources (files with a .ttf file extension) are not supported by the framework.

## Related topics

[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)

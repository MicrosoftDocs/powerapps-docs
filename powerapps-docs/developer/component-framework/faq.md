---
title: "FAQs | MicrosoftDocs"
description: "Frequently asked questions about component framework"
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 9f940264-d7d5-4930-8052-1bd582445d37
ms.author: "grhurl"
author: ghurlman
ms.reviewer: nkrb
---

# FAQs

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

### Component changes are not reflected after the updated solution import?

Update the component version (minor or patch) in the component manifest file (for example, 1.0.0 to 1.0.1). 
Every update in the component needs a component version bump to be reflected on the Common Data Service server.

> [!NOTE]
> - A new solution must be created everytime if you wish to have a major version bump. Incrementing the major version number (eg 1.0 to 2.0) is not supported as an upgrade.
> - Only three version sections are supported (i.e. MAJOR.MINOR.PATCH). These version number sections should be between 0 and 65536.

### What are the things to be considered from a performance perspective?

1. If you wish to access large chunk of data items, implement [filtering](reference/filtering.md) and [paging](reference/paging.md) methods to limit how much data should be loaded.
2. Batch your network calls, and make any network calls asynchronous. Design the component in such a way that all the required information is provided with a single call. 
3. Design the component such that the user has to perform an action (such as clicking on a button) to initiate the loading of specific item's data rather than making the call for each data item.
4. Ensure that you clean up the resources using the [destroy](reference/control/destroy.md) function. Open network calls, connections, and event handlers need to be cleaned up to increase the performance.

### Where can I find some good examples of code components?

Lots of great examples from the community are available on the [Power Apps Community Forums](https://powerusers.microsoft.com/t5/Power-Apps-Component-Framework/Community-content-sample-components-blogs-etc-Link-to-this-page/td-p/280710).

### How to use rich data types in code components such as Collections?

Currently, this feature is not supported. However, there is a [JSON function](https://docs.microsoft.com/powerapps/maker/canvas-apps/functions/function-json) in canvas-apps that allows app makers to stringify their data.

1. Pass the collection into the JSON function.
2. Pass the string representation of the collection data that is returned from the JSON function into one of the component's string properties.
3. Use [JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) in the component code to convert it back into a JavaScript Object.

### How can I define multiple components in a single manifest file?

Defining multiple components in a single manifest file is not supported. 

### How can I define behavior properties?

This is not supported at this time. Currently, you can only call dialog boxes using the [Navigation](reference/navigation.md) method in model-driven apps.

### How can I call other components from within another component?

This is not supported natively by the framework. You can use one of many third-party libraries to enable this functionality in your components.

### Can I bundle font resources?

Currently, font resources (files with a .ttf file extension) are not supported by the framework.

### Can I use img resource for canvas apps?

Currently, [img](manifest-schema-reference/img.md) resources are not supported in canvas apps.

## Related topics

[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)

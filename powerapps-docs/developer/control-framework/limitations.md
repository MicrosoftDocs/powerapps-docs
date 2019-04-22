---
title: "Limitations of PowerApps component framework | MicrosoftDocs"
description: "Limitations using PowerApps component framework"
author: nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
---

# Limitations of PowerApps component framework

With the release of the PowerApps component framework, you can now create your own custom components to improve the user experience in Common Data Service. Even though you can create your own components, there are some limitations that restrict developers implementing some features in the custom components. Below are some of the limitations:

### Multiple components in single manifest file

It is not possible to define multiple components in a single manifest file. 

### Calling Processes/Actions

This is not supported yet. For now you can only call dialog boxes using the [Navigation](reference/navigation.md) method.

### Support for external libraries

The PowerApps component framework supports all the external libraries for implementing custom components. 

> [!NOTE]
> When you use JQuery for implementing the custom components, at run time, it loads the platform version of the JQuery not the version you used to implement. 

### Calling components within another component

This is not supported yet.

### Font Resource

Currently font resource (.tff) is not supported in PowerApps component framework.

### Related topics

[PowerApps component framework API Reference](reference/index.md)<br/>
[PowerApps component framework Overview](overview.md)
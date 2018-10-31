---
title: "Testing tools for server-side development (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about testing frameworks for server-side development." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Testing tools for server-side development

Many developers strongly advocate including unit testing as part of their development process. Others are not convinced. Common Data Service for Apps doesn't provide testing framework tools, but you should be aware that there are community tools available that you can use. A popular framework for server-side development is [Fake Xrm Easy](https://dynamicsvalue.com/home). This framework can be combined with your choice of .NET framework testing frameworks. [FakeItEasy](https://fakeiteasy.github.io/) is a common choice.

> [!NOTE]
> Microsoft does not provide support for tools created by the community. If you have any issues with a community tool, please contact the publisher.

## Benefits of unit testing

Unit testing is strongly recommended but not required. When you are just getting started or if the amount of code in your solution is relatively small, you may feel that you spend more time writing tests than the functionality included in your solution.

The benefits of unit testing begin to accrue when your solution becomes larger and more complex. Particularly with server-side development, there can be significant benefits in debugging locally using mocked or faked data with a testing framework instead of having to go through all the steps described in [Debug Plug-ins](debug-plug-in.md) to generate a profile to debug.

When a solution is developed with unit testing, developers report greater productivity and a better quality product.

### See also

[Testing tools for client-side development](../model-driven-apps/testing-tools-client.md)<br />
[Video: Introduction to DevOps with Dynamics 365](https://youtu.be/AorM792M8nY)
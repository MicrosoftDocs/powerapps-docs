---
title: "Testing tools for client-side development (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about testing frameworks for client-side development."
ms.date: 04/01/2022
ms.topic: article
author: ChrisBal-MSFT
ms.subservice: mda-developer
ms.author: chrisbal
ms.reviewer: jdaly
search.audienceType: 
  - developer
---
# Testing tools for client-side development

Microsoft provides an automated UI testing framework specifically for model-driven apps called [Easy Repro](https://github.com/Microsoft/EasyRepro). This framework is built using the [SeleniumHQ](https://www.seleniumhq.org/) browser automation open-source project.

Easy Repro provides a set of classes and methods to work with various pages in model-driven apps so you don't need to parse the HTML elements of the application when writing test cases. This makes your tests resilient to changes made in the HTML elements that compose the application pages.

## Benefits of unit testing

Unit testing is strongly recommended but not required. When you are just getting started or if the amount of code in your solution is relatively small, you may feel that you spend more time writing tests than the functionality included in your solution.

The benefits of unit testing begin to accrue when your solution becomes larger and more complex. For client-side development, an automated UI framework for testing can help you detect issues initiated by user actions.  

When a solution is developed with unit testing, developers report greater productivity and a better quality product.

### See also

[Testing tools for server-side development](../data-platform/testing-tools-server.md)<br />
[Video:  Creating and running UI test](https://youtu.be/ryWgK34Akt0)<br />
[Blog post: Easy Repro: what is it?](https://www.itaintboring.com/dynamics-crm/easy-repro-what-is-it/)<br />
[Video: Introduction to DevOps](https://youtu.be/AorM792M8nY)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

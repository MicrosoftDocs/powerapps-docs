---
title: Microsoft Dataverse Developer Guide
description: Learn how to extend Microsoft Dataverse with code, including plug-ins, workflows, and APIs. Get started building custom apps on the Power Apps platform.
author: MsSQLGirl
ms.author: jukoesma
ms.topic: overview
ms.date: 03/09/2026
ms.subservice: dataverse-developer
ms.reviewer: jdaly
search.audienceType: 
  - developer
---

# Microsoft Dataverse Developer Guide

Microsoft Dataverse is the underlying data platform for Power Apps, providing core functionality such as server-side logic (plug-ins and workflows), business process flows, a sophisticated security model, and an extensible platform for developers. This guide helps developers understand how to extend Dataverse with code to build custom line-of-business apps for users, businesses, independent software vendors (ISVs), and systems integrators (SIs).

There are many ways developers can contribute to creating apps that use Dataverse. While you can build an application with code using Dataverse as your data source, most projects use either [model-driven apps](../../maker/model-driven-apps/model-driven-app-overview.md) or [canvas apps](../../maker/canvas-apps/getting-started.md) to generate the experience that people use. 

## Working with model-driven apps

Model-driven apps are built on Dataverse, and can only connect to a Dataverse environment. Dataverse stores all the data that defines a model-driven app.

Model-driven apps use [Solutions](introduction-solutions.md) to share customizations and extensions.

Model-driven apps also have many points where developers can write code to extend them. For information about what developers can do with model-driven apps, see [Model-driven apps Developer Guide](../model-driven-apps/overview.md).

Some examples of model-driven apps available from Microsoft are [Dynamics 365 Customer Service](/dynamics365/customer-service/help-hub), [Dynamics 365 Field Service](/dynamics365/field-service/overview), and [Dynamics 365 Marketing](/dynamics365/marketing/help-hub).

## Understand when to write code

Because Dataverse includes many capabilities for people to configure custom business logic without writing code, the most common scenarios for developers involve filling gaps where existing features don't provide the functionality you need. Fortunately, Dataverse provides many points for developers to extend the common functionality by using code.

As a developer, it's important to understand what you can do without writing code. Familiarize yourself with these capabilities. For more information, see [What is Dataverse?](../../maker/data-platform/data-platform-intro.md) 

## Content for on-premises deployments

Dataverse isn't available for on-premises deployments. Content in this guide doesn't include information about options that are only available for on-premises or internet facing deployments (IFD). For information related to these options, see the [Developer Guide for Dynamics 365 Customer Engagement (on-premises)](/dynamics365/customerengagement/on-premises/developer/overview).

> [!div class="nextstepaction"]
> [Get started](get-started-developers.md)

### See also

[Power Apps for developers](../../index.yml?panel=developer)<br/>
[Model-driven apps Developer Guide](../model-driven-apps/overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

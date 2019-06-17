---
title: "PowerApps component framework overview | Microsoft Docs"
description: "Use the PowerApps component framework to create custom components to provide enhanced experience for people to view and work with data in forms, views, and dashboards."
keywords: "Component Framework, custom components, PowerApps controls"
author: nkrb 
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.custom:
  - "dyn365-a11y"
  - "dyn365-developer"
ms.topic: article
ms.assetid: 7923e36d-3640-49f7-9f2f-c97358a632db
ms.author: nabuthuk
---

# PowerApps component framework overview

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use PowerApps component framework to create custom components in model-driven apps to provide an enhanced user experience for the users to view and work with data in forms, views and dashboards. For example:

- Replace a field that displays a numeric text value with a `dial` or `slider` component.
- Transform a list into an entirely different visual experience bound to the data set like a `Calendar` or `Map`.

> [!IMPORTANT]
> - PowerApps component framework is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 


PowerApps component framework enables professional developers to create custom components that can be used across the full breadth of PowerApps capabilities. Custom components have access to a rich set of framework APIs which expose capabilities like component lifecycle management, contextual data and metadata access, seamless server access via Web API, utility and data formatting methods, device features like camera, location and microphone along with easy to invoke UX elements like dialogs, lookups, full page rendering etc.  

> [!NOTE]
> Custom components are supported only on Unified Interface for [model-driven apps](/powerapps/maker/model-driven-apps/model-driven-app-overview) version 9.1.0.3842 or later.

Component developers can utilize modern web practices and also harness the power of external libraries to create advanced user interactions. The framework automatically handles component lifecycle, retains application business logic and optimizes for performance (no more async iframes). Components created using this framework are fully configurable and can be reused on multiple surfaces in model-driven apps like forms, dashboards, grids, etc. Component definition, dependencies, and configurations can all be packaged into a [solution](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/customize/solutions-overview) and moved across environments and can be shipped via [app source](https://appsource.microsoft.com/en-us/marketplace/apps?page=1&product=dynamics-365).  

## Related topics

[What are custom components?](custom-controls-overview.md)<br/>
[Create and deploy custom components](create-custom-controls-using-pcf.md)<br/>
[PowerApps for developers](https://docs.microsoft.com/powerapps/#pivot=home&panel=developer)


---
title: "PowerApps component framework | Microsoft Docs"
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

# PowerApps component framework

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use the PowerApps component framework to create custom components in Common Data Service to provide enhanced user experience for the users to view and work with data in forms, views and dashboards. For example:

- Replace a field that displays a numeric text value with a `dial` or `slider` component.
- Transform a list into an entirely different visual experience bound to the data set like a `Calendar` or `Map`.

> [!IMPORTANT]
> - The PowerApps component framework is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 
> - [!INCLUDE[cc_preview_features_no_MS_support](../../includes/cc-preview-features-no-ms-support.md)]

> [!NOTE]
> PowerApps component framework requires a server version 9.1.0.3842 or higher

PowerApps component framework enables professional developers to create fully custom components for use across the full breadth of PowerApps capabilities. Custom components have access to a rich set of framework APIs which expose capabilities like component lifecycle management, contextual data and metadata access, seamless server access via Web API,utility and data formatting methods, device features like camera, location and microphone along with easy to invoke UX elements like dialogs, lookups, full page rendering etc.  Component developers can utilize HTML 5\JS based modern web practices and also harness the power of external libraries to create advanced user interactions. The framework automatically handles component lifecycle, retains application business logic and optimizes for performance (no more async iframes). Components created using this framework are fully configurable and can be reused on multiple surfaces in the app like forms, dashboards, grids, etc. Component definition, dependencies, and configurations can all be packaged into a solution and moved across environments and can be shipped via app source.  

Majority of the controls found in Common Data Service that uses the **Unified Interface** are implemented using the PowerApps component framework. Custom components are metadata driven, configurable, reusable, solution aware and responsive. As a developer, you will implement an interface and the application will take care of the rest.

> [!NOTE]
> Custom components are supported only on Unified Interface for [model-driven apps](/powerapps/maker/model-driven-apps/model-driven-app-overview).

## Related topics

[What are custom components?](custom-controls-overview.md)<br/>
[Create custom components](create-custom-controls-using-pcf.md)

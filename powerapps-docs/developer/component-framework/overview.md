---
title: "Power Apps component framework overview in Microsoft Dataverse | Microsoft Docs"
description: "Use the Power Apps component framework to create code components to provide an enhanced experiences for people to view and work with data in forms, views, and dashboards."
keywords: "Component Framework, code components, Power Apps controls"
ms.author: anuitz
author: anuitz
ms.date: 01/09/2026
ms.reviewer: jdaly
ms.topic: overview
ms.subservice: pcf
contributors:
 - JimDaly
---

# Power Apps component framework overview

Power Apps component framework enables professional developers and app makers to create code components for model-driven and canvas apps. Use these code components to enhance the user experience for users working with data on forms, views, dashboards, and canvas app screens. For example, you can:

- Replace a column on a form that displays a numeric text value with a `dial` or `slider` code component.
- Transform a list into an entirely different visual experience bound to the dataset, like a `Calendar` or `Map`.

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=69a0fdf4-5b3c-461e-b921-94aad4b7f717]


> [!IMPORTANT]
>
> - Power Apps component framework isn't supported for on-premises environments.

## How is it different from web resources?

Unlike HTML web resources, code components render as part of the same context and load at the same time as any other components. This approach provides a seamless experience for the user. 

Create code components that you can use across the full breadth of Power Apps capabilities. Reuse these components many times across different tables and forms.

Developers can bundle all the HTML, CSS, and TypeScript files into a single [solution](../../maker/data-platform/solutions-overview.md) package file to move across environments. They can also make it available via [Marketplace](https://marketplace.microsoft.com/marketplace/apps?page=1&product=dynamics-365). 


## Advantages 

- Access to a rich set of framework APIs that expose capabilities like component lifecycle management, contextual data, and metadata
- Seamless server access via Web API; utility and data formatting methods; device features like camera, location, and microphone; and easy-to-invoke user experience elements like dialogs, lookups, and full-page rendering
- Support for modern web practices
- Optimized for performance
- Reusability
- Ability to bundle all files into a single solution file
- Ability to handle being destroyed and reloaded for performance reasons while preserving state

## Licensing

Power Apps component framework licensing requirements align with existing connectors and components. They're based on the type of data and connections you use in your app. For more information, see [Power Apps pricing](https://powerapps.microsoft.com/pricing/). To align with the licensing requirements, classify code components into two types:

- Code components that connect to external services or data directly through the user's browser client and not through connectors are premium. When these components are used in an app, the app becomes premium, and end-users need **Power Apps** licenses.
- Code components that don't connect to external services or data. When these components are used in an app that uses standard features, the app remains standard, and end-users need at least an **Office 365** license. For more information, see [Power Apps pricing](https://powerapps.microsoft.com/pricing/).
- Code components can be declared as premium components by adding a `<external-service-usage>` node to the component's manifest file with all the external service domains this component is connecting to.
   ```xml
    <external-service-usage enabled="true">
     <domain>www.microsoft.com</domain>
    </external-service-usage>
    ```

> [!NOTE]
> If you're currently using code components in model-driven apps connected to Microsoft Dataverse, end users need **Power Apps** licenses.

## Related topics

[What are code components?](custom-controls-overview.md)<br/>
[Code components for canvas apps](component-framework-for-canvas-apps.md)<br/>
[Create and build a code component](create-custom-controls-using-pcf.md)<br/>
[Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)<br/>
[Use code components in Power Pages](../../maker/portals/component-framework.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]

---
title: Use Liquid template tag for code components
description: Learn how to use the Liquid template tag for code components, and walk through a tutorial to configure Power Apps portals to add the component to a webpage.
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/10/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
  - nickdoelman
  - GitanjaliSingh33msft
  - nickdoelman
---

# Liquid template tag for code components (preview)

[This article is pre-release documentation and is subject to change.]

Power Apps component framework empowers professional developers and app makers to create code components for model-driven and canvas apps. These code components can provide an enhanced experience for users working with data on forms, views, and dashboards. More information: [Use code components in portals (preview)](component-framework.md)

> [!IMPORTANT]
> The Liquid template tag for code components requires portals version [9.3.10.x or later](/power-platform/released-versions/portals/portalupdate9310x).

With this release, we've introduced the ability to add code components using a [Liquid template tag](liquid/template-tags.md#codecomponent) on webpages, and enabled components using Web API that are enabled for field-level components on forms in portals.

Code components can be added using the `codecomponent` Liquid template tag. The key for denoting the code component that needs to be loaded is passed in using the `name` attribute. The key can be the GUID (which is the code component ID) or the name of the code component imported into Microsoft Dataverse.

The values of the properties that the code component expects need to be passed in as a key/value pair separated by "**:**" (colon sign), where the key is the property name and the value is the JSON string value.

```
{% codecomponent name: <ID or name> <property1:value> <property2:value> %}
```

For example, to add a code component expecting an input parameter named *controlValue*, use the following Liquid template tag: 

```
{% codecomponent name:abc_SampleNamespace.MapControl controlValue:'Space Needle' controlApiKey:<API Key Value>%}
```

> [!TIP]
> This example uses parameters called *controlvalue* and *controlApiKey*, however the component you use may require different parameter names.

You can use the [sample map control](../../developer/component-framework/sample-controls/map-control.md) and [package the code component as a solution](../../developer/component-framework/implementing-controls-using-typescript.md#packaging-your-code-components) for use with portals.

> [!NOTE]
> Resources created by the community are not supported by Microsoft. If you have questions or issues with community resources, contact the publisher of the resource. Before using these resources, you must ensure that they meet the Power Apps component framework guidelines and should only be used for reference purpose.

## Tutorial: Use code components on pages with Liquid template tag

In this tutorial, you'll configure Power Apps portals to add the component to a webpage and set access for the **Web Resource** table. You'll then visit the portals webpage and interact with the component.

### Before you begin

If you're using the sample code component used in this tutorial, ensure that you first import the sample solutions to the environment before you begin. To learn about solution import, go to [Import solutions](../data-platform/import-update-export-solutions.md).

### Prerequisites

For prerequisites, and to learn about supported/unsupported code components in portals, go to [Use code components in portals (preview)](component-framework.md).

> [!NOTE]
> This tutorial uses a sample code component created using Power Apps component framework to demonstrate a map control on a webpage. You can also use any existing or new component of your own, and any other webpage for this tutorial. In this case, be sure to use your component and webpage when following the steps in this tutorial. For more information about how to create code components, go to [Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md).

### Step 1. Add the code component to a webpage from Studio

1. Open your portal in [Power Apps portals Studio](portal-designer-anatomy.md).

1. On the top-left corner, select **New page**.

1. Select **Blank**.

1. On the right-side property pane, update the webpage name. For example, "Map Viewer."

1. Update partial URL. For example, "mapviewer."

1. Expand **Permissions**.

1. Disable **Page available to everyone.**

1. Select the web roles that should be allowed access to this page.

1. Select the editable area on page to edit the Liquid source code.

1. Open studio **code editor**.

1. Add control with Liquid template tag using the following syntax:

    ```
    {% codecomponent name:abc\_SampleNamespace.MapControl controlValue:'Space Needle' controlApiKey:<API Key Value> %}
    ```

    > [!TIP]
    > To retrieve the details of all imported components, and to search for a component name, refer to [CustomControl](../../developer/data-platform/reference/entities/customcontrol.md) Web API.

    For example:

    -   To search for a component:

        `https://contoso.api.crm10.dynamics.com/api/data/v9.2/customcontrols?$select=ContosoCustomControlName`

    -   To retrieve input parameters for a component:

        `https://contoso.api.crm10.dynamics.com/api/data/v9.2/customcontrols?$filter=name eq 'ContosoCustomControlName' &$select=manifest`

1. Save and close the code editor.

1. On the top-right corner, select **Browse website**.

1. The webpage will now show the control added on it.

### Step 2. Allow Read access to the Web Resource table

Follow the steps outlined in [Allow Read access to the Web Resource table](component-framework-tutorial.md#step-5-allow-read-access-to-the-web-resource-table).

## Next steps

[Overview: Use code components in portals](component-framework.md)

### See also

[Codecomponent Dataverse entity tag](liquid/portals-entity-tags.md#codecomponent) <br>
[Codecomponent Template tag](liquid/template-tags.md#codecomponent) <br>
[Power Apps component framework overview](../../developer/component-framework/overview.md) <br>
[Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md) <br>
[Add code components to a column or table in model-driven apps](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md)<br>
[Implement a sample portal Web API component](implement-webapi-component.md)

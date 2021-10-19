---
title: Liquid template tag for code components (preview)
description: Learn about using Liquid template tag for code components through portals Studio.
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/19/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
  - tapanm-msft
  - GitanjaliSingh33msft
  - nickdoelman
---

[This article is pre-release documentation and is subject to change.]

# Liquid template tag for code components (preview)

Power Apps component framework empowers professional developers and app makers to create code components for model-driven and canvas apps. These code components can provide an enhanced experience for users working with data on forms, views, and dashboards. More information: [Use code components in portals (Preview)](https://docs.microsoft.com/powerapps/maker/portals/component-framework)

With this release, we've introduced adding of code components created using Power Apps component framework using [Liquid template tag](https://docs.microsoft.com/powerapps/maker/portals/liquid/liquid-tags) on web pages and enabled components using Web API that are enabled for field-level components on forms in portals.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
> - Portals only currently supports [code components that are added to a field](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column) in a model-driven app.

Code components can be added using the **codecomponent** liquid template tag. The key for denoting the code component that needs to be loaded is passed in using the **name** attribute. The key can be the GUID (which is the custom component ID), or the name of the custom component imported in Microsoft Dataverse.

The values of the properties that the code component expects needs to be passed in as a key/value pair separated by "**:**" (colon sign), where key is the property name and the value is the JSON string value.

*{%codecomponent name:&lt;ID or name&gt; &lt;property1:value&gt;%}*

For example, to add a code component with Liquid template tag expecting an input parameter named "*controlValue*":

*{% codecomponent name:abc\_SampleNamespace.MapControl controlValue:'Space Needle' controlApiKey:&lt;API Key Value&gt;%}*

You can use [Sample Map Control](https://docs.microsoft.com/en-us/powerapps/developer/component-framework/sample-controls/map-control) and [package them as solutions](https://docs.microsoft.com/powerapps/developer/component-framework/implementing-controls-using-typescript#packaging-your-code-components) for use with portals.

> [!NOTE]
> Resources created by the community are not supported by Microsoft. If you have questions or issues with community resources, contact the publisher of the resource. Before using these resources, you must ensure that these community resources meet the Power Apps component framework guidelines and should only be used for reference purpose.

## Prerequisite

For prerequisites, and to know supported/unsupported code components in portals, see [Use code components in portals (Preview)](https://docs.microsoft.com/powerapps/maker/portals/component-framework).

## Tutorial: Use code components on pages with Liquid template tag

In this tutorial, you'll configure Power Apps portals to add the component to a web page and set access for the Web Resource table. And then, you'll visit the portals webpage and interact with the component.

> [!NOTE]
> This tutorial uses a sample code component created using Power Apps component framework to demonstrate a three-dimensional view of an equipment. You can also use any existing or new component of your own instead, and any other web page for this tutorial. In this case, ensure to use your component and web page when following the steps in this tutorial. For more information about how to create code components, see [Create your first component](https://docs.microsoft.com/powerapps/developer/component-framework/implementing-controls-using-typescript).

## Before you begin

If you're using the sample code component used in this tutorial, ensure you first import the sample solutions to the environment before you begin with the next steps. To learn about solution import, see [Import solutions](https://docs.microsoft.com/powerapps/maker/data-platform/import-update-export-solutions).

## Step 1. Add the code component to a web page from Studio

1.  Open your portal in [Power Apps portals Studio](https://docs.microsoft.com/en-us/powerapps/maker/portals/portal-designer-anatomy).

2.  On the top-left corner, select **New page**.

3.  Select **Blank**.

4.  On the right-side property pane, update the webpage name. For example, 3D viewer.

5.  Update partial URL. For example, 3Dviewer.

6.  Expand **Permissions**.

7.  Disable **Page available to everyone.**

8.  Select the web roles that should be allowed access to this page.

9.  Select the editable area on page to edit liquid source code.

10. Open studio **code editor**.

11. Add control with liquid template tag using the following syntax.

{% codecomponent name:abc\_SampleNamespace.MapControl controlValue:'Space Needle' controlApiKey:&lt;API Key Value&gt;%}

> [!TIP]
> To retrieve the details of all imported components, and to search for a component name, refer to [CustomControl](https://docs.microsoft.com/powerapps/developer/data-platform/reference/entities/customcontrol) Web API.

For example:

-   To search for a component:

[*https://contoso.api.crm10.dynamics.com/api/data/v9.2/customcontrols?$select=ContosoCustomControlName*](https://contoso.api.crm10.dynamics.com/api/data/v9.2/customcontrols?$select=ContosoCustomControlName)

-   To retrieve input parameters for a component:

*https://contoso.api.crm10.dynamics.com/api/data/v9.2/customcontrols?$filter=name eq 'ContosoCustomControlName' &$select=manifest*

12. Save and close the code editor.

13. On the top-right corner, select **Browse website**.

14. The webpage will now show the control added on it.

## Step 2. Allow Read access to the Web Resource table

See [Allow Read access to the Web Resource table](https://docs.microsoft.com/powerapps/maker/portals/component-framework-tutorial#step-5-allow-read-access-to-the-web-resource-table).


## Next steps

[Overview: Use code components in portals](component-framework.md)

### See also

[Power Apps component framework overview](../../developer/component-framework/overview.md) <br>
[Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md) <br>
[Add code components to a field or table in model-driven apps](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md)


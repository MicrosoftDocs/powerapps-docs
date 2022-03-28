---
title: Use code components in portals 
description: Learn about creating code components for model-driven and canvas apps using Power Apps component framework inside Power Apps portals.
author: GitanjaliSingh33msft

ms.topic: conceptual
ms.custom: 
ms.date: 02/11/2022
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
  - nickdoelman
  - GitanjaliSingh33msft
  - HemantGaur
---

# Use code components in portals

Power Apps component framework empowers professional developers and app makers to create code components for model-driven and canvas apps. These code components can provide an enhanced experience for users working with data on forms, views, and dashboards. More information: [Power Apps component framework overview](../../developer/component-framework/overview.md)

Power Apps portals now supports controls for model-driven apps created using Power Apps component framework. To use code components in portals webpages, follow these steps:

![Create code component using component framework, then add the code component to a model-driven app form, and configure the code component field inside the basic form for portals.](media/component-framework/steps.png "Create code component using component framework, then add the code component to a model-driven app form, and configure the code component field inside the basic form for portals.")

After following these steps, your users can now interact with the code component using the portal page that has the respective basic form.  

> [!IMPORTANT]
> - Portals only currently support [code components that are added to a field](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column) in a model-driven app.

## Prerequisites

- You must have System Administrator privileges to enable the Power Apps component feature in the environment.
- Your portal version must be [9.3.3.x](versions/version-9.3.3.x.md) or higher.
- Your starter portal package must be [9.2.2103.x](versions/package-version-9.2.2103.md) or higher.

## Create and package code component

To learn about creating and packaging code components created Power Apps component framework, go to [Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md).

### Supported field types and formats

Portals supports restricted field types and formats for using code components. The following table lists all supported field data types and formats:

:::row:::
   :::column span="":::
      Currency
   :::column-end:::
   :::column span="":::
      DateAndTime.DateAndTime
   :::column-end:::
   :::column span="":::
      DateAndTime.DateOnly
   :::column-end:::
   :::column span="":::
      Decimal
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Enum
   :::column-end:::
   :::column span="":::
      Floating Point Number
   :::column-end:::
   :::column span="":::
      Multiple
   :::column-end:::
   :::column span="":::
      OptionSet
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      SingleLine.Email
   :::column-end:::
   :::column span="":::
      SingleLine.Phone
   :::column-end:::
   :::column span="":::
      SingleLine.Text
   :::column-end:::
   :::column span="":::
      SingleLine.TextArea
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      SingleLine.Ticker
   :::column-end:::
   :::column span="":::
      SingleLine.URL
   :::column-end:::
   :::column span="":::
      TwoOptions
   :::column-end:::
   :::column span="":::
      Whole
   :::column-end:::
:::row-end:::

More information: [Attributes list and descriptions](../../developer/component-framework/manifest-schema-reference/property.md#remarks)

### Unsupported code components in portals

-   [Data-set
    components](../../developer/component-framework/sample-controls/data-set-grid-control.md)
    aren’t supported.

-   The following code component APIs aren’t supported:

    -   [Device.captureAudio](../../developer/component-framework/reference/device/captureaudio.md)

    -   [Device.captureImage](../../developer/component-framework/reference/device/captureimage.md)

    -   [Device.captureVideo](../../developer/component-framework/reference/device/capturevideo.md)

    -   [Device.getBarcodeValue](../../developer/component-framework/reference/device/getbarcodevalue.md)

    -   [Device.getCurrentPosition](../../developer/component-framework/reference/device/getcurrentposition.md)

    -   [Device.pickFile](../../developer/component-framework/reference/device/pickfile.md)

    -   [Utility](../../developer/component-framework/reference/utility.md)

-   The [uses-feature](../../developer/component-framework/manifest-schema-reference/uses-feature.md) element must not be set to **true**.

-   [Value elements not supported](../../developer/component-framework/manifest-schema-reference/property.md#value-elements-that-are-not-supported)
    by Power Apps component framework.

## Add a code component to a field in a model-driven app

To learn how to add a code component to a field in model-driven app, go to [Add a code component to a field](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column).

> [!IMPORTANT]
> Code components for portals are available for web browsers using the client option of **Web**.

## Configure portal for code component

After the code component is added to a field in a model-driven app, you can configure portals to use the code component on a basic form.

To add a code component to a basic form:

1. Open [Portal Management](configure/configure-portal.md) app.

1. On the left pane, select **Basic Forms**.

1. Select the basic form to which you want to add the code component.

1. Select **Related**.

1. Select **Basic Form Metadata**.

1. Select **New Basic Form Metadata**.

1. Select **Type** as **Attribute**.

1. Select **Attribute Logical Name.**

1. Enter **Label**.

1. For **Control Style**, select **Code Component.**

1. Save and close the form.

## Code components using the portal Web API

A code component can be built and added to a webpage that can use the [portal Web API](web-api-overview.md) to perform create, retrieve, update, and delete actions. This feature allows greater customization options when developing portal solutions. For more information, go to [Implement a sample portal Web API component](implement-webapi-component.md).

## Next steps

[Tutorial: Use code components in portals](component-framework-tutorial.md)

### See also

[Power Apps component framework overview](../../developer/component-framework/overview.md) <br>
[Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md) <br>
[Add code components to a column or table in model-driven apps](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
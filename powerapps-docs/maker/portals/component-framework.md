---
title: Use code components created using Power Apps Component Framework inside Power Apps portals | Microsoft Docs
description: Learn about using code components created using Power Apps Component Framework inside Power Apps portals.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/05/2021
ms.author: nenandw
ms.reviewer: tapanm
contributors:
  - tapanm-msft
  - sandhangitmsft
  - HemantGaur
---

# Use code components in portals (Preview)

[This article is pre-release documentation and is subject to change.]

Power Apps component framework empowers professional developers and app makers
to create code components for model-driven and canvas apps (public preview) to
provide enhanced user experience for the users to work with data on forms,
views, and dashboards. More information: [Power Apps component framework
overview](../../developer/component-framework/overview.md)

Power Apps portals now supports controls for model-driven apps created using
Power Apps component framework. To use code components in portals webpages,
follow these steps:

![Create code component using component framework, then add the code component to a model-driven app form, and configure the code component field inside the entity form for portals and allow Read permission to the Web Resource entity.](media/component-framework/steps.png "Create code component using component framework, then add the code component to a model-driven app form, and configure the code component field inside the entity form for portals and allow Read permission to the Web Resource entity.")

After following these steps, your users can now interact with the code component using the portal page that has the respective entity form.  

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
> - Portals only supports [code components that are added to a field](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-field) in a model-driven app currently.

## Prerequisites

-   User must have a valid Power Apps license. More information: [Power Apps
    component framework
    licensing](../../developer/component-framework/overview.md#licensing)

-   System Administrator privileges are required to enable the Power Apps
    component feature in the environment.
- Your portal version must be [9.3.3.x](versions/version-9.3.3.x.md) or higher.
- Your starter portal package must be [9.2.2103.x](versions/package-version-9.2.2103.md) or higher.

## Create and package code component

To learn about creating and packaging code components created using Power Apps
component framework, go to [Create your first
component](../../developer/component-framework/implementing-controls-using-typescript.md).

### Supported field types and formats

Portals supports restricted field types and formats for using code components.
The following table lists all supported field data types, and formats.

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

    -   [WebAPI](../../developer/component-framework/reference/webapi.md)

-   [uses-feature](../../developer/component-framework/manifest-schema-reference/uses-feature.md)
    element must not be set to **true**.

-   [Value elements not
    supported](../../developer/component-framework/manifest-schema-reference/property.md#value-elements-that-are-not-supported)
    by Power Apps component framework.

## Add a code component to a field in model-driven app

To learn about how to add code component to a field in model-driven app, go to
[Add a code component to a
field](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-field).

> [!IMPORTANT]
> Code components for portals are available for web browsers using the
client option of **Web**.

## Configure portal for code component

After the code component is added to a field in model-driven app, you can now
configure portals to use the code component in the entity form. Once you
configure the code component on an entity form, ensure you configure entity
permission to allow **Read** access to **Web Resource** entity for the portal
users before they can see the component on the portal page.

To add code component to an entity form:

1.  Open [Portal
    Management](configure/configure-portal.md)
    app.

2.  On the left-pane, select **Entity Forms**.

3.  Select the entity form you want to add the code component to.

4.  Select **Related**.

5.  Select **Entity Form Metadata**.

6.  Select **New Entity Form Metadata**.

7.  Select **Type** as **Attribute**.

8.  Select **Attribute Logical Unit Name.**

9.  Enter **Label**.

10. For **Control Style**, select **Code Component.**

11. Save and close the form.

## Allow Read access to Web Resource entity

Portals requires **Read** permission to be set on **Web Resource** entity before
users can see the code component on the web page with the entity form.

To configure Read access on Web Resource entity:

1.  Open [Portal
    Management](https://docs.microsoft.com/powerapps/maker/portals/configure/configure-portal)
    app.

2.  On the left-pane, select **Entity Permission**.

3.  Select **New**.

4.  Enter **Name.**

5.  Select *Web Resource (webresource)* for **Entity Name**.

6.  Select your website record.

7.  Select *Global* for **Scope.**

8.  In **Privileges**, select *Read*.

9.  Select **Save**.

10. Under **Web Roles** section, select **Add Existing Web Role**.

11. Select the web role for the users that you want to see the code component in
    portals.

    For example, A**nonymous Users** for anonymous users, **Authenticated
    Users** for users authenticated by portals, or a custom web role.

12. Select **Save & Close**.

Once you add the entity form to a web page, users assigned to the selected web
role can now see the code component on the portal page having the selected
entity form.

## Next steps

[Tutorial: Use code components in portals](component-framework-tutorial.md)

### See also

[Power Apps component framework overview](../../developer/component-framework/overview.md) <br>
[Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md) <br>
[Add code components to a field or entity in model-driven apps](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md)


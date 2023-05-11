---
title: Contact us sample
description: Overview of the Contact us sample page that's part of the portal starter template.
author: ankitavish

ms.topic: conceptual
ms.custom: 
ms.date: 06/05/2022
ms.subservice: portals
ms.author: avishwakarma
ms.reviewer: ndoelman
contributors:
    - ankitavish
    - nickdoelman
---

# Contact us sample


[!INCLUDE[cc-pages-banner](../../includes/cc-pages-banner.md)]

When you create a new portal by using the **Portal from blank** template, it creates an example page called **Contact us**. This page provides a working example of how portal users can enter information into a form that will be stored in a Dataverse table.

:::image type="content" source="media/contact-us-sample/contact-us-page.png" alt-text="Contact Us page.":::

## Contact us webpage

The contact us webpage can be viewed in Power Apps [portals Studio](portal-designer-anatomy.md) by selecting **Pages and navigation** from the toolbar and then selecting **Contact us**. This webpage is composed of three sections:

- A [text component](add-text.md) for the page title, set to "Contact us".

- A [basic form component](add-form.md) named **Simple contact us form**, which is linked to the Dataverse table Feedback and set to Insert mode.

- Earlier versions of the sample may have included an [iframe component](add-iframe.md) linked to a map url.

> [!NOTE]
> The maps link doesn't have any functionality or geo-location enabled. It's provided as an example of a iframe component.

:::image type="content" source="media/contact-us-sample/contact-us-portalstudio.png" alt-text="Contact us page in portals Studio.":::

## Table permissions

To allow portal users to be able to insert records into the feedback table, [table permissions](configure/assign-entity-permissions.md) 

are configured to provide Create, Read, Write, and Delete permissions for the Administrator, Anonymous User, and Authenticated User [web roles](configure/create-web-roles.md).

:::image type="content" source="media/contact-us-sample/feedback-tablepermissions.png" alt-text="Feedback table permissions.":::

> [!NOTE]
> It's good practice to review your security requirements before providing access to Dataverse tables through portals.

## Basic form metadata

All the form fields that the **Contact us** form requires have been created using [basic form metadata](configure/configure-basic-form-metadata.md). These settings can be viewed and modified using the [Portal Management app](configure/configure-portal.md).

:::image type="content" source="media/contact-us-sample/basicform-metadata.png" alt-text="Basic form metadata.":::

## View feedback data

To view the feedback data that was collected by the sample webpage, go to the [Power Apps maker portal](https://make.powerapps.com). 

1. On the left pane, expand **Dataverse**, and then select **Tables**.

1. Select **Feedback**, and then select **Data**.

:::image type="content" source="media/contact-us-sample/feedback-dataverse.png" alt-text="Feedback viewed in Dataverse.":::

You can also create an app in Power Apps [(canvas or model-driven)](../index.md) or another portal page to view the feedback data.

### See also

[Dataverse Form Designer](../model-driven-apps/form-designer-overview.md)  
[Add form](add-form.md)  
[Power Apps portals Studio](portal-designer-anatomy.md)  
[Create and manage webpages](create-manage-webpages.md)  
[WYSIWYG editor](compose-page.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

---
title: Contact Us sample
description: Overview of the Contact Us sample page that is part of the portal starter template.
author: ankitavish
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 12/06/2021
ms.subservice: portals
ms.author: avishwakarma
ms.reviewer: ndoelman
contributors:
    - ankitavish
    - nickdoelman
---

# Contact Us sample

When you provision a new portal using the *portal from blank* template it will create an example web page called *Contact Us*. This example page provides a working example of how portal users can enter information into a form that will be stored in a Dataverse table.

:::image type="content" source="media/contact-us-sample/contact-us-page.png" alt-text="Contact Us page.":::

## Contact Us web page

The contact us web page can be viewed in the [portals Studio](portal-designer-anatomy.md) by selecting **Pages and navigation** from the toolbelt and choosing **Contact Us**. 

The example web page is composed of three sections;

- A section with a [text component](add-text.md) for the page title, set to "Contact Us".

- A section with a [basic form component](add-form.md) named *simple contact us form* linked to the Dataverse table *feedback* set to *Insert* mode.

- A section with an [IFrame component](add-iframe.md) linked to Bing maps.

> [!NOTE]
> The Bing maps link does not have any functionality of geo-location enabled. It is provided as an example IFrame component.

:::image type="content" source="media/contact-us-sample/contact-us-portalstudio.png" alt-text="Contact Us page in the portal Studio.":::

## Table permissions

In order for portal users to be able to insert records to the feedback table, [table permissions](/configure/assign-entity-permissions.md) were configured to provide create, read, write and delete permissions for the Administrators, Anonymous Users, and Authenticated Users [webroles](/configure/create-web-roles.md).

:::image type="content" source="media/contact-us-sample/feedback-tablepermissions.png" alt-text="Feedback table permissions.":::

> [!NOTE]
> It is good practice to review your security requirements before providing access to Dataverse tables using portals.

## Basic form metadata

To make all the contact us form fields required, [basic form metadata](/configure/configure-basic-form-metadata.md) records were added to the basic form using the [Portal Management app](/configure/configure-portal.md).

:::image type="content" source="media/contact-us-sample/basicform-metadata.png" alt-text="Basic form metadata.":::

## View Feedback Data

To view the feedback data collected using the sample web page, go to the [Power Apps maker portal](https://make.powerapps.com). 

1. Select the **Dataverse** tab.

1. Select **Tables**.

1. Select **Feedback**.

1. Select **Data**.

:::image type="content" source="media/contact-us-sample/feedback-dataverse.png" alt-text="Feedback viewed in Dataverse.":::

You can also create a [Power App (canvas or model-driven)](../index.md) or another portal page to view the feedback data.

### See also

- [Dataverse Form Designer](../model-driven-apps/form-designer-overview.md)
- [Add form](add-form.md)
- [Power Apps portals Studio](portal-designer-anatomy.md)
- [Create and manage webpages](create-manage-webpages.md)
- [WYSIWYG editor](compose-page.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
---
title: Add fixed page layouts
description: Instructions to add fixed layouts to be available within portals Studio.
author: ankitavish

ms.topic: conceptual
ms.custom: 
ms.date: 12/08/2021
ms.subservice: portals
ms.author: avishwakarma
ms.reviewer: ndoelman
contributors:
    - ankitavish
    - nickdoelman
---

# Add fixed page layouts


[!INCLUDE[cc-pages-ga-banner](../../../includes/cc-pages-ga-banner.md)]
When you add a new webpage to a portal by using [Power Apps portals Studio](../portal-designer-anatomy.md), you can choose either **Layouts** or **Fixed layouts**. If there are no fixed layouts available in portals Studio but you'd like to use the layout of an existing web template, you can add these templates as fixed page layouts by creating page template records with the [Portal Management app](configure-portal.md).

:::image type="content" source="media/add-fixed-layouts/no-fixed-layouts.png" alt-text="Screenshot showing the message 'There are no fixed layouts.'":::

A new portal is provisioned with several fixed layout web templates. You can add these templates (whether provided by default or in a [custom web template](../liquid/create-custom-template.md)) to portals Studio by creating corresponding [page template](page-templates.md) records.

1. In the Portal Management app, select **Page Templates**.

1. Select **New**, and then select a web template. The following web templates are provided as part of the default portal.

    | Web template | Suggested page template name |
    | - | - |
    | Full Page | **Page with child links** |
    | Full Page without Child Links | **Page with title** |

1. Add a new page template record with the following details.

    | Page template setting | Value |
    | - | - |
    | Name | Add a name, or choose a suggested value (for example, **Page with title**). |
    | Website | Choose the corresponding website. |
    | Type | **Web Template** |
    | Web Template | Choose the corresponding provided template (for example, **Full Page without Child Links**) or another web template. |
    | Use Website Header and Footer | Selected |
    | Is Default | Not selected |
    | Table Name | **adx_webpage** |
    | Description | Optional |

    :::image type="content" source="media/add-fixed-layouts/page-with-title.png" alt-text="Page Template record showing the aforementioned settings.":::

1. In portals Studio, select **Sync configuration**.

   The fixed layouts will now be available when you create webpages in portals Studio.

   :::image type="content" source="media/add-fixed-layouts/fixed-layouts.png" alt-text="Screenshot showing a list of fixed layouts to choose from.":::

### See also

[Create and manage webpages](../create-manage-webpages.md) <br>
[Work with templates](../work-with-templates.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

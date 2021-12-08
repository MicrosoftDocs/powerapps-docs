---
title: Add fixed page layouts
description: Instructions to add fixed layouts to be available within the portals Studio.
author: ankitavish
ms.service: powerapps
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

When you add a new web page to a portal using the [portals Studio](../portal-designer-anatomy.md), you can choose either **Layouts** or **Fixed Layouts**. If there are no existing fixed layouts available in the portals Studio, you can add existing web templates as fixed page layouts by creating page template records using the [Portal Management app](configure-portal.md).

:::image type="content" source="media/add-fixed-layouts/no-fixed-layouts.png" alt-text="No fixed layouts.":::

## Add fixed layouts using page templates

A new portal is provisioned with many fixed layout web templates. Both the provided and [custom web templates](../liquid/create-custom-template.md) can be added to the portals Studio by creating corresponding [page template](page-templates.md) records.

1. In the Portal Management app, select **Page Templates**.

1. Select **New**.

    The following web templates are provided as part of the default portal template:

    | Web Template | Suggested Page Template Name |
    | - | - |
    | Full Page | Page with child links |
    | Full Page without Child Links | Page with title |

1. Add a new Page Template record with the following details;

    | Page Template setting | Value |
    | - | - |
    | Name | *add a name, or choose suggested value, for example; Page with title* |
    | Website | *choose the corresponding website.* |
    | Type | Web Template |
    | Web Template | *choose corresponding provided or custom web template, for example; Full Page without Child Links* |
    | Use Website Header and Footer | checked |
    | Is Default | Not checked |
    | Table Name | adx_webpage |
    | Description | Optional |

    :::image type="content" source="media/add-fixed-layouts/page-with-title.png" alt-text="No fixed layouts available.":::

1. In the portals Studio, select **Sync configuration**.

1. The fixed layouts should now be available when creating web pages using the portals Studio.

    :::image type="content" source="media/add-fixed-layouts/fixed-layouts.png" alt-text="Add pages using fixed layouts.":::

### See also

[Create and manage webpages](../create-manage-webpages.md) <br>
[Work with templates](../work-with-templates.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
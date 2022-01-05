---
title: Add fixed page layouts
description: Instructions to add fixed layouts to be available within portals Studio.
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
<!--note from editor: Maybe it would be better to follow the UI in this case and use the title "Add fixed layouts to pages"? It occurs to me that fixed layouts aren't really defined anywhere and there's no clear story about why you'd want to use them. This why I suggest adding "...but you'd like to use the layout of an existing web template" in the following paragraph. If this isn't why you'd want to use them, please excuse!-->
When you add a new webpage to a portal by using [Power Apps portals Studio](../portal-designer-anatomy.md), you can choose either **Layouts** or **Fixed layouts**. If there are no fixed layouts available in portals Studio but you'd like to use the layout of an existing web template, you can add these templates as fixed page layouts by creating page template records with the [Portal Management app](configure-portal.md).<!--note from editor: Please check my suggested alt text. I believe there's a way to get double quotation marks in alt text (by using a backslash), but I'd like to verify that before I break the build.-->

:::image type="content" source="media/add-fixed-layouts/no-fixed-layouts.png" alt-text="Screenshot showing the message 'There are no fixed layouts.'":::

<!--note from editor: If there is only one way to add fixed layouts, you don't need this heading. If or when you add another method, this H2 can come back and the new method will be an H2 too. 
## Add fixed layouts using page templates
-->

A new portal is provisioned with several<!--note from editor: Do you think "many" is the right word here? It looks like there are only two by default, unless I've misread this paragraph.--> fixed layout web templates. You can add these templates (whether provided by default or in a [custom web template](../liquid/create-custom-template.md)) to portals Studio by creating corresponding [page template](page-templates.md) records.

1. In the Portal Management app, select **Page Templates**.

1. Select **New**, and then select a web template. The following web templates are provided as part of the default portal template.

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
    | Web Template | Choose the corresponding provided template (for example, **Full Page without Child Links**) or custom web template.<!--note from editor: Edit okay?--> |
    | Use Website Header and Footer | Selected |
    | Is Default | Not selected |
    | Table Name | **adx_webpage** |
    | Description | Optional |

    :::image type="content" source="media/add-fixed-layouts/page-with-title.png" alt-text="Page Template record showing the aforementioned settings.":::

1. In portals Studio, select **Sync configuration**.

   The fixed layouts will now be available when you create webpages in portals Studio.<!--note from editor: Suggested. "Should" is kind of a dangerous word to use if you're not telling people what to do if the layouts aren't available.-->

   :::image type="content" source="media/add-fixed-layouts/fixed-layouts.png" alt-text="Screenshot showing a list of fixed layouts to choose from.":::

### See also

[Create and manage webpages](../create-manage-webpages.md) <br>
[Work with templates](../work-with-templates.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
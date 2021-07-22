---
title: Add IFrame
description: Learn about how to add IFrame component to a Power Apps portals page using portals Studio.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---

# Add IFrame

Add IFrame component to your portal page to embed a webpage from any other website. 

To add IFrame component:

1.  [Edit the portal](manage-existing-portals.md#edit) to open it in Power Apps portals Studio.  

2.  Select the page on which you want to add the component.

3.  Select an editable element on the canvas.

4.  Select **Components** ![components icon.](media/components-icon.png "Components icon") from the left side of the screen.  

5.  Under **Portal components**, select **IFrame**. The IFrame placeholder is added to the canvas.

6.  In the properties pane on the right side of the screen, enter the following information:

    - **Width**: Enter the width of the IFrame.

    - **Height**: Enter the height of the IFrame.

        > [!NOTE]
        > You can also select the IFrame on the canvas and drag the handles to resize it.

    - **Link**: Enter the URL of the website to be displayed in the IFrame. Only secured links are accepted—that is, https:// is mandatory. By default, <https://www.bing.com> is available as the value.
    
        > [!div class=mx-imgBorder]
        > ![IFrame properties.](media/iframe-props.png "IFrame properties")  

> [!NOTE]
> You can also add [Power Virtual Agent](/power-virtual-agents/fundamentals-what-is-power-virtual-agents) bot to the  IFrame similarly using steps described in [add bot to your web site](/power-virtual-agents/publication-connect-bot-to-web-channels#custom-website).

### See also

- [Power Apps portals Studio](portal-designer-anatomy.md)
- [Create and manage webpages](create-manage-webpages.md)
- [WYSIWYG editor](compose-page.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
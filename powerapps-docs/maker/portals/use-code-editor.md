---
title: Use code editor
description: Learn about how to use code editor in Power Apps portals Studio to customize your portal page.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 02/08/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---

# Use code editor

To view the source of a component on the canvas, select the component, and then select the source code editor icon **&lt;/&gt;** in the footer.

> [!div class=mx-imgBorder]
> ![code editor icon.](media/code-editor-icon.png "Code editor icon")  

The source code is displayed in the **Code Editor** pane at the bottom of the screen. The changes you made earlier are updated in the source code. To make changes, update the source code and select **Save**. The changes are reflected on the canvas.

> [!div class=mx-imgBorder]
> ![code editor.](media/code-editor.png "Code editor") 

> [!NOTE]
> You can also add Liquid tags in source code editor for advanced configuration. More information: [Work with Liquid templates](liquid/liquid-overview.md)

> [!IMPORTANT]
> Using `<script></script>` tags in the source code editor can lead to unexpected results. It is recommended to add custom code to the **Custom JavaScript** section under the **Advanced** tab in the [web page](configure/web-page.md) record using the [Portal Management app](configure/configure-portal.md) or by editing the web page custom javascript file using [Visual Studio Code](vs-code-extension.md).

### See also

- [Power Apps portals Studio](portal-designer-anatomy.md)
- [Create and manage webpages](create-manage-webpages.md)
- [WYSIWYG editor](compose-page.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
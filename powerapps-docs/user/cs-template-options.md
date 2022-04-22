---
title: "Customize an email template using the template editor| MicrosoftDocs"
description: Learn how to create an email template.
author: mgandham
manager: shujoshi

ms.component: pa-user
ms.topic: conceptual
ms.date: 6/30/2021
ms.subservice: end-user
ms.author: gandhamm
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Customize an email template using the template editor

Use the **Editor** tab in the **Email Template** page to create customized email templates per your organization's business requirements. The Editor tab has three sections:

- Design canvas
- Toolbox
- Layout section types
 
![Enhanced Email Template.](media\email_designer_callout.png "Enhanced Template")

## Create an email template

- In the main part of the page, on the design canvas, you can drag, arrange, delete, and enter content. By default, an empty single one-column section (layout) element appears.
You can perform the following actions:
   - Drag the element into the canvas section. When you have dragged the element to a suitable location, a blue shaded region appears. Release the mouse button to drop the element at the location.
   - Select the element or the column layout. An add icon appears on the canvas. Select the icon for the element to appear at the location. 
   - Select **Go to the parent** to identify the section or column in which the element is embedded.

![Design options.](media\email_dsgn_options.png "Enhanced Template")

- From the **Layout section types** section, choose the basic layout of your email template and add it to the design canvas. The **Edit layout** flyout appears. You can change the columns in the layout, spacing, style, add a background color, and add a background image. You can also customize the number of columns you can add and the width of each column in this panel. 

On the design canvas, you can also select a column. The **Edit column** flyout appears. Customize the layout, spacing, style, add a background color or a background image for the column.

- The Toolbox section provides design elements that you'll use to construct your message. The following elements are available:

    - Text:  To add content to your email template, select the text element and add it to the design canvas. When you add the text element, you'll see some placeholder text within the element. A floating toolbar appears above the text element. You can perform the following actions:
          - Enter the content of the email or insert dynamic text. 
          - Use the options in the toolbar to further format the content.
    - Image: To add an image to your template, select the image and add it to the design canvas. When you add the image element, you'll see an image placeholder and the **Edit Image**, which shows configuration settings for the selected element. You can perform the following actions:
          - Upload an image or specify an image URL. 
          - Modify the image size and alignment.
    - Button: To add a button to the template, select the Button element and add it to the design canvas. When you add the button element, The **Edit Button** panel appears. You can perform the following actions:
          - Link to which a user must be redirected to when the button is clicked
          - Change the text, font, color, and appearance of the button. 
    - Divider: Select this element to divide one section of the template from another with a line. When you add this element,the **Edit Divider** panel appears. You can change the appearance, color, width, alignment, and spacing of the divider line with the options in this panel.

- General Styles: Use the options in this tab to change the width, font, font size, background color, and text color of the layout.

### See also

[How to create an email template  in model-driven apps](email-template-create.md)  
[How to create an email template  in model-driven apps](cs_email_template_builder.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]

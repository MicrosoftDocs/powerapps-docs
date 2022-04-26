---
title: Customize an email template using the template editor
description: Create an email template using the enhanced email template editor
author: mgandham
manager: shujoshi

ms.topic: conceptual
ms.date: 4/20/2022
ms.subservice: end-user
ms.author: gandhamm 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Customize an email template using the template editor

Use the **Editor** tab in the **Email Template** form to create customized email templates. The **Editor** tab has three sections:

- Design canvas
- Toolbox
- Layout section types
 
![Enhanced Email Template.](media\email_designer_callout.png "Enhanced Template")

## Customize an email template 

On the design canvas, you can drag, arrange, enter, and delete content. By default, the canvas contains one empty one-column layout section.

### Add an element to the template

- In the main part of the page, on the design canvas, you can drag, arrange, delete, and enter content. By default, an empty single one-column section (layout) element appears.
You can perform the following actions:
   - Drag the element into the canvas section. When you have dragged the element to a suitable location, a blue shaded region appears. Release the mouse button to drop the element at the location.
   - Select the element or the column layout. An add icon appears on the canvas. Select the icon for the element to appear at the location. 
   - Select **Go to the parent** to identify the section or column in which the element is embedded.

      ![Design options.](media\email_dsgn_options.png "Enhanced Template")

- From the **Layout section types** section, choose the basic layout of your email template and add it to the design canvas. On the **Edit layout** flyout, you can change the spacing, style, background color, and image of the layout. You can also customize the number of columns you need in your layout and the width of each column in this panel. 
On the design canvas, to change the appearance of a column, select a column. On the **Edit column** flyout, you can change the spacing, style, background colors or images for the column. 

- The Toolbox section provides design elements that you'll use to construct your message. The following elements are available:

    - Text:  To add content to your email template, select the text element and add it to the design canvas. When you add the text element, you'll see some placeholder text within the element. A floating toolbar appears above the text element. You can perform the following actions:
          - Enter the content of the email or insert dynamic text. 
          - Use the options in the toolbar to further format the content.
          
    - Image: To add an image to your template, select the image element and add it to the design canvas. An image placeholder appears on the canvas. On the **Edit Image** flyout, you can perform the following actions:
          - Upload an image or specify an image URL. 
          - Modify the image size and alignment.
          
    - Button: To add a button to the template, select the button element and add it to the design canvas. On The **Edit Button** flyout, you can perform the following actions:
          - Link to which a user must be redirected to when the button is clicked
          - Change the text, font, color, and appearance of the button. 
          
    - Divider: Select this element to divide sections of the template with a line. When you add this element, the **Edit Divider** panel appears. You can change the appearance, color, width, alignment, and spacing of the divider line with the options in this panel.

- General Styles: Use the options in this tab to change the width, font, font size, background and text color of the layout.

### Limitations

When you select the text element, the following features of the rich text editor toolbar are not supported: 

1. The personalization option
2. Adding images from the Image option
3. Tracking option of the Link option
4. Insert table
5. On  copy paste of a formatted content in the rich text editor of the Text Element, Font style in the Font dropdown of the toolbar of the rich text editor is not auto detected


### See also

[How to create an email template  in model-driven apps](email-template-create.md)  
[Enable the enhanced email template editor page](cs_email_template_builder.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]

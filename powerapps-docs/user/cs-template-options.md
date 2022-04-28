---
title: Customize an email template using the template editor
description: Create an email template using the enhanced email template editor
author: mgandham
manager: shujoshi

ms.topic: conceptual
ms.date: 4/25/2022
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

:::image type="content" source="media\email_designer_callout.png" alt-text="Screenshot of the email template editor page, with the canvas, toolbox, and layout section areas highlighted.":::

## Create an email template
<!-- Please change this H2 to "Customize an email template" - thanks! -->

On the design canvas, you can drag, arrange, enter, and delete content. By default, the canvas contains one empty one-column layout section.

### Add an element to the template

You have a few different ways to add items to your template.

    - Text:  To add content to your email template, select the text element and add it to the design canvas. When you add the text element, you'll see some placeholder text within the element. A floating toolbar appears above the text element. You can perform the following actions:
          - Enter the content of the email or insert dynamic text. 
          - Use the options in the toolbar to further format the content.
        > [!NOTE]
        > When you select the text element, the following capabilities of the rich text editor toolbar are not supported:
        > - Personalization. Use the Insert dynamic text editor to personalize content.
        > - Insert image. Use the image element to add an image to column.
        > - Tracking for links
        > - Inserting tables
        > - Font style and size of the text isn't detected, if you paste formatted content from other sources.
                  
    - Image: To add an image to your template, select the image element and add it to the design canvas. An image placeholder appears on the canvas. On the **Edit Image** flyout, you can perform the following actions:
          - Upload an image or specify an image URL. 
          - Modify the image size and alignment.
          
    - Button: To add a button to the template, select the button element and add it to the design canvas. On The **Edit Button** flyout, you can perform the following actions:
          - Link to which a user must be redirected to when the button is clicked
          - Change the text, font, color, and appearance of the button. 
          
    - Divider: Select this element to divide sections of the template with a line. When you add this element, the **Edit Divider** panel appears. You can change the appearance, color, width, alignment, and spacing of the divider line with the options in this panel.
- Drag an element from the Toolbox to the canvas. Blue shading indicates the element is in a suitable location and may be dropped.

- Select an element in the Toolbox. An **add** icon appears on the canvas. Select the icon to add the element.
<!-- Please include a screenshot. -->

Select **Go to the parent** to identify the section or column in which the element is embedded.
<!-- Please include a screenshot and context. Where is "Go to the parent" found? -->

:::image type="content" source="media/email_dsgn_options.png" alt-text="Screenshot of PLEASE DESCRIBE WHAT THIS SCREENSHOT IS SHOWING.":::

The **Elements** tab in the Toolbox contains the following items:

- **Text**: Add text content to your template. Replace the placeholder text with your content. Use the floating toolbar to insert dynamic text or format the content.

- **Image**: Add an image to your template. Select the image placeholder, and then select **Edit Image** and upload an image or specify an image URL. You can also modify the image's size and alignment.

- **Button**: Add a button to your template. Select the button, and then select **Edit Button** and enter the URL to open when the user selects the button. You can also change the label, label font, color, and appearance of the button.

- **Divider**: Divide the template into bordered sections. Select a divider, and then select **Edit Divider** and change the divider's appearance, color, width, alignment, and spacing.

Use the **General Styles** tab to change the layout's width, font, font size, background, and text color.
<!--A screenshot of this would be helpful. -->

### Add a layout section to the template

Drag a layout section from the **Layout section types** box to the canvas.

To modify a layout, select it, and then select **Edit layout**. You can change a layout's spacing, style, background color, and image. You can also change the number of columns in the layout and the width of each column.

To change the appearance of a column, select it, and then select **Edit column**. You can change a column's spacing, style, background color, and image.


### See also

[How to create an email template  in model-driven apps](email-template-create.md)  
[Enable the enhanced email template editor page](cs_email_template_builder.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]

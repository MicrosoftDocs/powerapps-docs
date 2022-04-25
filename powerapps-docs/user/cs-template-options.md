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

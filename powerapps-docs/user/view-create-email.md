---
title: "View and create email in model-driven apps | MicrosoftDocs"
description: "View and create email while using a model-driven app."
ms.date: 02/03/2020
ms.service:
  - "dynamics-365"
ms.topic: article
author: lalexms
ms.author: lalexms
manager: shujoshi
---


# Preview: View and create email through the Activities grid

View and create email through the Activities grid is an early-access feature. You can opt in early to enable these features in your environment. This will allow you to test these features and then adopt them across your environments. For information on how to enable these features, see [Opt in to 2020 release wave 1 updates](https://docs.microsoft.com/power-platform/admin/opt-in-early-access-updates).

Dynamics 365 model-driven apps let you interact with customers through email. The email functionality allows you to:

- View and respond to emails. 

- Utilize common email toolbar functionality and rich text editor controls. 

- View and insert images inline using drag-and-drop or copy-and-paste functionality. 

- Create email in a pop-up window.  

- Preview templates before applying them. 



## View your email

To view your email:

1. In the model-driven app's sitemap, select **Activities**. 

2. Select the **All Activities** drop-down, and then select **My Received Emails**.

    ![view-email](media/view-email.png "Display received emails")

3. Select the email you want to view to open it. The email will open, where you can then reply to the sender and recipients or forward it.

## Create email

The following steps detail how to create an email.

1. In the model-driven app's sitemap, select **Activities**.

2. On the command bar, select **Email**. A new email window opens.

    ![create-email](media/create-email.png "Create a new email")

    The **From** field is automatically populated based on the currently logged-in user.

3. Write your email directly in the composer or select **Insert Template** to search for and apply a template. For more information on inserting an email template, see [Insert an email template](insert-email-template.md).

4. To compose your email in a full-screen window, select the expand icon.

    ![email-expand-window](media/email-expand-window.png "Expand the email window")

    The message box has a rich text editor that enables you to create rich and well-formatted content for the emails with emphasis. The editor brings common word processor features like: 

    - Copy formatting
    - Font and size
    - Bold, italic, and underline
    - Background color for text and text color
    - Bulleted and numbered list
    - Decrease and increase indent
    - Block quote
    - Text alignment (align left, center, and right)
    - Link and unlink
    - Text strikethrough
    - Image
    - Text direction from right to left and left to right
    - Undo and redo
    - Remove format
    - Table

    ![email-toolbar](media/email-toolbar.png "Use the rich text editor features")

5. When you're done, select **Send**.


### See also

[Set up enhanced email](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)<br>
[Insert an email template](insert-email-template.md)

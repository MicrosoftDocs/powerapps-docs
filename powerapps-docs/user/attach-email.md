---
title: "Attach a file to email in model-driven apps | MicrosoftDocs"
description: Learn how attach a file to email.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 6/30/2021
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Attach a file to email

Having the ability to attach file(s) to a message is one of the most useful features of email. You can attach a file using one of the two ways:

   ![How to attach a file to email](media\email-how-to-attach-file-to-email-1a.png "How to attach a file to email")

   1. **Attach file**. Located in the top nav bar, **Attach file** allows you to do file attachments.
   2. **New Attachments**. Located above the rich text editor, the **New Attachments** ![New Attachments](media\email-new-attachment-icon.png "new attachment") icon allows you to use drag-and-drop or copy-and-paste functionality. 

      > [!Note] 
      > Once you save your email, you can use **Attach file** and **New Attachments** interchangeably.

      > [!Important] 
      > The default file size limit for an email file attachment is 5MB. The size limitations on email file attachments can be increased by your system administrators. 

## Work with attachments

You can attach an unlimited number of files to an email; however, there are file size limitations that are managed by your system administrator. 

**Enhanced email** is the default email form, however you can switch forms by doing the following:

   ![Switch forms](media\email-work-with-attachments-1a.png "Switch forms")
   
   1. Under the email subject name, click on the caret (v) next to **Email**
   2.	A drop-down appears with a list of email form options you can choose from.<BR><BR>

File attachments display differently, depending on the email form you are working in. You can switch email forms without losing information.

## Email form file attachment

   ![Email form file attachment](media\email-work-with-attachments-2a.png "Email form file attachment")

   1. **Email**. This display confirms which email form you are working in. 
   2. **Attachment**. This section displays a list of file attachments in a vertical view and only displays the first three attachments.
   3. **File count**. This displays when you have more files than what can be viewed and allows you to see the total number of attached files on the left side under the last attachment with the option to page over to see more images.

### Enhanced email form file attachment
   ![Work with attachments](media\email-work-with-attachments-13b.png "Work with attachments")

   1. **Enhanced Email**. This display confirms you are working in the **Enhanced email** form.
   2. **Attached files**. This section displays all your email  attachments in a tile view above your message horizontally. The defaulted setting for the maximum number of files that can display is five attachments before displaying the page forward functionality.
   3. **File count**. This displays when you have files that occupy more than two rows and allows you to see the total number of attached files on the left side under the last attachment they the option to page over to see more images.
   4. **Attachment Commands**. This allow you to use the select, select all, sort, delete, and download functionality when working with your file attachments.  

## Work with the attachment command bar
When you’ve attached one or more files to a message, you can manage them using the file attachment commands.  

## Select commands

Select commands allow you to select individual files or multiple files at once.

   ![Attachment command bar](media\email-working-with-the-attachment-command-bar-11a.png "Work with the attachment command bar")

   Legend
   1. **Select All**. This command is located on the right, above your attached files and allows you to select all file attachments at once. 

      > [!Note] 
      > **Select All** only selects files that are visible. If you have multiple pages of file attachments, you will need to go to that page and select those files independently.

   2. **Tile Color Transparency**. The background color of selected file attachments changes to light grey to identify which files have been selected.
   3. **Check box** You can also verify which files have been selected by viewing whether the checkbox in the top-right corner of the file attachment is selected. 

Formatting of file attachments in email can be realign based on the device being used and format it is being worked in.

  ![Format file attachments](media\email-working-with-the-attachment-command-bar-12a.png "Format file attachments")

   1. **Format Display** Regardless of format display, file attachments will only display the number of files that are enabled by your system administrator.
   2. **Page view**. The page view displays the total number of email attachments and always is displayed under the file attachments. 

### Delete and download commands
These are two of the most important commands when working with images. 

   ![Delete and download commands](media\email-working-with-the-attachment-command-bar-13a.png "Delete and download commands")

   1. **Delete**. This command works with the **Select** commands. You must first select a file before you can delete it. A confirmation request appears, requiring you to confirm you want to delete the file(s) you’ve selected.
   2. **Download**. This command also works with the **Select** commands and your browser download settings, allowing you to download an individual file or multiple files at once.  

## Preview image attachments

   ![How to preview images attachments](media\email-how-to-preview-images-attachments-11a.png "How to preview images attachments")

   1. **More options**. This command provides a list of actions for that file type.
   2. **Non-preview image**. Only non-preview image types allow you to either **export selected records**, **download**, or **delete** the attached file.
   3. **Preview image types**. Allow you to **export selected record**, **preview**, **download**, or **delete** the attached file. When you select the **preview** option, a pop-up window appears, displaying the image with the image name listed below.

### Supported email file attachments
The following is a list of file image types that are supported:

|image type	 |supports preview	|supported inline (in editor)|
|------------|-------------------|----------------------------|
|BMP.bmp     | Yes               | Yes                        |
|GIF.gif     | Yes               | Yes                        |
|ICO.ico     | Yes               | Yes                        |
|JPG.jpg     | Yes               | Yes                        |
|PNG.png     | Yes               | Yes                        |
|SVG.svg     | Yes               | Yes                        |
|PDF.pdf     | Yes (preview not supported on IE) | No         |

## View and insert images in email

The use of visual aids helps users convey a tremendous amount of information with just a glance. Having the ability to view and insert inline images in email using the drag-and-drop or copy-and-paste functionality is a very powerful tool for users. Additionally, you can browse to a file or reference an online URL using the image toolbar button.

You can drag-and-drop or copy-and-paste images into the email.

   ![How to view and insert images in email](media\email-how-to-view-and-insert-images-in-email-1b.png "How to view and insert images in email")

   1. **Email images** You can adjust the image size.  
   2. **Save**. When you complete your edits, select **Save** or **Save & Close**.

      > [!Note]
      > There's a 1 MB file size limitation when adding an inline image to an email for email templates. (For new or replied emails, there isn't a limit to the email size (it becomes part of the total email size).

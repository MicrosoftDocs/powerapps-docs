---
title: "Send email to multiple recipients | MicrosoftDocs"
description: "Learn how to send email to multiple recipients."
ms.date: 05/26/2020
ms.service:
  - "dynamics-365-sales"
ms.topic: article
author: sbmjais
ms.author: shjais
manager: shujoshi
---

# Send email to multiple recipients

You can send an email to multiple recipients by using email templates. This is known as *direct* or *bulk* emailing. By default, the direct email feature is enabled. To enable this feature, an administrator must select **Yes** for **Enable Send Direct Email Action in Unified Interface for Send Email enabled entities** on the **Email** tab in the **System Settings** dialog box. More information: [System Settings Email tab](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)

**To send email to multiple recipients**
  
1. In the site map for the model-driven app, select an entity to which you want to send email. For example, **Contacts**.  
  
2. In the list of records, select the contacts you want to send an email to.  
  
3. On the command bar, select **Send Direct Email**.  

    ![Select multiple contacts and then select Send Direct Email](media/select-contacts.png "Select multiple contacts and then select Send Direct Email")

4. In the **Send Email** pane, select an email template from the **Template** list.

    > [!NOTE]
    > - If you have multiple records that span across multiple pages, you can select one of following options from the **To** list:
    >   - **All records on current page**: Sends the email to all records displayed on the current page.
    >   - **All records on all pages**: Send the email to all the stored records.
    > - If a few records don't have an email address or they have an invalid email address, those records will be skipped from sending the email.

5. Select **Send**.

    ![Send email to multiple recipients](media/direct-email.png "Send email to multiple recipients")

## Check the status of bulk email action

You can check the status of bulk email action on the **System Jobs** page. You can see whether the bulk email job has failed or succeeded. If a job has failed, you can open the failed job to see its details.

**To check the bulk email status**

1. In your app, select the **Settings** icon, and then select **Advanced Settings**.

    > [!div class="mx-imgBorder"]
    > ![Advanced settings](media/advanced-settings.png "Advanced settings") 

    The **Business Management** page opens in a new browser tab.

2.  On the navigation bar, select **Settings**, and then under **System**, select **System Jobs**.
    
    A list of system jobs is displayed.

    > [!div class="mx-imgBorder"]
    > ![List of system jobs](media/filter-jobs.png "List of system jobs") 

3. In the grid header, select the **Filter** ![Filter icon to filter system jobs](media/filter-icon.png "Filter icon to filter system jobs") icon.

4. In the **System Job Type** column header, select the down arrow, select **Bulk Email**, and then select **OK**.

    > [!div class="mx-imgBorder"]
    > ![Bulk email filter](media/bulk-email-filter.png "Bulk email filter") 

    A list of bulk email jobs are displayed with their corresponding status.

    > [!div class="mx-imgBorder"]
    > ![Bulk email jobs](media/bulk-email-jobs.png "Bulk email jobs") 

5. Double-click the failed job to see its details.

### See also

[Enable direct email](https://docs.microsoft.com/power-platform/admin/system-settings-dialog-box-email-tab)
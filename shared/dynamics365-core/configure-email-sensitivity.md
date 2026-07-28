Configure sensitivity labels for emails in model-driven apps, such as Dynamics Customer Service and Dynamics 365 Contact Center, to ensure email communications comply with your organization's policies and protect sensitive information across attachments, replies, and forwards.

## Prerequisites

- Create and configure sensitivity labels in the Microsoft Purview portal. For more information, see [Create and configure sensitivity labels](/purview/create-sensitivity-labels?tabs=classic-label-scheme).
- An email server profile with **Server-to-Server Authentication (Same Tenant)** is configured for Exchange Online. Learn more in [Connect to Exchange Online](/power-platform/admin/connect-exchange-online).
- Server side synchronization is set up for email. Learn more in [Set up server-side synchronization for email](/power-platform/admin/set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks).
- The Microsoft Entra ID user associated with the mailbox has access to the required sensitivity labels in Microsoft Purview. Learn more in [Permissions in the Microsoft Purview portal](/purview/purview-permissions).

## Enable email data sensitivity labels

Before you add sensitivity labels to the email form, enable email data sensitivity labels in the environment.

Perform the following steps:

1. Sign in to [Power Platform admin center](https://admin.powerplatform.microsoft.com/).
1. In the left navigation pane, select **Manage**.
1. In the **Manage** panel, select **Environments**.
1. On the **Environments** page, choose an environment.
1. In the command bar, select **Settings**.  
1. Expand **Email**, and then select **Email settings**.
1. In **Set Email data sensitivity labels**, turn on the toggle for **Enable data sensitivity labels for emails**.

## Add the sensitivity label column to email form

To display sensitivity labels in emails, add the **Sensitivity label** column and control to the email form in Power Apps.

Perform the following steps:

1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.
1. In the navigation pane, select **Solutions**.
1. Open the solution you want or create a new one.
1. Select **Objects** on the left navigation pane, and then select **Add existing** > **Table** > **Email** > **Next**.
1. Select **Forms** > **Add existing form** > **Email (Main form)** > **Add**.
1. Open the main form, and then in the form designer, select **Columns**.
1. Search for **Sensitivity label**.
1. Drag the **Sensitivity label** column onto the form canvas.
1. Select the **Sensitivity label** column on the form.
1. In the **Properties** pane, select **Components** > **More components**.   
1. Search for and select **Email sensitivity label control**, and then select **Add**.  
1. Configure the control properties as required.
1. Select **Done**.
1. Select **Save and publish**.

### Related information 

[Use sensitivity labels in emails](/dynamics365/customer-service/use/use-sensitivity-labels)

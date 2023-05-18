---
title: Example Dataverse low-code plug-ins
description: Microsoft Dataverse low-code plug-ins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 03/20/2023
ms.custom: template-how-to
---
# Example Dataverse low-code plug-ins (experimental)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The goal of these plug-ins is to help you get started by simply integrating into your app. You will understand the authoring experience includes authoring Dataverse customAPIs backed by powerfx expressions which can trigger actions internal or external to Dataverse. 

> [!IMPORTANT]
> - This is an experimental feature. Use this if you're an early adopter, see something useful to you, and would like to help test the feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - Experimental features can radically change or completely disappear at any time. For this reason the feature is not enabled by default and you must explicitly opt in to use it.

> [!NOTE]
> Email templates are only available for certain tables. Please read the email template documentation for more information.

## Prerequisite

To use one of the example plug-ins for the data event the Dataverse Accelerator app must be installed in the environment. More information: [Prerequisites for creating a low-code plug-in](low-code-plug-ins.md#prerequisites-for-creating-a-low-code-plug-in)

## SendEmail based on a data event

To set this up, you need these prerequisites:

- Server-side synchronization is set up for your environment. More information: [Set up server-side synchronization of email, appointments, contacts, and tasks](/power-platform/admin/set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks)
- An email template. 

### Example email template

Here's an email template example that you can create for the SenMail based data event:
- **Template type**: **Global**
- **Name**: *Order Thank You*
- **Description**: *Use this template to thank a customer for placing an order with you.*
- **Subject**: `Thank you for your order <orderconfirmation-{!salesorder:Order Number;  }>`
- **Body**: Use this code.

```powerappsfl
   Hello {!Sales Order:First Name;},
   Order Type: {! Sales Order: Order Type;},
   Location Type: {! Sales Order: Location Type;},
   Address1: {! Sales Order: Address 1;},
   Address2: {! Sales Order: Address 2;},
   Preferred Service Start Date 1: {! Sales Order: Preferred Service Start Date;},
   Next Step- We take upto 48 hrs to schedule an in-person and will notify you as soon as we have a In-person Technician allocated at your site. For any questions, please contact us at 1-800-CON-SOLAR
   Yours Sincerely, 
   Contoso Sales 

```

### Create the automated plug-in

1. Play the Dataverse Accelerator app, and then select **+New plugin** under **Automated plugins**.
1. Enter the following information: 
   - **Name**: *SendEmailUponCreate*
   - **Table**: Select the logical table name of the sales orders, which is **SalesOrder**. This event is based off of Sales Orders table.
   - **Run this plugin with the row is**: **Created**
   - **Formula**: Paste the code below into the **Formula** box. For more information abut the SendEmailFromTemplate function, to to [SendEmailFromTemplate Action](/power-apps/developer/data-platform/webapi/reference/sendemailfromtemplate?view=dataverse-latest).
   
     `XSendEmailFromTemplate(LookUp('Email Templates',StartsWith(description,"solar")).'Email Template',ThisRecord,LookUp(Users,'Primary Email'="sampleemail@sample.com"),[ThisRecord.Email])`
1. Select **Advanced** > **Post-operation**.
1. Select **Save**. 

The confirmation message **Plugin successfully saved** appears.

## SendInapp notifications based on an instant action

In-app notifications enable makers to configure contextual, actionable notifications for users in model-driven apps.

### Create the low-code plugin that sends an in-app notification

1. Play the Dataverse Accelerator app, and then select  **+New plugin** under under **Instant plugins**.
1. Enter the following information: 
   - **Name**: *NotifyTechnican1*
   - **Description**: *This instant plug-in notifies the app user.*
1. On the **Parameters** page, use these **Data types**:
   - **OrderID**: **String**
   - **TechnicianEmail**: **String**
1. **Formula**. Paste the following code in the **Formula** box. For more information about this function, go to [SendAppNotification Action](/power-apps/developer/data-platform/webapi/reference/sendappnotification?view=dataverse-latest).
   ```powerapps-dot
    XSendAppNotification(
    "New service",
    LookUp(Users,'Primary Email'=TechnicianEmail),
    "You have a new solar panel installation scheduled on "& LookUp('Scheduling Results','OrderId'=OrderID).'ServiceDate'&" in "& LookUp('Service Orders','Order Number'=OrderID).City &". Contact the coordinator with any questions.",
    [XCreateSidePaneActionForEntity(
        "View order",OrderID,"Sales Order","cr8b8_serviceorder1",LookUp('Service Orders','Order Number'=OrderID).'Service Order'
        )
    ]
    )
    ```
1. Select **Next**.
1. On the **Summary** page, select **Save**.

### Invoke the in app notification instant action

1. Select the **Service Order App** canvas app, and then select **Edit** on the command bar.
1. Select the **SchedulingResultScreen** page on the left navigation pane.
1. On the **Insert** menu, add a **Button** to the page using the **Text** *Notify technician*.
1. Select the button, and enter the following in the **fx** formula bar, where *DataCardValue17* is the column that contains the Order ID, and *DataCardValue15* is the column that contains the technician’s email address.:
	```powerapps-dot
       Environment.cr8b8_Notifytechnician1(
       {OrderID: DataCardValue17.Text,
       TechnicianEmail: DataCardValue15.Text }
       );

       Notify("The technician was notified!", NotificationType.Success, 2000);

	 ```

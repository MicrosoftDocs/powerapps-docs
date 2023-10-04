---
title: Example Dataverse low-code plug-ins
description: Examples of Microsoft Dataverse low-code plug-ins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 10/04/2023
ms.custom: template-how-to
---
# Example Dataverse low-code plug-ins (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The goal of these example plug-ins is to help you get started by integrating them into your apps. You'll understand the authoring experience includes authoring Microsoft Dataverse custom APIs backed by Power Fx expressions, which can trigger actions internal or external to Dataverse.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Prerequisite

To use one of the example plug-ins for the data event the Dataverse accelerator app must be installed in the environment. More information: [Prerequisites for creating a low-code plug-in](low-code-plug-ins.md#prerequisites-for-creating-a-low-code-plug-in)

> [!NOTE]
> Email templates are only available for certain tables. More information: [Create templates for email](/power-platform/admin/create-templates-email)

## Return a non-negative value

This example uses the [Abs() function](/power-platform/power-fx/reference/function-numericals) to return the non-negative value of its argument. If a number is negative, Abs returns the positive equivalent.

1. Play the Dataverse Accelerator app, on the command bar select **New action** > **Instant plugin**. 
1. Provide a display name, such as the formula name, and description.
1. Create an `Out` parameter to validate expected behavior that makes sense, such as a string Optionally use input parameters to make testing easier, that makes sense with the formula. 
1. In the formula editor, wrap the `Out` parameter in curly brackets: 

   ```powerapps-dot
   {Out: "" }
   ```

1. Enter an expression that tests the formula: 
   - Validate that intellisense accepts the formula (text will turn light blue).
   - Implement an expression that provides an output to help validate the result, for example.

   ```powerapps-dot
   {Out: "Abs(-5) = 5: " & Text( Abs(-5) = 5 )  }
   ```

1. Select **Next**, and then select **Save**.
1. Select **Test** to test the formula. Use the output parameter to validate the result.

## Input validation and custom errors

### Duplicate detection

Implement server-side input validation, such as duplicate error detection, that throws a custom error message.

1. Play the Dataverse Accelerator app, on the command bar select **New action** > **Automated plugin**.
1. In the **Name** box enter *Duplicate check*.
1. For **Table**, select **Contact**.
1. For **Run this plugin when the row is**, select **Created**.
1. In the **Formula** box, enter this formula:
  ```powerapps-dot
   If( !IsBlank(LookUp([@Contacts],'Last Name'=ThisRecord.'Last Name' && 'First Name'=ThisRecord.'First Name')),
  	  Error("You have existing contacts with the same first name and last name")
  )
  ```
6. Select **Save**.

### Test the plug-in

1. To test the plug-in, create a canvas app using the contacts table by following the steps here: [Specify a table](../canvas-apps/data-platform-create-app-scratch.md#specify-a-table)
1. Create a contact row.
1. Create another contact with the same name as in the previous step.
1. A message is displayed indicating duplicate records found. Select **Ignore and save** on the error message prompt.

This custom error message is displayed: **You have two contacts with the same first and last name**.

### Data validation

Display specific types of errors using the _ErrorKind_ enumeration.

1. Create a new automated plug-in.
1. Provide the following values:
   - **Name**: *Input validation*
   - **Description**: *Checks for valid date and throws an error if invalid*
   - **Table**:  **Appointment**
   - **Run this plugin when the row is**: **Updated**
1. Enter the formula below:

   ```powerapps-dot
   If(ThisRecord.'Due Date' < Now(), 
   	Error({ Kind: ErrorKind.Validation , Message: "The due date cannot be in the past" })
   );
   ```
1. Under **Advanced options**, set **When should this run** to **Pre-operation**; you want to run this rule before data is saved to prevent invalid data.
1. Select **Save**.

Go to the [Error() function](/power-platform/power-fx/reference/function-iferror#error) to learn more about custom errors.

## Send email based on a data event

Prerequisites:
> [!div class="checklist"]
> * Server-side synchronization is set up for your environment. More information: [Set up server-side synchronization of email, appointments, contacts, and tasks](/power-platform/admin/set-up-server-side-synchronization-of-email-appointments-contacts-and-tasks)
> * An email template.

### Example email template

Here's an email template example that you can create for the SenMail based data event:
- **Template type**: **Global**
- **Name**: *Order Thank You*
- **Description**: *Use this template to thank a customer for placing an order with you.*
- **Subject**: `Thank you for your order <orderconfirmation-{!salesorder:Order Number;  }>`
- **Body**: Use this code.

```
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
   - **Formula**: Paste the code below into the **Formula** box. For more information abut the SendEmailFromTemplate function, to to [SendEmailFromTemplate Action](/power-apps/developer/data-platform/webapi/reference/sendemailfromtemplate?view=dataverse-latest&preserve-view=true ).
   
     ```powerapps-dot
     XSendEmailFromTemplate(
         LookUp('Email Templates',StartsWith(title,"Order Thank You")).'Email Template',
	 ThisRecord,
	 LookUp(Users,'Primary Email'="sampleemail@sample.com"),[ThisRecord.Email]
     )
     ```
1. Select **Advanced** > **Post-operation**.
1. Select **Save**. 

The confirmation message **Plugin successfully saved** appears.

## Send in-app notifications based on an instant action

In-app notifications enable makers to configure contextual, actionable notifications for users in model-driven apps.

### Create the low-code plugin that sends an in-app notification

1. Play the Dataverse accelerator app, and then select  **+New plugin** under under **Instant plugins**.
1. Enter the following information, select **Next**: 
   - **Name**: *NotifyTechnican1*
   - **Description**: *This instant plug-in notifies the app user.*
1. On the **Definitions** page, create input parameters with these data types:
   - **OrderID**: **String**
   - **TechnicianEmail**: **String**
1. **Formula**. Paste the following code in the **Formula** box. For more information about this function, go to [SendAppNotification Action](/power-apps/developer/data-platform/webapi/reference/sendappnotification?view=dataverse-latest&preserve-view=true ).
   ```powerapps-dot
    XSendAppNotification(
    	"New service",
    	LookUp(Users,'Primary Email'=TechnicianEmail),
    	"You have a new solar panel installation scheduled on "& LookUp('Scheduling Results','OrderId'=OrderID).'ServiceDate'&" in "& LookUp('Service Orders','Order Number'=OrderID).City &". Contact the coordinator with any questions.",
	[
		XCreateSidePaneActionForEntity(
        		"View order",
			OrderID,
			"Sales Order",
			"cr8b8_serviceorder1",
			LookUp('Service Orders','Order Number'=OrderID).'Service Order'
        	)
    	]
    )
    ```
1. Select **Next**.
1. On the **Summary** page, select **Save**.

### Invoke the in-app notification instant action

1. Select a canvas app and then select **Edit** on the command bar (or [create a new one](/power-apps/maker/canvas-apps/create-blank-app)).
1. Select screen on the left navigation pane, or create a new one.
1. On the **Insert** menu, add a **Button** to the page using the **Text** *Notify technician*.
1. Select the button, and enter the following in the **fx** formula bar, where *DataCardValue17* is the column that contains the Order ID, and *DataCardValue15* is the column that contains the technician’s email address. In this example, a canvas app named **Service Order App** is used.
	```powerapps-dot
	Environment.cr8b8_Notifytechnician1({
           OrderID: DataCardValue17.Text,
	   TechnicianEmail: DataCardValue15.Text 
	});

       	Notify("The technician was notified!", NotificationType.Success, 2000);

	 ```
   :::image type="content" source="media/low-code-plugin-ex-notify-inapp.png" alt-text="Add a button with Power Fx formula to send notification to technician" lightbox="media/low-code-plugin-ex-notify-inapp.png":::
1. **Save** and **Publish** your changes.

When the notify technician action is selected in the app, an in-app notification is sent to the technician who has been assigned to the service order. An action on the notification opens the service order details in a side pane.

:::image type="content" source="media/low-code-plugin-ex-notification-sent.png" alt-text="Notification sent to technician who receives in app":::

## Sample instant plug-in with MSN Weather connector

This plugin returns the current weather for a specific location using [MSN Weather connector](/connectors/msnweather/).

Prerequisites:
> [!div class="checklist"]
> * [Prerequisites for creating a low-code plug-in](low-code-plug-ins.md#prerequisites-for-creating-a-low-code-plug-in)
> * MSN Weather connector is allowed in the environment

1. Create a connection reference for MSN Weather if not available yet in the environment:
:::image type="content" source="media/low-code-plugin-msn-createconnectionref.png" alt-text="Create a connection reference in the app from the connection references pane on the right":::

1. Copy snippet:
:::image type="content" source="media/low-code-plugin-msn-action.png" alt-text="Copy the action snippet from the connections pane":::

1. Finish editing the formula using intellisense and consume the connector response properties as needed:
:::image type="content" source="media/low-code-plugin-msn-definition.png" alt-text="Complete the plug-in definition in the editor":::

1. Save

1. [Test the plug-in](low-code-plug-ins.md#test-a-low-code-plug-in)

## Low-code plug-ins with AI samples

### Sample for `AISummarize`

Here's an example of how you can perform text summarization of a Dataverse column.

To store the summarized version of a note's description, you can create either an instant or automated low-code plug-in that creates a new note. For this example, create an automated plug-in.

**Create the plug-in**

1. Run the Dataverse accelerator app.
1. Select the **Create automated plug-in** card.
1. Give it the **Display name** of _Summarize Notes_.
1. Select the table **Annotations**
1. Keep the radio selection on **Create** for the event.
1. Enter the following as the expression:
   ```powerapps-dot
   // Check if 'AI Summarized' in title to preview infinite loop
   If("AI Summarized" in Title, false,
    // Create new notes record related to the same Dataverse record
    Collect(Notes, {Title: "AI Summarized: " &Title, Description: AISummarize(Description), Regarding:ThisRecord.Regarding})
   )
   ```
1. Under **Advanced settings**, choose the _post-operation_ stage to run the plug-in after the data event occurs.
1. **Save** the plug-in.

:::image type="content" source="media/low-code-plugin-aisummarize-definition.png" alt-text="AI Summarized definition in the automated plug-in editor":::

Test the plug-in by running the data event. In this case, create a new note on any table. Check using the accounts table below.

1. In Power Apps (make.powerapps.com), go to **Tables** > **Accounts**.
1. On the command bar, select **Edit**.
1. Open a row in the default form by selecting an account, then select **Edit row using form**.
   :::image type="content" source="media/low-code-plugin-aisummarize-edit-account.png" alt-text="Open the accounts form":::
1. Save a new note in the timeline with a **Title** and **Description**.
1. Refresh the page. A new note appears with a summarized version of the previous note.

:::image type="content" source="media/low-code-plugin-aisummarize-notes.png" alt-text="AI Summarized notes in the timeline":::

> [!NOTE]
> - `AISummarize` might not work if the length of text is too short.
> - Other languages will be accepted and summarized into English by default.

### Sample for `AITranslate`

You can perform text translation with the `AITranslate` function. It currently supports translation to English (Example scenario: If customers report issues in different languages, you could introduce a new column to capture a version of their issue description that is translated to English). You can use this action in instant or automated low-code plug-ins.

In this demonstration, use an instant plug-in to quickly try the function and see the result.

1. Open the Dataverse accelerator app.
1. Select **Create instant plug-in**.
1. For the **Display name** type *AITranslateDemo*.
1. Select **New input parameter**.
1. For the **Label**, type _input_. Leave the **Data type** as **String**.
1. Select **New out parameter**. 
1. For the **Label** type _output_. Leave the **Data type** as **String**.
1. Use the following as the Power Fx expression:
   ```powerapps-dot
   {output: AITranslate(input)}
   ``` 
1. **Save** the plug-in.
1. Select **Test**. 
1. For the input provide any text in a language other than English as input (example text in Spanish: `Me encantan las nuevas funciones de IA`).
1. Select **Run**.
1. Verify the **Response** returned the text translated to English (the sample Spanish text should return as `I love the new AI features`).

### Sample for `AISentiment`

Here's an example of how you can detect sentiment with the `AISentiment` function. You can use this action in instant or automated low-code plug-ins.

Example scenario: In a customer feedback scenario, you could introduce a new column to capture the sentiment of that feedback as either positive, negative, or neutral.

In this demonstration, use an instant plug-in to quickly try the function and see the result.

1. Open the Dataverse accelerator app.
2. Select **Create instant plug-in**.
3. For the **Display name** type _AISentimentDemo_.
4. Select **New input parameter**.
5. For the **Label** type _input_. Leave the **Data type** as **String**.
6. Select **New out parameter**.
7. For the **Label** type _output_. Leave the **Data type** as **String**.
8. Use the following in the Expression:
   ```powerapps-dot
   { output: AISentiment(input) }
   ``` 
9. **Save** the plug-in.
10. Select **Test**.
11. For the input provide the following text: `The product is amazing!`
12. Select **Run**.
13. Verify the **Response** returned shows the output value as _Positive_.

### Sample for `AIExtract`

Here's an example of how you can extract data from text with the `AIExtract` function. You can use this action in instant or automated low-code plug-ins.

Example scenario: If customers submit inquiries about orders, you could introduce a new column to capture the order numbers mentioned.

In this demonstration, use an instant plug-in to quickly try the function and see the result.

1. Open the Dataverse accelerator app.
2. Select **Create instant plug-in**.
3. For the **Display name** type _AIExtractDemo_.
4. Select **New input parameter**.
5. For the **Label** type _input_. Leave the **Data type** as **String**.
6. Create another input parameter with the label as _entity_. Leave the **Data type** as **String**.
7. Select **New out parameter**. 
8. For the **Label** type _output_. Leave the `Data type` as `String`. 
9. Use the following in the **Expression**. The result of the `AIExtract` action is a table. In this example the first function to return the first value from the table is used.
   ```powerapps-dot
   { output: First( AIExtract(input, entity) ).Value }
   ```
11. Select **Save**. 
12. Select **Test**. 
13. For the input provide the following text: `Can you please provide an estimated arrival for order 52342352?`
14. For entity type `order number`.
15. Select **Run**.
16. Verify the response returned shows the output value as the order number.

### Sample for `AIClassify`

Here's an example of how you can classify text with the `AIClassify` function. You can use this action in instant or automated low-code plug-ins. 

For example, if a customers submit inquiries, you could introduce a new column to capture the type of inquiry such as **Problem**, **Billing**, **How To**, or **Licensing**. 

In this demonstration use an instant plug-in to quickly try the function and see the result.

1. Open the Dataverse accelerator app.
2. Select **Create instant plug-in**.
3. For the **Display name** type _AIClassifyDemo_.
4. Select **New input parameter**.
5. For the **Label** type _input_. Leave the Data type as String.
6. Create another input parameter with the **label** as _entity_. Leave the **Data type** as **String**.
7. Select **New out parameter**. 
8. For the Label type _output_. Leave the **Data type** as **String**.
9. Use the following in the **Expression**. The second input of the `AIExtract` action is a table of choices the input can be classified into. In this example, an inline table with the options _Problem_, _Billing_, _How To_, and _Licensing_ is used.
   ```powerapps-dot
   { output: AIClassify(input, ["Problem", "Billing", "How To", "Licensing"]) }
   ```
11. Select **Save**. 
12. Select **Test**. 
13. For the input provide the following text: `I am encountering an error trying to create a new record.`
14. Select **Run**.
15. Verify the **Response** returned shows the output value as _Problem_.

## See also

[Low-code plug-ins Power Fx (preview)](low-code-plug-ins-powerfx.md)

---
title: Example Dataverse low-code plug-ins
description: Examples of Microsoft Dataverse low-code plug-ins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 03/20/2023
ms.custom: template-how-to
---
# Example Dataverse low-code plug-ins (experimental)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The goal of these example plug-ins is to help you get started by integrating them into your apps. You'll understand the authoring experience includes authoring Microsoft Dataverse custom APIs backed by Power Fx expressions, which can trigger actions internal or external to Dataverse.

> [!IMPORTANT]
> - This is an experimental feature. Use this if you're an early adopter, see something useful to you, and would like to help test the feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - Experimental features can radically change or completely disappear at any time. For this reason the feature is not enabled by default and you must explicitly opt in to use it.

> [!NOTE]
> Email templates are only available for certain tables. Please read the email template documentation for more information.

## Prerequisite

To use one of the example plug-ins for the data event the Dataverse Accelerator app must be installed in the environment. More information: [Prerequisites for creating a low-code plug-in](low-code-plug-ins.md#prerequisites-for-creating-a-low-code-plug-in)

## Return a non-negative value

This example uses the Abs function to return the non-negative value of its argument. If a number is negative, Abs returns the positive equivalent.

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

1. Select **Save**.

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

1. Play the Dataverse Accelerator app, and then select  **+New plugin** under under **Instant plugins**.
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

## Invoke SQL stored procedures using a low-code plug-in

SQL provides an action known as a stored procedure. A stored procedure is one or more transactions statements, or .Net commands, that are used to execute complex processes. These processes can accept inputs, provide statements that perform operations on the inputs, and produce an output or return value.

Stored procedures are used when complex processes or data needs would be better served being computed on the server rather than the client. Stored procedures often improve the performance of the calculation and provide many more complex operations than would be possible in an app.

In most cases stored procedures are executed in SQL by IT manually or by using automated triggers. This can cause a burden on IT and a bottleneck for getting needed information. However, Dataverse can be used to directly invoke stored procedures using a low-code plug-in.

Using the Data Accelerator app, low-code plug-ins for stored procedures can be easily created using a wizard. In order to create the plug-in you'll need:

- Credentials and details about the SQL server and database where the stored procedure is located (or, if a connection is already present on your Dataverse environment, you need to know which one to use).
- Which stored procedure on the SQL database you wish to use.
- To understand what inputs and outputs are required by your procedure.

### Create the low-code plug-in to invoke stored procedure

1. Play the Dataverse Accelerator App.
1. In the Dataverse Accelerator app, under **Instant plugins** select **New plugin**.
1. Enter a **Display name** for your plug-in, you can also provide a **Description**.
1. Select **Advanced options**, and then select **Launch the plugins wizard**.
1. On the **Connections** screen, any SQL connections you already have configured for your environment appear here. If the connection you need is already present you can select it. Otherwise select **New connection** or **Add connection**.

   If you create a new connection, you'll be asked for your SQL authentication type, credentials, and other necessary information. Complete the required fields and then select **Create**.

   Connections use a connection reference to interface between Dataverse and the data source you are connecting to. The connection reference will be created for you, but if you would like to be able to provide a custom name, you can do so by selecting **Advanced options** and then select **Manually Configure Connection Reference**. This can also be used to select from existing connection references for an existing connection.

1. When your connection is created, return to the wizard and select your connection from the connections list, and then select **Next**.
1. A list of available SQL actions are provided. Currently, **Execute Stored Procedure** is available. Select the action you want, and then select **Next**.
1. In the dropdown lists, select the values for:
   - **Server name**: The name of the server for your connection – This can only be set to Default at this time.
   - **Database name**: The name of the database on the server you wish to use. Currently, this can only be set to **Default**. 
   - **Procedure name**: The name of the stored procedure you want to use.

   After selecting the procedure, a list of input values are presented. The values can either be configured to use dynamic values for every invocation (and allow you to use a specific field from a row as an input), or you can enter a static value to use for every invocation.

   After completing all the fields, the Power Fx formula to invoke the procedure is generated.

1. Select **Next**.
1. A review page is displayed that shows you the plug-in you are about to create for the stored procedure. If the information is correct, select **Create**.

   The plug-in is created.
1. A **Plugin** page appears, which shows you the name of the plug-in you just created. Select **Next**.
1. A list of the inputs appear that will be sent to the stored procedure and their data types. The Power Fx formula is also displayed that will be used to invoke the stored procedure.

   > [!NOTE]
   > Currently you can't edit the parameters or formula on this page, however this will be possible in the future.

Click **Test** to test your plugin. Add in static data for your inputs and validate if it was run successfully or not.

### Invoke the low-code plug-in stored procedure with a button

Once the low-code plug-in stored procedure is created you can then decide how to invoke it from within a canvas app. One good way to easily invoke it is by using a button on the app. Using the `OnClick` formula you can specify you want it to be executed and link the input values to existing fields.

To do this, you will need to know the name of the plug-in you created, and also know the input parameters you set up. If you have forgotten you can look at your plug-in’s details to get this information before you start.

To set the button to invoke the stored procedure:

1. Open the canvas app you want to invoke the stored procedure plug-in from.
1. Select the data icon on the left navigation panel.
1. Search for *Environment* and install the **Environment** data source. This data source is used for plug-ins, actions, and other functions. It's required to use the plug-in. 
1. Add a button control onto the the canvas app. More information: [Button control in Power Apps](../canvas-apps/controls/control-button.md)
1. Select the **OnClick** property, and then select the formula bar.
1. In the formula bar you'll need to input a formula to:
   - Call the environment data source. This is used to execute the plug-ins you have created.
   - Specify the plug-in you want to use.
   - Identify which columns on the form you want to map to which input parameter.

   If an input parameter is configured to a static value and not a variable, that parameter doesn't need to be defined.
   
   ```powerapps-dot 
   Environment.<plug-in logical name>({
   	<<input parameter 1>>: <<form field 1>>. Selected<datatype>,
   	<<input parameter 2>>: <<form field 2>>. Selected<datatype>,
   	…
   });
   ```
   - *Environment* is the environment data source, which is used to call and execute plug-ins and actions from within canvas apps in Dataverse. After it is entered and selected enter the period "." You will then enter the logical name of your stored procedure plug-in you created.
   - Input parameters are the individual parameters that are used as inputs to the stored procedure when invoking it. There must be one line for each input parameter. Then add the colon ":".
   - Form field is the column on the canvas app form that contains the data you want to pass. This is what provides you the ability to execute the stored procedure with any set of data from a row.

   For an example, there's a stored procedure named *cr8b8_FindBestTech*, that has an input parameter of *customerZipCode* in SQL and a canvas app form has a column named *ZipCode*, you create it as: 
   
   ```powerapps-dot
   Environment.cr8b8_FindBestTech ({
   	customerZipCode: ZipCode.text,
   });
   ```

1. The formula to populate the plug-in is complete. Select the button in the running app. Then, it takes the input values from the columns specified, and passes them to SQL for processing. The stored procedure processes the data based on its configuration.

### How to get the stored procedure results

At this time, plug-ins can't pass output values back to Dataverse. So you'll be limited to stored procedures that, once run, process and handle the result entirely in SQL. You can however access the output if it's stored in a SQL table. You can do that by creating a virtual table using the SQL server connector. The virtual table allows you to view and manage the output data and integrate it with your Dataverse data and app. More information: [Create virtual tables using the virtual connector provider (preview)](create-virtual-tables-using-connectors.md) 

### Stored procedure plug-ins limitations

- Currently stored procedures will only output the results into SQL. Due to this, you'll need to take additional steps if you need to use the output of these procedures in Dataverse. In the future, outputs to Dataverse will be supported.

- Once the formula is generated and the input parameters are configured, you can't edit them directly. Currently, instead of making changes to the existing plug-in you must create a new one.

- If a stored procedure runs longer than two minutes, Dataverse and the Power Apps (make.powerapps.com) timeout and you won't receive the completion notification. However, you can still directly access the SQL table to get the results though direct connections or virtual tables.

## See also

[Low-code plug-ins Power Fx (preview)](low-code-plug-ins-powerfx.md)

---
title: Use Dataverse low-code plug-ins
description: Microsoft Dataverse low-code plug-ins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 03/20/2023
ms.custom: template-how-to
---
# Use Dataverse low-code plug-ins (experimental)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Optimize your data architecture and reduce client-side load using Microsoft Dataverse low-code plug-ins. Low-code plug-ins are reusable, server-side synchronous (real-time) business logic workflows that execute a set of specific commands in Dataverse.

A plug-in is a custom event handler that executes in response to a specific event raised during processing of a Microsoft Dataverse data action. Traditionally, a plug-in was created as custom class compiled into a .NET Framework assembly that is then uploaded and registered with Dataverse. With low-code plug-ins, makers can create plug-ins with no or little coding and without having to manually register the plug-in.

Low-code plug-ins are defined in a Dataverse database and integrated into Power Apps. They can add business logic using the Power Fx expression language and directly integrate with Dataverse business data and external data through Power Platform connectors. With low-code plug-ins, you can quickly build rich workflows without any code.

> [!IMPORTANT]
> - This is an experimental feature. Use this if you're an early adopter, see something useful to you, and would like to help test the feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - Experimental features can radically change or completely disappear at any time. For this reason the feature is not enabled by default and you must explicitly opt in to use it.

There are two types of plug-ins:

- Instant  plug-ins
- Automated plug-ins

For the most part, logic that can be defined for an instant plug-in can also be defined for an automated low-code plug-in.

The main difference between the plug-in types are, in the way the plug-in type is triggered, and whether parameters can be used. Only instant plug-ins support parameters.

> [!IMPORTANT]
> Currently, only automated plug-ins allow you to interact with a specific record when the plug-in is invoked. This is referred as the *bound* table record. When defining logic for bound records in Power Fx, use the `ThisRecord` keyword to reference the record and use dot notation to access the column values.

## Instant plug-ins

An instant plug-in is business logic that is manually triggered. A user must explicitly invoke an instant plugin. This can be defined on a button click in an app, or within a Power Automate cloud flow using **perform an unbound action**.

You can define input and output parameters that allow certain values in the formula to change, or be variable. They also give you the ability to pass information between the plug-in and the context that runs it, so the same business logic can be reused in varying situations.  

- Input parameters can take information into the formula when it’s run.
- Output parameters let you define information that is returned when the plug-in completes successfully.

## Automated plug-ins

An automated plug-in is business logic that runs when a data event (create, update, or delete) occurs for a specified table. You can also design whether the plug-in runs before or after the data event completes, which allows flexibility to access and modify values in key stages of the event.

## Plug-in access

Plug-ins run in the context of the user who invoked the plug-in:

- Instant plug-ins use the identity of the user who manually triggered it.
- Automated plug-ins use the identity of the user who performs the data event.

To invoke a plug-in, a user accesses the table data involved in the plug-in definition (the tables that are part of the formula, or if it’s <!-- what is "it's here?--> associated with the settings of an automated plug-in).
 
Plug-ins access the following contexts natively in Dataverse:

- Any table rows the user can access.
- Any connections the user can access.

## Prerequisites for creating a low-code plug-in

- System administrator or system customizer security role membership in the Power Platform environment.
- Dataverse Accelerator solution. [Download and install the Dataverse Accelerator from AppSource](https://aka.ms/DataverseAccelerator/AppSource).
    1. Sign in to AppSource.
    1. Select **Get it now**.
    1. The **Dynamics 365 apps** page in Power Platform admin center appears.
    1. Select the environment you want.
    1. Review the legal terms and privacy statement to continue.
    1. Select **Install**.

Once the solution import has completed, the status is set to **Enabled** next to **Dataverse Accelerator**.

## Calling low-code plug-ins as actions from a canvas app

When a low-code plug-in is created for the first time, you'll be able to call the plug-ins as a Dataverse action inside a canvas app as described here: [Call Dataverse actions directly in Power Fx](../canvas-apps/connections/connection-common-data-service.md#call-dataverse-actions-directly-in-power-fx-experimental). However, for any subsequent plugins created, you'll have to remove and re-add the Power Fx environment language object. Then you'll be able to see all the low-code plug-ins as actions.

## When to use Dataverse plug-ins vs flows

Since low-code plug-ins are real-time business logic that run on the Dataverse environment, logic is run directly on the server and is executed without additional API calls. Consider using plug-ins whenever you are dealing with business data in Dataverse.

You can invoke plug-ins whether you are designing a Power App, Power Automate flow, or even an application with a different interface that uses the Dataverse web API.

When to use Power Automate:

- If you need to run business logic on a schedule.
- If you need to connect to other external data.

<!-- This is flagged for revision in doc-- Star – needs revision -->
Imagine you have a custom table named jobapplication that's used for job applications in your organization.

- When you want to create Jobapplication statistic record every night, which is a recurring task that runs every night. For this situation, create a flow in Power Automate.
- When you want to create a Jobapplication record only when the student name is not available in the system. For this situation, use a Dataverse action.

## Create an instant low-code plug-in

1. Sign into the environment where the Dataverse Accelerator solution is installed and play the Dataverse Accelerator app.
1. On the first card for **Instant plug-ins**, select **New plug-in**.
   :::image type="content" source="media/low-code-plugin1.png" alt-text="New plug-in in Dataverse Accelerator solution":::
1. On the first page of the editor, enter the following information, and then select **Next**.

   - **Display name**. Enter a name for the instant plug-in, such as *Calculate sum*.
   - **Description**. Enter a description for the instant plug-in.

1. Optionally, define your parameters:
   - Select **New input parameter**. Available data types are **Boolean**, **String**, **Float**, **Decimal**, **DateTime**, or **Integer**. Enter an input parameter, such as **Label:** *X* and **Data type**: *Integer*.
   - Select **New output parameter**. Available data types are **Boolean**, **String**, **Float**, **Decimal**, **DateTime**, or **Integer**. Enter an output parameter, such as **Label**: *Sum* and **Data type**: *Integer*.
1. Add more input and output parameters as necessary.
1. Enter the Power Fx formula in the **Formula** box.
   - You can reference any parameters you defined previously in the formula.
   - You can reference any Dataverse table rows using the `LookUp()` function.
   - For example, you can calculate the sum of two integers. Create two input parameters, X and Y, both type integer, and one output parameter, `Z`, of type string. You could use the following formula: `{Z:  X + Y }`
   > [!TIP]
   > Note the intellisense in the **Formula** box. Underlined red is invalid. Squiggly yellow means your logic might be affected by delegation limitations. Avoid delegation issues by using [delegable functions]( /power-apps/maker/canvas-apps/delegation-overview#delegable-functions).
   :::image type="content" source="media/low-code-plugin2.png" alt-text="Instance low-code plug-in using Power Fx to derive a sum value with two integers":::
1. Select **Next** to review the details.
1. Select **Save**.
1. Test your plug-in. More information: [Test an instant low-code plug-in](#test-an-instant-low-code-plug-in)

## Create an automated low-code plug-in

1. Sign into the environment where the Dataverse Accelerator solution is installed and play the Dataverse Accelerator app.
1. On the **Automated plugins** card, select **New plugin**.
1. Provide the following values:
   - **Name**: Enter a name for the plug-in, such as *Input validation*.
   - **Description**: Enter a description for the plug-in, such as *Test error handling*.
   - **Run this plugin rule when the row is**. Specify the data event used to trigger the plug-in:
      - **Create**. Triggers the rule during a row create operation.
      - **Update**. Triggers the rule during a row change operation.
      - **Delete**. Triggers the rule during a row delete operation.
1. **Formula**. Enter a Power Fx formula in the ***Formula box**.  
   For example:

   ```powerapps-dot 
   If( IsBlank( ThisRecord.Email ), SetPatch(Contacts, ThisRecord, { ‘Email description’: “No email” } ));  
   ```

1. **Advanced options** > **When should this run**:
   - **Pre-operation**. Select this option if you want to run your plug-in logic after the form validation, but before the values are inserted or changed in Dataverse.
   - **Post operation**. Select this option to run your plug-in logic after the values have been inserted or changed in Dataverse.
1. Select **Save**.
1. Test your plug-in. More information: [Test an instant low-code plug-in](#test-an-instant-low-code-plug-in)

## Create a low-code plug-in that uses connectors

The low-code plug-in for connectors solution is a streamlined user interface that makes creating low-code plug-ins for connector actions easier. It supports the creation of plug-ins for stored procedures, which can then be invoked in Power Apps. A wizard is installed as an additional feature of the Dataverse Accelerator, which is used for creating plug-ins with Power Fx formulas.

> [!NOTE]
> Currently, there are a limited number of connectors and actions available.

### Prerequisites

- All prerequisites described earlier for creating an instant or automated plug-in. More information: [Prerequisites for creating a low-code plug-in](#prerequisites-for-creating-a-low-code-plug-in)
- To try the new low-code plugins for connectors feature, you must install the additional low-code
plug-in for connectors solution after installing the Dataverse Accelerator.

#### Why is the low-code plug-in for connectors solution optional?

The low-code plug-in for connectors wizard uses the **Power Apps for Makers** connector to retrieve assets used to construct a more convenient experience (e.g., connections and connector details).

If your tenant has a data loss prevention (DLP) policy with certain configurations applied to your environment, these changes might prevent both the low-code plug-ins for connectors feature and the Dataverse Accelerator from working.

#### Risk: Data Loss Prevention policy configurations that block the low-code plug-in for connectors solution

If your tenant has a DLP policy applied to your environment that has one of the following configurations you won't be able to run the Dataverse Accelerator app in that environment, including the low-code plug-ins for connectors feature:

- The Power Apps for makers connector is blocked.
- The Power Apps for makers connector and the Microsoft Dataverse connector are in different business groups.

#### How to avoid this risk

Before you install the low-code plug-ins for connectors solution, check the DLP policy applied to the environment where you want to install the Dataverse Accelerator.

> [!IMPORTANT]
> Admin and non-admin users can see DLP policies impacting environments where they have system administrator or system customizer privileges.

If you can't see the DLP policy applied to the environment where you want to install the solution:

- Create a new developer environment, which you will be the system administrator of, then check the DLP policies applied to that environment once created.
- Contact your Power Platform tenant admin to ask if the desired environment has either of the DLP Policy configurations shown above.

#### Troubleshooting the low-code plug-in for connectors solution

If you accidentally installed the low-code plug-in for connectors solution and the Dataverse Accelerator app is now blocked by a DLP policy, uninstall the low-code plug-in for connectors wizard solution and the Dataverse Accelerator will be able to run.

1. Go to https://make.powerapps.com/
2. Go to the environment where the low-code plug-in for connectors solution is installed, and then select **Solutions** on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
3. Select the low-code plug-in for connectors solution.
4. On the command bar, select **Delete**.
5. In the dialog, select **Delete** to confirm.
6. On the command bar, publish all customizations.

> [!NOTE]
>
> - When you play the Dataverse Accelerator app, you'll need to refresh the browser tab where the app is running. It might take some time for the app to reflect the updates.
> - If there was a DLP policy blocking the app, it might take at least 10 minutes after the uninstall is completed for the platform to unblock the Dataverse Accelerator app.

#### Install the low-code plug-ins for connectors solution

The option to install the low-code plug-in for connectors wizard is provided when you install the Dataverse Accelerator.

1.	You can install the Dataverse Accelerator two ways:
   - App Source 
   - In the Power Platform admin center
2.	When the installer launches, select the environment.
3. An option to install the low-code plug-ins for connectors solution is displayed. Make sure the checkbox is selected if you want to install the solution.
4. Review the terms of service.
5. Select **Install**.

Once you have installed the solution, play the Dataverse Accelerator app and [Create the low-code plug-in that uses connectors](#create-the-low-code-plug-in-that-uses-connectors).

#### Create the low-code plug-in that uses connectors

1. In Power Apps (make.powerapps.com) go to apps and play the Dataverse Accelerator app.
1. In the Dataverse Accelerator app, on the **Instant Plugins** card select **New plugin**.
1. Name your plugin and provide a description.
1. Select **Advanced Options**, and then select **Launch the plug-ins wizard**.
1. A connections screen appears. Any SQL connections you already have configured for your organization appear here. If the connection you need is already present you can select it. Otherwise, select **New connection** or **Add connection**.
  If you create a new connection, you'll be asked for your SQL authentication type, credentials, and other information. Complete the required fields, and then select **Create**.

1. When your connection is created, return to the wizard and select your connection from the connections list, and then select **Next**.
   Connections use a connection reference to interface between Dataverse and the data source you are connecting to. The connection reference will be created for you, but if you want to provide a custom name, you can do so by selecting **Advanced options** and then select **Manually Configure Connection Reference**. This can also be used to select from existing connection references for an existing connection.
1. A list of available actions are provided. This allows you to pick which action you want to create plug-in for. Select the action and then select **Next**.
1. In the provided dropdown lists, select the values for each parameter. As you select values, the dropdown list values for the dependent fields are fetched when available, so you should select or provide value in order (from top to bottom).
1. After providing values for the initial parameters available, a dynamic list of input values might be presented depending on the last parameter. These can either be configured to be input parameters for every invocation, or you can enter a static value to use for every invocation.
   :::image type="content" source="media/lowcode-plug-in-from-connector.png" alt-text="Specify parameters for low-code plug-in for connectors wizard":::

   If dynamic values are returned, they can be configured in two ways:
   - Input parameters, which allow you to change the value every time the plugin is run. Check the box below the parameter to expose it as an input parameter.
   - Static values, which stay the same every time the plugin is run. Provide a static value by typing in the text field or make a selection from the dropdown.
   :::image type="content" source="media/lowcode-plug-in-input-param.png" alt-text="Specify input and static values":::
1. After completing each field the Power FX formula to invoke the procedure is generated. Select **Next**.
1. A review page appears that shows you the plug-in you are about to create for the stored procedure. If everything looks correct, select **Create**.
1. The plug-in editor opens. On the **plug-in** page, the name of the plug-in you have just created is displayed. Select **Next**.
1. A list of all of the inputs that will be sent to the stored procedure and their data types is displayed. The PowerFX formula that will be used to invoke the stored procedure is also displayed. This is also the screen you will later use to update the plug-in.
   > [!NOTE] 
   > Currently, you can't edit the parameters or formula on this page in the plug-ins wizard.

Now, test your low-code plug-in by adding in data for your inputs and validate your output.

## Test an instant low-code plug-in

Manually test the plug-in to verify it behaves as expected.

1. From the **plug-ins** page, select an instant low-code plug-in from the list, and then select **Test** on the command bar.
  :::image type="content" source="media/low-code-plugin-test.png" alt-text="Test low-code plug-in":::

1.	Provide values for any input parameters that are defined in the low-code plug-in, and then select **Run**.

Observe the response.

> [!TIP]
> Use output parameters to help validate expected behavior and results. Otherwise, you will only see a success or failure when testing.

### Integrate test a low-code plug-in

On the **Integrate** tab of the test page, you can learn how to invoke the instant plug-in from other contexts within Power Platform.

1. Copy the formula and paste it into an action property, such as a button control, in your app.
1. If input parameters are required, provide direct values or reference values from other controls in your app.
1. Open a new browser tab, and then go to https://make.powerapps.com/.
1.	In the same environment, create a new canvas app from scratch.
1.	Add the **Environments** table to your app. <!-- Is this table created from the Dataverse Accelerator solution?-->
1. Insert a button. This will be used to  call the formula. More information: [Button control in Power Apps](../canvas-apps/controls/control-button.md)
1. Copy the formula from the text area by selecting the copy icon (or manually highlighting and copying from keyboard), and paste the formula into the button’s **OnSelect** property.
1. Map each input parameters  values to real values, such as `Environment.CalculateSum({ X: 10, Y: 200 });`
1. If an output parameter is defined for the low-code plug-in, capture the response using `Set()` or **UpdateContext()**, such as `Set( ActionResult, Environments.CalculateSum({ X: 10, Y: 200 , “The }sum is ” )) );`
1. Add a label control and set the text value to the response captured. For example, set the text value of the label control to the variable `ActionResult`.
1. Play the app and select the button to run the low-code plug-in.

## Contacting Help + support

For issues with the Dataverse Accelerator solution installation or low-code plug-ins, such as errors received, [use the Help + support experience](/power-platform/admin/get-help-support) and include the following information:

- Problem Type- Dataverse Web API and SDK
- Problem Subtype- Accelerator kit for Dataverse

## Example low-code plug-ins you can create

For a few examples of how to create a low-code plug-in, go to [Example Dataverse low-code plug-ins (experimental)](lowcode-plug-ins-examples.md)
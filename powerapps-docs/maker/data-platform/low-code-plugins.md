---
title: Use Dataverse low-code plugins
description: Microsoft Dataverse low-code plugins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 03/20/2023
ms.custom: template-how-to
---
# Use Dataverse low-code plugins (experimental)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Optimize your data architecture and reduce client-side load using Microsoft Dataverse low-code plugins. These low-code plugins are reusable, server-side synchronous (real-time) business logic workflows that execute a set of specific commands in Dataverse.

Low-code plugins are defined in a Dataverse database and integrated into Power Apps. They can add business logic using the Power Fx expression language and directly integrate with Dataverse business data and external data through Power Platform connectors. With low-code plugins, you can quickly build rich workflows with any code.

> [!IMPORTANT]
> - This is an experimental feature. Use this if you're an early adopter, see something useful to you, and would like to help test the feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - Experimental features can radically change or completely disappear at any time. For this reason the feature is not enabled by default and you must explicitly opt in to use it.

## Types of low-code plugins <!-- The doc dropped "low-code" and just refers "plugins." If this is different you need to explain before introducing this different term.-->

There are two types of low-code plug-ins:

- Instant  low-code plug-ins
- Automated low-code plug-ins

For the most part, logic that can be defined for an instant low-code plugin can also be defined for an automated low-code plugin.

The main difference between the plug-in types are, in the way the plugin type is triggered, and whether parameters can be used. Only instant low-code plug-ins support parameters.

> [!IMPORTANT]
> Currently, only automated low-code plug-ins allow you to interact with a specific record when the low-code plug-in is invoked. This is referred as the *bound* table record. When defining logic for bound records in Power Fx, use the `ThisRecord` keyword to reference the record and use dot notation to access the column values.

## Instant low-code plugins

An instant low-code plug-inaction is business logic that is manually triggered. Therefore, an app user must manually invoke the low-code plugin. This can be defined as a button click in an app, or within a Power Automate cloud flow using the `perform an unbound` action.

You can define input and output parameters that allow you to dynamically pass information between the formula and calling context.

## Automated low-code plugins

An automated low-code plugin is business logic that runs, which is invoked when based on an event for a specified table and occurs when a row is created, updated, or deleted - also known as a *data event*.

### Low-code plugin access 

Low-code plugins run in the context of the user who invoked the plugin:

- Instant low-code plugins use the identity of the user who manually triggered it.
- Automated low-code plugins use the identity of the user who performs the data event.

To invoke a low-code plugin, a user accesses the table data involved in the plugin definition (the tables that are part of the formula, or if it’s <!-- what is "it's here?--> associated with the settings of an automated plugin).
 
Actions access the following context natively in Dataverse:

- Any table the invoking user can access within the same Dataverse instance.
- Any connections the invoking user can access.

<!-- ### When to use Power Automate

When you want to create Jobapplication statistic record every night, which is a recurring task that runs every night. For this situation, create a flow in Power Automate.

:::image type="content" source="media/jobapplication-flow.png" alt-text="Job application flow":::

When you want to create a Jobapplication record only when the student name is not available in the system. For this situation, use a Dataverse action. -->

## Prerequisites

1. System administrator or system customizer security role membership in the Power Platform environment.
1. Dataverse Accelerator solution. [Download and install the Dataverse Accelerator from AppSource](https://aka.ms/DataverseAccelerator/AppSource).
    1. Sign in to AppSource.
    1. Select **Get it now**.
    1. The **Dynamics 365 apps** page in Power Platform admin center appears.
    1. Select the environment you want.
    1. Review and accept the legal terms and privacy statement to continue.
    1. Select **Install**.

Once the solution import has completed, the status is set to **Enabled** next to **Dataverse Accelerator**.

## Create an instant low-code plugin

1. Sign into the environment where the Dataverse Accelerator solution is installed and play the Dataverse Accelerator app.
1. On the first card for **Instant plugins**, select **New plugin**.
   :::image type="content" source="media/low-code-plugin1.png" alt-text="New plugin in Dataverse Accelerator solution":::
1. On the first page of the editor, enter the following information, and then select **Next**.

   - **Display name**. Enter a name for the instant plugin, such as *Calculate sum*.
   - **Description**. Enter a description for the instant plugin.

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
   :::image type="content" source="media/low-code-plugin2.png" alt-text="Instance low-code plugin using Power Fx to derive a sum value with two integers":::
1. Select **Next** to review the details.
1. Select **Save**.

### Test the instant low-code plugin

Manually test the plugin to verify it behaves as expected.

1. From the **Plugins** page, select an instant low-code plugin from the list, and then select **Test** on the command bar.
  :::image type="content" source="media/low-code-plugin-test.png" alt-text="Test low-code plugin":::

1.	Provide values for any input parameters that are defined in the low-code plugin, and then select **Run**.

Observe the response.

> [!TIP]
> Use output parameters to help validate expected behavior and results. Otherwise, you will only see a success or failure when testing.

#### Integrate

On the **Integrate** tab of the test page, you can learn how to invoke the instant plug-in from other contexts within Power Platform.

1. Copy the formula and paste it into an action property, such as a button control, in your app.
1. If input parameters are required, provide direct values or reference values from other controls in your app.
1. Open a new browser tab, and then go to https://make.powerapps.com/.
1.	In the same environment, create a new canvas app from scratch.
1.	Add the **Environments** table to your app. <!-- Is this table created from the Dataverse Accelerator solution?-->
1. Insert a button. This will be used to  call the formula. More information: [Button control in Power Apps](../canvas-apps/controls/control-button.md)
1. Copy the formula from the text area by selecting the copy icon (or manually highlighting and copying from keyboard), and paste the formula into the button’s **OnSelect** property.
1. Map each input parameters  values to real values, such as `Environment.CalculateSum({ X: 10, Y: 200 });`
1. If an output parameter is defined for the low-code plugin, capture the response using `Set()` or **UpdateContext()**, such as `Set( ActionResult, Environments.CalculateSum({ X: 10, Y: 200 , “The }sum is ” )) );`
1. Add a label control and set the text value to the response captured. For example, set the text value of the label control to the variable `ActionResult`.
1. Play the app and select the button to run the low-code plugin.

## Create an automated low-code plugin

<!-- Need more complete steps than what's in the doc -->

1. Create a new automated plugin. <!-- where do you go to do this? --
1. 
1. 

## Create an instant low-code plugin that connects to external data

You can use the plugin wizard in the Dataverse Accelerator app to connect to external data using the Power Apps connections ecosystem. The wizard takes you through the steps needed to connect to your data.

Currently, there are a limited number of connectors and actions available.

1.	Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), go to Apps, and then play the Dataverse Accelerator app. 
1. Select **New plugin** under **Instant plugins**.
1. Name your plugin, you can also provide a description.
1. Select **Advanced Options**, and then select **Launch the plugins wizard**.
1. A connections screen appears. Any SQL connections you already have configured for your organization appear here. If the connection you need is already present you can select it. Otherwise, select **New connection** or **Add connection**.
  If you create a new connection, you'll be asked for your SQL authentication type, credentials, and other information. Complete the required fields, and then select **Create**.

1. When your connection is created, return to the wizard and select your connection from the connections list, and then select **Next**.
   Connections use a connection reference to interface between Dataverse and the data source you are connecting to. The connection reference will be created for you, but if you want to provide a custom name, you can do so by selecting **Advanced options** and then select **Manually Configure Connection Reference**. This can also be used to select from existing connection references for an existing connection.
1. A list of available actions are provided. This allows you to pick which action you want to create a virtual plugin for. Select the action and then select **Next**. <!-- Virtual plugin? You haven't defined this anywhere yet. -->
1. In the provided dropdown lists, select the values for each parameter. As you select values, the dropdown list values for the dependent fields are fetched when available, so you should select or provide value in order (from top to bottom).
1. After providing values for the initial parameters available, a dynamic list of input values might be presented depending on the last parameter. These can either be configured to be input parameters for every invocation, or you can enter a static value to use for every invocation.
1. After completing each field the Power FX formula to invoke the procedure is generated. Select **Next**.
1. A review page appears that shows you the plugin you are about to create for the stored procedure. If everything looks correct, select **Create**.
1. On the **Plugin** page, the name of the plugin you have just created is displayed. Select **Next**.
1. A list of all of the inputs that will be sent to the stored procedure and their data types is displayed. The PowerFX formula that will be used to invoke the stored procedure is also displayed. This is also the screen you will later use to update the plugin.
   > [!NOTE] 
   > Currently, you can't edit the parameters or formula on this page in the plugins wizard.

Now, test your low-code plugin by adding in data for your inputs and validate your output.

## Example low-code plugins you can create

The goal of these plugins is to help you get started by simply integrating into your app. You will understand the authoring experience includes authoring Dataverse customAPIs backed by powerfx expressions which can trigger actions internal or external to Dataverse. 

> [!NOTE]
> Email templates are only available for certain entities. Please read the email template documentation for more information. 

### SendEmail based on a data event

<!-- What kind of low-code plugin is this? Instant or automated? -->

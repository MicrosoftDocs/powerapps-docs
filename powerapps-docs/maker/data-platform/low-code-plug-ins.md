---
title: Use Dataverse low-code plug-ins
description: Overview and how to create Microsoft Dataverse low-code plug-ins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 06/28/2023
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

There are two types of low-code plug-ins:

# [Instant](#tab/instant)

An instant low code plug-in is business logic that's manually triggered. A user must explicitly invoke an instant plug-in. This can be defined on a button click in an app, or within a Power Automate cloud flow using perform an unbound action.

You can define input and output parameters that allow certain values in the formula to change, or be variable. They also give you the ability to pass information between the plug-in and the context that runs it, so the same business logic can be designed generically and reused in varying situations.  
- Input parameters can take information into the formula when it’s run.
- Output parameters let you define information that is returned when the plug-in completes successfully.

Supported data types for input and output parameters:
- Boolean
- String
- Float
- Decimal
- DateTime
- Integer

## Calling instant low-code plug-ins as actions from a canvas app

When an instant low-code plug-in is created, you'll be able to call the plug-in as a Dataverse action inside a canvas app as described in this article: [Call Dataverse actions directly in Power Fx](../canvas-apps/connections/connection-common-data-service.md#call-dataverse-actions-directly-in-power-fx-preview). However, for any subsequent plug-ins created, you'll have to remove and readd the Power Fx environment language object. Then you'll be able to see all the low-code plug-ins as actions.

More information on how to integrate: [Integrate a low-code plug-in](#integrate-a-low-code-plug-in)

# [Automated](#tab/automated)

An automated low code plug-in is business logic that runs when a data event (create, update, or delete) occurs for a specified table. You can also design whether the plug-in runs before or after the data event completes, which allows flexibility to access and modify values in key stages of the event.

---

For the most part, logic that can be defined for an instant plug-in can also be defined for an automated low-code plug-in.

The main difference between the plug-in types is in the way the plug-in type is triggered, and whether parameters can be used. Only instant plug-ins support parameters.

> [!IMPORTANT]
> Currently, only automated plug-ins allow you to interact with a specific record when the plug-in is invoked. This is referred as the *bound* table record. When defining logic for bound records in Power Fx, use the `ThisRecord` keyword to reference the record and use dot notation to access the column values. In the future, instant plug-ins will support bound settings. 

## Plug-in permissions

**Design time**
Makers who have system customizer or system administrator security role membership in the Power Platform environment can access all plug-ins in that environment.

**Run time**
When a plug-in is invoked, it accesses the table data involved in the plug-in definition (the tables that are part of the formula, or if the table is associated with the settings of an automated plug-in) in the context of the user who invoked it.

If a plug-in uses a connector action, the connector permissions enforce the ability for organizational users to access and operate on the plug-in call to the connector. The connection can be shared with one user or can be shared with the entire organization. This allows users to access and operate plug-ins with connectors using a shared connection if desired. By using security roles, plug-ins with connectors access can be restricted to a specific set of users within your organization. You can even specify which roles have create, read, update, or delete privileges in this way.

## Prerequisites for creating a low-code plug-in

- System administrator or system customizer security role membership in the Power Platform environment.
- Install the Dataverse Accelerator solution. [Download and install the Dataverse Accelerator from AppSource](https://aka.ms/dvaccelerator).
    1. Sign in to [AppSource](https://aka.ms/dvaccelerator).
    1. Select **Get it now**.
    1. The **Dynamics 365 apps** page in Power Platform admin center appears.
    1. Select the environment you want.
    1. Review the legal terms and privacy statement to continue.
    1. Select **Install**.

> [!TIP]
> Alternatively, the Dataverse Accelerator can be [installed from the environment apps view](/power-platform/admin/manage-apps#install-an-app-in-the-environment-view).

Once the solution import has completed, the status is set to **Enabled** next to **Dataverse Accelerator** in the [list of licensed applications in the environment](/power-platform/admin/manage-apps#environment-level-view-of-apps).

### Update the Dataverse Accelerator

1. Follow the instructions to [view licensed apps in your environment](/power-platform/admin/manage-apps#environment-level-view-of-apps).
1. If the **Dataverse Accelerator** is already installed and an update is available, it is indicated in the table next to the item.
1. Select **Dataverse Accelerator** and then select **Update** on the command bar.

> [!TIP]
> Enable [auto app updates](/power-platform/developer/isvstudio/auto-update) for the **Microsoft - Power CAT** publisher to automatically receive updates when available.

> [!NOTE]
> If you previously installed the optional Low Code Plugins for Connectors solution, it will be automatically deleted if you update after June 29. The capabilities will be available in the main solution.

## Create an instant low-code plug-in

1. Sign into the environment where the Dataverse Accelerator solution is installed and play the Dataverse Accelerator app.
1. On **Instant plug-ins** card, select **New plug-in**.
   :::image type="content" source="media/low-code-plugin1.png" alt-text="New plug-in Dataverse Accelerator solution":::
1. On the first page of the editor, enter the following information, and then select **Next**.

   - **Display name**. Enter a name for the instant plug-in, such as *Calculate sum*.
   - **Description**. Enter a description for the instant plug-in.

1. Optionally, define your parameters:
   - Select **New input parameter**. For example, **Label:** *X* and **Data type**: *Integer*.
   - Select **New output parameter**. For example, **Label**: *Sum* and **Data type**: *Integer*.
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
1. Test your plug-in. More information: [Test a low-code plug-in](#test-a-low-code-plug-in)

## Create an automated low-code plug-in

1. Sign into the environment where the Dataverse Accelerator solution is installed and play the Dataverse Accelerator app.
1. On the **Automated plugins** card, select **New plugin**.
1. Provide the following values:
   - **Name**: Enter a name for the plug-in, such as *Input validation*.
   - **Table**: Choose a table to associate the plug-in to, such as *Account*.
   - **Run this plugin rule when the row is**. Specify the data event used to trigger the plug-in:
      - **Create**. Triggers the rule during a row create operation.
      - **Update**. Triggers the rule during a row change operation.
      - **Delete**. Triggers the rule during a row delete operation.
1. **Formula**. Enter a Power Fx formula in the ***Formula box**.  
   For example:

   ```powerapps-dot 
   If( IsBlank( ThisRecord.Email ), Patch([@Accounts], ThisRecord, { 'Do not allow Emails': true }))  
   ```

1. **Advanced options** > **When should this run**:
   - **Pre-operation**. Select this option if you want to run your plug-in logic after the form validation, but before the values are inserted or changed in Dataverse.
   - **Post operation**. Select this option to run your plug-in logic after the values have been inserted or changed in Dataverse.
1. Select **Save**.
1. Test your plug-in. More information: [Test a low-code plug-in](#test-a-low-code-plug-in)

## Create a low-code plug-in that uses connectors

The low-code plug-in for connectors solution is a streamlined user interface that makes creating low-code plug-ins for connector actions easier. It supports the creation of plug-ins for stored procedures, which can then be invoked in Power Apps. A wizard is installed as an additional feature of the Dataverse Accelerator, which is used for creating plug-ins with Power Fx formulas.

> [!NOTE]
> Currently, there are a limited number of connectors and actions available.

### Prerequisites for low-code plug-ins with connectors wizard

- All prerequisites described earlier for creating an instant or automated plug-in. More information: [Prerequisites for creating a low-code plug-in](#prerequisites-for-creating-a-low-code-plug-in)
- At least **can use and share** permission to a SQL Server connection (using SQL Server Authentication), or **owner** permission on a SQL Server connection using any other authentication type (e.g, Azure Active Directory).

### Create a low-code plug-in that uses connectors

#### Launch the plug-ins for connectors wizard

1. In [Power Apps](https://make.powerapps.com) go to apps and play the Dataverse Accelerator app.
1. In the Dataverse Accelerator app, on the **Instant Plugins** card select **New plugin**.
1. Name your plug-in and provide a description.
1. Open **Advanced Options**, and then select **Launch the plug-ins wizard**.

#### Configure the connector action

1. In the **plug-in from external data** wizard on the **Connections** screen, you can either select an existing connection if you're already made one or choose to create a new connection:
    - If you want to use an existing connection, select the connection you want.
    - Otherwise, select **New connection** or **Add connection**. You'll be asked for your SQL authentication type, credentials, and other information. Complete the required fields, and then select **Create**.
      When your connection is created, return to the wizard and select **Refresh**, and then select your connection.
1. (Optional) If you select **Next** after selecting the connection, the connection reference is automatically created for the plug-in. However, if you want to provide a custom name, you can do so by expanding **Advanced options** and then select **Manually Configure Connection Reference** to create a connection reference for the plug-in.
    - On the **Connection Reference** page, select or name your connection reference, and then select **Next**.
1. A list of available connector actions are provided. This allows you to pick which action you want to create the plug-in for. Select the action and then select **Next**.
1. In the provided dropdown lists, provide a value for each parameter. As you select values, the dropdown list values for the dependent fields are fetched if more are available, so you should provide values in order (from top to bottom).
1. After providing values for the initial parameters available, a dynamic list of input values might be presented depending on the last parameter. These can either be configured to be input parameters for every invocation, or you can enter a static value to use for every invocation.
   :::image type="content" source="media/lowcode-plug-in-from-connector.png" alt-text="Specify parameters for low-code plug-in for connectors wizard":::

   If dynamic values are returned, they can be configured in two ways:
   - Input parameters, which allow you to change the value every time the plug-in is run. Check the box below the parameter to expose it as an input parameter.
   - Static values, which stay the same every time the plug-in is run. Provide a static value by typing in the text field or make a selection from the dropdown.
   :::image type="content" source="media/lowcode-plug-in-input-param.png" alt-text="Specify input and static values":::

   Once all parameters have values, the Power Fx formula to invoke the procedure is generated. Select **Next**.

1. The **Review** page shows you the plug-in that will be created in Dataverse, and the external connector action you're connecting to in the formula. If everything looks correct, select **Create**.
1. Once the plug-in is created, you're taken directly to your new plug-in where you can view the definition and begin testing it:
   - On the **plug-in** page, the name of the plug-in you have created is displayed. Select **Next**.
   - A list of all of the inputs that will be sent to the connector and their data types is displayed. The Power Fx formula that is used to invoke the stored procedure is also displayed. This is also the screen you'll later use to update the plug-in.
   > [!NOTE]
   > Currently, you can't edit the parameters or formula on this page in the plug-ins wizard.

1. Test your plug-in. More information: [Test a low-code plug-in](#test-a-low-code-plug-in)

### Plug-ins with connectors limitations

- Currently, only the SQL Server **Execute Stored Procedure (V2)** action is available.
- Plug-ins that use connectors will only output results into the external data source. Due to this, you'll need to take additional steps if you need to use the output of stored procedures in Dataverse. In the future, outputs to Dataverse will be supported.
- Once the formula is generated and the input parameters are configured, you can't edit them directly. Currently, instead of making changes to the existing plug-in you must create a new one.
- If a stored procedure runs longer than two minutes, Dataverse and Power Apps (make.powerapps.com) timeout and you won't receive the completion notification. However, you can still directly access the SQL table to get the results though direct connections or virtual tables.
- Currently, there's no application lifecycle management (ALM) support for stored procedure plug-ins. This means they'll have to be re-created when importing solutions between environments.

## Test a low-code plug-in

- Manually test the instant plug-in to verify it behaves as expected.

  1. From the **plug-ins** page, select an instant low-code plug-in from the list, and then select **Test** on the command bar.
  :::image type="content" source="media/low-code-plugin-test.png" alt-text="Test low-code plug-in":::

  1. Provide values for any input parameters that are defined in the low-code plug-in, and then select **Run**.

  Observe the response.
  
  > [!TIP]
  > Use output parameters to help validate expected behavior and results. Otherwise, you will only see a success or failure when testing.

- You can test automated plug-ins by invoking the data event. Observe if the plug-in ran successfully by validating expected changes that were defined in the formula.

### Integrate a low-code plug-in

On the **Integrate** tab of the test page, you can learn how to invoke the instant plug-in from other contexts within Power Platform.

**Invoke an instant plug-in from a canvas app or custom page**
1. Open a new browser tab, and then go to https://make.powerapps.com/.
1.	In the same environment, create a new canvas app from scratch.
1.	Add the **Environment** table from the Dataverse connector as a data source.
1. Copy the formula from the **Integrate** tab.
1. Insert a button and two text input controls. Set the **Format** property of the input controls to **Number**.
   These will be used to provide input into and call the formula. More information: [Button control in Power Apps](../canvas-apps/controls/control-button.md)
1. In the Dataverse Accelerator app, from the **Plug-ins** page, select an instant low-code plug-in from the list, and then select **Test** on the command bar. 
1. Select the **Integrate** tab.
1. Copy the formula from the text area by selecting the copy icon.
1. Paste the formula into the button's `OnSelect` property.
1. Map each input parameter `Value` to reference the app controls, such as `Environment.CalculateSum({ X: TextInput1.Text, Y: TextInput2.Text });`
1. If an output parameter is defined for the low-code plug-in, capture the response using `Set()` or **UpdateContext()**, such as `Set( ActionResult, Environments.CalculateSum({ X: 10, Y: 200 }) );`
1. Add a label control and set the text value to the response captured. For example, set the text value of the label control to the variable `ActionResult`.
1. Play the app and select the button to run the low-code plug-in.

**Invoke an instant plug-in from a Power Automate cloud flow**
1. In a cloud flow, add an action from the Microsoft Dataverse connector.
2. Select the action called **Perform an unbound action**.
3. Select your plug-in (it will have the unique name with a prefix).
4. Provide values for all of the input parameters (if any).

## Contacting Help + support

For issues with the Dataverse Accelerator solution installation or low-code plug-ins, such as errors received, [use the Help + support experience](/power-platform/admin/get-help-support) and include the following information:

- Problem Type- Dataverse Web API and SDK
- Problem Subtype- Accelerator kit for Dataverse

## Example low-code plug-ins you can create

For a few examples of how to create a low-code plug-in, go to [Example Dataverse low-code plug-ins (experimental)](lowcode-plug-ins-examples.md)

## Known limitations

- The environment language object needs to be readded to access new plug-ins inside existing canvas apps. For any plug-ins created after you have added the environment table data source to an existing canvas app, you'll have to remove and readd the Power Fx environment language object. Then you'll see the updated list of plug-ins as actions.
- Application lifecycle management (ALM) isn't currently supported for automated low-code plug-ins. When you import a solution with an automated low-code plugin, the plug-in logic won't be successfully executed in the target environment. However, ALM is supported for instant low-code plug-ins; users can manually add plug-in solution components to an unmanaged solution, and the plug-in will run successfully in the target environment.
- Intellisense requires explicit notation in automated plugins if you want to refer any tables in the formula. Use the following disambiguation syntax such as [@Accounts] (and not Accounts).
- Nested support. Plug-ins can only call first-party actions published by Microsoft from Power Fx expressions. In the future, plug-ins will be able to call other user-defined plug-ins.
- Some `Collect` scenarios require `Patch`. There are some scenarios where `Collect()` doesn't work. The workaround is to use `Patch()` as shown in the populating regarding column example below.
    ```powerapps-dot
    Patch(Faxes,
        Collect(Faxes, { Subject : "Sub1" } ),
        { Regarding : First(Accounts) }
    )
    ```
- Formulas operating on tables with more than 1000 rows will fail at runtime, except if a primary ID is provided as a condition formula, such as `LookUp(Accounts, Account = GUID(AccountID))`, where `AccountID` is an input parameter of type string.

## See also

[Low-code plug-ins Power Fx (preview)](low-code-plug-ins-powerfx.md)

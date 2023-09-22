---
title: Use Dataverse low-code plug-ins
description: Overview and how to create Microsoft Dataverse low-code plug-ins  
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 07/27/2023
ms.custom: template-how-to
---
# Use Dataverse low-code plug-ins (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse offers a powerful solution for achieving more efficient data architecture and reducing client-side workload through low-code plug-ins. These plug-ins are reusable, real-time workflows that execute a specific set of commands within Dataverse, running server-side and triggered by personalized event handlers.

Traditionally, plug-ins were created as custom classes compiled into a .NET Framework assembly, which were then uploaded and registered within Dataverse. However, with the introduction of low-code plug-ins, users can now create these event handlers with minimal or no coding required, and without the need for manual registration.

Low-code plug-ins are stored within a Dataverse database and can be seamlessly integrated into Power Apps and Power Automate. The behavior of the workflow is defined using the Power FX expression language and can directly connect with Dataverse business data and external data sources through Power Platform connectors. With low-code plug-ins, users can rapidly construct complex workflows with minimal coding expertise, resulting in a more streamlined and efficient data architecture.

## Benefits of server-side logic
Defining server-side business logic offers several benefits, including:
1. **Increased security**. Since server-side logic executes on the server, it can help prevent unauthorized access to sensitive data or processes.
2. **Improved performance**. By executing on the server, business logic can reduce the amount of data that needs to be transferred between the client and server, resulting in faster processing times.
3. **Consistency and reliability**. Server-side logic ensures that business rules are consistently applied across all clients, reducing the risk of errors or inconsistencies.
4. **Easier maintenance and upgrades**. By centralizing business logic on the server, it becomes easier to maintain and update, as changes can be made in one place rather than having to update multiple clients.
5. **Scalability**. Server-side logic can be scaled more easily than client-side logic, allowing for better performance and handling of larger workloads.

> [!IMPORTANT]
> - This is a preview feature. Use this if you're an early adopter, see something useful to you, and would like to help test the feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - Experimental features can radically change or completely disappear at any time. For this reason the feature is not enabled by default and you must explicitly opt in to use it.

There are two types of low-code plug-ins:

| Type | Trigger | Supports parameters | Supported [binding types](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api#select-a-binding-type) |
|-|-|-|-|
| Instant | Manually run | Yes | Bound and unbound |
| Automated | Dataverse table event | No | Bound |

All low-code plug-ins have the following properties:
- **Display name** - The human-readable name of the plug-in. It is used to identify the component in the user interface and can be customized to make it more meaningful or descriptive. This must be unique and cannot be changed once created.
- **Name** - The internal name of the plug-in. It is used by the platform to identify the component in code and database operations, and cannot be changed once created.
- **Description** - Used to provide additional context and information about the plug-in, and can be used to document its purpose, behavior, or other important details. The description can be viewed in the user interface and can be helpful for other developers or users who need to understand the plug-in's functionality.
- **Solution** - Used to group plug-ins and related components together in Microsoft Dataverse, and can be exported and imported between different Power Platform environments. Learn more about [solutions](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/solutions-overview).
- **Expression** - This is the custom function that can be used to perform actions or calculations, defined using the Power FX expression language. Power FX is a formula language used in Power Apps canvas apps, and has been extended to be used in low-code plug-ins. See the supported functions and examples.

# [Instant plug-ins](#tab/instant)

An instant low-code plug-in is custom code logic that's manually triggered by a user.

Properties unique to instant plug-ins:
- **Scope** - Used to associate an operation to a specific table. It can be set to either entity or global, where entity scope means the plug-in will be triggered only for a specific entity, and global scope means the operation is not associated with a specific table ([learn more](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api#select-a-binding-type)).
- **Parameters** - Parameters allow you to pass information between the plug-in and the context that runs it, making it easier to design business logic that can be reused in varying situations.  
  - **Input parameters** are used to provide data to the plug-in, and allow you to control how the function behaves by passing in different values you specify in the Power FX formula.
  - **Output parameters** allow you to retrieve the results of a function or method for further use in your program.
 
 Supported parameter data types:
 - Boolean
 - String
 - Float
 - Decimal
 - DateTime
 - Integer
 - Entity Reference

## Manually trigger instant low-code plug-ins
You can call the plug-in as a Dataverse action from a canvas app or in a Power Automate cloud flow, and even directly from the Dataverse Web API. More information on how to integrate: [Integrate a low-code plug-in](#integrate-a-low-code-plug-in)


# [Automated plug-ins](#tab/automated)
An automated low-code plug-in is custom code that is executed during the processing of a specific data event.

Properties unique to automated plug-ins:
- **Data event ('Run this plug-in when the row is')** - Specifies which data event triggers the plug-in. Multiple events can be selected to invoke the plug-in.
- **Stage ('When should this run')** - You can design whether the plug-in runs before or after the data event completes, which allows flexibility to access and modify values in key stages of the event.

Supported data events:
- Create
- Update
- Delete

---

## Plug-in permissions

**Design time**
Makers who have system customizer or system administrator security role membership in the Power Platform environment can access all plug-ins in that environment.

**Run time**
When a plug-in is invoked, it accesses the table data involved in the plug-in definition (the tables that are part of the formula, or if the table is associated with the settings of an automated plug-in) in the context of the user who invoked it.

If a plug-in uses a connector action, the connector permissions enforce the ability for organizational users to access and operate on the plug-in call to the connector. The connection can be shared with one user or can be shared with the entire organization. This allows users to access and operate plug-ins with connectors using a shared connection if desired. By using security roles, plug-ins with connectors access can be restricted to a specific set of users within your organization. You can even specify which roles have create, read, update, or delete privileges in this way.

## Prerequisites for creating a low-code plug-in
- System administrator or system customizer security role membership in the Power Platform environment.
- Access to the Dataverse Accelerator App

> [!TIP]
> All new environments have the Dataverse Accelerator app automatically installed as of October 1st 2023. If you already had the Dataverse Accelerator installed, you can manually update the Dataverse Accelerator.

### Update the Dataverse Accelerator

1. Follow the instructions to [view licensed apps in your environment](/power-platform/admin/manage-apps#environment-level-view-of-apps).
1. If the **Dataverse Accelerator** is already installed and an update is available, it's indicated in the table next to the item.
1. Select **Dataverse Accelerator**, and then select **Update** on the command bar.

> [!TIP]
> Enable [auto app updates](/power-platform/developer/isvstudio/auto-update) for the **Microsoft - Power CAT** publisher to automatically receive updates when available.

> [!NOTE]
> If you previously installed the optional Low Code Plugins for Connectors solution, it will be automatically deleted if you update after June 29, 2023. The capabilities will be available in the main solution.

## Create an instant low-code plug-in

1. Play the Dataverse Accelerator app.
1. Click the **New instant plug-in** card.
   :::image type="content" source="media/low-code-plugin1.png" alt-text="New plug-in Dataverse Accelerator solution":::
1. Provide a **Display name**
2. Optionally, define your parameters:
   - Select **New input parameter** or **New output parameter**, then enter the label and data type.
   - If EntityReference data type is chosen, select a table in the additional combobox that appears.
   - Add more input and output parameters as needed.
1. Enter the Power FX expression in the **Expression** editor.
   - Reference input parameters in the formula by the label name.
   - Output parameters must be returned within curly brackets (e.g., `{ out: "This is returned in an output parameter within brackets" }`
   - Reference Dataverse tables using data collection functions (e.g., [Filter() and LookUp()](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-filter-lookup)).
   - Example: Calculate the sum of two integers. Create two input parameters, X and Y (boty type integer), and one output parameter, `Z` (type string). You could use the following formula: `{Z:  X + Y }`
   - If the scope is set to entity, use `ThisRecord` to access column values in the table row associated with the plug-in run (e.g., `ThisRecord.'Account Name')
   > [!TIP]
   > Note the intellisense in the **Expression** box. Underlined red is invalid. Squiggly yellow means your logic might be affected by delegation limitations. Avoid delegation issues by using [delegable functions]( /power-apps/maker/canvas-apps/delegation-overview#delegable-functions).
   :::image type="content" source="media/low-code-plugin2.png" alt-text="Instance low-code plug-in using Power Fx to derive a sum value with two integers":::
1. Optionally expand **advanced options** to modify the **solution**, **scope**, or **description**.
1. Select **Save**.
1. Test your plug-in. More information: [Test a low-code plug-in](#test-a-low-code-plug-in)

## Create an automated low-code plug-in

1. Play the Dataverse Accelerator app.
1. Click the **New automated plug-in** card.
1. Provide the following values:
   - **Name**: Enter a name for the plug-in, such as *Input validation*.
   - **Table**: Choose a table to associate the plug-in to, such as *Account*.
   - **Run this plugin rule when the row is**. Specify the data event (or combination) that invokes the plug-in.
1. Enter the Power FX expression in the **Expression** editor.
   - Reference Dataverse tables using data collection functions (e.g., [Filter() and LookUp()](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-filter-lookup)).
   - Use `ThisRecord` to access column values in the table row associated with the plug-in run (e.g., `ThisRecord.'Account Name')
1. Optinally expand **advanced options** to modify the stage **When should this run**:
   - **Pre-operation**. Select this option if you want to run your plug-in logic after the form validation, but before the values are inserted or changed in Dataverse.
   - **Post operation**. Select this option to run your plug-in logic after the values have been inserted or changed in Dataverse.
1. Select **Save**.
1. Test your plug-in. More information: [Test a low-code plug-in](#test-a-low-code-plug-in)

## Use Power Platform connectors in low-code plug-ins

> [!NOTE]
> Not all connector actions are supported at this time.

### Prerequisites for using connectors in low-code plug-ins

- [Prerequisites for creating a low-code plug-in](#prerequisites-for-creating-a-low-code-plug-in)
- A connection reference with an active connection. Learn more about [connection references](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference).
- Either **owner** or **can use and share** permission on the connection.

### Using connector actions in low-code plug-ins

1. In both low-code plug-in editors, click the **connection references** button in the top right corner. A pane will expand on the right.
1. A list of available connection references are displayed.
   - Use the search box to filter the list.
   - Only connection references with an assigned connection ID will be listed.
1. Click on the display name link to list the supported connector actions
2. If the connector you need is not listed, create a new connection reference
   1. Click '+ New' in the command bar of the pane.
   1. Fill out the form details and click **Create** ([similar to the solutions portal experience](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference#manually-add-a-connection-reference-to-a-solution-using-solution-explorer)).
   > [!NOTE]
   > In the current release, there are limited connectors available in the in-app form. If you don’t see the connector you want, go to the maker portal and create a new connection reference in an unmanaged solution. You can click the action button that says 'Take me there' in the warning message of the form to jump there.
   1. When the connection reference is created, the list of connector actions will be displayed
1. A list of available connector actions are provided. Select a connector action, then choose an option in the command bar:
   2. **Copy**: Copies the action formula to the clipboard. You can then paste (CRTL+V) the action into the formula editor.
   3. **Learn**: Takes you to the documentation page of the action, which contains the description and parameters of the action.
1.	Once the action formula is pasted into the Power FX expression, use intellisense to provide the correct values for any input parameters (if any are required).
  	> [!TIP]
   > Pasting the action formula might not immediately display the intellisense. Delete and re-type the opening (left) parameter after the action name to trigger the intellisense window.


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

#### Invoke an instant plug-in from a canvas app or custom page
1. In the **Dataverse Accelerator** app:
    1. Select the instant plug-in in the list,
    1. Click the 'copy to clipboard' action in the command bar.
    2. Save the copied formula to a text editor or note pad (somewhere you can easily refer back to)
1. In the [Power Apps maker portal](https://make.powerapps.com/), create or edit a canvas app (or custom page) in the Power Apps studio.
1. In the left navigation, under the **Data Sources** tab, click **+ New data source** and search for the **Environment** option from the Dataverse connector.
1. Insert the following components into the canvas:
    1. Add input controls corresponding to appropriate data type (Text input for text or numbers, toggle for boolean)
    2. If the plug-in scope is bound to a table, add a combobox that is associated with the same table. 
    3. Add a button to call the plug-in. More information: [Button control in Power Apps](../canvas-apps/controls/control-button.md)
1. Paste the plug-in formula you copied into the button's `OnSelect` property.
1. Map each input parameter `Value` to reference the corresponding input controls
    1. If the formula was originally `Environment.CalculateSum({ X: Value, Y: Value });`, it could would be re-written as: `Environment.CalculateSum({ X: TextInput1.Text, Y: TextInput2.Text });`
1. If an output parameter is defined for the low-code plug-in:
    2. capture the response in a `Set()` or `UpdateContext()` formula: `Set( ActionResult, Environments.CalculateSum({ X: TextInput1.Text, Y: TextInput2.Text }) );`
    1. Add a label control and set the text value to the response captured. For example, set the text value of the label control to the variable `ActionResult`.
1. Play the app and click the button to run the low-code plug-in.

Learn more about how to [call Dataverse actions directly in Power Fx](../canvas-apps/connections/connection-common-data-service.md#call-dataverse-actions-directly-in-power-fx-preview).

#### Invoke an instant plug-in from a Power Automate cloud flow
1. In a cloud flow, add a new action from the Microsoft Dataverse connector.
2. Select the action called [Perform an unbound action](https://learn.microsoft.com/connectors/commondataserviceforapps/#perform-an-unbound-action) or [Perform a bound action](https://learn.microsoft.com/connectors/commondataserviceforapps/#perform-a-bound-action).
3. Select your plug-in (it will have the unique name with a prefix).
4. Provide values for all of the input parameters (if any).

#### Invoke an instant plug-in from the Dataverse Web API
Follow the steps for **Unbound action** or **Function bound to table** sections in the [Invoking custom APIs from the Web API documentation](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api#invoking-custom-apis-from-the-web-api) (depending on the appropriate scope of the plug-in).

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
- Some `Collect` scenarios require `Patch`. There are some scenarios where `Collect()` doesn't work. The workaround is to use `Patch()` as shown in the populating regarding column example below. If you're creating an automated plug-in, prepend @ to each table referenced in the Power Fx formula.

    ```powerapps-dot
    Patch(Faxes,
        Collect(Faxes, { Subject : "Sub1" } ),
        { Regarding : First(Accounts) }
    )
    ```
- Formulas operating on tables with more than 1000 rows will fail at runtime, except if a primary ID is provided as a condition formula, such as `LookUp(Accounts, Account = GUID(AccountID))`, where `AccountID` is an input parameter of type string.

## See also

[Low-code plug-ins Power Fx (preview)](low-code-plug-ins-powerfx.md)

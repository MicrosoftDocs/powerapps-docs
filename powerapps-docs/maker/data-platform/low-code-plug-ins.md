---
title:  Streamline app development with low-code plug-ins in Microsoft Dataverse
description: Guide to crafting low-code plug-ins in Microsoft Dataverse
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 11/13/2024
ms.custom: template-how-to
contributors:
- denise-msft
---
# Use low-code plug-ins in Dataverse (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse offers a powerful solution for achieving more efficient data architecture and reducing client-side workload through low-code plug-ins. These plug-ins are reusable, real-time workflows that execute a specific set of commands within Dataverse, running server-side and triggered by personalized event handlers.

> [!IMPORTANT]
>
> - Instant low-code plug-ins are deprioritized and aren't being delivered as a feature. Instant low-code plug-ins are replaced with functions. More information: [Functions in Microsoft Dataverse (preview)](functions-overview.md)
> - This is a preview feature.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Traditionally, plug-ins were created as custom classes compiled into a .NET Framework assembly, which were then uploaded and registered within Dataverse. However, with the introduction of low-code plug-ins, users can create these event handlers with minimal or no coding required, and without the need for manual registration.

Low-code plug-ins are stored within a Dataverse database and can be seamlessly integrated into Power Apps and Power Automate. The behavior of the workflow is defined using the Power Fx expression language and can directly connect with Dataverse business data and external data sources through Power Platform connectors. With low-code plug-ins, makers can rapidly construct complex workflows with minimal coding expertise, resulting in a more streamlined and efficient data architecture.

## Benefits of server-side logic

Defining server-side business logic offers several benefits, including:

- Increased security. Since server-side logic executes on the server, it can help prevent unauthorized access to sensitive data or processes.
- Improved performance. By executing on the server, business logic can reduce the amount of data that needs to be transferred between the client and server, resulting in faster processing times.
- Consistency and reliability. Server-side logic ensures that business rules are consistently applied across all clients, reducing the risk of errors or inconsistencies.
- Easier maintenance and upgrades. By centralizing business logic on the server, it becomes easier to maintain and update, as changes can be made in one place rather than having to update multiple clients.
- Scalability. Server-side logic can be scaled more easily than client-side logic, allowing for better performance and handling of larger workloads.

## Low-code plug-ins

There are two types of low-code plug-ins supported in Dataverse:

| Type | Trigger | Supports parameters | Supported [scope](/power-apps/developer/data-platform/custom-api#select-a-binding-type) |
|-|-|-|-|
| Instant | Manually run | Yes | Global and table |
| Automated | Dataverse table event | No | Table |

All low-code plug-ins have the following common properties:

| Property | Description |
|-|-|
| Display name | The human-readable name of the plug-in. Can't be changed once created. |
| Name | The internal name of the plug-in. It's used by the platform to identify the component in code and database operations. Can't be changed once created. |
| Description | Used to provide additional context about the plug-in (purpose, behavior, or other important details). |
| Solution| Used to group components and export to other environments. Learn more about [solutions](/power-apps/maker/data-platform/solutions-overview). |
| Expression | This is the custom function that can be used to perform actions or calculations, defined using the Power Fx expression language. Power Fx is a formula language used in Power Apps canvas apps, and has been extended to be used in low-code plug-ins. See [supported functions for more details](/power-apps/maker/data-platform/low-code-plug-ins-powerfx).|

# [Instant plug-ins](#tab/instant)

An instant low-code plug-in is custom code logic that's manually triggered by a user. Custom input and output parameters can be used.

Unique properties:

| Property | Description |
|-|-|
| Scope | Used to associate a plug-in to a specific table. It can be set to either table (shown as entity) or global, where table (entity) scope means the plug-in is triggered with the context of a specific table record, and global scope means the operation isn't associated with a table ([learn more](/power-apps/developer/data-platform/custom-api#select-a-binding-type)). |
| Parameters | Parameters allow you to pass information between the plug-in and the context that runs it, making it easier to design business logic that can be reused in varying situations.<br><br>**Input parameters** are used to provide data to the plug-in, and allow you to control how the function behaves by passing in different values you specify in the Power Fx formula.<br><br>**Output parameters** allow you to retrieve the results of a function or method for further use in your program.<br><br>Supported data types:<br><ul><li>Boolean<li>String</li><li>Float</li><li>Decimal</li><li>DateTime</li><li>Integer</li></ul>|

More information about how to integrate from a canvas app or in a Power Automate cloud flow: [Integrate a low-code plug-in](#integrate-a-low-code-plug-in)

# [Automated plug-ins](#tab/automated)
An automated low-code plug-in is custom code that is executed during the processing of a specific data event.

Unique properties:

| Property | Description |
|-|-|
| Data event<br>('Run this plug-in when the row is') | Specifies which data event triggers the plug-in. Any of the following events can be selected to invoke the plug-in:<br><ul><li>Create</li><li>Update</li><li>Delete</li>|
| Stage<br>('When should this run') | You can design whether the plug-in runs before or after the data event completes, which allows flexibility to access and modify values in key stages of the event.<br><br><ul><li>**Pre-operation**. Select this option if you want to run your plug-in logic after the form validation, but before the values are inserted or changed in Dataverse.</li><li>**Post operation**. Select this option to run your plug-in logic after the values have been inserted or changed in Dataverse.</li></ul> |

---

## Plug-in permissions

:::row:::
   :::column span="":::
      **Design time**
      
      Makers who have system customizer or system administrator security role membership in the Power Platform environment can access all plug-ins in that environment. Custom security roles can be used to restrict access to low-code plug-ins.
   :::column-end:::
   :::column span="":::
      **Run time**
      
      When a plug-in is invoked, it accesses the table data involved in the plug-in definition (the tables that are part of the formula, or if the table is associated with the settings of an automated plug-in) in the context of the user who invoked it.
   :::column-end:::
   :::column span="":::
      **Connections**
      
      Using [security roles](/power-platform/admin/security-roles-privileges#security-roles-and-the-new-modern-ui), connector access within plug-ins can be restricted to a specific set of users within your organization. Specify which roles have create, read, update, or delete privileges.
   :::column-end:::
:::row-end:::

## Prerequisites for creating a low-code plug-in

> [!div class="checklist"]
> * System administrator or system customizer security role membership in the Power Platform environment.
> * Access to the Dataverse accelerator app.

> [!TIP]
> All new environments have the Dataverse accelerator app automatically installed as of October 1st 2023. If you already had the Dataverse accelerator installed, you can manually update the Dataverse accelerator.

**Update the Dataverse accelerator**

1. Follow the instructions to [view licensed apps in your environment](/power-platform/admin/manage-apps#environment-level-view-of-apps).
1. If the **Dataverse Accelerator** is already installed and an update is available, it's indicated in the table next to the item.
1. Select **Dataverse Accelerator**, and then select **Update** on the command bar.

> [!TIP]
> Enable [auto app updates](/power-platform/developer/isvstudio/auto-update) for the **Microsoft - Power CAT** publisher to automatically receive updates when available (not necessary for new environments created after October 1st 2023).

> [!NOTE]
> If you previously installed the optional **Low-Code Plug-ins for Connectors** solution, it will be automatically deleted when you update after June 29, 2023. The capabilities will be available in the main solution.

## Create an instant low-code plug-in

1. Play the Dataverse accelerator app.
1. Select the **Create instant plug-in** card.
   :::image type="content" source="media/low-code-plugin-instant-create.png" alt-text="Create instant plug-in card":::
1. Provide a **Display name**.
1. Optionally, define parameters:
   - Select **New input parameter** or **New output parameter**, then enter the label and data type.
   - Add more input and output parameters as needed.
1. Enter the Power Fx expression in the **Expression** editor.
   - Reference input parameters in the formula by the label name.
   - Output parameters must be referenced inside of curly brackets, such as `{ Out: "Return value" }`.
   - Reference Dataverse tables using data collection functions, such as [Filter() and LookUp()](/power-platform/power-fx/reference/function-filter-lookup).
   - If the scope is set to entity, use `ThisRecord` to access column values in the table row associated with the plug-in run, such as `ThisRecord.'Account Name'`.
   > [!TIP]
   > Note the intellisense in the **Expression** box. Underlined red is invalid. Squiggly yellow means your logic might be affected by delegation limitations. Avoid delegation issues by using [delegable functions]( /power-apps/maker/canvas-apps/delegation-overview#delegable-functions).
1. Optionally expand **Advanced options** to modify the **solution**, **scope**, or **description**.
1. Select **Save**.
1. [Test your instant low-code plug-in](#test-a-low-code-plug-in).

**Example**: Calculate the sum of two integers.

- Create two input parameters, `X` and `Y` (both of type integer), and one output parameter, `Z` (type string).
- Use the following formula: `{Z:  X + Y }`

:::image type="content" source="media/low-code-plugin-instant-newform.png" alt-text="Instant plug-in example in Dataverse Accelerator app":::

## Create an automated low-code plug-in

1. Play the Dataverse accelerator app.
1. Select the **Create automated plug-in** card.
   :::image type="content" source="media/low-code-plugin-automated-create.png" alt-text="Create automated plug-in card":::
1. Provide the following values:
   - **Name**: Enter a name for the plug-in, such as *Input validation*.
   - **Table**: Choose a table to associate the plug-in to, such as *Account*.
   - **Run this plug-in rule when the row is**. Specify the data event that invokes the plug-in.
1. Enter the Power Fx expression in the **Expression** editor.
   - Reference Dataverse tables using data collection functions, such as [Filter() and LookUp()](/power-platform/power-fx/reference/function-filter-lookup).
   - Use `ThisRecord` to access column values in the table row associated with the plug-in run, such as `ThisRecord.'Account Name'`.
1. Optionally, expand **Advanced options** to modify the **stage** (when this should run) and the **solution** where the plug-in is saved.
1. Select **Save**.
1. [Test your automated low-code plug-in](#test-a-low-code-plug-in).

## Use Power Platform connectors in low-code plug-ins

Power Platform connectors can be used in low-code plug-ins to easily integrate data and functionality from systems outside of Dataverse, such as SQL Server, Salesforce, and SharePoint, without the need for complex coding or custom development.

### Prerequisites for using connectors in low-code plug-ins

> [!div class="checklist"]
> * [Prerequisites for creating a low-code plug-in](#prerequisites-for-creating-a-low-code-plug-in)
> * [Connection reference](/power-apps/maker/data-platform/create-connection-reference) with an active connection.

### Using connector actions in low-code plug-ins

You can easily use [connectors]( /connectors/connector-reference/connector-reference-powerapps-connectors) and [custom connectors]( /connectors/custom-connectors/) from within a low-code plug-in a Power Fx formula.

1. Create a connection to the connector you want to use.
1. [Add a connection reference](/power-apps/maker/data-platform/create-connection-reference#manually-add-a-connection-reference-to-a-solution-using-solution-explorer) to the connection in the Dataverse environment.
1. In the low-code plug-in Power Fx expression editor, type the name of the connection reference (the internal name with a prefix and underscore, like `new_connectorName`, not the display name).
1. Intellisense shows you the available actions. Select the action you want, and then enter the required parameters.

Before using a connector in a low-code plug-in, review the connector's [documentation](/connectors/connector-reference/connector-reference-powerapps-connectors) to ensure that you're passing the input and output parameters correctly.

More information: [example](lowcode-plug-ins-examples.md#sample-instant-plug-in-with-msn-weather-connector)

> [!NOTE]
> * Not all connector actions are supported at this time.
> * Do not use the Dataverse connector to connect to Dataverse tables from a plug-in expression. Instead, use the native Power Fx functions to interact with collections: [Filter, Search, LookUp](/power-platform/power-fx/reference/function-filter-lookup), [Patch](/power-platform/power-fx/reference/function-patch), [Collect](/power-platform/power-fx/reference/function-clear-collect-clearcollect#collect), and [Set](/power-platform/power-fx/reference/function-set), where columns are treated as global variables.

## Test a low-code plug-in

### Test instant plug-ins

  1. From the **Home screen**, select an instant plug-in from the list, then select **Test** on the command bar. You can also get to this screen from the instant plug-in editor in the command bar after it's been saved.
  :::image type="content" source="media/low-code-plugin-test-home.png" alt-text="Select Test for the low-code plug-in":::

  1. Provide values for any input parameters that are defined in the low-code plug-in, and then select **Run**.
  :::image type="content" source="media/low-code-plugin-test.png" alt-text="Select Run to test low-code plug-in":::

  Observe the response.
  
  > [!TIP]
  > Use output parameters to help validate expected behavior and results. Otherwise, you only see a success or failure when testing.

### Test automated plug-ins

Test automated plug-ins by invoking the data event. Observe if the plug-in ran successfully by validating expected changes that were defined in the formula.
> [!TIP]
> During the preview, you can invoke the associated data event using the table editor in Power Apps:
> 1. Sign into [Power Apps](https://make.powerapps.com), go to **Tables** and select the **Plug-in** table.
> 1. On the command bar, select **Edit**.
> 1. Create, update, or delete rows directly from this view. Alternatively, open a row in the default form by selecting a row, then select **Edit row using form** on the command bar.

### Integrate a low-code plug-in

#### Invoke an instant plug-in from a canvas app or custom page

1. In the **Dataverse Accelerator** app:
    1. Select the instant plug-in in the list.
    1. Select **Copy code snippet** on the command bar.
    :::image type="content" source="media/low-code-plugin-instant-integrate.png" alt-text="Invoke an instance low-code plug-in":::
    1. Paste and save the copied formula to a text editor or notepad (somewhere you can easily refer back to).
1. In [Power Apps](https://make.powerapps.com/):
   1. Create or edit a canvas app (or custom page) in the Power Apps studio.
   1. In the left navigation, under the **Data Sources** tab, select **+ New data source**, and search for the **Environment** option from the Dataverse connector.
   1. Insert the following components into the canvas:
    - Add input controls that correspond with each parameter's data type, such as [Text input](/power-apps/maker/canvas-apps/controls/control-text-input) for text or numbers, [toggle](/power-apps/maker/canvas-apps/controls/control-toggle) for boolean.
    - If the plug-in scope is bound to a table, add a combobox that is associated with the same table so you can choose the input.
    - Add a [button](../canvas-apps/controls/control-button.md) to call the plug-in.
1. Paste the plug-in formula you copied into the button's `OnSelect` property.
1. Map each input parameter `Value` to reference the corresponding input controls:
    - If the formula was `Environment.new_CalculateSum({ X: Value, Y: Value });`, it could be rewritten as: `Environment.new_CalculateSum({ X: TextInput1.Text, Y: TextInput2.Text });`
    - If the formula was bound, replace `Environment` with the table display name to access the plug-in.
1. If an output parameter is defined for the low-code plug-in:
    1. Capture the response in a `Set()` or `UpdateContext()` formula: `Set( ActionResult, Environments.CalculateSum({ X: TextInput1.Text, Y: TextInput2.Text }) );`. Display the variable in a label. Alternatively use the `Notify()` formula to display data in a notification.
1. Play the app and select the command on the command bar to run the low-code plug-in.

Learn more about how you can [call Dataverse actions directly from Power Fx in canvas apps](../canvas-apps/connections/connection-common-data-service.md#call-dataverse-actions-directly-in-power-fx).

#### Invoke an instant plug-in from a Power Automate cloud flow

1. In a cloud flow, add a new action from the Microsoft Dataverse connector.
2. Select the action called [Perform an unbound action](/connectors/commondataserviceforapps/#perform-an-unbound-action) or [Perform a bound action](/connectors/commondataserviceforapps/#perform-a-bound-action).
3. Select your plug-in (it has the unique name with a prefix).
4. Provide values for all of the input parameters (if any).

#### Invoke an instant plug-in from the Dataverse Web API

Follow the steps for **Unbound action** or **Function bound to table** sections in the [Invoking custom APIs from the Web API documentation](/power-apps/developer/data-platform/custom-api#invoking-custom-apis-from-the-web-api) (depending on the appropriate scope of the plug-in).

## Getting help with your low-code plug-ins

If you encounter issues creating or running your low-code plug-in, go to these tips for common issues that can occur: [Microsoft Dataverse low-code plug-ins tips and known issues](low-code-plug-ins-tips.md)

### Contacting Help + support

For issues with the Dataverse Accelerator solution installation or low-code plug-ins not covered in [Microsoft Dataverse low-code plug-ins tips and known issues](low-code-plug-ins-tips.md), such as undocumented errors received, [use the Help + support experience](/power-platform/admin/get-help-support) and include the following information:

- Problem Type- Dataverse Web API and SDK
- Problem Subtype- Accelerator kit for Dataverse

## Example low-code plug-ins you can create

For a few examples of how to create a low-code plug-in, go to [Example Dataverse low-code plug-ins (preview)](lowcode-plug-ins-examples.md)

## Limitations

- The environment language object needs to be readded to access new plug-ins inside existing canvas apps. For any plug-ins created after you have added the environment table data source to an existing canvas app, you have to remove and readd the Power Fx environment language object. Then you see the updated list of plug-ins as actions.
- Intellisense requires explicit notation in automated plug-ins if you want to refer any tables in the formula. Use the following disambiguation syntax such as `[@Accounts]`, using square brackets and the `@` symbol (not `Accounts`).
- Nested support. Plug-ins can only call first-party actions published by Microsoft from Power Fx expressions.
- Some `Collect` scenarios require `Patch`. There are some scenarios where `Collect()` doesn't work. The workaround is to use `Patch()` as shown in the populating regarding column example below. If you're creating an automated plug-in, prepend @ to each table referenced in the Power Fx formula.

    ```power-fx
    Patch(Faxes,
        Collect(Faxes, { Subject : "Sub1" } ),
        { Regarding : First(Accounts) }
    )
    ```
- When low-code plug-ins interact with connectors and DLP is employed, the admin can block creation of connections using DLP. However, existing connection references in the Dataverse environment continue to function. In case the admin needs to block all low-code plug-in interactions with any connectors, they can disable the organization setting `Allowconnectorsonpowerfxactions`. This setting is enabled by default and can be disabled by usual SDK methods (WebAPI, SDK, PowerShell, and so on). You can disable this using a low-code instant plug-in as follows:
   ```power-fx
   Patch(Organizations, First(Organizations), { 'Enable connectors on power fx actions.': 'Enable connectors on power fx actions. (Organizations)'.No })
   ```
- Plug-ins that use connectors can only output results from specific fields. Due to this, you need to map specific primitive values from the connector response to output values.

### Low-code plugins that have custom connectors limitation

If you have low-code plugins with custom connectors, the custom connectors must be imported first, before connection references or flows.

If your environment doesn’t contain the custom connector in a solution, import a separate solution that only includes the custom connector. Do this import before you import the actual solution. You need to do this first because Azure must register the custom connector before the other solution components can be imported.

If you import a solution that contains custom connectors and flows, Azure isn't able to register the custom connector while it's registering your connection references or flows. This also applies to connection references for the custom connector that wasn't previously imported in a separate solution. If Azure didn't register your custom connector, the import fails, or you aren't able to start the import.

More information: [Create custom connectors in solutions: Known limitations](/connectors/custom-connectors/customconnectorssolutions#known-limitations)

## See also

[Low-code plug-ins Power Fx (preview)](low-code-plug-ins-powerfx.md)

[Use a prebuilt prompt in a Dataverse low-code plug-in in Power Apps](/ai-builder/prebuilt-prompts-in-dataverse-plug-in-powerapps)

[Create an automated low-code plug-in with Power Apps (video)](https://youtu.be/hwqVochKJJA?feature=shared)

[Create an instant low-code plug-in with Power Apps (video)](https://youtu.be/2Bj57PiUr0E?feature=shared)

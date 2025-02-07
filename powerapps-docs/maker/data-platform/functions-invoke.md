---
title: "Invoke a function using Power Platform"
description: "Learn how to invoke a function from an app, flow, code, or from another function in Power Apps."
ms.custom: ""
ms.date: 02/07/2025
ms.reviewer: "Mattp123"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "powerapps"
author: "paulliew"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "paulliew"
search.audienceType: 
  - maker
---
# Invoke a function from app, flow, code, or another function (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can invoke functions in Dataverse from a canvas app, a custom page in a model-driven app, a flow, code, or from another function.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Invoke a function from a canvas app or custom page

1. From the **Functions** area in Power Apps (make.powerapps.com), select the function you want to invoke from a canvas app or custom page.
1. Select **Copy code snippet** on the command bar.
1. Paste and save the copied formula to a text editor, Notepad, or somewhere you can easily refer to.
1. In Power Apps Studio:
   1. Create or edit a canvas app or custom page in Power Apps Studio.
   1. On the left navigation pane, under the **Data Sources** tab, select **New data source**, and search for the **Environment** option from the Dataverse connector.
   1. Insert the following components onto the canvas:
      - Add input controls that correspond with each parameter's data type, such as Text input for text or numbers, toggle for boolean.
      - Add a button to call the function.
1. Paste the function formula you copied into the button's **OnSelect** property.
1. Map each input parameter Value to reference the corresponding input controls:
   - If the formula is `Environment.new_CalculateSum({ X: Value, Y: Value });`, it could be rewritten as: `Environment.new_CalculateSum({ X: TextInput1.Text, Y: TextInput2.Text });`.
1. If an output parameter is defined for the function: 
   - Capture the output value using a “.” after the function. If the function is `Func1` and it stored output in “Value” parameter name, use `Environment.Func1().Value` to access the output. Display the variable in a label. Learn more about how you can [call Dataverse actions directly from Power Fx in canvas apps](/power-apps/maker/canvas-apps/connections/connection-common-data-service#call-dataverse-actions-directly-in-power-fx)

## Invoke functions from a Power Automate cloud flow

1. In a cloud flow, add a new action from the Microsoft Dataverse connector.
1. Select either the action called **Perform an unbound action** or the action **Perform a bound action**.
1. Select your function. The function has a unique name with a prefix.
1. Provide values for all the input parameters (if any).

## Invoke functions from the Dataverse Web API

Follow the steps for the unbound action sections in the [Invoking custom APIs from the Web API](/power-apps/developer/data-platform/custom-api#invoking-custom-apis-from-the-web-api) article (depending on the appropriate scope of the plug-in).

## Invoke existing functions from within new functions

To invoke an existing function within a new function, use the syntax: `Environment.ExistingFunction({inputParam1: value1, inputParam2: value2, ... inputParamN: valueN})`

Since the output is always a record, use the dot notation to access the output parameters. For example, if the function "ExistingFunction" has two output parameters defined as out1 and out2, you can access them in either of these two ways:  

- `Environment.ExistingFunction({inputParam1: value1, inputParam2: value2, ... inputParamN: valueN}).out1`
- `Environment.ExistingFunction({inputParam1: value1, inputParam2: value2, ... inputParamN: valueN}).out2`

## Limitations with functions in Dataverse

- The environment language object needs to be re-added to access new functions inside existing canvas apps. For any functions created after you have added the environment table data source to an existing canvas app, you must remove and re-add the Power Fx environment language object. Then you see the updated list of functions as actions.
- Nested support. functions can only call Microsoft actions published by Microsoft from Power Fx expressions.
- Some `Collect` scenarios require `Patch`. There are some scenarios where `Collect()` doesn't work. The workaround is to use `Patch()` as shown in the populating regarding column example here.

```powerappsfl
Patch(Faxes,
       Collect(Faxes, {  Subject : "Sub1" } ),
       { Regarding : First(Accounts) }
    )
```

## Debug and get help with your functions

If you encounter issues creating or running your Function, you can use the trace() function for debugging or go to these tips for common issues that can occur.

### Debugging using the trace() function

1. To debug using the trace function, make sure that you have enabled plug-in and custom workflow activity tracking. 
1. Go to Power Apps (make.powerapps.com), select the **Settings** gear icon on the upper right, and then select **Advance settings**.  
1. Select Settings > Auditing > Global Audit Settings.  
1. On the **Customization** tab, ensure that **Enable logging to plug-in trace log** is enabled for **All**.  

Once you have enabled tracking, you can start using trace() functions to debug Power Fx formulas. Learn more about how to use the trace() function inside a Power Fx expression: [Trace function - Power Platform](/power-platform/power-fx/reference/function-trace).

### Contacting help + support

For issues with functions not covered in Microsoft Dataverse low-code plug-ins tips and known issues, such as undocumented errors received, use the Help + support experience and include the following information:

- Problem Type- Dataverse Web API and SDK.
- Problem Subtype.

## Related articles

[Example functions (preview)](functions-examples.md)

[Create and use functions in Microsoft Dataverse](functions-create.md)
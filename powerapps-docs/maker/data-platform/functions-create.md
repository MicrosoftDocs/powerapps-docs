---
title: "Create and use functions in Microsoft Dataverse"
description: "Learn how to create functions that can be used to execute a specific set of commands within Dataverse."
ms.custom: ""
ms.date: 02/24/2025
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
# Create and use functions in Microsoft Dataverse (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Create and use reusable functions in Microsoft Dataverse. Functions use Power Fx to execute a specific set of commands within Dataverse that run server-side.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

## Prerequisites

System customizer security role membership in the Power Platform environment.

## Create a function in a solution

1. Go to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Solutions** in the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the solution where you want to create a function.
1. On the command bar, select **New** > **Automation** > **Function**. 
1. Enter the following information in the **New function** side panel that appears.
   - Provide a Display name and Description for your function.
   - Select **New input parameter** and/or **New output parameter**, then provide a name and data type for the parameter. Add more input and output parameters as needed.
   - In the **Table references** list you can optionally select tables. You can reference the Dataverse tables you choose using data collection functions, such as **Filter()** and **LookUp()**.
   - Enter the Power Fx expression in **the Formula** box. 
1. Select **Save**.
1. [Test the function](#test-a-function).

Reference input parameters in the formula by their names.

Output parameters must be referenced inside of curly brackets, such as `{ Out: "Return value" }`.

> [!TIP]
>
> - Notice the intellisense in the **Formula** box. Underlined red is invalid. Squiggly yellow means your logic might be affected by delegation limitations. Avoid delegation issues by using delegable functions.
> - Expand Advanced options to review your schema name.

## Example functions

This section provides a few example functions.

### Calculate the sum of two integers

1. Enter a **Display name**, such as **new_calculateSum**, and a **Description**.
1. Add two input parameters, x and y (both of data type integer), and one output parameter, z (data type integer).
1. In the **Formula** box, enter the formula:  
   `{ z:x+y }`

   :::image type="content" source="media/function-example1.png" alt-text="Function that multiplies two numbers." lightbox="media/function-example1.png":::
1. [Test the function](#test-a-function).

### Add a new title to article table

1. Create two input parameters title and url (both with string data types) and one output variable, message (data type string).
1. Select the **Knowledge Federated Articles** table in the **Table references** dropdown.
1. In the **Formula** box, enter the formula:  

```powerappsfl
Collect('Knowledge Federated Articles',  
   { 
    Title: title, 
    URL: url 
    } 
    ); 
{ 
    message: "New Article title added: " & title 
}
```

### Validate if an input string contains the strings of your choice

1. Create an input parameter **DocumentTextInput** (with string data type) and one output variable, named **result** (data type string).
1. In the **Formula** box, enter the formula: 

```powerappsfl
{
    result: If("Confidentiality" in DocumentTextInput && "Dispute Resolution" in DocumentTextInput && "Governing Law" in DocumentTextInput && "Termination" in DocumentTextInput, 

    "Document is compliant.", 
    "Document is missing one or more compliance clauses." 
    ) 
}
```

### Calculate a hotel stay price

1. Create six input parameters: nights, rooms, tax, discount, roomservice, ratepernight (all with string data type) and one output variable, price (data type float).
1. In the **Formula** box, enter the formula:


```powerappsfl
{ 
   price: ((nights*rooms*ratepernight)*(1+(tax/100))*(1-(discount/100)))+roomservice 

}
```

## More function examples

For more example functions, go to [Example functions (preview)](functions-examples.md).

## Edit, test, or delete a function

### Edit a function

1. Select your function in the **Functions** area.
1. Select **Edit** on the command bar.
1. Modify your formula, and then **Save** it.

### Test a function

1. Select the function in the **Functions** area.
1. Select **Test** on the command bar.
1. Provide values for the input parameters that are defined in the function, and then select **Play**.

A successful test returns an OData response that includes information such as the organization URI, function name, and output parameters and values.

:::image type="content" source="media/function-example1-test.png" alt-text="Test a function" lightbox="media/function-example1-test.png":::

> [!TIP]
> Use output parameters to help validate expected behavior and results. Otherwise, you only observe success or failure when testing.

### Delete a function

> [!IMPORTANT]
> During the preview, don't delete your functions from the **Solutions** area as it might result in orphan components. Functions should be deleted by going to Power App (make.powerapps.com) > **Functions** on the left navigation pane. 

1. Select **Functions** on the left navigation pane, and then select your function. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Delete** on the command bar.

## Related articles

[Functions in Microsoft Dataverse (preview)](functions-overview.md)

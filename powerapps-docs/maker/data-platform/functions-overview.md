---
title: "Functions in Microsoft Dataverse"
description: "Learn how reusable functions can be used to execute a specific set of commands within Dataverse"
ms.custom: ""
ms.date: 02/03/2025
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
# Functions in Microsoft Dataverse (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse offers a powerful solution for achieving more efficient data architecture and reducing client-side workload through functions (formerly known as instant low-code plug-ins). Functions in Dataverse use [Power Fx](/power-platform/power-fx/overview) to create your business logic. Power Fx is a general-purpose, strong-typed, declarative, and functional programming language. Whereas functions in Dataverse are reusable solution objects, which execute a specific set of commands within Dataverse, running server-side.

> [!IMPORTANT]
>
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Traditionally, functions were created using plug-ins. These plug-ins were created as custom classes compiled into a .NET Framework assembly, which were then uploaded and registered within Dataverse. However, now with the introduction of functions, users can create them with minimal or no coding required, and without the need for manual registration.

Functions are stored within a Dataverse database and can be seamlessly integrated into Power Apps and Power Automate. The behavior of the workflow is defined using the Power Fx expression language and can directly connect with Dataverse business data and external data sources through Power Platform connectors. With functions, makers can rapidly construct complex logic with minimal coding expertise.

## Benefits of creating server-side logic

Defining server-side business logic offers several benefits, including: 

- Increased security. Since server-side logic executes on the server, it can help prevent unauthorized access to sensitive data or processes.
- Improved performance. When executed on the server, business logic can reduce the amount of data that needs to be transferred between the client and server, resulting in faster processing times.
- Consistency and reliability. Server-side logic ensures that business rules are consistently applied across all clients, reducing the risk of errors or inconsistencies.
- Easier maintenance and upgrades. By centralizing business logic on the server, it becomes easier to maintain and update, as changes can be made in one place rather than having to update multiple clients.
- Scalability. Server-side logic can be scaled more easily than client-side logic, allowing for better performance and handling of larger workloads.

## Functions overview

Functions in Dataverse use Power Fx. Power Fx is the low-code language that is used across Microsoft Power Platform. It's a general-purpose, strong-typed, declarative, and functional programming language used in Power Apps canvas apps as well as areas in model-driven apps, such as custom pages and commanding.

Functions offer these benefits:

- Can use parameters.
- Can manually run with trigger.
- Can support either global or table scope.

Functions have these general properties.

| Property      | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| Display name  | The human-readable name of the function. Can't be changed once created.                           |
| Name          | The internal name of the function. It's used by the platform to identify the component in code and database operations. Can't be changed once created. |
| Description   | Used to provide additional context about the function, such as purpose, behavior, and so on. Can't be changed once created. |
| Solution      | Used to group components and export to other environments. [Learn more about solutions](solutions-overview.md).            |
| Expression    | This is the custom function that can be used to perform actions or calculations, defined using the Power Fx expression language. Go to [Supported functions](functions-supported-power-fx.md) for more details.  |

A function is custom code logic that's manually invoked by a user. Custom input and output parameters can be used with these unique properties.

|Property  |Column2  |
|---------|---------|
|Table Reference   |  Used to associate Functions to specific tables. You can select up to five tables to read or write from in your function’s formula.   |
|Parameters   |  Parameters allow you to pass information between the function and the context that runs it, making it easier to design business logic that can be reused in varying situations. Input parameters are used to provide data to the function, and allow you to control how the function behaves by passing in different values you specify in the Power Fx formula. Output parameters allow you to retrieve the results of a function for further use in your program. More information: [Supported data types for input and output parameters](#supported-data-types-for-input-and-output-parameters)      |

### Supported data types for input and output parameters

- Boolean
- String
- Float
- Decimal
- DateTime
- Integer

For more information about how to integrate from a canvas app or in a Power Automate cloud flow, go to [Invoke a function from a canvas app or custom page](functions-invoke.md#invoke-a-function-from-a-canvas-app-or-custom-page).

## Functions permissions

| How run  | Description  |
|---------|---------|
|Design time     |   Makers who have system customizer security role membership or higher level role in the Power Platform environment can access all functions in that environment. Custom security roles can be used to restrict access to functions.       |
|Run time     | When a function is invoked, it accesses the table data involved in the function definition, which includes the tables that are part of the formula in the context of the user who invoked it.     |

## Related content

[Learning path: Work with Power Fx functions](/training/paths/work-powerfx-functions/?WT.mc_id=power-169350)

[Create and use functions in Microsoft Dataverse (preview)](functions-create.md)

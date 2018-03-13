---
title: Apply Business Logic with code | Microsoft Docs
description: Learn how developers can use code to apply business logic in the Common Data Service for Apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/26/2018
ms.author: jdaly
---
# Apply Business Logic with code

Whenever possible, you should first look to applying one of several declarative process options when a requirement involves defining business logic. See [Customization Guide: Create custom business logic through processes](/dynamics365/customer-engagement/customize/guide-staff-through-common-tasks-processes)

When a declarative process doesn’t meet a requirement, as a developer you have several options. This topic will introduce common options to write code.

## Create a workflow extension

You can write a .NET assembly to provide new options within the process designer. This method provides a new option for people using the workflow designer to apply a condition or perform a new action. A workflow extension can then be re-used by people who are not developers to apply the logic in your code.

More information: [Developer Guide: Custom workflow activities (workflow assemblies)](/dynamics365/customer-engagement/developer/custom-workflow-activities-workflow-assemblies)

## Create a plug-in

You can write a .NET assembly to plug-in to the data transaction flow to apply business logic on the server. With the Common Data Service for Apps platform there is a framework that allows you to register specific events to execute code defined within a class in an assembly. That class inherits a specific interface that exposes an [Execute method](/dotnet/api/microsoft.xrm.sdk.iplugin.execute). When the registered event occurs, the `Execute` method on the class is invoked and passed contextual data about the event.

You will use the *Plug-in Registration Tool* to register your assemblies.

Within the `Execute` method, you can use the object model defined within the SDK Assemblies to evaluate the contextual event data and perform appropriate actions to do the following:
- Determine whether to cancel the operation by throwing an error
- Make changes to the contextual data passed to the Execute method
- Perform additional operations to automate processes using the Organization Service.

### Synchronous and asynchronous plug-ins
Plug-ins can be registered to execute synchronously within the transaction or to be deferred and sent to a queue that will apply the logic at a time that will have less impact on the server. For this reason, asynchronous plug-ins are preferred.

When you register the plugin to run synchronously for an event, you have options about when the code should run. There are three stages:

|Event  |Description  |
|---------|---------|
|Pre-validation|Occurs before the database transaction begins. This is a good place to apply business logic to determine whether the operation should be cancelled before the transaction begins to avoid the performance penalty of rolling back the transaction.|
|Pre-operation|Occurs after the database transaction has started. Cancelling an operation at this stage must roll back the transaction|
|Post-operation|Occurs within the database transaction after the main data operation is completed. Includes any changes which may have been applied in earlier events but incurs an even larger penalty when cancelling the operation.|

> [!NOTE]
> Synchronous plug-ins have constraints on the amount of system resources they can use. If a plug-in exceeds thresholds or becomes unresponsive an exception will be thrown cancelling the operation.

More information: [Developer Guide: Write plug-ins to extend business processes](/dynamics365/customer-engagement/developer/write-plugin-extend-business-processes)

## Create a form or grid event handler

> [!NOTE]
> Before you create event handlers, consider if Business Rules can be applied to meet your requirements. More information: [Customization Guide: Create business rules and recommendations to apply logic in a form](/dynamics365/customer-engagement/customize/create-business-rules-recommendations-apply-logic-form)

Within the form designer there are properties to associate JavaScript web resource libraries to the form and then to associate specific functions in those libraries to events that occur.

There is a complete set of client APIs you can use to interact with data and visual elements in the form or grid. There are also API to interact with data on the server using the Web API.

Client scripting is powerful because it allows you to provide the most responsive interaction with the user in the form. It is popular because many developers know JavaScript. But it is important to use it appropriately. Scripts should compliment business rule enforced on the server rather than replace them. Logic applied via a script in the model-driven app will not be applied to data entered via a canvas app or any other means where data can be modified. Performance can be impacted as more scripts are added.

> [!IMPORTANT]
> Interacting directly with the DOM of the page or any undocumented APIs is not supported. The DOM generated for the page may change with different implementations over time. Undocumented APIs may change or be removed without notice. Any of these kinds of changes will cause your script to break.
More information: [Developer Guide: Client scripting in Customer Engagement using JavaScript](/dynamics365/customer-engagement/developer/clientapi/client-scripting)

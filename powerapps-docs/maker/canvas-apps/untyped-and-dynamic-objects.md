---
title: Working with dynamic values
description: How to work with dynamic values.
author: lancedMicrosoft
ms.topic: overview
ms.custom: canvas
ms.collection: get-started
ms.reviewer: mkaur
ms.date: 03/2/2023
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
---
# Working with dynamic values 

When dealing with actions in Power Apps, it's possible to encounter dynamic return values or input values for some actions. Before, Power Apps would ignore dynamic input fields, and they wouldn't be visible in Power Fx expressions but now you can work directly with these fields. Before, when a return type was dynamic, Power Apps would return a Boolean value. Now, it returns a Dynamic valueinstead.

> [!NOTE]
> Suppose your Power Fx expressions rely on a Boolean return value from these functions. In that case, you'll have to rewrite the formula and explicitly cast the dynamic value to a Boolean. Certain functions, such as 'IfError,' don't fully support dynamic values yet. If your expression contains such a function, refer to the note at the end of this article for workarounds.


## Passing in dynamic values as parameters

Certain actions necessitate using a dynamic value as a parameter. If you have a Power Fx record, you can convert it to a dynamic value, making it suitable for passing to the action.

In the example below, the merge action available on a Dataverse **Account** table requires several dynamic arguments. To prepare, we'll define three variables to hold the TargetObject, SubordinateObject, and UpdateContextObject. We'll begin by assigning the text string **Microsoft.Dynamics.CRM.account** to a variable, which will be reuse throughout the example.

```power-fx
Set (OdataType, “Microsoft.Dynamics.CRM.account”);
```

Then TargetObject is assigned a Power Fx record with the properties of name, accountid, and @odata.type. We similarly assign Power Fx records to the Subordinate and UpdateContext objects as well.
```power-fx
Set (TargetObject, {name: "Test 2", accountid: "145dc2ba-85a2-ed11-aado-0022482d76a5", '@odata.type': OdataType});
Set (SubordinateObject, {name: FirstRecord.’Account name’, accountid: FirstRecord.Account, ‘@odata.type’ : OdataType });
Set (UpdateContextObject, {telephone1: FirstRecord.’Main Phone’, address1_city: FirstRecord.’Address 1 : City’, ‘@odata.type’ : OdataType }); 
```

Next, we'll create three more variables to store the dynamic records after the conversion: TargetDynamicValue, SubordinateDynamicValue, and UpdateContextDynamicValue. To perform the conversion, we'll use the ParseJSON(JSON()) function on the original variables. This action will transform the Power Fx records into dynamic values.

```power-fx
Set (TargetDynamicValue, ParseJSON(JSON(TargetObject)));
Set (SubordinateDynamicValue, ParseJSON(JSON(SubordinateObject)));
Set (UpdateContextDynamicValue, ParseJSON(JSON(UpdateContextObject)));
```
Lastly, we call the merge action by passing in the necessary parameters, including for both dynamic and specific types:

```power-fx
Environment.Merge({Target: TargetDynamicValue, Subordinate: SubordinateDynamicValue, UpdateContent: UpdateContextDynamicValue, PerformParentingChecks: false  });
```
## Using dynamic values returned via an action

If an **Action** based connector returns an object, its properties can be accessed directly, regardless of whether they've been assigned a type. However, if you intend to use a property for a specific purpose in Power Apps, such as for labeling, you'll need to cast it first.

In the following example, the httpRequest function returns a dynamic value that has been previously cast as a Boolean.

```power-fx
Set (response, Office365Groups.HttpRequest("/v1.0/me", "GET", ""));
```
One of the properties in the response is displayName. It can be accessed, and cast, with a Power Fx expression like the following:
```power-fx
Text(response.displayName)
```
Cast to the object **Text** to use it in a Power Apps label control. 

## Working with Dynamic fields

Action responses now capture dynamic output, and you can utilize the method described above to access these properties. Additionally, working with dynamic input fields is also possible.

Consider the 'GetMessageDetails' action in Microsoft Teams that has a dynamic input body parameter. Previously, this parameter could not be viewed or specified. With the recent update, you can set a variable called 'body' with the appropriate Power Fx record structure. 

```power-fx
Set ( body, ParseJSON(JSON( {recipient: { groupID: “7f733b36-7c7f-4f4c-9699-0a7b7a2b3897”, channelID: “19: 085d522328fb4a439220641006f7f25@thread.tacv2”}})));
```
Then, we can call the GetMessageDetails action and assign the response to the teamsResponse variable.
```power-fx
Set (teamsResponse, MicrosoftTeams.GetMessageDetails ( 1661365068558, “channel”, body ));
```
## Converting formulas that return dynamic values that previously returned Boolean.  

Power Fx takes a limited number of dynamic values so explicit conversion may be necessary for your formula. In particular, if your formula depends on a Boolean response then you will need to convert. If you need to simply know if an error exists, you can use the IsError function:

```power-fx
If(
  IsError(Office365Outlook.CalendarDeleteItemV2("Calendar", 1)),
  Notify("An Outlook appointment could not be found or could not be deleted")
)
```
To access error information that is exclusively available through IfError, you must transform the dynamic value into a specific type using a conversion function such as Boolean, Text, or Value. These functions will produce an error if they are given one. The following example, illustrates this:

```power-fx
With({result: Office365Outlook.CalendarDeleteItemV2("Calendar", 1)},
If( IsError(result),
  IfError(
    Boolean(result),  // any conversion function would do, such as Text, Value, …
    Notify("An Outlook appointment could not be found or could not be deleted: " & FirstError.Message)
) ) )
```


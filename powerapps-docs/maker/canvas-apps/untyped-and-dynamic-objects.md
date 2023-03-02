---
title: Working with untyped and dynamic objects 
description: Working with untyped and dynamic objects .
author: lancedMicrosoft
ms.topic: overview
ms.custom: 
  - canvas
  - intro-internal
ms.reviewer: mkaur
ms.date: 03/1/2023
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - lancedMicrosoft
  - mduelae
  - alaug
---
# Working with untyped and dynamic objects 

When working with actions the return value or input value of some actions may be untyped. Previously Power Apps would ignore untyped or dynamic input fields. They would simply not show up in PowerFX expressions. Now you can work directly with them. Additionally, Power Apps would return Boolean if a return type was untyped. Now we return an untyped object. 

> [!NOTE]
> If your Power Fx expressions depend on a Boolean return value from one of these functions, you will need to rewrite the formula to parse the untyped object and explicitly cast it to a Boolean.  For instance, ‘IfError’ of an untyped object is not yet fully supported.  If you have an expression like this please see the note at the bottom of this article on work-arounds.

## Passing in untyped objects as parameters
Some actions require an untyped object as a parameter value. If you have a Power Fx record, you can convert it to an untyped object so that it can be passed to the action.
The example below uses the merge action that is available on a Dataverse Account table.  This action requires several untyped arguments. 
We will first set up three variables to hold the TargetObject, SubordinateObject, and the UpdateContextObject.  
First we assign the text string “Microsoft.Dynamics.CRM.account” to a variable – which we will use in several places.

```powerapps-dot
Set (OdataType, “Microsoft.Dynamics.CRM.account”);
```

Then TargetObject is assigned a Power Fx record with the properties of name, accountid, and @odata.type. We similarly assign Power Fx records to the Subordinate and UpdateContext objects as well.
```powerapps-dot
Set (TargetObject, {name: "Test 2", accountid: "145dc2ba-85a2-ed11-aado-0022482d76a5", '@odata.type': OdataType});
Set (SubordinateObject, {name: FirstRecord.’Account name’, accountid: FirstRecord.Account, ‘@odata.type’ : OdataType });
Set (UpdateContextObject, {telephone1: FirstRecord.’Main Phone’, address1_city: FirstRecord.’Address 1 : City’, ‘@odata.type’ : OdataType }); 
```

Next we will create three more variables to hold the untyped records after conversion : TargetUntypedObject, SubordinateUntypedObject, and UpdateContextUntypedObject.  We use ParseJSON(JSON()) on the original variables to convert them to untyped objects. 
```powerapps-dot
Set (TargetUntypedObject, ParseJSON(JSON(TargetObject)));
Set (SubordinateUntypedObject, ParseJSON(JSON(SubordinateObject)));
Set (UpdateContextUntypedObject, ParseJSON(JSON(UpdateContextObject)));
```
Finally we call the merge action by passing in the required parameters (both untyped and typed):
```powerapps-dot
Environment.Merge({Target: TargetUntypedObject, Subordinate: SubordinateUntypedObject, UpdateContent: UpdateContextUntypedObject, PerformParentingChecks: false  });
```
## Using untyped object returned via an action
When a Action based connector returns an object, you can directly access the object's properties even if the values are untyped. To use such a property however, you will need to first cast it for specific use in Power Apps such as label. 
For instance, in the example below, the httpRequest returns an untyped object (which previously was cast to Boolean.) 
```powerapps-dot
Set (response, Office365Groups.HttpRequest("/v1.0/me", "GET", ""))```;

One of the properties in the response is displayName. It can be accessed, and cast, with a Power Fx expression like the following:
```powerapps-dot
Text(response.displayName)
```
Cast to the object Text to use it in a Power Apps label control. 
## Working with Dynamic fields
Dynamic output is now captured in action responses and you can access those properties using the method described above.  You can also work with dynamic input fields. 
In the example below, the Microsoft Teams ‘GetMessageDetails’ action has a dynamic input body argument.  Previously you would not have been able to see or specify this argument.  Now, however, you can.  Again, we set a variable ‘body’ to have the appropriate Power Fx record structure. 
```powerapps-dot
Set ( body, ParseJSON(JSON( {recipient: { groupID: “7f733b36-7c7f-4f4c-9699-0a7b7a2b3897”, channelID: “19: 085d522328fb4a439220641006f7f25@thread.tacv2”}}));
```
Then, we can call the GetMessageDetails action and assign the response to the teamsResponse variable.
```powerapps-dot
Set (teamsResponse, MicrosoftTeams.GetMessageDetails ( 1661365068558, “channel”, body ));
```
## Converting formulas that return untyped objects that previously returned Boolean.  
Power Fx takes a limited number of untyped objects so explicit conversion may be necessary for your formula.  In particular if your formula depends on a Boolean response then you will need to convert.  If you need to simply know if an error exists, you can use the IsError function:

```powerapps-dot
If(
  IsError(Office365Outlook.CalendarDeleteItemV2("Calendar", 1)),
  Notify("An Outlook appointment could not be found or could not be deleted")
)
```
On the other hand, if you need error information (which is only exposed in IfError), then you need to convert the untyped object into some other valid type.  You can do this with any conversion function (Boolean, Text, Value, …).  Conversion functions will return an error if one is given to them. Below is an example for this case: 
```powerapps-dot
With({result: Office365Outlook.CalendarDeleteItemV2("Calendar", 1)},
If( IsError(result),
  IfError(
    Boolean(result),  // any conversion function would do, such as Text, Value, …
    Notify("An Outlook appointment could not be found or could not be deleted: " & FirstError.Message)
) ) )
```


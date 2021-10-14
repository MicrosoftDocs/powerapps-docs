---
title: "Use Web API actions (Microsoft Dataverse)| Microsoft Docs"
description: "Actions are reusable operations that can be performed using the Web API. These are used with a POST request to modify data on Microsoft Dataverse"
ms.custom: ""
ms.date: 05/04/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 53eafd67-385a-485b-9022-5127df08ea2f
caps.latest.revision: 14
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Use Web API actions

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Actions and functions represent re-usable operations you can perform using the Web API. Use a POST request with actions listed in <xref:Microsoft.Dynamics.CRM.ActionIndex> to perform operations that have side effects. You can also define custom actions and they’ll be available for you to use.

<a name="bkmk_unboundActions"></a>

## Unbound actions

Actions are defined in [CSDL metadata document](web-api-types-operations.md#bkmk_csdl). As an example, the following is the definition of the <xref href="Microsoft.Dynamics.CRM.WinOpportunity?text=WinOpportunity Action" /> represented in the metadata document.

```xml
<Action Name="WinOpportunity">
  <Parameter Name="OpportunityClose" Type="mscrm.opportunityclose" Nullable="false" />
  <Parameter Name="Status" Type="Edm.Int32" Nullable="false" />
</Action>
```

The <xref href="Microsoft.Dynamics.CRM.WinOpportunity?text=WinOpportunity Action" /> corresponds to the <xref:Microsoft.Crm.Sdk.Messages.WinOpportunityRequest> using the organization service. Use this action to set the state of an opportunity to Won and create an <xref href="Microsoft.Dynamics.CRM.opportunityclose?text=opportunityclose EntityType" /> to record the event. This action doesn’t include a return value. If it succeeds, the operation is complete.

The `OpportunityClose` parameter requires a JSON representation of the opportunityclose entity to create in the operation. This entity must be related to the opportunity issuing the opportunityid single-valued navigation property. In the JSON this is set using the `@odata.bind` annotation as explained in [Associate tables on create](create-entity-web-api.md#bkmk_associateOnCreate).

The `Status` parameter must be set to the status to for the opportunity when it is closed. You can find the default value for this in the <xref href="Microsoft.Dynamics.CRM.opportunity?text=opportunity EntityType" /> statuscode property. The **Won** option has a value of 3. You may ask yourself, why is it necessary to set this value when there is only one status reason option that represents **Won**? The reason is because you may define custom status options to represent a win, such as **Big Win** or **Small Win**, so the value could potentially be different from 3 in that situation.

The following example is the HTTP request and response to call the `WinOpportunity` action for an opportunity with an opportunityid value of `b3828ac8-917a-e511-80d2-00155d2a68d2`.

 **Request**

```http
POST [Organization URI]/api/data/v9.0/WinOpportunity HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
 "Status": 3,
 "OpportunityClose": {
  "subject": "Won Opportunity",
  "opportunityid@odata.bind": "[Organization URI]/api/data/v9.0/opportunities(b3828ac8-917a-e511-80d2-00155d2a68d2)"
 }
}

```

 **Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

<a name="bkmk_boundActions"></a>

## Bound actions

There are two ways that an action can be bound. The most common way is for the action to be bound by an entity. Less frequently, it can also be bound to an entity collection.

In the [CSDL metadata document](web-api-types-operations.md#bkmk_csdl), when an `Action` element represents a bound action, it has an `IsBound` attribute with the value `true`. The first `Parameter` element defined within the action represents the entity that the operation is bound to. When the `Type` attribute of the parameter is a collection, the operation is bound to a collection of entities.

When invoking a bound function, you must include the full name of the function including the `Microsoft.Dynamics.CRM` namespace. If you do not include the full name, you will get the following error: `Status Code:400 Request message has unresolved parameters`.

### Actions bound to a table

As an example of an action bound to an entity, the following is the definition of the <xref href="Microsoft.Dynamics.CRM.AddToQueue?text=AddToQueue Action" /> represented in the CSDL:

```xml
 <ComplexType Name="AddToQueueResponse">
 <Property Name="QueueItemId" Type="Edm.Guid" Nullable="false" />
 </ComplexType>
 <Action Name="AddToQueue" IsBound="true">
  <Parameter Name="entity" Type="mscrm.queue" Nullable="false" />
  <Parameter Name="Target" Type="mscrm.crmbaseentity" Nullable="false" />
  <Parameter Name="SourceQueue" Type="mscrm.queue" />
  <Parameter Name="QueueItemProperties" Type="mscrm.queueitem" />
  <ReturnType Type="mscrm.AddToQueueResponse" Nullable="false" />
</Action>
```

This entity bound action is equivalent to the <xref:Microsoft.Crm.Sdk.Messages.AddToQueueRequest> used by the organization service. In the Web API this action is bound to the <xref href="Microsoft.Dynamics.CRM.queue?text=queue EntityType" /> that represents the <xref:Microsoft.Crm.Sdk.Messages.AddToQueueRequest>.<xref:Microsoft.Crm.Sdk.Messages.AddToQueueRequest.DestinationQueueId> property. This action accepts several additional parameters and returns a <xref href="Microsoft.Dynamics.CRM.AddToQueueResponse?text=AddToQueueResponse ComplexType" /> corresponding to the <xref:Microsoft.Crm.Sdk.Messages.AddToQueueResponse> returned by the organization service. When an action returns a complex type, the definition of the complex type will appear directly above the action in the CSDL.

An action bound to an entity must be invoked using a URI to set the first parameter value. You cannot set it as a named parameter value.

The following example shows using the <xref href="Microsoft.Dynamics.CRM.AddToQueue?text=AddToQueue Action" /> to add a letter to a queue. Because the type of the `Target` parameter type is not specific (`mscrm.crmbaseentity`), you must explicitly declare type of the object using the `@odata.type` property value of the full name of the entity, including the `Microsoft.Dynamics.CRM` namespace. In this case, `Microsoft.Dynamics.CRM.letter`. More information: [Specify entity parameter type](#bkmk_specifyentityparametertype)

 **Request**

```http
POST [Organization URI]/api/data/v9.0/queues(56ae8258-4878-e511-80d4-00155d2a68d1)/Microsoft.Dynamics.CRM.AddToQueue HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
 "Target": {
  "activityid": "59ae8258-4878-e511-80d4-00155d2a68d1",
  "@odata.type": "Microsoft.Dynamics.CRM.letter"
 }
}
```

 **Response**

```http

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
 "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.AddToQueueResponse",
 "QueueItemId": "5aae8258-4878-e511-80d4-00155d2a68d1"
}
```

### Actions bound to a table collection

It is less common to find actions bound to an entity collection. The following are some you may find:

|&nbsp; |&nbsp;|&nbsp;|
|-|-|-|  
|<xref:Microsoft.Dynamics.CRM.CreateException?text=CreateException Action/>|<xref:Microsoft.Dynamics.CRM.DeliverIncomingEmail?text=DeliverIncomingEmail Action/>|<xref:Microsoft.Dynamics.CRM.ExportTranslation?text=ExportTranslation Action/>|  
|<xref:Microsoft.Dynamics.CRM.FulfillSalesOrder?text=FulfillSalesOrder Action/>|<xref:Microsoft.Dynamics.CRM.ValidateSavedQuery?text=ValidateSavedQuery Action >||

As an example of an action bound to an entity collection, the following is the definition of the <xref href="Microsoft.Dynamics.CRM.ExportTranslation?text=ExportTranslation Action" /> represented in the CSDL:

```xml
<ComplexType Name="ExportTranslationResponse">
	<Property Name="ExportTranslationFile" Type="Edm.Binary" />
</ComplexType>
<Action Name="ExportTranslation" IsBound="true">
	<Parameter Name="entityset" Type="Collection(mscrm.solution)" Nullable="false" />
	<Parameter Name="SolutionName" Type="Edm.String" Nullable="false" Unicode="false" />
	<ReturnType Type="mscrm.ExportTranslationResponse" Nullable="false" />
</Action>
```

This entity collection bound action is equivalent to the <xref:Microsoft.Crm.Sdk.Messages.ExportTranslationRequest> used by the organization service. In the Web API this action is bound to the <xref href="Microsoft.Dynamics.CRM.solution?text=solution EntityType" />. But rather than passing a value to the request, the entity collection binding simply applies the constraint that the URI of the request must include the path to the specified entity set.

The following example shows using the <xref href="Microsoft.Dynamics.CRM.ExportTranslation?text=ExportTranslation Action" /> which exports a binary file containing data about localizable string values which can be updated to modify or add localizable values. Note how the entity collection bound action is preceded by the entity set name for the solution entity: `solutions`.

 **Request**

```http
POST [Organization URI]/api/data/v9.1/solutions/Microsoft.Dynamics.CRM.ExportTranslation HTTP/1.1
Accept: application/json
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0

{
    "SolutionName":"MySolution"
}
```

 **Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.ExportTranslationResponse",
    "ExportTranslationFile": "[Binary data Removed for brevity]"
}
```

<a name="bkmk_customActions"></a>

## Use a custom action

<!-- TODO: 
If you define custom actions for your organization or solution these will also be included in the [CSDL metadata document](web-api-types-operations.md#bkmk_csdl). For information about creating actions using the customization tools in the application, see the TechNet topic [Actions](/dynamics365/customer-engagement/customize/actions). For information about creating and using your own custom actions, see [Create your own actions](../create-own-actions.md). -->

Regardless of whether the operations included in your custom action have side effects, they can potentially modify data and therefore are considered actions rather than functions. There is no way to create a custom function.

### Custom action example: Add a note to a contact

 Let’s say that you want to create a custom action that will add a new note to a specific contact. You can create a custom action bound to the contact entity with the following properties.

|UI Label|Value|
|--------------|-----------|
|**Process Name**|AddNoteToContact|
|**Unique Name**|new_AddNoteToContact|
|**Entity**|Contact|
|**Category**|Action|

 **Process Arguments**

|Name|Type|Required|Direction|
|----------|----------|--------------|---------------|
|NoteTitle|String|Required|Input|
|NoteText|String|Required|Input|
|NoteReference|EntityReference|Required|Output|

 **Steps**

|Name|Step Type|Description|
|----------|---------------|-----------------|
|Create the note|Create Record|Title = {NoteTitle(Arguments)}<br /> Note Body = {NoteText(Arguments)}<br /> Regarding = {Contact{Contact}}|
|Return a reference to the note|Assign Value|NoteReference Value = {Note(Create the note (Note))}|

 After you publish and activate the custom action, when you download the CSDL you will find this new action defined.

```xml

<Action Name="new_AddNoteToContact" IsBound="true">
  <Parameter Name="entity" Type="mscrm.contact" Nullable="false" />
  <Parameter Name="NoteTitle" Type="Edm.String" Nullable="false" Unicode="false" />
  <Parameter Name="NoteText" Type="Edm.String" Nullable="false" Unicode="false" />
  <ReturnType Type="mscrm.annotation" Nullable="false" />
</Action>

```

The following HTTP request and response shows how to call the custom action and the response it returns if successful.  

 **Request**

```http
POST [Organization URI]/api/data/v9.0/contacts(94d8c461-a27a-e511-80d2-00155d2a68d2)/Microsoft.Dynamics.CRM.new_AddNoteToContact HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
 "NoteTitle": "New Note Title",
 "NoteText": "This is the text of the note"
}
```


 **Response**

```http

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
 "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#annotations/$entity",
 "annotationid": "9ad8c461-a27a-e511-80d2-00155d2a68d2"
}
```

<a name="bkmk_specifyentityparametertype"></a>

## Specify table type parameter

When an action requires an entity as a parameter and the type of entity is ambiguous, you must use the `@odata.type` property to specify the type of entity. The value of this property is the fully qualified name of the entity, which follows this pattern:
`Microsoft.Dynamics.CRM.`+*\<entity logical name>*.

As shown in the [Bound actions](#bkmk_boundActions) section above, the `Target` parameter to the <xref href="Microsoft.Dynamics.CRM.AddToQueue?text=AddToQueue Action" /> is an activity. But since all activities inherit from the <xref href="Microsoft.Dynamics.CRM.activitypointer?text=activitypointer EntityType" />, you must include the following property in the entity JSON to specify the type of entity is a letter: `"@odata.type": "Microsoft.Dynamics.CRM.letter"`.

Two other examples are <xref href="Microsoft.Dynamics.CRM.AddMembersTeam?text=AddMembersTeam Action" /> and <xref href="Microsoft.Dynamics.CRM.RemoveMembersTeam?text=RemoveMembersTeam Action" /> because the `Members` parameter is a collection of  <xref href="Microsoft.Dynamics.CRM.systemuser?text=systemuser EntityType" /> which inherits it's `ownerid` primary key from the <xref href="Microsoft.Dynamics.CRM.principal?text=principal EntityType" />. If you pass the following JSON to represent a single systemuser in the collection, it is clear that the entity is a systemuser and not a <xref href="Microsoft.Dynamics.CRM.team?text=team EntityType" />, which also inherits from the principal entitytype.

```json
{
 "Members": [{
  "@odata.type": "Microsoft.Dynamics.CRM.systemuser",
  "ownerid": "5dbf5efc-4507-e611-80de-5065f38a7b01"
 }]
}
```

If you do not specify the type of entity in this situation, you can get the following error: `"EdmEntityObject passed should have the key property value set."`.

### See also

[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)<br />
[Web API Functions and Actions Sample (Client-side JavaScript)](samples/functions-actions-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create a table using the Web API](create-entity-web-api.md)<br />
[Retrieve a table using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete tables using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate tables using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
---
title: "Use Web API actions (Microsoft Dataverse)| Microsoft Docs"
description: "Actions are reusable operations that can be performed using the Web API. Actions are used with a POST request to modify data on Microsoft Dataverse."
ms.date: 07/22/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Use Web API actions

Actions and functions represent reusable operations you can perform using the Web API. Use a `POST` request with actions listed in <xref:Microsoft.Dynamics.CRM.ActionIndex> to perform operations that have side effects. You can also define custom actions. More information: [Create your own messages](../custom-actions.md).

Actions are defined in the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document). See [Web API Actions](web-api-actions.md) for more information.


<a name="bkmk_unboundActions"></a>

## Unbound actions

The following XML is the definition of the <xref:Microsoft.Dynamics.CRM.Merge> action represented in the $metadata service document.

```xml
<Action Name="Merge">
   <Parameter Name="Target" 
      Type="mscrm.crmbaseentity" 
      Nullable="false" />
   <Parameter Name="Subordinate" 
      Type="mscrm.crmbaseentity" 
      Nullable="false" />
   <Parameter Name="UpdateContent" 
      Type="mscrm.crmbaseentity" />
   <Parameter Name="PerformParentingChecks" 
      Type="Edm.Boolean" 
      Nullable="false" />
</Action>
```

The <xref:Microsoft.Dynamics.CRM.Merge> action corresponds to the <xref:Microsoft.Crm.Sdk.Messages.MergeRequest> using the organization service. Use this action to merge a pair of duplicate records. This action doesn't include a return value. If it succeeds, the operation is complete.

The following example is the HTTP request and response to call the `Merge` action for two account records.

 **Request:**

```http
POST [Organization URI]/api/data/v9.2/Merge HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
  "Target": {
    "@odata.type": "Microsoft.Dynamics.CRM.account",
    "accountid": "cc1e2c4a-e577-ec11-8d21-000d3a554dcd"
  },
  "Subordinate": {
    "@odata.type": "Microsoft.Dynamics.CRM.account",
    "accountid": "e408fa45-3a70-ec11-8943-00224823561e"
  },
  "PerformParentingChecks": false
}

```

 **Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

More information: [Merge table rows using the Web API](merge-entity-using-web-api.md)

<a name="bkmk_boundActions"></a>

## Bound actions

There are two ways that an action can be bound. The most common way is for the action to be bound to an entity. Less frequently, it can also be bound to an entity collection.

In the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), when an `Action` element represents a bound action, it has an `IsBound` attribute with the value `true`. The first `Parameter` element defined within the action represents the entity that the operation is bound to. When the `Type` attribute of the parameter is a collection, the operation is bound to a collection of entities.

When invoking a bound function, you must include the full name of the function including the `Microsoft.Dynamics.CRM` namespace. If you don't include the full name, you get the following error: `Status Code:400 Request message has unresolved parameters`.

### Actions bound to a table

As an example of an action bound to an entity, the following is the definition of the <xref:Microsoft.Dynamics.CRM.AddToQueue> action represented in the CSDL:

```xml
 <ComplexType Name="AddToQueueResponse">
     <Property Name="QueueItemId" 
        Type="Edm.Guid" 
        Nullable="false" />
 </ComplexType>
 <Action Name="AddToQueue" 
    IsBound="true">
  <Parameter Name="entity" 
    Type="mscrm.queue" 
    Nullable="false" />
  <Parameter Name="Target" 
    Type="mscrm.crmbaseentity" 
    Nullable="false" />
  <Parameter Name="SourceQueue" 
    Type="mscrm.queue" />
  <Parameter Name="QueueItemProperties" 
    Type="mscrm.queueitem" />
  <ReturnType Type="mscrm.AddToQueueResponse" 
    Nullable="false" />
</Action>
```

This entity bound action is equivalent to the <xref:Microsoft.Crm.Sdk.Messages.AddToQueueRequest> used by the organization service. In the Web API, this action is bound to the <xref:Microsoft.Dynamics.CRM.queue> entity type that represents the <xref:Microsoft.Crm.Sdk.Messages.AddToQueueRequest>.<xref:Microsoft.Crm.Sdk.Messages.AddToQueueRequest.DestinationQueueId> property. This action accepts several more parameters and returns a <xref:Microsoft.Dynamics.CRM.AddToQueueResponse> complex type corresponding to the <xref:Microsoft.Crm.Sdk.Messages.AddToQueueResponse> returned by the organization service. When an action returns a complex type, the definition of the complex type appears directly above the action in the CSDL.

An action bound to an entity must be invoked using a URI to set the first parameter value. You can't set it as a named parameter value.

The following example shows using the <xref:Microsoft.Dynamics.CRM.AddToQueue> action to add a letter to a queue. Because the type of the `Target` parameter type isn't specific (`mscrm.crmbaseentity`), you must explicitly declare type of the object using the `@odata.type` property value of the full name of the entity, including the `Microsoft.Dynamics.CRM` namespace. In this case, `Microsoft.Dynamics.CRM.letter`. More information: [Specify entity parameter type](#bkmk_specifyentityparametertype)

 **Request:**

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

 **Response:**

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

It's less common to find actions bound to an entity collection. The following are some you may find:

:::row:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.CreateException>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.DeliverIncomingEmail>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.ExportTranslation>
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.ValidateSavedQuery>
   :::column-end:::
   :::column:::
      `FulfillSalesOrder` in [Dynamics 365 for Sales](/dynamics365/sales/help-hub)
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.CreateMultiple>
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.UpdateMultiple>
   :::column-end:::
   :::column:::
      
   :::column-end:::
   :::column:::
      
   :::column-end:::
:::row-end:::

As an example of an action bound to an entity collection, the following is the definition of the <xref:Microsoft.Dynamics.CRM.ExportTranslation> action represented in the CSDL $metadata:

```xml
<ComplexType Name="ExportTranslationResponse">
   <Property Name="ExportTranslationFile" 
    Type="Edm.Binary" />
</ComplexType>
<Action Name="ExportTranslation" 
    IsBound="true">
   <Parameter Name="entityset" 
    Type="Collection(mscrm.solution)" 
    Nullable="false" />
   <Parameter Name="SolutionName" 
    Type="Edm.String" 
    Nullable="false" 
    Unicode="false" />
   <ReturnType Type="mscrm.ExportTranslationResponse" 
    Nullable="false" />
</Action>
```

This entity collection bound action is equivalent to the <xref:Microsoft.Crm.Sdk.Messages.ExportTranslationRequest> used by the organization service. In the Web API, this action is bound to the <xref:Microsoft.Dynamics.CRM.solution> entity type. But rather than passing a value to the request, the entity collection binding simply applies the constraint that the URI of the request must include the path to the specified entity set.

The following example shows using the <xref:Microsoft.Dynamics.CRM.ExportTranslation> action, which exports a binary file containing data about localizable string values that can be updated to modify or add localizable values. Note how the entity collection bound action is after the entity set name for the solution entity: `solutions`.

 **Request:**

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

 **Response:**

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

A custom action may be a custom API or Custom Process Action. Either way it's created, there's a corresponding operation that you can use. With custom API, the operation may be a function. More information: [Create your own messages](../custom-actions.md)

The following example is for a custom process action.

### Custom action example: Add a note to a contact

Let's say that you want to create a custom action that adds a new note to a specific contact. You can create a custom action bound to the contact entity with the following properties.

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

 After you publish and activate the custom action, when you download the CSDL you'll find this new action defined.

```xml

<Action Name="new_AddNoteToContact" 
    IsBound="true">
  <Parameter Name="entity" 
    Type="mscrm.contact" 
    Nullable="false" />
  <Parameter Name="NoteTitle" 
    Type="Edm.String" 
    Nullable="false" 
    Unicode="false" />
  <Parameter Name="NoteText" 
    Type="Edm.String" 
    Nullable="false" 
    Unicode="false" />
  <ReturnType Type="mscrm.annotation" 
    Nullable="false" />
</Action>

```

The following HTTP request and response shows how to call the custom action and the response it returns if successful.  

 **Request:**

```http
POST [Organization URI]/api/data/v9.2/contacts(94d8c461-a27a-e511-80d2-00155d2a68d2)/Microsoft.Dynamics.CRM.new_AddNoteToContact HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
 "NoteTitle": "New Note Title",
 "NoteText": "This is the text of the note"
}
```


 **Response:**

```http

HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#annotations/$entity",
 "annotationid": "9ad8c461-a27a-e511-80d2-00155d2a68d2"
}
```

<a name="bkmk_specifyentityparametertype"></a>

## Specify the table type parameter

When an action requires an entity as a parameter and the type of entity is ambiguous, you must use the `@odata.type` property to specify the type of entity. The value of this property is the fully qualified name of the entity, which follows this pattern:
`Microsoft.Dynamics.CRM.`+*\<entity logical name>*.

As shown in the [Bound actions](#bkmk_boundActions) section above, the `Target` parameter to the <xref:Microsoft.Dynamics.CRM.AddToQueue> action is an activity. But since all activities inherit from the <xref:Microsoft.Dynamics.CRM.activitypointer> entity type, you must include the following property in the entity JSON to specify the type of entity is a letter: `"@odata.type": "Microsoft.Dynamics.CRM.letter"`.

Two other examples are <xref:Microsoft.Dynamics.CRM.AddMembersTeam> and <xref:Microsoft.Dynamics.CRM.RemoveMembersTeam> actions because the `Members` parameter is a collection of  <xref:Microsoft.Dynamics.CRM.systemuser> entity type, which inherits it's `ownerid` primary key from the <xref:Microsoft.Dynamics.CRM.principal> entity type. If you pass the following JSON to represent a single systemuser in the collection, it's clear that the entity is a systemuser and not a <xref:Microsoft.Dynamics.CRM.team> entity type, which also inherits from the principal entitytype.

```json
{
 "Members": [{
  "@odata.type": "Microsoft.Dynamics.CRM.systemuser",
  "ownerid": "5dbf5efc-4507-e611-80de-5065f38a7b01"
 }]
}
```

If you don't specify the type of entity in this situation, you can get the following error: `"EdmEntityObject passed should have the key property value set."`.

### See also

[Web API Actions](web-api-actions.md)<br />
[Web API Functions and Actions Sample (C#)](samples/webapiservice-functions-and-actions.md)<br />
[Web API Functions and Actions Sample (Client-side JavaScript)](samples/functions-actions-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Query Data using the Web API](query-data-web-api.md)<br />
[Create a table row using the Web API](create-entity-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

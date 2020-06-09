---
title: Perform portals Web API operations | Microsoft Docs
description: Learn how to perform different Web API operations on Power Apps portals.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/08/2020
ms.author: tapanm
ms.reviewer:
---

# Portals operations using the Web API

You can perform the [available Web API operations](web-api-overview.md#web-api-operations) in portals. Web API operations consist of [HTTP requests and responses](../../developer/common-data-service/webapi/compose-http-requests-handle-errors.md). This article shows sample operations, methods, URI, and the sample JSON you can use in the HTTP request.

## Retrieve an entity record

### Basic retrieve

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Basic retrieve</td>
    <td>GET</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)</i></td>
  </tr>
</table>

Complete request and response details: [Basic retrieve](../../developer/common-data-service/webapi/retrieve-entity-using-web-api.md#basic-retrieve-example)

### Retrieve specific properties

Complete request and response details: [Retrieve specific properties](../../developer/common-data-service/webapi/retrieve-entity-using-web-api.md#retrieve-specific-properties)

## Create an entity record

### Basic Create

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Basic create</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/accounts</i></td>
    <td>@Neeraj: need sample</td>
  </tr>
</table>

Complete request and response details: [Basic Create](../../developer/common-data-service/webapi/create-entity-web-api.md#basic-create)

### Create related entity records in one operation

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Create related entity records in one operation</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/accounts</i></td>
  </tr>
</table>

Complete request and response details: [Create related entity records in one operation](../../developer/common-data-service/webapi/create-entity-web-api.md#create-related-entity-records-in-one-operation)


### Associate entity records on create

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Associate entity records on create</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/accounts</i></td>
    <td><code>{"name":"Sample Account","primarycontactid@odata.bind":"/contacts(00000000-0000-0000-0000-000000000001)"}</code></td>
  </tr>
</table>

#### Sample JSON for creating annotation via Web API

```json
{
    "new_attribute1": "test attribute 1",
    "new_attribute2": "test attribute 2",
    "new_comments": "test comments",
    "new_recordurl": recordURL,
    "new_feedback_Annotations":
        [
            {
                "notetext": "Screenshot attached",
                "subject": "Attachment",
                "filename": file.name,
                "mimetype": file.type,
                "documentbody": base64str,
            }
        ]
    }
```

`documentbody` will contain the attachment as base64 string.

Complete request and response details: [Associate entity records on create](../../developer/common-data-service/webapi/create-entity-web-api.md#associate-entity-records-on-create)

### Create with data returned

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Create with data returned</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/accounts?$select=name,creditonhold,address1_latitude,description,revenue,accountcategorycode,createdon</i></td>
  </tr>
</table>

Complete request and response details: [Create with data returned](../../developer/common-data-service/webapi/create-entity-web-api.md#create-with-data-returned)

Portal Web API will not  --> @Neeraj - Incomplete sentence. What will portals Web API NOT...?

## Update and delete entities using the Web API

### Basic update

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Basic update</td>
    <td>PATCH</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>{      "name": "Updated Sample Account ",      "creditonhold": true,      "address1_latitude": 47.639583,      "description": "This is the updated description of the sample account",      "revenue": 6000000,      "accountcategorycode": 2  }</code></td>
  </tr>
</table>

Complete request and response details: [Basic update](../../developer/common-data-service/webapi/update-delete-entities-using-web-api.md#basic-update)

### Update with data returned

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Update with data returned</td>
    <td>PATCH</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)?$select=name,creditonhold,address1_latitude,description,revenue,accountcategorycode,createdon </code></td>
  </tr>
</table>

Complete request and response details: [Update with data returned](../../developer/common-data-service/webapi/update-delete-entities-using-web-api.md#update-with-data-returned)

### Update a single property value

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Update a single property value</td>
    <td>PUT</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)/name</i></td>
    <td><code>{"value": "Updated Sample Account Name"}</code></td>
  </tr>
</table>

Complete request and response details: [Update a single property value](../../developer/common-data-service/webapi/update-delete-entities-using-web-api.md#update-a-single-property-value)

### Delete a single property value

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Delete a single property value</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)/description</i></td>
    <td><code>@Neeraj: need sample</code></td>
  </tr>
</table>

Complete request and response details: [Delete a single property value](../../developer/common-data-service/webapi/update-delete-entities-using-web-api.md#delete-a-single-property-value)

### Upsert an entity

For more details about `upsert` operation, go to [Upsert an entity](../../developer/common-data-service/webapi/update-delete-entities-using-web-api.md#upsert-an-entity).

#### Prevent create in upsert

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Prevent create in upsert</td>
    <td>PATCH</td>
    <td><i>[Portal URI]/_api/v9.0/accounts(00000000-0000-0000-0000-000000000001)</i></td>
  </tr>
</table>

Complete request and response details: [Prevent create in upsert](../../developer/common-data-service/webapi/perform-conditional-operations-using-web-api.md#prevent-create-in-upsert)

#### Prevent update in upsert

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Prevent update in upsert</td>
    <td>PATCH</td>
    <td><i>[Portal URI]/_api/v9.0/accounts(00000000-0000-0000-0000-000000000001)</i></td>
  </tr>
</table>

Complete request and response details: [Prevent update in upsert](../../developer/common-data-service/webapi/perform-conditional-operations-using-web-api.md#prevent-update-in-upsert)

### Basic delete

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Basic delete</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>@Neeraj: need sample</code></td>
  </tr>
</table>

Complete request and response details: [Basic delete](../../developer/common-data-service/webapi/update-delete-entities-using-web-api.md#basic-delete)

## Associate and disassociate entities using Web API

### Add a reference to a collection-valued navigation property

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Add a reference to a collection-valued navigation property</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts/$ref</i></td>
    <td><code>{"@odata.id":"[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)"}</code></td>
  </tr>
</table>

Complete request and response details: [Add a reference to a collection-valued navigation property](../../developer/common-data-service/webapi/associate-disassociate-entities-using-web-api.md#add-a-reference-to-a-collection-valued-navigation-property)

### Remove a reference to an entity

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Remove a reference to an entity</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts/$ref?$id=[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>@Neeraj: need sample</code></td>
  </tr>
</table>

Complete request and response details: [Remove a reference to an entity](../../developer/common-data-service/webapi/associate-disassociate-entities-using-web-api.md#remove-a-reference-to-an-entity)

### Change the reference in a single-valued navigation property

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Change the reference in a single-valued navigation property</td>
    <td>PUT</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref </i></td>
  </tr>
</table>

Complete request and response details: [Change the reference in a single-valued navigation property](../../developer/common-data-service/webapi/associate-disassociate-entities-using-web-api.md#change-the-reference-in-a-single-valued-navigation-property)

### Remove a reference to an entity for a single-valued navigation property

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Remove a reference to an entity for a single-valued navigation property</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref</i></td>
    <td><code>For a single-valued navigation property, remove the $id query string parameter. @Neeraj: please elaborate or share sample</code></td>
  </tr>
</table>

Complete request and response details: [Remove a reference to an entity for a single-valued navigation property](../../developer/common-data-service/webapi/associate-disassociate-entities-using-web-api.md#remove-a-reference-to-an-entity)

### Change the reference in a single-valued navigation property

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Change the reference in a single-valued navigation property</td>
    <td>PUT</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref</i></td>
    <td><code>{"@odata.id":"[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)"}</code></td>
  </tr>
</table>

Complete request and response details: [Remove a reference to an entity for a single-valued navigation property](../../developer/common-data-service/webapi/associate-disassociate-entities-using-web-api.md#change-the-reference-in-a-single-valued-navigation-property)

### Associate entities on create

As described in [Create related entities in one operation](#create-related-entity-records-in-one-operation), new entities can be created with relationships using *deep* insert.

### Associate entities on update using single-valued navigation property

You can associate entities on update using the same message described in [Basic update](#basic-update) but you must use the `@odata.bind` annotation to set the value of a single-valued navigation property. The following example changes the account associated to an opportunity using the customerid_account single-valued navigation property.

### Associate entities on update using single-valued navigation property

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Associate entities on update using single-valued navigation property</td>
    <td>PATCH</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>{"customerid_account@odata.bind":"[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)"}</code></td>
  </tr>
</table>

Complete request and response details: [Associate entities on update using single-valued navigation property](../../developer/common-data-service/webapi/associate-disassociate-entities-using-web-api.md#associate-entities-on-update-using-single-valued-navigation-property)

### Associate entities on update using collection-valued navigation property

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Associate entities on update using collection-valued navigation property</td>
    <td>PUT</td>
    <td><i>[Portal URI]/_api/emails(00000000-0000-0000-0000-000000000001)/email_activity_parties</i></td>
    <td><code>{"value": [{"partyid_contact@odata.bind":"contact(a30d4045-fc46-e711-8115-e0071b66df51)","participationtypemask":3},{"partyid_contact@odata.bind":"contact(1dcdda07-3a39-e711-8145-e0071b6a2001)","participationtypemask":2}]}</code></td>
  </tr>
</table>

Complete request and response details: [Associate entities on update using collection-valued navigation property](../../developer/common-data-service/webapi/associate-disassociate-entities-using-web-api.md#associate-entities-on-update-using-collection-valued-navigation-property)

## User actions

### Bound actions

<table style="text-align:left">
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Bound actions</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/queues(56ae8258-4878-e511-80d4-00155d2a68d1)/Microsoft.Dynamics.CRM.AddToQueue</i></td>
  </tr>
</table>

Complete request and response details: [Bound actions](../../developer/common-data-service/webapi/use-web-api-actions.md#bound-actions)

## Web API Ajax samples

@Neeraj - need prologue of how to use AJAX sample. And is the format/spacing/line breaks correct? There seem to be more or less semicolons/line breaks in code so please confirm if the formatted code is correct/works.

```javascript
(function(webapi, \$){
    function safeAjax(ajaxOptions) {
        var deferredAjax = \$.Deferred();
        shell.getTokenDeferred().done(function (token) {
        // Add headers for Ajax
        if (!ajaxOptions.headers) {
            \$.extend(ajaxOptions, { headers: {
             "__RequestVerificationToken": token}});
        } else {
            ajaxOptions.headers["__RequestVerificationToken"] = token;
            } \$.ajax(ajaxOptions)
            .done(function(data, textStatus, jqXHR) {
                validateLoginSession(data, textStatus, jqXHR, deferredAjax.resolve);
            }).fail(deferredAjax.reject); // Ajax headers
        }).fail(function () {
            deferredAjax.rejectWith(this, arguments); // on token failure pass the token
            ajax and args });
    return deferredAjax.promise();
    } webapi.safeAjax = safeAjax;
})(window.webapi = window.webapi \|\| {}, jQuery)
```

### Create

```javascript
webapi.safeAjax({
type: "POST",
url: "<https://YourPortalURL.powerappsportals.com/_api/accounts>",
contentType: "application/json",
data: JSON.stringify({"name": "Sample Account 02:20 PM"}),
success: function (res, status, xhr) {
console.log(res);
console.log("entityID: "+ xhr.getResponseHeader("entityid"))}});
```

### Update

```javascript
webapi.safeAjax({
type: "PATCH",
url:"<https://YourPortalURL.powerappsportals.com/_api/accounts(GUID)>",
contentType: "application/json",
data: JSON.stringify({"name": "Sample Account 02:20 PM"}),
success: function (res) {
console.log(res);
}});
```

### Delete

```javascript
webapi.safeAjax({
type: "DELETE",
url:"<https://[YourPortalURL].powerappsportals.com/_api/accounts(1da81c42-ee99-ea11-a811-000d3a37ed0b)>",
contentType: "application/json",
success: function (res) {
console.log(res);
}});
```

## Next steps

[Compose HTTP requests and handle errors](web-api-http-requests-handle-errors.md)

### See also

- [Web API overview](web-api-overview.md)

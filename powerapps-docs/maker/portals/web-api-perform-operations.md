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
    <td>{"name":"Sample Account"}</td>
  </tr>
</table>

#### Sample JSON for creating related entity records in one operation
For example, the following request body posted to the Account entity set will create a total of four new entities in the context of creating an account.
- A contact is created because it is defined as an object property of the single-valued navigation property primarycontactid.
- An opportunity is created because it is defined as an object within an array that is set to the value of a collection-valued navigation property opportunity_customer_accounts.
- A task is created because it is defined an object within an array that is set to the value of a collection-valued navigation property Opportunity_Tasks.

```json
{
 "name": "Sample Account",
 "primarycontactid":
 {
     "firstname": "John",
     "lastname": "Smith"
 },
 "opportunity_customer_accounts":
 [
  {
      "name": "Opportunity associated to Sample Account",
      "Opportunity_Tasks":
      [
       { "subject": "Task associated to opportunity" }
      ]
  }
 ]
}
```

Complete request and response details: [Basic Create](../../developer/common-data-service/webapi/create-entity-web-api.md#basic-create)

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

## Web API Ajax samples

@Neeraj - need prologue of how to use AJAX sample. And is the format/spacing/line breaks correct? There seem to be more or less semicolons/line breaks in code so please confirm if the formatted code is correct/works.

```javascript
	(function(webapi, $){
		function safeAjax(ajaxOptions) {
			var deferredAjax = $.Deferred();
	
			shell.getTokenDeferred().done(function (token) {
				// add headers for ajax
				if (!ajaxOptions.headers) {
					$.extend(ajaxOptions, {
						headers: {
							"__RequestVerificationToken": token
						}
					}); 
				} else {
					ajaxOptions.headers["__RequestVerificationToken"] = token;
				}
				$.ajax(ajaxOptions)
					.done(function(data, textStatus, jqXHR) {
						validateLoginSession(data, textStatus, jqXHR, deferredAjax.resolve);
					}).fail(deferredAjax.reject); //ajax
			}).fail(function () {
				deferredAjax.rejectWith(this, arguments); // on token failure pass the token ajax and args
			});
	
			return deferredAjax.promise();	
		}
		webapi.safeAjax = safeAjax;
	})(window.webapi = window.webapi || {}, jQuery)
```

### Create

```javascript
	webapi.safeAjax({
		type: "POST",
		url: "/_api/accounts",
		contentType: "application/json",
		data: JSON.stringify({
			"name": "Sample Account"
		}),
		success: function (res, status, xhr) {
      //print id of newly created entity record
			console.log("entityID: "+ xhr.getResponseHeader("entityid"))
		}
	});

```

### Update

```javascript
  webapi.safeAjax({
    type: "PATCH",
    url: "/_api/accounts(1da81c42-ee99-ea11-a811-000d3a37ed0b)",
    contentType: "application/json",
    data: JSON.stringify({
      "name": "Sample Account - Updated"
    }),
    success: function (res) {
      console.log(res);
    }
  });
```

### Delete

```javascript
	webapi.safeAjax({
		type: "DELETE",
		url: "/_api/accounts(1da81c42-ee99-ea11-a811-000d3a37ed0b)",
		contentType: "application/json",
		success: function (res) {
			console.log(res);
		}
  });
```

## Next steps

[Compose HTTP requests and handle errors](web-api-http-requests-handle-errors.md)

### See also

- [Web API overview](web-api-overview.md)

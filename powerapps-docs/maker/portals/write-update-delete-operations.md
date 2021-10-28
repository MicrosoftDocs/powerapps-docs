---
title: Portals write, update and delete operations using the Web API
description: Learn how to perform write, update and delete Web API operations on Power Apps portals.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/31/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - tapanm-msft
    - nickdoelman
---

# Portals operations using the Web API

You can perform [available Web API operations](web-api-overview.md#web-api-operations) in portals. Web API operations consist of HTTP requests and responses. This article shows sample write, update, and delete operations, methods, URI, and sample JSON you can use in the HTTP requests.

> [!IMPORTANT]
> - **Your portal version must be 9.3.3.x or later for this feature to work.**

## Create a record in a table

### Basic create

<table>
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

#### Sample JSON for creating related table records in one operation

For example, the following request body posted to the Account table set will create a total of four new tables&mdash;including the account&mdash;in the context of creating the account.

- A contact is created because it's defined as an object property of the single-valued navigation property primarycontactid.
- An opportunity is created because it's defined as an object within an array that's set to the value of a collection-valued navigation property opportunity_customer_accounts.
- A task is created because it's defined as an object within an array that's set to the value of a collection-valued navigation property Opportunity_Tasks.

```json
{
 "name": "Sample Account",
 "primarycontactid":
 {
     "firstname": "Alton",
     "lastname": "Stott"
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

### Associate table records on create

<table>
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Associate table records on create</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/accounts</i></td>
    <td><code>{"name":"Sample Account","primarycontactid@odata.bind":"/contacts(00000000-0000-0000-0000-000000000001)"}</code></td>
  </tr>
</table>

#### Sample JSON for creating an annotation via the Web API

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

`documentbody` will contain the attachment as a base64 string.

## Update and delete records by using the Web API

### Basic update

<table>
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

### Update a single property value

<table>
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

### Delete a single property value

<table>
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Delete a single property value</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)/description</i></td>
  </tr>
</table>

### Basic delete

<table>
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Basic delete</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)</i></td>    
  </tr>
</table>

## Associate and disassociate tables by using the Web API

### Add a reference to a collection-valued navigation property

<table>
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

### Remove a reference to a table

<table>
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Remove a reference to a table</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts/$ref?$id=[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)</i></td>
  </tr>
</table>

### Remove a reference to a table for a single-valued navigation property
For a single-valued navigation property, remove the $id query string parameter.
<table>
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
  </tr>
  <tr>
    <td>Remove a reference to a table for a single-valued navigation property</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref</i></td>
  </tr>
</table>

### Change the reference in a single-valued navigation property

<table>
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

### Associate tables on create

New tables can be created with relationships by using *deep* insert.

### Associate tables on update by using a single-valued navigation property

You can associate tables on update by using the same message described in [Basic update](#basic-update), earlier in this topic, but you must use the `@odata.bind` annotation to set the value of a single-valued navigation property. The following example changes the account associated to an opportunity by using the customerid_account single-valued navigation property.

### Associate tables on update by using a single-valued navigation property

<table>
  <tr>
    <th>Operation</th>
    <th>Method</th>
    <th>URI</th>
    <th>JSON Sample</th>
  </tr>
  <tr>
    <td>Associate tables on update by using a single-valued navigation property</td>
    <td>PATCH</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>{"customerid_account@odata.bind":"[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)"}</code></td>
  </tr>
</table>

## Web API AJAX samples

This sample demonstrates how to create, update, and delete table records by using Asynchronous JavaScript and XML (AJAX).

### Wrapper AJAX function

```javascript
	(function(webapi, $){
		function safeAjax(ajaxOptions) {
			var deferredAjax = $.Deferred();
	
			shell.getTokenDeferred().done(function (token) {
				// add headers for AJAX
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
					}).fail(deferredAjax.reject); //AJAX
			}).fail(function () {
				deferredAjax.rejectWith(this, arguments); // on token failure pass the token AJAX and args
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
      //print id of newly created table record
			console.log("entityID: "+ xhr.getResponseHeader("entityid"))
		}
	});

```

### Update

```javascript
  webapi.safeAjax({
    type: "PATCH",
    url: "/_api/accounts(00000000-0000-0000-0000-000000000001)",
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
		url: "/_api/accounts(00000000-0000-0000-0000-000000000001)",
		contentType: "application/json",
		success: function (res) {
			console.log(res);
		}
  });
```

## Next step
[Portals read operations using the Web API](read-operations.md)

### See also

[Web API overview](web-api-overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
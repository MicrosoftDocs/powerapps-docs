---
title: Use the Web API for portals | Microsoft Docs
description: Learn how to use the portals Web API to create, read, update and delete Common Data Service entities.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/05/2020
ms.author: tapanm
ms.reviewer:
---

# Portals Web API

## Web API JSON samples

You can perform the [available Web API operations](#web-api-operations) in portals. Web API operations consist of [HTTP requests and responses](../..developer/common-data-service/webapi/compose-http-requests-handle-errors.md). The following table shows sample operations, methods, URI and the sample JSON you can use in the HTTP request.

<!--- Consider in format of https://docs.microsoft.com/en-us/powerapps/developer/common-data-service/webapi/create-entity-web-api - ## title for each operation and URI/JSON samples in code blocks of HTTP-->

@Neeraj - can we please get all HTTP requests and responses with HTTP headers? That way we can show HTTP code blocks with entire HTTP request and HTTP response.

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
  <tr>
    <td>Associate entity records on create</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/accounts</i></td>
    <td><code>{"name":"Sample Account","primarycontactid@odata.bind":"/contacts(00000000-0000-0000-0000-000000000001)"}</code></td>
  </tr>
  <tr>
    <td>Basic update</td>
    <td>PATCH</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>{      "name": "Updated Sample Account ",      "creditonhold": true,      "address1_latitude": 47.639583,      "description": "This is the updated description of the sample account",      "revenue": 6000000,      "accountcategorycode": 2  }</code></td>
  </tr>
  <tr>
    <td>Update a single property value</td>
    <td>PUT</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)/name</i></td>
    <td><code>{"value": "Updated Sample Account Name"}</code></td>
  </tr>
  <tr>
    <td>Update a single property value</td>
    <td>PUT</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)/name</i></td>
    <td><code>{"value": "Updated Sample Account Name"}</code></td>
  </tr>
  <tr>
    <td>Delete a single property value</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)/description</i></td>
    <td><code>@Neeraj: need sample</code></td>
  </tr>
  <tr>
    <td>Basic delete</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>@Neeraj: need sample</code></td>
  </tr>
  <tr>
    <td>Add a reference to a collection-valued navigation property</td>
    <td>POST</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts/$ref</i></td>
    <td><code>{"@odata.id":"[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)"}</code></td>
  </tr>
  <tr>
    <td>Remove a reference to an entity</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts/$ref?$id=[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>@Neeraj: need sample</code></td>
  </tr>
  <tr>
    <td>Remove a reference to an entity</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts(00000000-0000-0000-0000-000000000001)/$ref</i></td>
    <td><code>@Neeraj: need sample & please confirm if sample is different than earlier since both have same operation - "Remove a reference to an entity"</code></td>
  </tr>
  <tr>
    <td>Remove a reference to an entity for a single-valued navigation property</td>
    <td>DELETE</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref</i></td>
    <td><code>For a single-valued navigation property, remove the $id query string parameter. @Neeraj: please elaborate or share sample</code></td>
  </tr>
  <tr>
    <td>Change the reference in a single-valued navigation property</td>
    <td>PUT</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref</i></td>
    <td><code>{"@odata.id":"[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)"}</code></td>
  </tr>
  <tr>
    <td>Associate entities on update using single-valued navigation property</td>
    <td>PATCH</td>
    <td><i>[Portal URI]/_api/opportunities(00000000-0000-0000-0000-000000000001)</i></td>
    <td><code>{"customerid_account@odata.bind":"[Portal URI]/_api/accounts(00000000-0000-0000-0000-000000000002)"}</code></td>
  </tr>
  <tr>
    <td>Associate entities on update using collection-valued navigation property</td>
    <td>PUT</td>
    <td><i>[Portal URI]/_api/emails(00000000-0000-0000-0000-000000000001)/email_activity_parties</i></td>
    <td><code>{"value": [{"partyid_contact@odata.bind":"contact(a30d4045-fc46-e711-8115-e0071b66df51)","participationtypemask":3},{"partyid_contact@odata.bind":"contact(1dcdda07-3a39-e711-8145-e0071b6a2001)","participationtypemask":2}]}</code></td>
  </tr>
</table>

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

### See also

- [Web API overview](web-api-overview.md)
- [Perform Web API operations](web-api-perform-operations.md)
- [Compose HTTP requests and handle errors](web-api-http-requests-handle-errors.md)
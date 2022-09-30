---
title: "createRecord (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the createRecord method.
ms.author: aorth
author: adrianorth
ms.date: 08/22/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# createRecord (Client API reference)

[!INCLUDE[./includes/createRecord-description.md](./includes/createRecord-description.md)] 

## Syntax

`Xrm.WebApi.createRecord(entityLogicalName, data).then(successCallback, errorCallback);`

## Parameters

<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td>entityLogicalName</td>
<td>String</td>
<td>Yes</td>
<td>Logical name of the table you want to create. For example: "account".</td>
</tr>
<tr>
<td>data</td>
<td>Object</td>
<td>Yes</td>
<td><p>A JSON object defining the columns and values for the new table record.</p>
<p>See examples later in this topic to see how you can define the <code>data</code> object for various create scenarios.</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when a record is created. An object with the following properties will be passed to identify the new record:</p>
<ul>
<li><b>entityType</b>: String. The table logical name of the new record.</li>
<li><b>id</b>: String. GUID of the new record.</li>
</ul></td>
</tr>
<tr>
<td>errorCallback</td>
<td>Function</td>
<td>No</td>
<td>A function to call when the operation fails. An object with the following properties will be passed:
<ul>
<li><b>errorCode</b>: Number. The error code.</li>
<li><b>message</b>: String. An error message describing the issue.</li>
</ul></td>
</tr>
</table>

## Return Value

On success, returns a promise object containing the values specified earlier in the description of the **successCallback** parameter.

## Examples

These examples use the same request objects as demonstrated in [Create a table row using the Web API](../../../../data-platform/webapi/create-entity-web-api.md) to define the data object for creating a table record.

### Basic create

Creates a sample account record.

```JavaScript
// define the data to create new account
var data =
    {
        "name": "Sample Account",
        "creditonhold": false,
        "address1_latitude": 47.639583,
        "description": "This is the description of the sample account",
        "revenue": 5000000,
        "accountcategorycode": 1
    }

// create account record
Xrm.WebApi.createRecord("account", data).then(
    function success(result) {
        console.log("Account created with ID: " + result.id);
        // perform operations on record creation
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

### Create related table records along with the primary record

 You can create tables related to each other by defining them as navigation properties values. This is known as *deep insert*. In this example, we will create a sample account record along with the primary contact record and an associated opportunity record.

> [!NOTE]
> Creating related table records in a single create operation is not supported for offline mode.

```JavaScript
// define data to create primary and related table records
var data =
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

// create account record
Xrm.WebApi.createRecord("account", data).then(
    function success(result) {
        console.log("Account created with ID: " + result.id);
        // perform operations on record creation
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

### Associate tables on creating new records

To associate new table records to existing table records, set the value of single-valued navigation properties using the `@odata.bind` annotation.

> [!NOTE]
> The names of single-valued navigation properties are not always the same as the `LogicalName` for the lookup attribute. You should make sure you are using the `Name` attribute value of the `NavigationProperty` element in the Web API $metadata service document. More information: [Web API Navigation Properties](../../../../data-platform/webapi/web-api-navigation-properties.md)

Here is code example:

The following example creates an account record, and associates it to an existing contact record to set the latter as the primary contact for the new account record:

```JavaScript
var data =
    {
        "name": "Sample Account",
        "primarycontactid@odata.bind": "/contacts(465b158c-541c-e511-80d3-3863bb347ba8)"
    }

// create account record
Xrm.WebApi.createRecord("account", data).then(
    function success(result) {
        console.log("Account created with ID: " + result.id);
        // perform operations on record creation
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

**Deprecated method for mobile offline scenario**

> [!NOTE]
> Instead of using `@odata.bind` annotation example above, the deprecated **lookup** object with case-sensitive properties (`logicalname` and `id`) is still supported for existing customizations. However, it is recommended to use `@odata.bind` annotation for both online and offline scenario instead of using this deprecated object.

The following example uses the deprecated method to create an account record, and associate it to an existing contact record to set the latter as the primary contact for the new account record from mobile clients when working in the offline mode:

```JavaScript
var data =
    {
        "name": "Sample Account",
        "primarycontactid":
        {
            "logicalname": "contact",
            "id": "465b158c-541c-e511-80d3-3863bb347ba8"
        } 
    }

// create account record
Xrm.WebApi.offline.createRecord("account", data).then(
    function success(result) {
        console.log("Account created with ID: " + result.id);
        // perform operations on record creation
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```
 
### Related topics

[Create a table row using the Web API](../../../../data-platform/webapi/create-entity-web-api.md)<br />
[Xrm.WebApi](../xrm-webapi.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
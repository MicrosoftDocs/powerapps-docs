---
title: "Xrm.WebApi.online.execute (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 09/23/2019
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d4e92999-3b79-4783-8cac-f656fc5f7fda
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Xrm.WebApi.online.execute (Client API reference)

[!INCLUDE[./includes/execute-description.md](./includes/execute-description.md)]

> [!NOTE]
> This method is supported only for the online mode ([Xrm.WebApi.online](../online.md)).

## Syntax

`Xrm.WebApi.online.execute(request).then(successCallback, errorCallback);`

## Parameters

<table style="width:100%">
<tr>
<th>Name</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td>request</td>
<td>Object</td>
<td>Yes</td>
<td><p>Object that will be passed to the Web API endpoint to execute an action, function, or CRUD request. The object exposes a <b>getMetadata</b> method that lets you define the metadata for the action, function or CRUD request you want to execute. The <b>getMetadata</b> method has the following parameters:</p>
<ul>
<li><b>boundParameter</b>: (Optional) String. The name of the bound parameter for the action or function to execute.
<ul><li>Specify <code>undefined</code> if you are executing a CRUD request.</li>
<li>Specify <code>null</code> if the action or function to execute is not bound to any entity.</li>
<li>Specify <code>entity</code> in case the action or function to execute is bound to an entity. </li></ul>
<li><b>operationName</b>: (Optional). String. Name of the action, function, or one of the following values if you are executing a CRUD request: "Create", "Retrieve", "Update", or "Delete".</li>
<li><b>operationType</b>: (Optional). Number. Indicates the type of operation you are executing; specify one of the following values:
<br/><code>0: Action</code>
<br/><code>1: Function</code>
<br/><code>2: CRUD</code></li>
<li><b>parameterTypes</b>: Object. The metadata for parameter types. The object has the following attributes:
<ul>
<li><b>enumProperties</b>: (Optional) Object. The metadata for enum types. The object has two string attributes: <b>name</b> and <b>value</b></li>
<li><b>structuralProperty</b>: Number. The category of the parameter type. Specify one of the following values:
<br/><code>0: Unknown</code>
<br/><code>1: PrimitiveType</code>
<br/><code>2: ComplexType</code>
<br/><code>3: EnumerationType</code>
<br/><code>4: Collection</code>
<br/><code>5: EntityType</code></li>
<li><b>typeName</b>: String. The fully qualified name of the parameter type.
</ul>
</li>
</ul>
</td>
</tr>
<tr>
<td>successCallback</td>
<td>Function</td>
<td>No</td>
<td><p>A function to call when operation is executed successfully. A response object is passed to the function with the following attributes:</p>
<ul>
<li><b>body (Deprecated)</b>: Object. Response body.</li>
<li><b>headers</b>: Object. Response headers.</li>
<li><b>ok</b>: Boolean. Indicates whether the request was successful.</li>
<li><b>status</b>: Number. Numeric value in the response status code. For example: <b>200</b></li>
<li><b>statusText</b>: String. Description of the response status code. For example: <b>OK</b></li>
<li><b>type (Deprecated)</b>: String. Response type. Values are: the empty string (default), "arraybuffer", "blob", "document", "json", and "text".</b></li>
<li><b>url</b>: String. Request URL of the action, function, or CRUD request that was sent to the Web API endpoint.</b></li>
<li><b>json</b>: Promise. Parameter to the callback delegate is of type any (JSON object).</b></li>
<li><b>text</b>: Promise. Parameter to the callback delegate is a String.</b></li>
</ul>
</td>
</tr>
<tr>
<td>errorCallback</td>
<td>Function</td>
<td>No</td>
<td>A function to call when the operation fails.</td>
</tr>
</table>

## Return Value

On success, returns a promise object with the attributes specified earlier in the description of **successCallback** function.

## Examples

### Execute an action

The following example demonstrates how to execute the <xref:Microsoft.Dynamics.CRM.WinOpportunity> action. The request object is created based on the action definition here: [Unbound actions](../../../../../common-data-service/webapi/use-web-api-actions.md#unbound-actions)
```JavaScript
var Sdk = window.Sdk || {};
/**
 * Request to win an opportunity
 * @param {Object} opportunityClose - The opportunity close activity associated with this state change.
 * @param {number} status - Status of the opportunity.
 */
Sdk.WinOpportunityRequest = function (opportunityClose, status) {
    this.OpportunityClose = opportunityClose;
    this.Status = status;

    this.getMetadata = function () {
        return {
            boundParameter: null,
            parameterTypes: {
                "OpportunityClose": {
                    "typeName": "mscrm.opportunityclose",
                    "structuralProperty": 5 // Entity Type
                },
                "Status": {
                    "typeName": "Edm.Int32",
                    "structuralProperty": 1 // Primitive Type
                }
            },
            operationType: 0, // This is an action. Use '1' for functions and '2' for CRUD
            operationName: "WinOpportunity",
        };
    };
};


var opportunityClose = {
    "opportunityid@odata.bind": "/opportunities(c60e0283-5bf2-e311-945f-6c3be5a8dd64)",
    "description": "Product and maintainance for 2018",
    "subject": "Contract for 2018"
}

// Construct a request object from the metadata
var winOpportunityRequest = new Sdk.WinOpportunityRequest(opportunityClose, 3);

// Use the request object to execute the function
Xrm.WebApi.online.execute(winOpportunityRequest).then(
    function (result) {
        if (result.ok) {
            console.log("Status: %s %s", result.status, result.statusText);
            // perform other operations as required;
        }
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```


### Execute a function

The following example demonstrates how to execute the <xref:Microsoft.Dynamics.CRM.WhoAmI> function:

```JavaScript
var Sdk = window.Sdk || {};
/**
 * Request to execute WhoAmI function
 */
Sdk.WhoAmIRequest = function () { };
Sdk.WhoAmIRequest.prototype.getMetadata = function () {
    return {
        boundParameter: null,
        parameterTypes: {},
        operationType: 1, // This is a function. Use '0' for actions and '2' for CRUD
        operationName: "WhoAmI",
    };
};

// Construct a request object from the metadata
var whoAmIRequest = new Sdk.WhoAmIRequest();

// Use the request object to execute the function
Xrm.WebApi.online.execute(whoAmIRequest).then(
    function (result) {
        if (result.ok) {
            console.log("Status: %s %s", result.status, result.statusText);
            result.json().then(
                function (response) {
                    console.log("User Id: %s", response.UserId);
                    // perform other operations as required;
                });
        }
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

### Perform CRUD operations

#### Create a record

The following example demonstrates how to perform a Create operation.

```JavaScript
var Sdk = window.Sdk || {};

/**
 * Request to execute a create operation
 */
Sdk.CreateRequest = function (entityName, payload) {
    this.etn = entityName;
    this.payload = payload;

    this.getMetadata = function () {
        return {
            boundParameter: null,
            parameterTypes: {},
            operationType: 2, // This is a CRUD operation. Use '0' for actions and '1' for functions
            operationName: "Create",
        };
    };
};

// Construct a request object from the metadata
var payload = {
    name: "Fabrikam Inc."
};
var createRequest = new Sdk.CreateRequest("account", payload);

// Use the request object to execute the function
Xrm.WebApi.online.execute(createRequest).then(
    function (result) {
        if (result.ok) {
            console.log("Status: %s %s", result.status, result.statusText);
            // perform other operations as required;
        }
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
 ```
 
#### Retrieve a record

The following example demonstrates how to perform a Retrieve operation.

```JavaScript
var Sdk = window.Sdk || {};

/**
 * Request to execute a retrieve operation
 */
Sdk.RetrieveRequest = function (entityReference, columns) {
    this.entityReference = entityReference;
    this.columns = columns;

    this.getMetadata = function () {
        return {
            boundParameter: null,
            parameterTypes: {},
            operationType: 2, // This is a CRUD operation. Use '0' for actions and '1' for functions
            operationName: "Retrieve",
        };
    };
};

// Construct request object from the metadata
var entityReference = {
    entityType: "account",
    id: "0b9b8a43-e0dd-e911-a849-000d3a11e59b"
};
var retrieveRequest = new Sdk.RetrieveRequest(entityReference, ["name"]);

// Use the request object to execute the function
Xrm.WebApi.online.execute(retrieveRequest).then(
    function (result) {
        if (result.ok) {
            console.log("Status: %s %s", result.status, result.statusText);
            result.json().then(
                function (response) {
                    console.log("Name: %s", response.name);
                    // perform other operations as required;
                });
        }
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);

```

#### Update a record

The following example demonstrates how to perform a Update operation.

```JavaScript
var Sdk = window.Sdk || {};


/**
 * Request to execute an update operation
 */
Sdk.UpdateRequest = function (entityName, entityId, payload) {
    this.etn = entityName;
    this.id = entityId;
    this.payload = payload;

    this.getMetadata = function () {
        return {
            boundParameter: null,
            parameterTypes: {},
            operationType: 2, // This is a CRUD operation. Use '0' for actions and '1' for functions
            operationName: "Update",
        };
    };
};

// Construct a request object from the metadata
var payload = {
    name: "Updated Sample Account"
};
var updateRequest = new Sdk.UpdateRequest("account", "0b9b8a43-e0dd-e911-a849-000d3a11e59b", payload);

// Use the request object to execute the function
Xrm.WebApi.online.execute(updateRequest).then(
    function (result) {
        if (result.ok) {
            console.log("Status: %s %s", result.status, result.statusText);
            // perform other operations as required;
        }
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

#### Delete a record

The following example demonstrates how to perform a Delete operation.

```JavaScript
var Sdk = window.Sdk || {};

/**
 * Request to execute a delete operation
 */
Sdk.DeleteRequest = function (entityReference) {
    this.entityReference = entityReference;

    this.getMetadata = function () {
        return {
            boundParameter: null,
            parameterTypes: {},
            operationType: 2, // This is a CRUD operation. Use '0' for actions and '1' for functions
            operationName: "Delete",
        };
    };
};

// Construct request object from the metadata
var entityReference = {
    entityType: "account",
    id: "0b9b8a43-e0dd-e911-a849-000d3a11e59b"
};
var deleteRequest = new Sdk.DeleteRequest(entityReference);

// Use the request object to execute the function
Xrm.WebApi.online.execute(deleteRequest).then(
    function (result) {
        if (result.ok) {
            console.log("Status: %s %s", result.status, result.statusText);
            // perform other operations as required;
        }
    },
    function (error) {
        console.log(error.message);
        // handle error conditions
    }
);
```

### Related topics


[Xrm.WebApi](../../xrm-webapi.md)


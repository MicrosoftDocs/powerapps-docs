---
title: "Xrm.WebApi.online.execute (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the Xrm.WebApi.online.execute method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d4e92999-3b79-4783-8cac-f656fc5f7fda
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
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
<td><p>Object that will be passed to the Web API endpoint to execute an action, function, or CRUD request. The object exposes a <b>getMetadata</b> method <u>via its prototype</u> that lets you define the metadata for the action, function or CRUD request you want to execute. The <b>getMetadata</b> method has the following parameters:</p>
<ul>
<li><b>boundParameter</b>: (Optional) String. The name of the bound parameter for the action or function to execute.
<ul><li>Specify <code>undefined</code> if you are executing a CRUD request.</li>
<li>Specify <code>null</code> if the action or function to execute is not bound to any table.</li>
<li>Specify <code>entity</code> in case the action or function to execute is bound to a table. </li></ul>
<li><b>operationName</b>: (Optional). String. Name of the action, function, or one of the following values if you are executing a CRUD request: "Create", "Retrieve", "Update", or "Delete".</li>
<li><b>operationType</b>: (Optional). Number. Indicates the type of operation you are executing; specify one of the following values:
<br/><code>0: Action</code>
<br/><code>1: Function</code>
<br/><code>2: CRUD</code></li>
<li><b>parameterTypes</b>: Object. The metadata for parameter types. The object has the following values:
<ul>
<li><b>enumProperties</b>: (Optional) Object. The metadata for enum types. The object has two string values: <b>name</b> and <b>value</b></li>
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
<td><p>A function to call when operation is executed successfully. A response object is passed to the function with the following values:</p>
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

On success, returns a promise object with the values specified earlier in the description of **successCallback** function.

## Examples

### Execute an action

The following example demonstrates how to execute the <xref:Microsoft.Dynamics.CRM.WinOpportunity> action. The request object is created based on the action definition here: [Unbound actions](../../../../../data-platform/webapi/use-web-api-actions.md#unbound-actions)

```JavaScript
var Sdk = window.Sdk || {};
/**
 * Request to win an opportunity
 * @param {Object} opportunityClose - The opportunity close activity associated with this state change.
 * @param {number} status - Status of the opportunity.
 */
Sdk.WinOpportunityRequest = function(opportunityClose, status) {
    this.OpportunityClose = opportunityClose;
    this.Status = status;
};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.WinOpportunityRequest.prototype.getMetadata = function () {
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

var opportunityClose = {
    "opportunityid@odata.bind": "/opportunities(c60e0283-5bf2-e311-945f-6c3be5a8dd64)",
    "description": "Product and maintenance for 2018",
    "subject": "Contract for 2018"
}

// Construct a request object from the metadata
var winOpportunityRequest = new Sdk.WinOpportunityRequest(opportunityClose, 3);

// Use the request object to execute the function
Xrm.WebApi.online.execute(winOpportunityRequest).then(function (response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);
        // The WinOpportunityRequest does not return any response body content. So we
        // need not access the response.json() property.

        // Perform other operations as required.
    }
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
```


### Execute a function

The following example demonstrates how to execute the <xref:Microsoft.Dynamics.CRM.WhoAmI> function:

```JavaScript
var Sdk = window.Sdk || {};
/**
 * Request to execute WhoAmI function
 */
Sdk.WhoAmIRequest = function () { };

// NOTE: The getMetadata property should be attached to the function prototype instead of the
//       function object itself.
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
Xrm.WebApi.online.execute(whoAmIRequest)
.then(function (response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);

        // Use response.json() to access the content of the response body.
        return response.json();
    }
}
)
.then(function (responseBody) {
    console.log("User Id: %s", responseBody.UserId);
    // perform other operations as required;
})
.catch(function (error) {
    console.log(error.message);
    // handle error conditions
});
```

The following example demonstrates how to execute the <xref:Microsoft.Dynamics.CRM.CalculateRollupField> function:

```JavaScript
var Sdk = window.Sdk || {};

Sdk.CalculateRollupFieldRequest = function(target, fieldName) {
    this.Target = target;
    this.FieldName = fieldName;
};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
//       function object itself.
Sdk.CalculateRollupFieldRequest.prototype.getMetadata = function() {
    return {
        boundParameter: null,
        parameterTypes: {
            "Target": {
                "typeName": "mscrm.crmbaseentity",
                "structuralProperty": 5
            },
            "FieldName": {
                "typeName": "Edm.String",
                "structuralProperty": 1
            }
        },
        operationType: 1, // This is a function. Use '0' for actions and '2' for CRUD
        operationName: "CalculateRollupField"
    };
};

// Create variables to point to a quote record and to a specific column
var quoteId = {
    "@odata.type": "Microsoft.Dynamics.CRM.quote",
    "quoteid": "7bb01e55-2394-ea11-a811-000d3ad97943"
};

// The roll-up column for which we want to force a re-calculation
var fieldName = "new_test_rollup";

// Create variable calculateRollupFieldRequest and pass those variables created above
var calculateRollupFieldRequest = new Sdk.CalculateRollupFieldRequest(quoteId, fieldName);

// Use the request object to execute the function
Xrm.WebApi.online.execute(calculateRollupFieldRequest)
.then(function(response) {
    if (response.ok) { // If a response was received.
        console.log("Status: %s %s", response.status, response.statusText);

        // Use response.json() to access the content of the response body.
        return response.json();
    }
})
.then(function(responseBody) { 
    //Do something with the response
    console.log("The response is: %s", responseBody);
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
```

The following example demonstrates how to execute the <xref:Microsoft.Dynamics.CRM.RetrieveDuplicates> function:

```JavaScript
var Sdk = window.Sdk || {};

Sdk.RetrieveDuplicatesRequest = function(businessEntity, matchingEntityName, pagingInfo) {
    this.BusinessEntity = businessEntity;
    this.MatchingEntityName = matchingEntityName;
    this.PagingInfo = pagingInfo;

};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.RetrieveDuplicatesRequest.prototype.getMetadata = function() {
    return {
        boundParameter: null,
        parameterTypes: {
            "BusinessEntity": {
                "typeName": "mscrm.crmbaseentity",
                "structuralProperty": 5 // Entity Type
            },
            "MatchingEntityName": {
                "typeName": "Edm.String",
                "structuralProperty": 1 // Primitive Type
            },
            "PagingInfo": {
                "typeName:": "mscrm.PagingInfo", // Complex Type
                "structuralProperty": 5
            }
        },
        operationType: 1, // This is a function. Use '0' for actions and '2' for CRUD
        operationName: "RetrieveDuplicates",
    };
};

// Create a variable to point to a contact record and with specific data in the needed columns
var contactRecord = {
    "@odata.type": "Microsoft.Dynamics.CRM.contact",
    "firstname": "Test",
    "lastname": "Account"
};

// Create a paging object to keep track of the current page and how many records we get per page
var pagingInfo = {
    "PageNumber": 1,
    "Count": 10
};

// Create the variable retrieveDuplicatesRequest to build the request
var retrieveDuplicatesRequest = new Sdk.RetrieveDuplicatesRequest(contactRecord, "contact", pagingInfo);

// Use the request object to execute the function
Xrm.WebApi.online.execute(retrieveDuplicatesRequest)
.then(function (response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);

        // Use response.json() to access the content of the response body.
        return response.json();
    }
})
.then(function(responseBody) { 
    // Do something with the response
    console.log("The response is: %s", responseBody);
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
```

The following example demonstrates how to execute the <xref:Microsoft.Dynamics.CRM.InitializeFrom> function:
```JavaScript
var Sdk = window.Sdk || {};

Sdk.InitializeFromRequest = function (
  entityMoniker,
  targetEntityName,
  targetFieldType
) {
  this.EntityMoniker = entityMoniker;
  this.TargetEntityName = targetEntityName;
  this.TargetFieldType = targetFieldType;
};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.InitializeFromRequest.prototype.getMetadata = function () {
  return {
    boundParameter: null,
    parameterTypes: {
      EntityMoniker: {
        typeName: "mscrm.crmbaseentity",
        structuralProperty: 5, //Entity Type
      },
      TargetEntityName: {
        typeName: "Edm.String",
        structuralProperty: 1, // PrimitiveType
      },
      TargetFieldType: {
        typeName: "Microsoft.Dynamics.CRM.TargetFieldType",
        structuralProperty: 3, // Enum Type
        enumProperties: [
          {
            name: "All",
            value: 0,
          },
          {
            name: "ValidForCreate",
            value: 1,
          },
          {
            name: "ValidForUpdate",
            value: 2,
          },
          {
            name: "ValidForRead",
            value: 3,
          },
        ],
      },
    },
    operationType: 1, // This is a function. Use '0' for actions and '2' for CRUD
    operationName: "InitializeFrom",
  };
};

// Create a variable to point to tje parent account record
var parentAccountRecord = {
  "@odata.type": "Microsoft.Dynamics.CRM.account",
  accountid: "141da047-eaad-eb11-b1b4-000d3ac581a0",
};

// Create a variable for the target entity name
var targetEntityName = "account";

// Create a variable for the target field type
var targetFieldType = 0;

// Build the request
var initializeFromRequest = new Sdk.InitializeFromRequest(
  parentAccountRecord,
  targetEntityName,
  targetFieldType
);

// Execute the request
Xrm.WebApi.online.execute(initializeFromRequest)
.then(function (response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);

        // Use response.json() to access the content of the response body.
        return response.json();
    }
})
.then(function(responseBody) { 
    // Do something with the response
    console.log("The response is: %s", responseBody);
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});

```

### Perform CRUD operations

#### Create a record

The following example demonstrates how to perform a create operation.

```JavaScript
var Sdk = window.Sdk || {};

/**
 * Request to execute a create operation
 */
Sdk.CreateRequest = function(entityName, payload) {
    this.etn = entityName;
    this.payload = payload;
};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.CreateRequest.prototype.getMetadata = function () {
    return {
        boundParameter: null,
        parameterTypes: {},
        operationType: 2, // This is a CRUD operation. Use '0' for actions and '1' for functions
        operationName: "Create",
    };
};
// Construct a request object from the metadata
var payload = {
    name: "Fabrikam Inc."
};
var createRequest = new Sdk.CreateRequest("account", payload);

// Use the request object to execute the function
Xrm.WebApi.online.execute(createRequest)
.then(function (response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);
        
        // The Create request does not return any response body content. So we
        // need not access the response.json() property.

        // Perform other operations as required.
    }
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
 ```
 
#### Retrieve a record

The following example demonstrates how to perform a retrieve operation.

```JavaScript
var Sdk = window.Sdk || {};

/**
 * Request to execute a retrieve operation
 */
Sdk.RetrieveRequest = function(entityReference, columns) {
    this.entityReference = entityReference;
    this.columns = columns;
};
// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.RetrieveRequest.prototype.getMetadata = function () {
    return {
        boundParameter: null,
        parameterTypes: {},
        operationType: 2, // This is a CRUD operation. Use '0' for actions and '1' for functions
        operationName: "Retrieve",
    };
};

// Construct request object from the metadata
var entityReference = {
    entityType: "account",
    id: "d2b6c3f8-b0fa-e911-a812-000d3a59fa22"
};
var retrieveRequest = new Sdk.RetrieveRequest(entityReference, ["name"]);

// Use the request object to execute the function
Xrm.WebApi.online.execute(retrieveRequest)
.then(function (response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);

        // Use response.json() to access the content of the response body.
        return response.json();
    }
})
.then(function(responseBody) {
    console.log("Name: %s", responseBody.name);
    
    // perform other operations as required;
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
```

#### Update a record

The following example demonstrates how to perform a update operation.

```JavaScript
var Sdk = window.Sdk || {};


/**
 * Request to execute an update operation
 */
Sdk.UpdateRequest = function(entityName, entityId, payload) {
    this.etn = entityName;
    this.id = entityId;
    this.payload = payload;
};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.UpdateRequest.prototype.getMetadata = function () {
    return {
        boundParameter: null,
        parameterTypes: {},
        operationType: 2, // This is a CRUD operation. Use '0' for actions and '1' for functions
        operationName: "Update",
    };
};

// Construct a request object from the metadata
var payload = {
    name: "Updated Sample Account"
};
var updateRequest = new Sdk.UpdateRequest("account", "d2b6c3f8-b0fa-e911-a812-000d3a59fa22", payload);

// Use the request object to execute the function
Xrm.WebApi.online.execute(updateRequest)
.then(function (response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);

        // The Update request does not return any response body content. So we
        // need not access the response.json() property.
        
        // perform other operations as required;
    }
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
```

#### Delete a record

The following example demonstrates how to perform a delete operation.

```JavaScript
var Sdk = window.Sdk || {};

/**
 * Request to execute a delete operation
 */
Sdk.DeleteRequest = function(entityReference) {
    this.entityReference = entityReference;
};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.DeleteRequest.prototype.getMetadata = function () {
        return {
            boundParameter: null,
            parameterTypes: {},
            operationType: 2, // This is a CRUD operation. Use '0' for actions and '1' for functions
            operationName: "Delete",
        };
    };
};
};

// Construct request object from the metadata
var entityReference = {
    entityType: "account",
    id: "d2b6c3f8-b0fa-e911-a812-000d3a59fa22"
};
var deleteRequest = new Sdk.DeleteRequest(entityReference);

// Use the request object to execute the function
Xrm.WebApi.online.execute(deleteRequest)
.then(function(response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);
        
        // The Delete request does not return any response body content. So we
        // need not access the response.json() property.

        // perform other operations as required;
    }
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
```

### Associate a record
The following code sample demonstrates how to perform an Associate operation on collection-valued navigation properties (Many-To-One and Many-To-Many relationships). For single-valued navigation properties (One-To-Many relationships a.k.a Lookup columns), you can perform an Update operation as shown above or use [Xrm.WebApi.updateRecord](../updateRecord.md).

```JavaScript
var Sdk = window.Sdk || {};

/*
 * Request to execute an Associate operation.
 */
Sdk.AssociateRequest = function(target, relatedEntities, relationship) {
    this.target = target;
    this.relatedEntities = relatedEntities;
    this.relationship = relationship;
};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.AssociateRequest.prototype.getMetadata = function() {
    return {
        boundParameter: null,
        parameterTypes: {},
        operationType: 2, // Associate and Disassociate fall under the CRUD umbrella
        operationName: "Associate"
    }
};

// Construct the target EntityReference object
var target = {
    entityType: "account",
    id: "0b4abc7d-7619-eb11-8dff-000d3ac5c7f9"
};

// Construct the related EntityReferences that the Target will be associated with.
var relatedEntities = [
    {
        entityType: "contact",
        id: "180a9aad-7619-eb11-8dff-000d3ac5c7f9"
    },
    {
        entityType: "contact",
        id: "753c58b4-7619-eb11-8dff-000d3ac5c7f9"
    }
];

// The name of the existing relationship to associate on.
var relationship = "new_account_contact";

var manyToManyAssociateRequest = new Sdk.AssociateRequest(target, relatedEntities, relationship)

Xrm.WebApi.online.execute(manyToManyAssociateRequest)
.then(function(response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);

        // The Associate request does not return any response body content. So we
        // need not access the response.json() property.

        // perform other operations as required;
    }
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
```

### Disassociate a record
The following code sample demonstrates how to perform a Disassociate operation on collection-valued navigation properties (Many-To-One and Many-To-Many relationships). For single-valued navigation properties (One-To-Many relationships a.k.a Lookup columns), you can perform an Update operation as shown above or use [Xrm.WebApi.updateRecord](../updateRecord.md).

> [!NOTE]
> Unlike the Associate operation which allows associating the target entity record with multiple related entity records in a single operation, the Disassociate operation is limited to only disassociating one entity record from the target entity record per operation.

```JavaScript
var Sdk = window.Sdk || {};

/*
 * Request to execute a Disassociate operation.
 */
Sdk.DisassociateRequest = function(target, relatedEntityId, relationship) {
    this.target = target;
    this.relatedEntityId = relatedEntityId;
    this.relationship = relationship;
};

// NOTE: The getMetadata property should be attached to the function prototype instead of the
// function object itself.
Sdk.DisassociateRequest.prototype.getMetadata = function() {
    return {
        boundParameter: null,
        parameterTypes: {},
        operationType: 2, // Associate and Disassociate fall under the CRUD umbrella
        operationName: "Disassociate"
    }
};

// Construct the target EntityReference object
var target = {
    entityType: "account",
    id: "0b4abc7d-7619-eb11-8dff-000d3ac5c7f9"
};

// The GUID of the related entity record to disassociate.
var relatedEntityId = "180a9aad-7619-eb11-8dff-000d3ac5c7f9";

// The name of the existing relationship to disassociate from.
var relationship = "new_account_contact";

var manyToManyDisassociateRequest = new Sdk.DisassociateRequest(target, relatedEntityId, relationship)

Xrm.WebApi.online.execute(manyToManyDisassociateRequest)
.then(function(response) {
    if (response.ok) {
        console.log("Status: %s %s", response.status, response.statusText);

        // The Disassociate request does not return any response body content. So we
        // need not access the response.json() property.

        // perform other operations as required;
    }
})
.catch(function(error) {
    console.log(error.message);
    // handle error conditions
});
```

### Related topics


[Xrm.WebApi](../../xrm-webapi.md)



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]

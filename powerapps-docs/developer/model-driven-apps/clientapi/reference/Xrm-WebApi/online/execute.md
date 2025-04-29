---
title: "Xrm.WebApi.online.execute (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the Xrm.WebApi.online.execute method.
author: sriharibs-msft
ms.author: srihas
ms.date: 12/08/2023
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Xrm.WebApi.online.execute (Client API reference)

[!INCLUDE[./includes/execute-description.md](./includes/execute-description.md)]

> [!NOTE]
> This method is supported only for the online mode ([Xrm.WebApi.online](../online.md)).

## Syntax

`Xrm.WebApi.online.execute(request).then(successCallback, errorCallback);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`request`|Object|Yes|Object that will be passed to the Web API endpoint to execute an action, function, or CRUD request. The object exposes a `getMetadata` method *via its prototype* that lets you define the metadata for the action, function or CRUD request you want to execute. See [request.getMetadata method](#requestgetmetadata-method)|
|`successCallback`|Function|No|A function to call when operation is executed successfully. See [Return Value](#return-value)|
|`errorCallback`|Function|No|A function to call when the operation fails. An object with the following properties is passed:<br /> - `errorCode`: Number. The error code as a positive decimal number.  For example, the error code documented as `0x80040333` will be returned as `2147746611`.<br /> - `message`: String. An error message describing the issue.|

### request.getMetadata method

The `getMetadata` method has the following parameters:

|Name|Type|Required|Description|
|---|---|---|---|
|`boundParameter`|String|No|The name of the bound parameter for the action or function to execute.<br />- Specify `undefined` if you are executing a CRUD request.<br />- Specify `null` if the action or function to execute is not bound to any table.<br />- Specify `entity` in case the action or function to execute is bound to a table.|
|`operationName`|String|No|Name of the action, function, or one of the following values if you are executing a CRUD request: `Create`, `Retrieve`, `Update`, or `Delete`.|
|`operationType`|Number|No|Indicates the type of operation you are executing; specify one of the following values:<br/>- `0`: Action<br/>- `1`: Function<br/>- `2`: CRUD|
|`parameterTypes`|Object|Yes|The metadata for parameter types. The object has the following values:<br />`enumProperties` : (Optional) Object. The metadata for enum types. The object has two string values: `name` and `value`<br />`structuralProperty` : Number. The category of the parameter type. Specify one of the following values:<br />- `0`: Unknown<br />- `1`: PrimitiveType<br />- `2`: ComplexType<br />- `3`: EnumerationType<br />- `4`: Collection<br />- `5`: EntityType<br />`typeName` : String. The fully qualified name of the parameter type.|

## Return Value

On success, returns a promise object to the `successCallback` with the following properties:

|Name|Type|Description|
|---|---|---|
|`body`(Deprecated)|Object|Response body.|
|`headers`|Object|Response headers.|
|`ok`|Boolean|Indicates whether the request was successful.|
|`status`|Number|Numeric value in the response status code. For example: `200`|
|`statusText`|String|Description of the response status code. For example: `OK`|
|`type`(Deprecated)|String|Response type. Values are: the empty string (default), `arraybuffer`, `blob`, `document`, `json`, and `text`.|
|`url`|String|Request URL of the action, function, or CRUD request that was sent to the Web API endpoint.|
|`json`|Promise|Parameter to the callback delegate is of type any (JSON object).|
|`text`|Promise|Parameter to the callback delegate is a String.|

## Examples

Find these examples below:

- [Execute an action](#execute-an-action)
- [Execute a function](#execute-a-function)
- [Create a record](#create-a-record)
- [Retrieve a record](#retrieve-a-record)
- [Update a record](#update-a-record)
- [Delete a record](#delete-a-record)
- [Associate a record](#associate-a-record)
- [Disassociate a record](#disassociate-a-record)

> [!TIP]
> You can use the [Dataverse REST Builder](https://github.com/GuidoPreite/DRB) to generate JavaScript code that uses the `Xrm.WebApi.online.execute` method.

### Execute an action

The following example demonstrates how to execute the `WinOpportunity` action found in the Dynamics 365 for Sales solution. The request object is created based on the action definition here: [Unbound actions](../../../../../data-platform/webapi/use-web-api-actions.md#unbound-actions)

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

The following example demonstrates how to execute the [WhoAmI function](xref:Microsoft.Dynamics.CRM.WhoAmI):

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
The following code sample demonstrates how to perform an Associate operation on collection-valued navigation properties (One-To-Many and Many-To-Many relationships). For single-valued navigation properties (Many-To-One relationships a.k.a Lookup columns), you can perform an Update operation as shown above or use [Xrm.WebApi.updateRecord](../updateRecord.md).

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
The following code sample demonstrates how to perform a Disassociate operation on collection-valued navigation properties (One-To-Many and Many-To-Many relationships). For single-valued navigation properties (Many-To-One relationships a.k.a Lookup columns), you can perform an Update operation as shown above or use [Xrm.WebApi.updateRecord](../updateRecord.md).

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

### Related articles


[Xrm.WebApi](../../xrm-webapi.md)



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]

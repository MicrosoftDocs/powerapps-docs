---
title: "Create a Custom API with code (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can write code create custom APis." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/13/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create a Custom API with code

> [!NOTE]
> This is an advanced topic that assumes you have already read and understood these topics:
> - [Create and use Custom APIs](custom-api.md)
> - [Create a Custom API in the maker portal](create-custom-api-maker-portal.md)
>
> You should also understand how to create Microsoft Dataverse records, using either the Web API or Organization Service. For more information see:
> - [Create an entity record using the Web API](webapi/create-entity-web-api.md)
> - [Create entities using the Organization Service](org-service/entity-operations-create.md)

Because Custom API data is saved in tables, you can programmatically create new APIs using either the Web API or the Organization Service.

The tables in [Create and use Custom APIs](custom-api.md) describe all the properties you can set using code. For the following code examples, please refer to the following tables:

- [CustomAPI Table Columns](customapi-table-columns.md)
- [CustomAPIRequestParameter Table Columns](customapirequestparameter-table-columns.md)
- [CustomAPIResponseProperty Table Columns](customapiresponseproperty-table-columns.md)


## Create a Custom API using the Web API

This example shows the creation of a Custom API action with one request parameter and one response property in a single operation. More information: [Create related table rows in one operation](webapi/create-entity-web-api.md#create-related-table-rows-in-one-operation)

This custom api is created as part of a solution with the uniquename `CustomAPIExample` and is associated with a plug-in type with id = `3926874e-387b-4045-94b2-a5cafe44b06f`.

**Request**

```http
POST [Organization URI]/api/data/v9.1/customapis HTTP/1.1
MSCRM.SolutionUniqueName: CustomAPIExample
Content-Type: application/json

{
    "allowedcustomprocessingsteptype": 0,
    "boundentitylogicalname": null,
    "uniquename": "sample_CustomAPIExample",
    "displayname": "Custom API Example",
    "bindingtype": 0,
    "executeprivilegename": null,
    "isfunction": false,
    "isprivate": false,
    "name": "sample_CustomAPIExample",
    "description": "A simple example of a Custom API",
    "iscustomizable": {
                "Value": false
            },
    "CustomAPIRequestParameters": [
        {
            "type": 10,
            "isoptional": false,
            "displayname": "Custom API Example String Parameter",
            "name": "sample_CustomAPIExample.StringParameter",
            "uniquename": "StringParameter",
            "logicalentityname": null,
            "description": "The StringParameter request parameter for Custom API Example",
            "iscustomizable": {
                "Value": false
                }
        }
    ],
    "CustomAPIResponseProperties": [
        {
            "type": 10,
            "name": "sample_CustomAPIExample.StringProperty",
            "logicalentityname": null,
            "displayname": "Custom API Example String Property",
            "uniquename": "StringProperty",
            "description": "The StringProperty response property for Custom API Example",
            "iscustomizable": {
                "Value": false
                }
        }
    ],
    "PluginTypeId@odata.bind": "plugintypes(3926874e-387b-4045-94b2-a5cafe44b06f)"
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.1/customapis(b532b299-4684-eb11-a812-0022481d298f)
```

## Create a Custom API using the Organization Service

This code uses the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> with a early-bound programming style: More information: 

- [Use CrmServiceClient constructors to connect to Dataverse](xrm-tooling/use-crmserviceclient-constructors-connect.md)
- [Late-bound and Early-bound programming using the Organization service](org-service/early-bound-programming.md)
- [Create entities using the Organization Service](org-service/entity-operations-create.md)

This example shows the creation of a Custom API action with one request parameter and one response property in a single operation. More information: [Create related entities in one operation](org-service/entity-operations-create.md#create-related-entities-in-one-operation)

This custom api is created as part of a solution with the uniquename `CustomAPIExample` and is associated with a plug-in type with id = `3926874e-387b-4045-94b2-a5cafe44b06f`.

```csharp
string conn = $@"
    Url = {url};
    AuthType = OAuth;
    UserName = {userName};
    Password = {password};
    AppId = 51f81489-12ee-4a9e-aaae-a2591f45987d;
    RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97;
    LoginPrompt=Auto;
    RequireNewInstance = True";

var service = new CrmServiceClient(conn);

//The plug-in type
var pluginType = new EntityReference("plugintype", new Guid("3926874e-387b-4045-94b2-a5cafe44b06f"));
var solutionUniqueName = "CustomAPIExample";

//The custom API
var customAPI = new CustomAPI
{
    AllowedCustomProcessingStepType = new OptionSetValue(0),//None
    BindingType = new OptionSetValue(0), //Global
    Description = "A simple example of a Custom API",
    DisplayName = "Custom API Example",
    ExecutePrivilegeName = null,
    IsFunction = false,
    IsPrivate = false,
    Name = "sample_CustomAPIExample",
    PluginTypeId = pluginType,
    UniqueName = "sample_CustomAPIExample",
    IsCustomizable = new BooleanManagedProperty(false),
    customapi_customapirequestparameter = new List<CustomAPIRequestParameter>()
    {
        new CustomAPIRequestParameter {
            Description = "The StringParameter request parameter for Custom API Example",
            DisplayName = "Custom API Example String Parameter",
            LogicalEntityName = null,
            IsOptional = false,
            Name = "sample_CustomAPIExample.StringParameter",
            Type = new OptionSetValue(10), //String
            UniqueName = "StringParameter",
            IsCustomizable = new BooleanManagedProperty(false)
        }
    },
    customapi_customapiresponseproperty = new List<CustomAPIResponseProperty>()
    {
        new CustomAPIResponseProperty {
            Description = "The StringProperty response property for Custom API Example",
            DisplayName = "Custom API Example String Property",
            Name = "sample_CustomAPIExample.StringProperty",
            Type = new OptionSetValue(10), //String
            UniqueName = "StringProperty",
            IsCustomizable = new BooleanManagedProperty(false)
        }
    }
};

var createReq = new CreateRequest
{
    Target = customAPI
};
createReq["SolutionUniqueName"] = solutionUniqueName;

Guid customAPIId = ((CreateResponse)service.Execute(createReq)).id;
```

### See also

[Create and use Custom APIs](custom-api.md)<br/>
[Create a Custom API in the maker portal](create-custom-api-maker-portal.md)<br/>
[Create a Custom API with solution files](create-custom-api-solution.md)<br/>


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
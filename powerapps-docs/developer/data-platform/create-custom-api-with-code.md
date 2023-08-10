---
title: "Create a custom API with code (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can write code create custom APis." # 115-145 characters including spaces. This abstract displays in the search result.
author: divkamath
ms.author: dikamath
ms.date: 09/27/2022
ms.topic: article
ms.subservice: dataverse-developer
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Create a custom API with code

> [!NOTE]
> This is an advanced topic that assumes you have already read and understood these topics:
> - [Create and use custom APIs](custom-api.md)
> - [Create a custom API using the plug-in registration tool](create-custom-api-prt.md)
>
> You should also understand how to create Microsoft Dataverse records, using either the Web API or Organization Service. For more information see:
> - [Create an entity record using the Web API](webapi/create-entity-web-api.md)
> - [Create entities using the Organization Service](org-service/entity-operations-create.md)

Because custom API data is saved in tables, you can programmatically create new APIs using either the Web API or the Organization Service.

The tables in [Custom API tables](custom-api-tables.md) describe all the properties you can set using code.

#### [SDK for .NET](#tab/sdk)

This code uses the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> with a early-bound programming style. You can also use <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient>. More information:

- [Use CrmServiceClient constructors to connect to Dataverse](xrm-tooling/use-crmserviceclient-constructors-connect.md)
- [Late-bound and Early-bound programming using the Organization service](org-service/early-bound-programming.md)
- [Create entities using the Organization Service](org-service/entity-operations-create.md)

This example shows the creation of a custom API action with one request parameter and one response property in a single operation. More information: [Create related entities in one operation](org-service/entity-operations-create.md#create-related-entities-in-one-operation)

This custom api is created as part of a solution with the uniquename `CustomAPIExample` and is associated with a plug-in type with id = `00000000-0000-0000-0000-000000000001`.

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

//var service = new ServiceClient(conn);
var service = new CrmServiceClient(conn);
// var service = new ServiceClient(conn);

//The plug-in type
var pluginType = new EntityReference("plugintype", new Guid("00000000-0000-0000-0000-000000000001"));
var solutionUniqueName = "CustomAPIExample";

//The custom API
var customAPI = new CustomAPI
{
    AllowedCustomProcessingStepType = new OptionSetValue(0),//None
    BindingType = new OptionSetValue(0), //Global
    Description = "A simple example of a custom API",
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
            Description = "The StringParameter request parameter for custom API Example",
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
            Description = "The StringProperty response property for custom API Example",
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

#### [Web API](#tab/webapi)

This example shows the creation of a custom API action with one request parameter and one response property in a single operation. More information: [Create related table rows in one operation](webapi/create-entity-web-api.md#create-related-table-rows-in-one-operation)

This custom api is created as part of a solution with the uniquename `CustomAPIExample` and is associated with a plug-in type with id = `00000000-0000-0000-0000-000000000001`.

**Request:**

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
    "description": "A simple example of a custom API",
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
            "description": "The StringParameter request parameter for custom API Example",
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
            "description": "The StringProperty response property for custom API Example",
            "iscustomizable": {
                "Value": false
                }
        }
    ],
    "PluginTypeId@odata.bind": "plugintypes(00000000-0000-0000-0000-000000000001)"
}
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.1/customapis(b532b299-4684-eb11-a812-0022481d298f)
```

---

### See also

[Create and use custom APIs](custom-api.md)<br/>
[Custom API tables](custom-api-tables.md)<br/>
[Create a custom API using the plug-in registration tool](create-custom-api-prt.md)<br/>
[Create a custom API in Power Apps](create-custom-api-maker-portal.md)<br/>
[Create a custom API with solution files](create-custom-api-solution.md)<br/>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

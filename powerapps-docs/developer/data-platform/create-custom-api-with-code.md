---
title: "Create a Custom API with code (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can write code create custom APis." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/26/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create a Custom API with code

[This topic is pre-release documentation and is subject to change.]

> [!NOTE]
> This is an advanced topic that assumes you have already read and understood these topics:
> - [Create and use Custom APIs](custom-api.md)
> - [Create a Custom API in the maker portal](create-custom-api-maker-portal.md)
>
> You should also understand how to create Microsoft Dataverse records, using either the Web API or Organization Service. For more information see:
> - [Create an entity record using the Web API](webapi/create-entity-web-api.md)
> - [Create entities using the Organization Service](org-service/entity-operations-create.md)

Because Custom API data is saved in entities, you can programmatically create new APIs using either the Web API or the Organization Service.

The tables in [Create and use Custom APIs](custom-api.md) describe all the properties you can set using code. For the following code examples, please refer to the following tables:

- [CustomAPI entity attributes](custom-api.md#customapi-entity-attributes)
- [CustomAPIRequestParameter entity attributes](custom-api.md#customapirequestparameter-entity-attributes)
- [CustomAPIResponseProperty entity attributes](custom-api.md#customapiresponseproperty-entity-attributes)

> [!NOTE]
> Because of this known issue: [Custom API and related records cannot be created using one operation](custom-api.md#custom-api-and-related-records-cannot-be-created-using-one-operation) you cannot currently define a custom API in a single request using either the Web API or Organization Service. These examples show creating the items individually and associating them with the Custom API.

## Create a Custom API using the Web API

This sample uses the [CDSWebApiService class library (C#)](webapi/samples/cdswebapiservice.md), a helper used in the Web API samples.

```csharp
using (CDSWebApiService svc = new CDSWebApiService(config))
{
    Console.WriteLine("--Starting Custom API Create --");

    //The custom API
    var customApi = new JObject() {
        { "allowedcustomprocessingsteptype", 0}, //None
        { "bindingtype", 0 }, //Global
        { "description", "A simple example of a Custom API" },
        { "displayname", "Custom API Example" },
        { "executeprivilegename", null },
        { "isfunction", false}, //False
        { "isprivate", false}, //False
        { "name", "sample_CustomAPIExample"},
        { "PluginTypeId@odata.bind",  pluginTypeReference},//Reference to the plug-in type
        { "uniquename", "sample_CustomAPIExample"}
    };

    var retrievedcustomApi = svc.PostGet("customapis", customApi);
    var customApiReference = $"customapis({retrievedcustomApi["customapiid"]})";
    Guid customapiId = new Guid((string)retrievedcustomApi["customapiid"]);

    //A Custom API Request Parameter
    var stringparameter = new JObject() {
        { "description", "The StringParameter request parameter for Custom API Example"},
        { "displayname", "Custom API Example String Parameter"},
        { "isoptional", false}, //False
        { "name", "sample_CustomAPIExample.StringParameter"},
        { "type", 10}, //String
        { "uniquename", "StringParameter"},
        { "CustomAPIId@odata.bind", customApiReference} //Refers to the Custom API
    };

    var retrievedParameter = svc.PostGet("customapirequestparameters", stringparameter);
    Guid parameterid = new Guid((string)retrievedParameter["customapirequestparameterid"]);

    //A Custom API Response Property
    var stringproperty = new JObject() {
        { "description", "The StringProperty response property for Custom API Example"},
        { "displayname", "Custom API Example String Property"},
        { "name", "sample_CustomAPIExample.StringProperty"},
        { "type", 10}, //String
        { "uniquename", "StringProperty"},
        { "CustomAPIId@odata.bind", customApiReference} //Refers to the Custom API
    };

    var retrievedProperties = svc.PostGet("customapiresponseproperties", stringproperty);
    Guid propertyid = new Guid((string)retrievedProperties["customapiresponsepropertyid"]);

    var addCustomAPI = new JObject {
        { "ComponentId", customapiId },
        { "ComponentType", 10546},
        { "SolutionUniqueName", solutionUniqueName},
        { "AddRequiredComponents", true}
    };
    //Add the Custom API to the solution.
    svc.Post("AddSolutionComponent", addCustomAPI);

    var addParameter = new JObject {
        { "ComponentId", parameterid },
        { "ComponentType", 10547},
        { "SolutionUniqueName", solutionUniqueName},
        { "AddRequiredComponents", true}
    };
    //Add the request parameter to the solution.
    svc.Post("AddSolutionComponent", addParameter);

    var addProperty = new JObject {
        { "ComponentId", propertyid },
        { "ComponentType", 10548},
        { "SolutionUniqueName", solutionUniqueName},
        { "AddRequiredComponents", true}
    };
    //Add the response property to the solution.
    svc.Post("AddSolutionComponent", addProperty);

}
```

## Create a Custom API using the Organization Service

This code uses the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> with a late-bound programming style: More information: 

- [Use CrmServiceClient constructors to connect to Dataverse](xrm-tooling/use-crmserviceclient-constructors-connect.md)
- [Late-bound and Early-bound programming using the Organization service](org-service/early-bound-programming.md)
- [Create entities using the Organization Service](org-service/entity-operations-create.md)


The following code will create a Custom API with one request parameter and one response property. It will associate the custom api with an existing plug-in type, and finally it will add each of the new items to the solution with the unique name `CustomAPIExample` using the `AddSolutionComponent` message.

```csharp
string conn = $@"
    Url = {url};
    AuthType = Office365;
    UserName = {userName};
    Password = {password};
    RequireNewInstance = True";

var svc = new CrmServiceClient(conn);

//The plug-in type
var pluginType = new EntityReference("plugintype", new Guid("3926874e-387b-4045-94b2-a5cafe44b06f"));
var solutionUniqueName = "CustomAPIExample";

//The custom API
var customApi = new Entity("customapi")
{
    Attributes = {
        { "allowedcustomprocessingsteptype", new OptionSetValue(0)}, //None
        { "bindingtype", new OptionSetValue(0)}, //Global
        { "description","A simple example of a Custom API" },
        { "displayname","Custom API Example" },
        { "executeprivilegename", null },
        { "isfunction", false}, //False
        { "isprivate", false}, //False
        { "name","sample_CustomAPIExample"},
        { "plugintypeid", pluginType},//Reference to the plug-in type
        { "uniquename","sample_CustomAPIExample"}
    }
};

Guid customApiId = svc.Create(customApi);
//Reference to the custom API
var customApiReference = new EntityReference("customapi", customApiId);

//A Custom API Request Parameter
var stringparameter = new Entity("customapirequestparameter")
{
    Attributes = {
        { "description", "The StringParameter request parameter for Custom API Example"},
        { "displayname", "Custom API Example String Parameter"},
        { "logicalentityname", null},
        { "isoptional", false}, //False
        { "name", "sample_CustomAPIExample.StringParameter"},
        { "type", new OptionSetValue(10)}, //String
        { "uniquename", "StringParameter"},
        { "customapiid", customApiReference} //Refers to the Custom API
    }
};

Guid stringparameterId = svc.Create(stringparameter);

//A Custom API Response Property
var stringproperty = new Entity("customapiresponseproperty")
{
    Attributes = {
        { "description", "The StringProperty response property for Custom API Example"},
        { "displayname", "Custom API Example String Property"},
        { "logicalentityname", null},
        { "name", "sample_CustomAPIExample.StringProperty"},
        { "type", new OptionSetValue(10)}, //String
        { "uniquename", "StringProperty"},
        { "customapiid", customApiReference} //Refers to the Custom API
    }
};
Guid stringpropertyId = svc.Create(stringproperty);


var addCustomAPI = new AddSolutionComponentRequest { 
        ComponentId = customApiId,
        ComponentType = 10546,
        SolutionUniqueName = solutionUniqueName,
        AddRequiredComponents = true,
};
//Add the Custom API to the solution.
svc.Execute(addCustomAPI);

var addParameter = new AddSolutionComponentRequest
{
    ComponentId = stringparameterId,
    ComponentType = 10547,
    SolutionUniqueName = solutionUniqueName,
    AddRequiredComponents = true,
};
//Add the parameter to the solution.
svc.Execute(addParameter);

var addProperty = new AddSolutionComponentRequest
{
    ComponentId = stringpropertyId,
    ComponentType = 10548,
    SolutionUniqueName = solutionUniqueName,
    AddRequiredComponents = true,
};
//Add the property to the solution.
svc.Execute(addProperty);
```

### See also

[Create and use Custom APIs](custom-api.md)<br/>
[Create a Custom API in the maker portal](create-custom-api-maker-portal.md)<br/>
[Create a Custom API with solution files](create-custom-api-solution.md)<br/>


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
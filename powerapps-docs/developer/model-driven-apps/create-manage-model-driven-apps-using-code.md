---
title: "Create and manage model-driven apps using code | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about how to create, manage, and publish model-driven apps using code in PowerApps." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 4261c476-2eff-10e3-a334-d02e0cbbb9d5
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Create and manage model-driven apps using code

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/create-manage-custom-business-apps-using-code -->

In addition to creating a model-driven app using the PowerApps app designer, you can programmatically create and manage model-driven apps. 

> [!IMPORTANT]
> You don't have to write code to build model-driven apps if you don't need to! The app designer provides a much simpler and intuitive experience for building model-driven apps without having to write code by providing a tile-based information structure and simplified interface. Check it out here: [Design model-driven apps by using the app designer](../../maker/model-driven-apps/design-custom-business-apps-using-app-designer.md)  
  
Creating a model-driven app involves the following steps:
1. Create an [AppModule Entity](../common-data-service/reference/entities/appmodule.md) instance to define your app and its properties.
2. Add or remove components to your app such as entity, sitemap, and other components for your custom app using the <xref:Microsoft.Dynamics.CRM.AddAppComponents> and <xref:Microsoft.Dynamics.CRM.RemoveAppComponents> actions.
3. Check your app for any required components thats missing by using the <xref:Microsoft.Dynamics.CRM.ValidateApp> function.
4. Publish your app.
5. Associate appropriate security roles to your model-driven app to provide access to users.


## Create your business app and define its properties

You must have the System Administrator or System Customizer security role or equivalent permissions to be able to create an app. You can select from one of the following types for your app to specify the client that the app will the app will be used for: 
- **Web**:  This is the classic Dynamics 365 web browser client..
- **Unified Interface**: Runs on the new Unified Interface, which provides key accessibility and responsive design benefits. For more information about Unified Interface, see [Unified Interface framework for new apps](/dynamics365/get-started/whats-new/customer-engagement/new-in-version-9#unified-interface-framework-for-new-apps). 

You select the app type by specifying an integer value for the **clienttype** attribute: 2 for **Web** and 4 for **Unified Interface**. If you do not specify the type for an app, the type is set to **Web** by default. 

You must specify the following properties at a minimum to create an app:
- **name**: Unique for your app
- **uniquename**: This can be different than the name of your app, and can only have English characters and numbers. On creating this app, the name is automatically prefixed with your solution publisher prefix (for example 'new_'). 
- **webresourceid**: ID of the web resource that you want to be set as the image icon for your app. The system provides you with a default web resource (ID: 953b9fac-1e5e-e611-80d6-00155ded156f) that you can use as an icon for your app.

The following Web API request creates an Unified Interface type of an app:

```http
POST [Organization URI]/api/data/v9.0/appmodules HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
    "name": "SDKTestApp",
    "uniquename":"SDKTestApp",
    "webresourceid":"953b9fac-1e5e-e611-80d6-00155ded156f",
    "clienttype": 4
}
```

The response **OData-EntityId** header contains the Uri of the created app.

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.0/appmodules(dd621d4a-d898-e711-80e7-00155db763be)
```  

## Add or remove components from your business app

You can add or remove components in an app such as sitemap, entity, dashboard, business process flows, views, and forms that you want to be included in your business app. For detailed information about components that can be added to a business app, see [Add or edit app components in the app designer](../../maker/model-driven-apps/add-edit-app-components.md).

Use the <xref:Microsoft.Dynamics.CRM.AddAppComponents> action or the <xref:Microsoft.Crm.Sdk.Messages.AddAppComponentsRequest> message to add components to your business app. The action requires you to specify the following:
- **AppId**: ID of the app where you want to add components
- **Components** A collection of components to be added. You need to specify the ID and the entity type of the component you want to add. For a list of entity types in CDS for Apps Web API, see <xref:Microsoft.Dynamics.CRM.EntityTypeIndex>.

The following Web API request adds a view (savedquery) and a form (systemform) to your app:

```http
POST [Organization URI]/api/data/v9.0/AddAppComponents HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
	"AppId":"dd621d4a-d898-e711-80e7-00155db763be",
	"Components":[
		{
			"savedqueryid":"00000000-0000-0000-00aa-000000666000",
			"@odata.type":"Microsoft.Dynamics.CRM.savedquery"
		},
		{
			"formid":"c9e7ec2d-efca-4e4c-b3e3-f63c4bba5e4b",
			"@odata.type":"Microsoft.Dynamics.CRM.systemform"
		}
	]
}
```

To remove a component from an app, use the <xref:Microsoft.Dynamics.CRM.RemoveAppComponents> action or the <xref:Microsoft.Crm.Sdk.Messages.RemoveAppComponentsRequest> message. This action takes the same set of parameters as the **AddAppComponents** action.

The following Web API request removes a view (savedquery) from your app: 

```http
POST [Organization URI]/api/data/v9.0/RemoveAppComponents HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
	"AppId":"dd621d4a-d898-e711-80e7-00155db763be",
	"Components":[
		{
			"savedqueryid":"00000000-0000-0000-00aa-000000666000",
			"@odata.type":"Microsoft.Dynamics.CRM.savedquery"
		}
	]
}
```

## Validate your business app

Validating an app involves checking for any dependencies for the components you have added in your business app to ensure that your app works fine. This is the same as clicking **Validate** in the app designer. More information: [Validate your app](../../maker/model-driven-apps/validate-app.md)

Use the <xref:Microsoft.Dynamics.CRM.ValidateApp> function or the <xref:Microsoft.Crm.Sdk.Messages.ValidateAppRequest> message to validate your app. The following Web API request shows how to validate your business app with ID: dd621d4a-d898-e711-80e7-00155db763be:

`GET [Organization URI]/api/data/v9.0/ValidateApp(AppModuleId=dd621d4a-d898-e711-80e7-00155db763be)`

If there are no validation errors, the response is as follows:

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.ValidateAppResponse",
    "AppValidationResponse": {
        "ValidationSuccess": true,
        "ValidationIssueList": []
    }
}
```

If there are validation issues in your app, the response displays errors/warnings in the **ValidationIssueList** collection:

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.ValidateAppResponse",
    "AppValidationResponse": {
        "ValidationSuccess": false,
        "ValidationIssueList": [
            {
                "ErrorType": "Error",
                "Message": "App does not contain Site Map",
                "DisplayName": null,
                "ComponentId": "00000000-0000-0000-0000-000000000000",
                "ComponentType": 0,
                "ComponentSubType": 0,
                "ParentEntityId": "00000000-0000-0000-0000-000000000000",
                "ParentEntityName": null,
                "CRMErrorCode": -2147155684,
                "RequiredComponents": []
            },
            {
                "ErrorType": "Warning",
                "Message": "Account doesn’t reference a form or view. App users will see all forms and views.",
                "DisplayName": null,
                "ComponentId": "00000000-0000-0000-0000-000000000000",
                "ComponentType": 0,
                "ComponentSubType": 0,
                "ParentEntityId": "00000000-0000-0000-0000-000000000000",
                "ParentEntityName": null,
                "CRMErrorCode": -2147155691,
                "RequiredComponents": []
            }
        ]
    }
}
```

## Publish your business app

After you have added required components to your model-driven app and validated it, you must publish it to make it available to users.

Use the <xref:Microsoft.Dynamics.CRM.PublishXml> action or the <xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest> messageto publish your model-driven app. The following request shows how to publish your business app with ID: dd621d4a-d898-e711-80e7-00155db763be:

```http
POST [Organization URI]/api/data/v9.0/PublishXml HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{  
  "ParameterXml":"<importexportxml><appmodules><appmodule>dd621d4a-d898-e711-80e7-00155db763be</appmodule></appmodules></importexportxml>"
}
```

## Manage access to business app using security roles

To provide users access to your apps so that they can access it from their **Settings** > **My Apps** area or the Dynamics 365 home page, you can associate security roles to your business apps. Users assigned to the associated security roles and can see and use your business apps in CDS for Apps. 

Use the **appmoduleroles_association** navigation property of the [AppModule Entity](../common-data-service/reference/entities/appmodule.md) entity to associate a business app with a security role. The following request shows how to associate a business app with a security role:

```http
POST [Organization URI]/api/data/v9.0/appmodules(dd621d4a-d898-e711-80e7-00155db763be)appmoduleroles_association/$ref HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{  
  "@odata.id":"[Organization URI]/api/data/v9.0/roles(<roleId>)"
}
```

To disassociate a security role from a business app, you use the DELETE request with the same navigation property. For example:

`DELETE	[Organization URI]/api/data/v9.0/appmodules(dd621d4a-d898-e711-80e7-00155db763be)/appmoduleroles_association/$ref?$id=[Organization URI]/api/data/v9.0/roles(<roleId)
`

## Manage your business apps and its components

This section provides you information information about retrieving your apps, updating app properties, retrieving app components, and deleting apps.

### Retrieve published apps
To retrieve published apps, use the following request:

`GET [Organization URI]/api/data/v9.0/appmodules?$select=name,clienttype`

### Retrieve unpublished apps
To retrieve unpublished apps, use the <xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple> function. For example:

`GET [Organization URI]/api/data/v9.0/appmodules/Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple()?$select=name,clienttype`

### Retrieve components in a published business app
To retrieve app components for a business app, use the <xref:Microsoft.Dynamics.CRM.RetrieveAppComponents> function or the <xref:Microsoft.Crm.Sdk.Messages.RetrieveAppComponentsRequest> message. For example:

`GET [Organization URI]/api/data/v9.0/RetrieveAppComponents(AppModuleId=dd621d4a-d898-e711-80e7-00155db763be)`

### Retrieve security roles associated with published business app

To retrieve the security roles associated with your business app, use the `$expand` system query option with the **appmoduleroles_association** navigation property. For example, here is the request to retrieve all the security roles associated to a business app with ID: dd621d4a-d898-e711-80e7-00155db763be:

`GET [Organization URI]/api/data/v9.0/appmodules(dd621d4a-d898-e711-80e7-00155db763be)?$expand=appmoduleroles_association&$select=name,appmoduleroles_association`

### Delete business apps

Use the DELETE request to delete a business app. For example:

`DELETE [Organization URI]/api/data/v9.0/appmodules(dd621d4a-d898-e711-80e7-00155db763be)`

## Client API support for business apps

You can use the following client APIs to work with business apps:

- [getCurrentAppName](clientapi/reference/xrm-utility/getglobalcontext/getcurrentappname.md)
- [getCurrentAppProperties](clientapi/reference/xrm-utility/getglobalcontext/getCurrentAppProperties.md)
- [getCurrentAppUrl](clientapi/reference/xrm-utility/getglobalcontext/getCurrentAppUrl.md) 
  
### See also  
[Design model-driven apps by using the app designer](../../maker/model-driven-apps/design-custom-business-apps-using-app-designer.md)
 
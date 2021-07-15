---
title: "Bypass Custom Business Logic (Microsoft Dataverse) | Microsoft Docs" 
description: "Make data changes which bypass custom business logic" 
ms.custom: ""
ms.date: 05/27/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" 
ms.subservice: dataverse-developer
ms.author: "jdaly" 
manager: "ryjones" 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Bypass Custom Business Logic

There are times when you want to be able to perform data operations without having custom business logic applied. For example, if you are going to import a lot of records which you know already conform to the data consistency logic for your business. You want this operation to be done as quickly as possible, so the additional time spent processing custom logic for each request is something you want to avoid.  

One option is to locate and disable the custom plug-ins that contain the business logic. But this means that the logic will be disabled for all users while those plug-ins are disabled. It also means that you have to take care to only disable the right plug-ins and remember to re-enable them when you are done.

The option described here allows you to disable custom synchronous plug-ins for specific requests sent by an application configured to use this option.

For these kinds of situations, you have the option to disable custom business logic which would normally be applied. There are two requirements:

- You must send the requests using the `BypassCustomPluginExecution` option.
- The user sending the requests must have the `prvBypassCustomPlugins` privilege. By default, only users with the system administrator security role have this privilege.

> [!NOTE]
> The `prvBypassCustomPlugins` is not available to be assigned in the UI at this time. You can add a privilege to a security role using the API. More information: [Adding the prvBypassCustomPlugins privilege to another role](#adding-the-prvbypasscustomplugins-privilege-to-another-role)

## What does this do?

This solution targets the custom synchronous business logic that has been applied for your organization. When you send requests that bypass custom business logic, all synchronous plug-ins and real-time workflows are disabled except:

- Plug-ins which are part of the core Microsoft Dataverse system or part of a solution where Microsoft is the publisher.
- Workflows included in a solution where Microsoft is the publisher.

System plug-ins define the core behaviors for specific entities. Without these plug-ins you would encounter data inconsistencies that may not be easily fixed.

Solutions shipped by Microsoft that use Dataverse such as Microsoft Dynamics 365 Customer Service, or Dynamics 365 Sales also include critical business logic that cannot be bypassed with this option.

> [!IMPORTANT]
> You may have purchased and installed solutions from other Independent Software Vendors (ISVs) which include their own business logic. The synchronous logic applied by these solutions will be bypassed. You should check with these ISVs before you use this option to understand what impact there may be if you use this option with data that their solutions use.

## How do I use the BypassCustomPluginExecution option?

You can use this option with either the Web API or the Organization service.

### Using the Web API

To apply this option using the Web API, pass `MSCRM.BypassCustomPluginExecution : true` as a header in the request.

**Example request:**

The following Web API request will create a new account record without custom business logic applied:

```http
POST https://yourorg.api.crm.dynamics.com/api/data/v9.1/accounts HTTP/1.1
MSCRM.BypassCustomPluginExecution: true
Authorization: Bearer [REDACTED]
Content-Type: application/json
Accept: */*

{
  "name":"Test Account"
}
```


### Using the Organization Service

There are two ways to use this with the Organization Service.

#### You can set CrmServiceClient.BypassPluginExecution Property to true

The following example sets the [CrmServiceClient.BypassPluginExecution Property](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient.bypasspluginexecution) when creating a new account record:

```csharp
var svc = new CrmServiceClient(conn);

svc.BypassPluginExecution = true;

var account = new Entity("account")
{
    Attributes = {
        { "name", "Test Account" }
    }
};

svc.Create(account);
```
Because this setting is applied to the service, it will remain set for all requests sent using the service until it is set to false.

#### You can set the value as an optional parameter with one of the Request classes

The following example sets the optional `BypassCustomPluginExecution` parameter when creating a new account record:

```csharp
var svc = new CrmServiceClient(conn);

var account = new Entity("account")
{
    Attributes = {
        { "name", "Test Account" }
    }
};

var createRequest = new CreateRequest
{
    Target = account
};
createRequest.Parameters.Add("BypassCustomPluginExecution", true);

svc.Execute(createRequest);
```
This optional parameter must be applied to each request individually. You cannot use this with the 7 other IOrganizationService Methods, such as Create, Update, Delete. You can only use the [Execute method](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.execute) using one of the classes that are derived from the [OrganizationRequest Class](/dotnet/api/microsoft.xrm.sdk.organizationrequest).

You can use this method for data operations you initiate in your plug-ins.

## Adding the prvBypassCustomPlugins privilege to another role

Because the `prvBypassCustomPlugins` is not available in the UI to set for different security roles, if you need to grant this privilege to another security role you must use the API. For example, you may want to grant this privilege to a user with the system customizer security role.

The `prvBypassCustomPlugins` privilege has the id `148a9eaf-d0c4-4196-9852-c3a38e35f6a1` in every organization.

### Using Web API

Associate the `prvBypassCustomPlugins` privilege to the security role using the `roleprivileges_association` collection-valued navigation property.

**Request**

```http
POST [Organization URI]/api/data/v9.1/roles(<id of role>)/roleprivileges_association/$ref HTTP/1.1
Content-Type: application/json   
Accept: application/json   
OData-MaxVersion: 4.0   
OData-Version: 4.0 

{  
"@odata.id":"[Organization URI]/api/data/v9.1/privileges(148a9eaf-d0c4-4196-9852-c3a38e35f6a1)"
} 
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```

More information: [Add a reference to a collection-valued navigation property](webapi/associate-disassociate-entities-using-web-api.md#add-a-reference-to-a-collection-valued-navigation-property).

### Using the Organization Service

Associate the `prvBypassCustomPlugins` privilege to the security role using the `roleprivileges_association` relationship.


```csharp
var roleId = new Guid(<id of role>);
service.Associate(
    "role",
    roleId,
    new Relationship("roleprivileges_association"),
    new EntityReferenceCollection {
        {
            new EntityReference("privilege", new Guid("148a9eaf-d0c4-4196-9852-c3a38e35f6a1"))
        }
    }
);
```

More information: [Associate and disassociate entities using the Organization Service](org-service/entity-operations-associate-disassociate.md).


## Frequently asked questions (FAQ)

### Does this bypass plug-ins for data operations by Microsoft plug-ins?

No. If a synchronous plug-in or real-time workflow in a Microsoft solution performs operations on other records, the logic for those operations are not bypassed. Only those synchronous plugins or real-time workflows that apply to the specific operation will be bypassed.

### Can I use this option for data operations I perform within a plug-in?

Yes, But only when the plug-in is running in the context of a user who has the `prvByPassPlugins` privilege. For the Organization Service, set the optional `BypassCustomPluginExecution` parameter on the class derived from [OrganizationRequest Class](/dotnet/api/microsoft.xrm.sdk.organizationrequest). You cannot use the CrmServiceClient in a plug-in.

### What about asychronous plug-in steps, asynchronous workflows and flows?

Asynchronous logic is not bypassed. Asynchronous logic doesn't significantly contribute to the cost of processing the records, therefore it is not by passed by this parameter.

## See also

[Web API: Compose HTTP requests and handle errors](webapi/compose-http-requests-handle-errors.md)<br />
[Passing optional parameters with a request](org-service/use-messages.md#passing-optional-parameters-with-a-request)


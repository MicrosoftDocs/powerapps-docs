---
title: "Bypass Custom Business Logic (Microsoft Dataverse) | Microsoft Docs" 
description: "Make data changes which bypass custom business logic." 
ms.date: 03/08/2023
ms.reviewer: jdaly
ms.topic: article
author: divkamath
ms.subservice: dataverse-developer
ms.author: dikamath
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - PHecke
  - JimDaly
  - LearningEveryday1
  - NHelgren
---
# Bypass Custom Business Logic

There are times when you want to be able to perform data operations without having custom business logic applied.  These scenarios typically involve bulk data operations where large numbers of records are being created, updated or deleted.

As a developer of a client application, you can pass special [optional parameters](optional-parameters.md) with your requests to control two types of custom business logic as described in the following table:


|Logic type|When to use|
|---------|---------|
|**Synchronous Logic**|To enable bulk data operation to be completed as quickly as possible. Use this when the data you are changing is known to meet the requirements of the organization or you have a plan to achieve this by other means. Bypass all custom synchronous logic so that each operation can complete faster, shortening the total time of the bulk operation.|
|**Power Automate Flows**|When flows triggered by bulk operations cause a backup within Dataverse that can impact performance. You can mitigate this by not triggering the flows.|

## Bypass Synchronous Logic

Use the `BypassCustomPluginExecution` optional parameter to bypass custom synchronous logic.

The alternative to using this optional parameter is to locate and disable the custom plug-ins that contain the synchronous business logic. But this means that the logic will be disabled for all users while those plug-ins are disabled. It also means that you have to take care to only disable the right plug-ins and remember to re-enable them when you are done.

Using the optional parameter allows you to disable custom synchronous plug-ins for specific requests sent by an application configured to use this option.

There are two requirements:

- You must send the requests using the `BypassCustomPluginExecution` optional parameter.
- The user sending the requests must have the `prvBypassCustomPlugins` privilege. By default, only users with the system administrator security role have this privilege.

> [!NOTE]
> The `prvBypassCustomPlugins` is not available to be assigned in the UI at this time. You can add a privilege to a security role using the API. More information: [Adding the prvBypassCustomPlugins privilege to another role](#adding-the-prvbypasscustomplugins-privilege-to-another-role)

### What does this do?

This solution targets the custom synchronous business logic that has been applied for your organization. When you send requests that bypass custom business logic, all synchronous plug-ins and real-time workflows are disabled except:

- Plug-ins which are part of the core Microsoft Dataverse system or part of a solution where Microsoft is the publisher.
- Workflows included in a solution where Microsoft is the publisher.

System plug-ins define the core behaviors for specific entities. Without these plug-ins you would encounter data inconsistencies that may not be easily fixed.

Solutions shipped by Microsoft that use Dataverse such as Microsoft Dynamics 365 Customer Service, or Dynamics 365 Sales also include critical business logic that cannot be bypassed with this option.

> [!IMPORTANT]
> You may have purchased and installed solutions from other Independent Software Vendors (ISVs) which include their own business logic. The synchronous logic applied by these solutions will be bypassed. You should check with these ISVs before you use this option to understand what impact there may be if you use this option with data that their solutions use.

### How do I use the BypassCustomPluginExecution option?

You can use this option with either the SDK for .NET or the Web API.

#### [SDK for .NET](#tab/sdk)

There are two ways to use this with the SDK for .NET.

##### Set the CrmServiceClient.BypassPluginExecution property

The following example sets the [CrmServiceClient.BypassPluginExecution Property](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.BypassPluginExecution) when creating a new account record:

```csharp
var service = new CrmServiceClient(connectionString);  

service.BypassPluginExecution = true;

var account = new Entity("account");
account["name"] = "Sample Account";

service.Create(account);
```

Because this setting is applied to the service, it remains set for all requests sent using the service until it's set to `false`.

> [!NOTE]
> This property is not available in the [Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), but it is available on the [Dataverse.Client.Extensions.CRUDExtentions methods](xref:Microsoft.PowerPlatform.Dataverse.Client.Extensions.CRUDExtentions).

##### Set the value as an optional parameter

The following example sets the optional `BypassCustomPluginExecution` parameter when creating a new account record using the [CreateRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest).

```csharp
static void DemonstrateBypassCustomPluginExecution(IOrganizationService service)
{
    Entity account = new("account");
    account["name"] = "Sample Account";

    CreateRequest request = new()
    {
        Target = account
    };
    request.Parameters.Add("BypassCustomPluginExecution", true);
    service.Execute(request);
}
```

You can use this method for data operations you initiate in your plug-ins when the calling user has the `prvBypassCustomPlugins` privilege.

#### [Using Web API](#tab/webapi)

To apply this option using the Web API, pass `MSCRM.BypassCustomPluginExecution : true` as a header in the request.

**Example request:**

The following Web API request will create a new account record without custom synchronous business logic applied:

```http
POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.BypassCustomPluginExecution: true

{
  "name":"Sample Account"
}
```

---

### Adding the prvBypassCustomPlugins privilege to another role

Because the `prvBypassCustomPlugins` privilege is not available in the UI to set for different security roles, if you need to grant this privilege to another security role you must use the API. For example, you may want to grant this privilege to a user with the system customizer security role.

The `prvBypassCustomPlugins` privilege has the id `148a9eaf-d0c4-4196-9852-c3a38e35f6a1` in every organization.

#### [SDK for .NET](#tab/sdk)

Associate the `prvBypassCustomPlugins` privilege to the security role using <xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest>.

```csharp
var request = new AddPrivilegesRoleRequest
{
    RoleId = new Guid("<id of role>"),
    Privileges = new[]{
        new RolePrivilege{
            PrivilegeId = new Guid("148a9eaf-d0c4-4196-9852-c3a38e35f6a1"),
            Depth = PrivilegeDepth.Global
        }
    }
};
svc.Execute(request);

```
#### [Using Web API](#tab/webapi)

Associate the `prvBypassCustomPlugins` privilege to the security role using the [AddPrivilegesRole Action](xref:Microsoft.Dynamics.CRM.AddPrivilegesRole).

**Request**

```http
POST [Organization URI]/api/data/v9.1/roles(<id of role>)/Microsoft.Dynamics.CRM.AddPrivilegesRole HTTP/1.1
Content-Type: application/json   
Accept: application/json   
OData-MaxVersion: 4.0   
OData-Version: 4.0 

{
  "Privileges": [
    {
      "PrivilegeId": "148a9eaf-d0c4-4196-9852-c3a38e35f6a1",
      "Depth": "3"
    }
  ]
}
```

You must set the <xref:Microsoft.Dynamics.CRM.RolePrivilege?text=RolePrivilege>.`Depth` property to <xref:Microsoft.Dynamics.CRM.PrivilegeDepth?text=PrivilegeDepth>.`Global` (`3`) because this is a global privilege.

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```

---

### Frequently asked questions for bypassing synchronous logic (FAQ)

Following are frequently asked questions about using the `BypassCustomPluginExecution` optional parameter to bypass synchronous business logic.
#### Does this bypass plug-ins for data operations by Microsoft plug-ins?

No. If a synchronous plug-in or real-time workflow in a Microsoft solution performs operations on other records, the logic for those operations are not bypassed. Only those synchronous plugins or real-time workflows that apply to the specific operation will be bypassed.

#### Can I use this option for data operations I perform within a plug-in?

Yes, but only when the plug-in is running in the context of a user who has the `prvByPassPlugins` privilege. For the Organization Service, set the optional `BypassCustomPluginExecution` parameter on the class derived from [OrganizationRequest Class](xref:Microsoft.Xrm.Sdk.OrganizationRequest). You cannot use the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> or <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> classes in a plug-in.

#### What about asychronous plug-in steps, asynchronous workflows and flows?

Asynchronous logic is not bypassed. Asynchronous logic doesn't significantly contribute to the cost of processing the records, therefore it is not by passed by this parameter.

## Bypass Power Automate Flows

When bulk data operations occur that trigger flows, Dataverse creates system jobs to execute the flows. When the number of system jobs is very large, it may cause performance issues for the system. If this occurs, you can choose to bypass triggering the flows by using the `SuppressCallbackRegistrationExpanderJob` optional parameter.

The [CallbackRegistration table](reference/entities/callbackregistration.md) manages flow triggers, and there's an internal operation called *expander* that starts the registered flows.

> [!NOTE]
> When this option is used, the flow owners will not receive a notification that their flow logic was bypassed.

### When to bypass Power Automate Flows

People have added flows for business reasons and they shouldn't be bypassed without careful consideration. Be sure to consider the [Mitigation strategies](#mitigation-strategies) mentioned below.


Use this option if you see performance issues after bulk operations occur. You should look for a large number of **CallbackRegistration Expander Operation** system jobs with a [StatusCode](reference/entities/asyncoperation.md#BKMK_StatusCode) set to `0` : **Waiting for Resources**.


You can use the following queries to get information about the status of these jobs.

If the total count is greater than 50,000, these queries will return the following error.

> Name: `AggregateQueryRecordLimitExceeded`<br />
> Code: `0x8004E023`<br />
> Number: `-2147164125`<br />
> Message: `The maximum record limit is exceeded. Reduce the number of records.`

> [!NOTE]
> If the queries do not return an error, the number of queued jobs is not likely to be the issue. Typically, the number of queued jobs exceeds 50,000 records before performance issues will occur.

#### [SDK for .NET](#tab/sdk)


```csharp
static void RetrieveCallbackRegistrationExpanderStatus(IOrganizationService service)
{
    string fetchXml = @"<fetch aggregate='true'>
        <entity name='asyncoperation'>
        <attribute name='statuscode' alias='statuscode' groupby='true' />
        <attribute name='statuscode' alias='count' aggregate='count' />
        <filter>
            <condition attribute='operationtype' operator='eq' value='79' />
        </filter>
        </entity>
    </fetch>";

    FetchExpression fetchExpression = new(fetchXml);

    EntityCollection response = service.RetrieveMultiple(fetchExpression);

    foreach (Entity result in response.Entities)
    {
        string statusCode = result.FormattedValues["statuscode"];
        int count = (int)((AliasedValue)result["count"]).Value;
        Console.WriteLine($"{statusCode}: {count}");
    }
}
```

**Output:**

```
Canceled: 4101
Failed: 13
Waiting for Resources: 50,000
```

#### [Using Web API](#tab/webapi)


**Request**

```http
GET [Organization URI]/asyncoperations?$filter=operationtype eq 79&$apply=groupby((statuscode),aggregate($count as count)) HTTP/1.1
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
Content-Type: application/json   
Accept: application/json   
OData-MaxVersion: 4.0   
OData-Version: 4.0 
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#asyncoperations",
    "value": [

        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Canceled",
            "statuscode": 32,
            "count@OData.Community.Display.V1.FormattedValue": "4,101",
            "count": 4101
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Failed",
            "statuscode": 31,
            "count@OData.Community.Display.V1.FormattedValue": "13",
            "count": 13
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Waiting for Resources",
            "statuscode": 0,
            "count@OData.Community.Display.V1.FormattedValue": "50,000",
            "count": 50000
        }
    ]
}

```

---

### How to bypass Power Automate flows

How you bypass flows depends on whether you are using the SDK for .NET or Web API.

> [!NOTE]
> For data operations initiated within plug-ins, you must use the SDK for .NET.

### [SDK for .NET](#tab/sdk)

```csharp
static void DemonstrateSuppressCallbackRegistrationExpanderJob(IOrganizationService service)
{
    Entity account = new("account");
    account["name"] = "Sample Account";

    CreateRequest request = new()
    {
        Target = account
    };
    request.Parameters.Add("SuppressCallbackRegistrationExpanderJob", true);
    service.Execute(request);
}
```

### [Web API](#tab/webapi)

**Request**

```http
POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.SuppressCallbackRegistrationExpanderJob: true

{
    "name":"Sample Account"
}
```

---

### Mitigation strategies

Bypassing flows using this optional parameter will result in business logic expected by the flow owner to not be executed. They will not have any notification that their logic was bypassed.  It is important that this be communicated to flow owners so that they will know when and why this was done. They can then determine whether or how to apply their logic.

People can create child flows which contain logic that could be invoked by multiple triggers, even manually. If the logic is contained within a child flow, it may be triggered by other means, perhaps manually later. More information [Create child flows](/power-automate/create-child-flows)


### Frequently asked questions about bypassing Power Automate flows (FAQ)

Following are frequently asked questions about using the `SuppressCallbackRegistrationExpanderJob` optional parameter to bypass Power Automate flows.
#### Is there a specific privilege that calling users must have?

No. Unlike [Bypass Synchronous Logic](#bypass-synchronous-logic), no special privilege is required.

#### If my client application uses this optional parameter, will it also be applied by any plug-ins registered against the operation?

No. The parameter is not passed through to any operations performed by plug-ins that are registered for the events that your client application will execute. If you want to bypass flows for operations performed by plug-ins, you must use the `SuppressCallbackRegistrationExpanderJob` optional parameter in your plug-in code.

#### Can I create a plug-in that block all flows from being triggered for a given event?

Yes, but we don't recommend you do this. This will not prevent people from creating flows using the triggers for these events, their flows will simply never be triggered.


### See also

[Web API: Compose HTTP requests and handle errors](webapi/compose-http-requests-handle-errors.md)<br />
[Passing optional parameters with a request](org-service/use-messages.md#passing-optional-parameters-with-a-request)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
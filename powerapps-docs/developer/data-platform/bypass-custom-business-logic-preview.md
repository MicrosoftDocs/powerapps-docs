---
title: "New capabilities to bypass Custom Business Logic (preview) | Microsoft Docs" 
description: "Introducing new ways to make data changes which bypass custom business logic." 
ms.date: 04/24/2024
ms.reviewer: jdaly
ms.topic: article
author: divkamath
ms.subservice: dataverse-developer
ms.author: dikamath
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
  - JosinaJoy
---
# New capabilities to bypass Custom Business Logic (preview)

There are two new ways for client developers to bypass custom business logic. Please try these new [optional parameters](optional-parameters.md) and let us know your thoughts.

There are times when you want to be able to perform data operations without having custom business logic applied. These scenarios typically involve bulk data operations where large numbers of records are being created, updated, or deleted.

Without a way to tell Dataverse not to invoke the business logic, you need to locate and disable the custom plug-ins and workflows that contain the business logic. Disabling plug-ins and workflows means that the logic is disabled for all users while those plug-ins and workflows are disabled. It also means that you have to take care to only disable the right plug-ins and workflows and remember to re-enable them when you're done.

The existing [`BypassCustomPluginExecution` optional parameter](bypass-custom-business-logic.md#bypass-synchronous-logic) is limited because you can only bypass *synchronous* business logic. These new options provide more flexibility. The `BypassCustomPluginExecution` optional parameter will remain supported. When these new capabilities become GA, they will be our recommended method.

> [!NOTE]
> Power Automate flows are not bypassed using these optional parameters.[Learn how to bypass Power Automate flows](bypass-custom-business-logic.md#bypass-power-automate-flows)

## New optional parameters

The two new [optional parameters](optional-parameters.md) you can use to bypass custom business logic are introduced in the table below.

|Optional parameter|Description|
|---|---|
|`BypassBusinessLogicExecution`|Pass the `CustomSync`, `CustomAsync`, or `CustomSync,CustomAsync` values to this optional parameter to bypass synchronous logic, asynchronous logic or, both. |
|`BypassBusinessLogicExecutionStepIds`|Pass a comma separated list of plug-in step registrations to bypass only the specified plug-in steps.|

## BypassBusinessLogicExecution

The `BypassBusinessLogicExecution` optional parameter works similarly to the `BypassCustomPluginExecution`optional parameter except that you can choose whether to bypass synchronous logic, asynchronous logic or, both.

This [optional parameter](optional-parameters.md) targets the custom business logic applied for your organization. When you send requests that bypass custom business logic, all custom plug-ins and workflows are disabled except:

- Plug-ins that are part of the core Microsoft Dataverse system or part of a solution where Microsoft is the publisher.
- Workflows included in a solution where Microsoft is the publisher.

System plug-ins define the core behaviors for specific entities. Without these plug-ins, you would encounter data inconsistencies that might not be easily fixed.

Solutions shipped by Microsoft that use Dataverse such as Microsoft Dynamics 365 Customer Service, or Dynamics 365 Sales also include critical business logic that can't be bypassed with this option.

> [!IMPORTANT]
> You may have purchased and installed solutions from other Independent Software Vendors (ISVs) which include their own business logic. The logic applied by these solutions will be bypassed. You should check with these ISVs before you use this option to understand what impact there may be if you use this option with data that their solutions use.

The following table describes when to use the parameter values with `BypassBusinessLogicExecution`.

|Parameter|Description |
|---------|---------|
|`CustomSync` |Bypass only synchronous custom logic.<br />The compute time necessary for synchronous logic accrues to the total time required to perform each data operation. Use this option to reduce the amount of time required to complete operations in bulk.|
|`CustomAsync`|Bypass only asynchronous custom logic, excluding Power Automate Flows.<br />Dataverse applies asynchronous logic after an operation completes. When a large number of operations trigger asynchronous logic, Dataverse requires more resources to process the custom logic and this can impact performance. Use this option to avoid general performance issues that might occur when large numbers of operations trigger asynchronous logic.|
|`CustomSync,CustomAsync`|Bypass both synchronous and asynchronous custom logic, excluding Power Automate Flows.|

### Requirements to use the BypassBusinessLogicExecution optional parameter

- You must send the requests using the `BypassBusinessLogicExecution` [optional parameter](optional-parameters.md).
- The user sending the requests must have the `prvBypassCustomBusinessLogic` privilege. By default, only users with the system administrator security role have this privilege. [Learn how to add the the `prvBypassCustomBusinessLogic` privilege to another role](#adding-the-prvbypasscustombusinesslogic-privilege-to-another-role)

### How do I use the BypassBusinessLogicExecution optional parameter?

You can use this option with either the SDK for .NET or the Web API.

#### [SDK for .NET](#tab/sdk)

The following example sets the `BypassBusinessLogicExecution` [optional parameter](optional-parameters.md) for both synchronous and asynchronous custom logic when creating a new account record using the SDK for .NET [CreateRequest class](/dotnet/api/microsoft.xrm.sdk.messages.createrequest).

```csharp
static void DemonstrateBypassBusinessLogicExecution(IOrganizationService service)
{
    Entity account = new("account");
    account["name"] = "Sample Account";

    CreateRequest request = new()
    {
        Target = account
    };
    request.Parameters.Add("BypassBusinessLogicExecution", "CustomSync,CustomAsync");
    service.Execute(request);
}
```

#### [Web API](#tab/webapi)

The following example sets the `BypassBusinessLogicExecution` [optional parameter](optional-parameters.md) for both synchronous and asynchronous custom logic when [creating a new account record using the Dataverse Web API](webapi/create-entity-web-api.md). This request uses the `MSCRM.BypassBusinessLogicExecution` request header.

```http
POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.BypassBusinessLogicExecution: CustomSync,CustomAsync

{
  "name":"Sample Account"
}

```
---

## BypassBusinessLogicExecutionStepIds

Use the `BypassBusinessLogicExecutionStepIds` [optional parameter](optional-parameters.md) to bypass specified registered plug-in steps instead of all synchronous and asynchronous custom logic. Pass the GUID values of the registered plug-in step registrations with this parameter.

### Identify the steps you want to bypass

There are a couple of ways to locate the GUID values of the plug-in step registration.

#### Use the Plug-in registration tool

1. From the **View** menu, select **Display by Entity**.
1. Select the entity and message
1. Select the step.

   In the detail pane, the **Properties** tab shows the **StepId**. Copy the value from there.

   :::image type="content" source="media/get-stepid-prt.png" alt-text="Use the Plug-in Registration tool to find the StepId value":::

[Learn more about the Plug-in registration tool](download-tools-nuget.md)

#### Query your environment with Web API

Use a query like the following to retrieve the set plug-in step registrations for a given table and message. The following example specifies the `account` table, using the table logical name. `Create` is the name of the message. Replace these values with the table and message you need.

**Request**

```http
GET [Organization URI]/api/data/v9.2/sdkmessagefilters?$select=sdkmessagefilterid
&$filter=primaryobjecttypecode eq 'account' 
and sdkmessageid/name eq 'Create'
&$expand=sdkmessagefilterid_sdkmessageprocessingstep($select=name;
$filter=statecode eq 0 
and customizationlevel eq 1 
and iscustomizable/Value eq true)
Accept: application/json   
OData-MaxVersion: 4.0   
OData-Version: 4.0 
```

**Response**

In the response, look for the `sdkmessageprocessingstepid` values. Use the `name` value to identify the plug-in that you want to bypass.

In this case, there's only one: `4ab978b0-1d77-ec11-8d21-000d3a554d57`

```http
{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sdkmessagefilters(sdkmessagefilterid,sdkmessagefilterid_sdkmessageprocessingstep(name))",
   "value": [
      {
         "@odata.etag": "W/\"31434372\"",
         "sdkmessagefilterid": "c2c5bb1b-ea3e-db11-86a7-000a3a5473e8",
         "sdkmessagefilterid_sdkmessageprocessingstep": [
            {
               "@odata.etag": "W/\"115803276\"",
               "name": "BasicPlugin.FollowupPlugin: Create of account",
               "_sdkmessagefilterid_value": "c2c5bb1b-ea3e-db11-86a7-000a3a5473e8",
               "sdkmessageprocessingstepid": "4ab978b0-1d77-ec11-8d21-000d3a554d57"
            }
         ],
         "sdkmessagefilterid_sdkmessageprocessingstep@odata.nextLink": "[Organization URI]/api/data/v9.2/sdkmessagefilters(c2c5bb1b-ea3e-db11-86a7-000a3a5473e8)/sdkmessagefilterid_sdkmessageprocessingstep?$select=name&$filter=statecode%20eq%200%20and%20customizationlevel%20eq%201%20and%20iscustomizable/Value%20eq%20true"
      }
   ]
}
```

[Learn more about querying data using Web API](webapi/query-data-web-api.md)


#### Query your environment with FetchXml

Use a query like the following to retrieve the set plug-in step registrations for a given table and message. The following example specifies `1` to represent the `account` table, using the [table object type code](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.objecttypecode).

> [!NOTE]
> For tables where the object type code is over `10000`, the value will not be the same in every environment because this value is assigned an incrementing value when the table is created.
>
> If you know the logical name of the table, you can get the object type code using a Web API request. This request returns the value `1`, the object type code for the `account` table.
>
> `GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='account')/ObjectTypeCode/$value`

`Create` is the name of the message. Replace these values with the table and message you need.

Use this FetchXml query to return `step.sdkmessageprocessingstepid` values you can use with the `BypassBusinessLogicExecutionStepIds` optional parameter

```xml
<fetch>
  <entity name='sdkmessagefilter'>
    <filter>
      <condition attribute='primaryobjecttypecode'
        operator='eq'
        value='1' />
    </filter>
    <link-entity name='sdkmessage'
      from='sdkmessageid'
      to='sdkmessageid'
      link-type='inner'
      alias='message'>
      <filter>
        <condition attribute='name'
          operator='eq'
          value='Create' />
      </filter>
    </link-entity>
    <link-entity name='sdkmessageprocessingstep'
      from='sdkmessagefilterid'
      to='sdkmessagefilterid'
      link-type='inner'
      alias='step'>
      <attribute name='name' />
      <filter>
        <condition attribute='statecode'
          operator='eq'
          value='0' />
        <condition attribute='customizationlevel'
          operator='eq'
          value='1' />
        <condition attribute='iscustomizable'
          operator='eq'
          value='1' />
      </filter>
    </link-entity>
  </entity>
</fetch>
```

[Learn more about retrieving data using FetchXml](fetchxml/overview.md)


### Limit to the number of steps

To ensure that the parameter size isn't too large, the default limit on the number of steps you can pass is three. The limit is controlled using data in the [Organization table OrgDbOrgSettings column](reference/entities/organization.md#BKMK_OrgDbOrgSettings). Don't try to edit this value yourself. Use the [OrgDBOrgSettings tool for Microsoft Dynamics CRM](https://support.microsoft.com/topic/orgdborgsettings-tool-for-microsoft-dynamics-crm-20a10f46-2a24-a156-7144-365d49b842ba) or [OrgDbOrgSettings app](https://github.com/seanmcne/OrgDbOrgSettings?tab=readme-ov-file#where-to-find-the-releases) to change the `BypassBusinessLogicExecutionStepIdsLimit` value.

The maximum size for this limit is 400.

## Adding the `prvBypassCustomBusinessLogic` privilege to another role

The [optional parameters](optional-parameters.md) described in this article require security roles that are only added to the system administrator security role. This privilege isn't available in the security role designer to add to other security roles. If you need to grant this privilege to another security role, you must use the API. For example, you might want to grant this privilege to a user with the system customizer security role.

To add the privilege to another security role, you need the ID of the privilege. The ID for the `prvBypassCustomBusinessLogic` privilege is `0ea552b0-a491-4470-9a1b-82068deccf66`. This ID value is the same for all Dataverse environments.

##### [SDK for .NET](#tab/sdk)

Associate the `prvBypassCustomBusinessLogic` privilege to a security role using <xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest>.

```csharp
static void AddprvBypassCustomPluginsToRole(IOrganizationService service, Guid roleId)
{
    var request = new AddPrivilegesRoleRequest
    {
        RoleId = roleId,
        Privileges = new[]{
            new RolePrivilege{
                PrivilegeId = new Guid("0ea552b0-a491-4470-9a1b-82068deccf66"),
                Depth = PrivilegeDepth.Global
            }
        }
    };
    service.Execute(request);
}
```
##### [Web API](#tab/webapi)

Associate the `prvBypassCustomBusinessLogic` privilege to a security role using the [AddPrivilegesRole Action](xref:Microsoft.Dynamics.CRM.AddPrivilegesRole).

**Request:**

```http
POST [Organization URI]/api/data/v9.2/roles(<id of role>)/Microsoft.Dynamics.CRM.AddPrivilegesRole HTTP/1.1
Content-Type: application/json   
Accept: application/json   
OData-MaxVersion: 4.0   
OData-Version: 4.0 

{
  "Privileges": [
    {
      "PrivilegeId": "0ea552b0-a491-4470-9a1b-82068deccf66",
      "Depth": "3"
    }
  ]
}
```

You must set the <xref:Microsoft.Dynamics.CRM.RolePrivilege?text=RolePrivilege>.`Depth` property to <xref:Microsoft.Dynamics.CRM.PrivilegeDepth?text=PrivilegeDepth>.`Global` (`3`) because these are global privileges.

**Response:**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```

---

## Frequently asked questions for bypassing custom business logic (FAQ)

Following are frequently asked questions about using the [optional parameters](optional-parameters.md) described in this article to bypass custom business logic.

### Do these optional parameters work for data operations by Microsoft plug-ins and workflows?

No. If a plug-in or workflow in a Microsoft solution performs operations on other records, the logic for those operations aren't bypassed. Only those plugins or workflows that apply to the specific operation are bypassed.

### Can I use these optional parameters for data operations I perform within a plug-in?

Yes, but only when the plug-in is running in the context of a user who has the necessary privilege. For plug-ins, set the optional parameter on the class derived from [OrganizationRequest Class](xref:Microsoft.Xrm.Sdk.OrganizationRequest).

### See also

[Web API: Compose HTTP requests and handle errors](webapi/compose-http-requests-handle-errors.md)   
[Use optional parameters](optional-parameters.md)   
[Bypass Synchronous Logic](bypass-custom-business-logic.md#bypass-synchronous-logic)   
[Bypass Power Automate Flows](bypass-custom-business-logic.md#bypass-power-automate-flows)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
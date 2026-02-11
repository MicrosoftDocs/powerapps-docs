---
title: "Bypass custom Dataverse logic" 
description: "Make data changes which bypass custom Dataverse logic." 
ms.date: 02/11/2026
ms.reviewer: jdaly
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
  - LearningEveryday1
  - NHelgren
---
# Bypass custom Dataverse logic

Sometimes, you want to perform data operations without applying custom business logic in Dataverse. These scenarios typically involve bulk data operations where you create, update, or delete large numbers of records.

If you don't have a way to tell Dataverse not to invoke the business logic, you need to locate and disable the individual custom plug-ins and workflows that contain the business logic. When you disable plug-ins and workflows, you disable the logic for all users. You also need to take care to only disable the right plug-ins and workflows and remember to re-enable them when you're done.

Instead of this manual process, as a developer of a client application or plug-in, you can pass special [optional parameters](optional-parameters.md) with your requests to control two types of custom business logic as described in the following table:

|Logic type|When to bypass|
|---------|---------|
|**Synchronous Logic**|To enable bulk data operation to complete as quickly as possible. Bypass synchronous logic when the data you're changing is known to meet the requirements of the organization, or you have a plan to achieve this logic by other means. Bypass all custom synchronous logic so that each operation can complete faster, shortening the total time of the bulk operation.|
|**Asynchronous Logic**|When large numbers of system jobs created to process asynchronous logic cause a backup within Dataverse that can affect performance. You can mitigate this performance issue by not triggering the asynchronous logic while performing bulk operations.|

> [!NOTE]
> Power Automate flows represent another type of asynchronous logic that you can manage separately. For more information, see [Bypass Power Automate Flows](bypass-power-automate-flows.md).

## Optional parameters

Use these optional parameters to control business logic execution in Dataverse:

|Optional parameter|Description|
|---|---|
|[`BypassBusinessLogicExecution`](#bypassbusinesslogicexecution)|Pass the values `CustomSync`, `CustomAsync`, or `CustomSync,CustomAsync` to this optional parameter to bypass synchronous logic, asynchronous logic, or both. |
|[`BypassBusinessLogicExecutionStepIds`](#bypassbusinesslogicexecutionstepids)|Pass a comma separated list of plug-in step registrations to bypass only the specified plug-in steps.|
|[`BypassCustomPluginExecution`](#bypasscustompluginexecution)|Bypass only synchronous logic. This optional parameter is supported, but not recommended. Use `BypassBusinessLogicExecution` with the `CustomSync` value to get the same result.|

## `BypassBusinessLogicExecution`

The `BypassBusinessLogicExecution` optional parameter works similarly to the [`BypassCustomPluginExecution`](#bypasscustompluginexecution) optional parameter, except that you can choose whether to bypass synchronous logic, asynchronous logic, or both.

This optional parameter targets the custom business logic applied for your organization. When you send requests that bypass custom business logic, all custom plug-ins and workflows are disabled except for the following exceptions:

- Plug-ins that are part of the core Microsoft Dataverse system or part of a solution where Microsoft is the publisher.
- Workflows included in a solution where Microsoft is the publisher.

System plug-ins define the core behaviors for specific entities. Without these plug-ins, you encounter data inconsistencies that might not be easily fixed.

Solutions shipped by Microsoft that use Dataverse such as Microsoft Dynamics 365 Customer Service or Dynamics 365 Sales also include critical business logic that you can't bypass by using this option.

> [!IMPORTANT]
> You might purchase and install solutions from other Independent Software Vendors (ISVs) that include their own business logic. This option bypasses the logic applied by these solutions. Check with these ISVs before you use this option to understand what impact there might be if you use this option with data that their solutions use.

The following table describes when to use the parameter values with `BypassBusinessLogicExecution`.

|Parameter|Description |
|---------|---------|
|`CustomSync` |Bypass only synchronous custom logic.<br />The compute time necessary for synchronous logic accrues to the total time required to perform each data operation. Use this option to reduce the amount of time required to complete operations in bulk.|
|`CustomAsync`|Bypass only asynchronous custom logic, excluding Power Automate Flows.<br />Dataverse applies asynchronous logic after an operation completes. When a large number of operations trigger asynchronous logic, Dataverse requires more resources to process the custom logic and this resource consumption can affect performance. Use this option to avoid general performance issues that might occur when large numbers of operations trigger asynchronous logic.|
|`CustomSync,CustomAsync`|Bypass both synchronous and asynchronous custom logic, excluding Power Automate Flows.|

### Requirements to use the `BypassBusinessLogicExecution` optional parameter

- You must send the requests by using the `BypassBusinessLogicExecution` [optional parameter](optional-parameters.md).
- The user sending the requests must have the `prvBypassCustomBusinessLogic` privilege. By default, only users with the system administrator security role have this privilege. [Learn how to add the the `prvBypassCustomBusinessLogic` privilege to another role](#adding-the-required-privileges-to-another-role)

### How do I use the `BypassBusinessLogicExecution` optional parameter?

Use this option with either the SDK for .NET or the Web API.

#### [SDK for .NET](#tab/sdk)

The following example sets the `BypassBusinessLogicExecution` [optional parameter](optional-parameters.md) for both synchronous and asynchronous custom logic when creating a new account record by using the SDK for .NET [CreateRequest class](/dotnet/api/microsoft.xrm.sdk.messages.createrequest).

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

## `BypassBusinessLogicExecutionStepIds`

Use the `BypassBusinessLogicExecutionStepIds` optional parameter to bypass specified registered plug-in steps instead of all synchronous and asynchronous custom logic. Pass the GUID values of the registered plug-in step registrations with this parameter. If the step ID passed doesn't run in the given request, it's ignored.

### How do I use the BypassBusinessLogicExecutionStepIds option?

Use this option with either the SDK for .NET or the Web API.

#### [SDK for .NET](#tab/sdk)

The following example sets the optional `BypassBusinessLogicExecutionStepIds` parameter when creating a new account record by using the [CreateRequest class](/dotnet/api/microsoft.xrm.sdk.messages.createrequest).

```csharp
static void DemonstrateBypassBusinessLogicExecutionStepIds(IOrganizationService service)
{
   Entity account = new("account");
   account["name"] = "Sample Account";

   CreateRequest request = new()
   {
         Target = account
   };
   request.Parameters.Add("BypassBusinessLogicExecutionStepIds", "45e0c603-0d0b-466e-a286-d7fc1cda8361,d5370603-e4b9-4b92-b765-5966492a4fd7");
   service.Execute(request);
}
```

#### [Web API](#tab/webapi)

The following Web API request creates a new account record by using the `MSCRM.BypassBusinessLogicExecutionStepIds` request header:

```http
POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.BypassBusinessLogicExecutionStepIds: 45e0c603-0d0b-466e-a286-d7fc1cda8361,d5370603-e4b9-4b92-b765-5966492a4fd7
{
  "name":"Sample Account"
}
```

---

### Identify the steps you want to bypass

There are a couple of ways to locate the GUID values of the plug-in step registration.

#### Use the Plug-in registration tool

1. From the **View** menu, select **Display by Entity**.
1. Select the entity and message.
1. Select the step.

   In the detail pane, the **Properties** tab shows the **StepId**. Copy the value from there.

   :::image type="content" source="media/get-stepid-prt.png" alt-text="Use the Plug-in Registration tool to find the StepId value":::

[Learn more about the Plug-in registration tool](download-tools-nuget.md).

#### Query your environment with Web API

Use a query like the following one to retrieve the set plug-in step registrations for a given table and message. The following example specifies the `account` table, using the table logical name. `Create` is the name of the message. Replace these values with the table and message you need.

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

In this case, there's only one: `4ab978b0-1d77-ec11-8d21-000d3a554d57`.

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

[Learn more about querying data using Web API](webapi/query/overview.md).

#### Query your environment with FetchXml

Use a query like the following one to retrieve the set of plug-in step registrations for a given table and message. The following example specifies `1` to represent the `account` table, using the [table object type code](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.objecttypecode).

> [!NOTE]
> For tables where the object type code is over `10000`, the value isn't the same in every environment because this value is assigned an incrementing value when the table is created.
>
> If you know the logical name of the table, you can get the object type code by using a Web API request. This request returns the value `1`, the object type code for the `account` table.
>
> `GET [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='account')/ObjectTypeCode/$value`

`Create` is the name of the message. Replace these values with the table and message you need.

Use this FetchXml query to return `step.sdkmessageprocessingstepid` values you can use with the `BypassBusinessLogicExecutionStepIds` optional parameter.

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

[Learn more about retrieving data using FetchXml](fetchxml/overview.md).

### Limit on the number of steps

To keep the parameter size manageable, the default limit for the number of steps you can pass is three. The [Organization table OrgDbOrgSettings column](reference/entities/organization.md#BKMK_OrgDbOrgSettings) controls this limit. Use the [OrgDBOrgSettings tool for Microsoft Dynamics CRM](https://support.microsoft.com/topic/orgdborgsettings-tool-for-microsoft-dynamics-crm-20a10f46-2a24-a156-7144-365d49b842ba) or the [OrgDbOrgSettings app](https://github.com/seanmcne/OrgDbOrgSettings?tab=readme-ov-file#where-to-find-the-releases) to change the `BypassBusinessLogicExecutionStepIdsLimit` value.

The maximum recommended size for this limit is 10 steps.

## `BypassCustomPluginExecution`

Use the `BypassCustomPluginExecution` optional parameter to bypass custom synchronous logic.

> [!NOTE]
> This parameter was the first optional parameter that allowed limiting business logic. It remains supported, but use [`BypassBusinessLogicExecution`](#bypassbusinesslogicexecution) with the `CustomSync` value instead.

Use this optional parameter in the same way you use `BypassBusinessLogicExecution`, except it requires a different privilege: `prvBypassCustomPlugins`.

### How do I use the BypassCustomPluginExecution option?

Use this option with either the SDK for .NET or the Web API.

#### [SDK for .NET](#tab/sdk)

Use two approaches to use this optional parameter with the SDK for .NET.

##### Set the value as an optional parameter

The following example sets the optional `BypassCustomPluginExecution` parameter when creating a new account record by using the [CreateRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest).

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

Use this method for data operations you initiate in your plug-ins when the calling user has the `prvBypassCustomPlugins` privilege.

##### Set the CrmServiceClient.BypassPluginExecution property

The following example sets the [CrmServiceClient.BypassPluginExecution Property](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.BypassPluginExecution) when creating a new account record:

```csharp
var service = new CrmServiceClient(connectionString);  

service.BypassPluginExecution = true;

var account = new Entity("account");
account["name"] = "Sample Account";

service.Create(account);
```

Because this setting applies to the service, it remains set for all requests sent by using the service until you set it to `false`.

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](includes/cc-connection-string.md)]

> [!NOTE]
> This property isn't available in the [Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), but it is available on the [Dataverse.Client.Extensions.CRUDExtentions methods](xref:Microsoft.PowerPlatform.Dataverse.Client.Extensions.CRUDExtentions).

#### [Web API](#tab/webapi)

To apply this option by using the Web API, pass `MSCRM.BypassCustomPluginExecution : true` as a header in the request.

**Request:**

The following Web API request creates a new account record without custom synchronous business logic applied:

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

## Add the required privileges to another role

The optional parameters described in this article require privileges that only the system administrator security role has. You can't add these privileges to other security roles in the security role designer. If you need to grant this privilege to another security role, use the API. For example, you might want to grant this privilege to a user with the system customizer security role.

To add the privilege to another security role, you need the ID of the privilege.

|Name|ID|Optional Parameter(s)|
|---------|---------|---------|
|`prvBypassCustomBusinessLogic`|`0ea552b0-a491-4470-9a1b-82068deccf66`|[`BypassBusinessLogicExecution`](#bypassbusinesslogicexecution)<br />[`BypassBusinessLogicExecutionStepIds`](#bypassbusinesslogicexecutionstepids)|
|`prvBypassCustomPlugins`|`148a9eaf-d0c4-4196-9852-c3a38e35f6a1`|[`BypassCustomPluginExecution`](#bypasscustompluginexecution)|

 These ID values are the same for all Dataverse environments.

### [SDK for .NET](#tab/sdk)

Associate the `prvBypassCustomBusinessLogic` privilege to a security role by using <xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest>.

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

### [Web API](#tab/webapi)

Associate the `prvBypassCustomBusinessLogic` privilege to a security role by using the [AddPrivilegesRole Action](xref:Microsoft.Dynamics.CRM.AddPrivilegesRole).

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

Set the <xref:Microsoft.Dynamics.CRM.RolePrivilege?text=RolePrivilege>.`Depth` property to <xref:Microsoft.Dynamics.CRM.PrivilegeDepth?text=PrivilegeDepth>.`Global` (`3`) because these privileges are global.

**Response:**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```

---

### Frequently asked questions for bypassing business logic (FAQ)

The following questions are frequently asked about using the optional parameters to bypass synchronous business logic.

#### Do these optional parameters bypass plug-ins for data operations by Microsoft plug-ins?

 No. If a plug-in or workflow in a Microsoft solution performs operations on other records, the logic for those operations isn't bypassed. Only those plugins or workflows that apply to the specific operation are bypassed.

#### Can I use these optional parameters for data operations I perform within a plug-in?

Yes, but only when the plug-in runs in the context of a user who has the required privilege. For plug-ins, set the optional parameter on the class derived from [OrganizationRequest Class](xref:Microsoft.Xrm.Sdk.OrganizationRequest). You can't use the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> or <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> classes in a plug-in.

### See also

- [Bypass Power Automate Flows](bypass-power-automate-flows.md)
- [Use optional parameters](optional-parameters.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

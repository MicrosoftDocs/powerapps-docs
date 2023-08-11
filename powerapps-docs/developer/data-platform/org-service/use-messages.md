---
title: "Use messages with the Organization service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Understand how messages are used to invoke operations using the organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.collection: get-started
ms.date: 04/24/2023
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: article
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---
# Use messages with the Organization service

It's important to understand that all data operations in Dataverse are defined as *messages* and the definitions of these messages are stored in Dataverse.

Every message has:

- A unique name
- A collection of input parameters
- A collection of output parameters

There are three different ways you can use a message with the SDK for .NET as explained in the following sections:

|Method|Description|
|---------|---------|
|[OrganizationRequest and OrganizationResponse classes](#organizationrequest-and-organizationresponse-classes)| Use these classes when you don't have SDK Request and Response classes. You might prefer to use this approach rather than generating SDK Request and Response classes when you know the message name and details of the input and output parameters.|
|[SDK Request and Response classes](#sdk-request-and-response-classes)|Using these classes is the most common way you use messages. Many messages already have classes defined in the SDK for .NET. For custom actions, you can generate classes.|
|[IOrganizationService methods](#iorganizationservice-methods)|The <xref:Microsoft.Xrm.Sdk.IOrganizationService> provides some methods for common data operations. These methods are the quickest and easiest ways to perform most common data operations.|

## OrganizationRequest and OrganizationResponse classes

> [!NOTE]
> Using <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes isn't the most common way to use messages in Dataverse. However, these classes demonstrate how messages are implemented. Understanding this is important to understand how other parts of Dataverse work.

You can use a message without SDK Request and Response classes.

1. Use the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class.

   - Set the [OrganizationRequest.RequestName](xref:Microsoft.Xrm.Sdk.OrganizationRequest.RequestName)
   - Set the items in the [OrganizationRequest.Parameters](xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters) collection.

1. Send the request using the [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) method, which returns an <xref:Microsoft.Xrm.Sdk.OrganizationResponse> instance.

   The items in the [OrganizationResponse.Results](xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results) collection contains the results.

For example, if you want to create an account record, you could do it this way:

```csharp
public static Guid OrganizationRequestExample(IOrganizationService service) {

   // Instantiate an Entity instance of type 'account'
    var account = new Entity("account");
    account["name"] = "Test account";

   // Instantiate a collection of parameters with one item 'Target',
   // set to the account entity instance
    ParameterCollection parameters = new ParameterCollection
    {
        { "Target", account }
    };

   // Instantiate an OrganizationRequest instance setting the
   // RequestName and Parameters
    OrganizationRequest request = new OrganizationRequest()
    {
        RequestName = "Create",
        Parameters = parameters
    };

   // Send the request using the IOrganizationService.Execute method
    OrganizationResponse response = service.Execute(request);

   // Parse the output parameter 'id' from the Results
    return (Guid)response.Results["id"];
}
```

To create an account record using this method, you need to know:

- The name of the message: `Create`.
- The name and data type of each input parameter: A single parameter named `Target` that is an [Entity](xref:Microsoft.Xrm.Sdk.Entity).
- The name and data type of each output parameter: A single parameter named `id` that is a [Guid](xref:System.Guid).

This information stored in Dataverse. The [SdkMessage table](../reference/entities/sdkmessage.md) contains information about all the messages.

Dataverse manages information about the input and output parameters in private tables. You don't need to retrieve it because there's an easier way: using the SDK Request and Response classes.

## SDK Request and Response classes

SDK Request and Response classes reduce the complexity of using the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes. You don't need to know the name of the message and the input and output parameters because the classes have them included.

The SDK for .NET contains definitions for common Dataverse messages in these namespaces:

|Namespace|Description|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Messages?displayProperty=fullName>|Messages for common data operations and messages used to create and modify schema data, also known as metadata.|
|<xref:Microsoft.Crm.Sdk.Messages?displayProperty=fullName>|Messages for business logic and operations to support special capabilities to support ALM and apps. Some messages in this namespace support capabilities only found in Microsoft Dynamics 365 business applications. |

These classes contain properties for all the input and output parameters.

- The classes ending with `*Request` contain the properties for input parameters.

   These classes inherit from the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class.

- The classes ending with `*Response` contain the properties for output parameters.

   These classes inherit from the <xref:Microsoft.Xrm.Sdk.OrganizationResponse> class.

For example, to create a record, you can use the [Microsoft.Xrm.Sdk.Messages.CreateRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest) class to prepare the request. Use [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) to send the request and the results will be in form of an [Microsoft.Xrm.Sdk.Messages.CreateResponse](xref:Microsoft.Xrm.Sdk.Messages.CreateResponse) class instance.

The following example uses the [Microsoft.Xrm.Sdk.Messages.CreateRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest) class with a generated early-bound class for the account entity:

```csharp
public static Guid CreateRequestExample(IOrganizationService service)
{
    // Instantiate an Account using generated early-bound class
    var account = new Account
    {
        Name = "Test account"
    };

    // Instantiate a CreateRequest
    var request = new CreateRequest
    {
        // Set the Target property
        Target = account
    };

    // Send the request using the IOrganizationService.Execute method
    // Cast the OrganizationResponse into a CreateResponse
    var response = (CreateResponse)service.Execute(request);

    // Return the id property value
    return response.id;
}
```

### Generate classes for custom actions

There are other messages that don't have classes in the SDK. For example, solutions installed frequently include new message definitions defined as custom actions (custom API or custom process actions). More information: [Create your own messages](../custom-actions.md)

Developers can generate Request and Response classes for the messages found in their environment using the following tools:

|Tool|Description|
|---------|---------|
|Power Platform CLI<br />[pac modelbuilder build](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build)<br />command|Generates cross-platform .NET (Core) classes for applications that use the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient?displayProperty=fullName>.<br />Use the [--generateActions](/power-platform/developer/cli/reference/modelbuilder#--generateactions--a) parameter to generate Request and Response classes.|
|CrmSvcUtil.exe|Generates .NET Framework classes to support applications that use .NET Framework, such as Dataverse plug-ins.<br />Use the `generateActions` parameter to generate Request and Response classes.|

More information: [Generate early-bound classes for the Organization service](generate-early-bound-classes.md)

### Passing optional parameters with a request

There are several optional parameters you can pass to apply special behaviors to messages. You can't use the [IOrganizationService](xref:Microsoft.Xrm.Sdk.IOrganizationService) methods when you use optional parameters. You must use the SDK Request classes or the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class.

More information: [Use optional parameters](../optional-parameters.md)


## IOrganizationService methods

In addition to the [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) method, the [IOrganizationService Interface](xref:Microsoft.Xrm.Sdk.IOrganizationService) specifies that the following methods must also be implemented. These methods encapsulate the corresponding Request and Response classes:


|Method|Request/Response classes|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A>|<xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> / <xref:Microsoft.Xrm.Sdk.Messages.CreateResponse>|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A>|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> / <xref:Microsoft.Xrm.Sdk.Messages.RetrieveResponse>|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A>|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> / <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleResponse>|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update%2A>|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> / <xref:Microsoft.Xrm.Sdk.Messages.UpdateResponse>|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete%2A>|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRequest> / <xref:Microsoft.Xrm.Sdk.Messages.DeleteResponse>|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate%2A>|<xref:Microsoft.Xrm.Sdk.Messages.AssociateRequest> / <xref:Microsoft.Xrm.Sdk.Messages.AssociateResponse>|
|<xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate%2A>|<xref:Microsoft.Xrm.Sdk.Messages.DisassociateRequest> / <xref:Microsoft.Xrm.Sdk.Messages.DisassociateResponse>|

These methods simplify performing these operations with fewer lines of code. The following example uses the [IOrganizationService.Create](xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A) method to create an account record:

```csharp
public static Guid CreateMethodExample(IOrganizationService service)
{
   // Instantiate an Account using generated early-bound class
    var account = new Account
    {
        Name = "Test account"
    };

    // Use the Create method to get the id of the created account.
    return service.Create(account);
}
```

As you can see, common data operations have been streamlined using the <xref:Microsoft.Xrm.Sdk.IOrganizationService> methods and other messages are made easier to use with the Request and Response classes in the SDK assemblies or generated with tooling. Most of the time you don't need to use the underlying <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes, but it's important to understand the different options available to use messages, especially when working with custom API and plug-ins.

## Working with messages in plug-ins

The data describing an operation in a plug-in are in the form of [IExecutionContext.InputParameters](xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters) and [IExecutionContext.OutputParameters](xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters).

In the `PreValidation` and `PreOperation` stages before the `main` operation of the event pipeline, the [IExecutionContext.InputParameters](xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters) contain the [OrganizationRequest.Parameters](xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters).

With a custom API, your plug-in will read the [IExecutionContext.InputParameters](xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters) and contain logic to set the [IExecutionContext.OutputParameters](xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters) as part of the `main` operation stage.

After the `main` operation stage, in the `PostOperation` stage, the [IExecutionContext.OutputParameters](xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters) contain the [OrganizationResponse.Results](xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results).

Understanding the structure of the messages helps you understand where to find the data you want to check or change within the plug-in.

More information:

- [Write plug-ins to extend business processes](../plug-ins.md)
- [Create and use custom APIs](../custom-api.md)
- [Event Framework](../event-framework.md)

## Private Messages

Microsoft Dataverse contains some messages that aren't intended for third party developers to use. Microsoft added these messages enable feature functionality, but third party solutions can also add them with the custom API feature. The [SdkMessage.IsPrivate](../reference/entities/sdkmessage.md#BKMK_IsPrivate) property tells you which messages are private.

> [!CAUTION]
> You should not use private messages unless you created them as a custom API. By marking a message as private, the solution publisher is explicitly calling out that they do not support other apps to use the message. They may remove the message or introduce breaking changes at any time. Use of these messages by anyone other than the solution publisher are not supported.
> Calling private messages from plug-ins is not supported.

More information: [Create and use custom APIs](../custom-api.md)

## Table support for messages

Some messages can be used with multiple tables. For example the `Create`, `Update`, and `Delete` messages can be used for most tables, but some tables may not support all the common messages.

This information is stored in the [SdkMessageFilter table](../reference/entities/sdkmessagefilter.md). You can query this table to determine if you can use a message for a table.

#### [SDK for .NET](#tab/sdk)

Use this static method to get a list of names of messages that can work with a table:

```csharp
/// <summary>
/// Write the names of messages for a table to the console
/// </summary>
/// <param name="service">The authenticated IOrganizationService to use</param>
/// <param name="tableName">The logical name of the table</param>
static void OutputTableMessageNames(IOrganizationService service, string tableName)
{
    var query = new QueryExpression(entityName: "sdkmessagefilter")
    {
        Criteria =
        {
            Conditions =
            {
                new ConditionExpression(
                    attributeName:"primaryobjecttypecode",
                    conditionOperator: ConditionOperator.Equal,
                    value: tableName)
            }
        },
        // Link to SdkMessage to get the names
        LinkEntities =
        {
            new LinkEntity(
                linkFromEntityName:"sdkmessagefilter",
                linkToEntityName: "sdkmessage",
                linkFromAttributeName: "sdkmessageid",
                linkToAttributeName: "sdkmessageid",
                joinOperator: JoinOperator.Inner)
            {
                EntityAlias = "sdkmessage",
                Columns = new ColumnSet("name"),
                LinkCriteria =
                {
                    Conditions =
                    {
                        // Don't include private messages
                        new ConditionExpression("isprivate", ConditionOperator.Equal, false)
                    }
                }
            }
        }
    };

    EntityCollection results = service.RetrieveMultiple(query);

        foreach (var entity in results.Entities)
        {
            Console.WriteLine(((AliasedValue)entity["sdkmessage.name"]).Value);
        }
}
```

If you use this method setting the `tableName` parameter to `account`, you will get results that include these message names:

**Output:**

```console
Assign
Create
Delete
GrantAccess
Merge
ModifyAccess
Retrieve
RetrieveMultiple
RetrievePrincipalAccess
RetrieveSharedPrincipalsAndAccess
RevokeAccess
SetState
SetStateDynamicEntity
Update
```



#### [Web API](#tab/webapi)

Use the following `GET` request to retrieve the messages supported by a table. The request below retrieves messages for the `account` table.  Replace the `@table` alias parameter value for the table you want to retrieve message names for.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/sdkmessagefilters?$select=sdkmessagefilterid
&$filter= primaryobjecttypecode eq @table
&$expand=sdkmessageid($select=name)
&@table='account'
Content-Type: application/json
```


**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#sdkmessagefilters(sdkmessagefilterid,sdkmessageid(name))",
    "value": [
        {
            "@odata.etag": "W/\"31433272\"",
            "sdkmessagefilterid": "87c5bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "Assign",
                "sdkmessageid": "8cbdbb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31434372\"",
            "sdkmessagefilterid": "c2c5bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "Create",
                "sdkmessageid": "9ebdbb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31435906\"",
            "sdkmessagefilterid": "2bc6bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "Delete",
                "sdkmessageid": "a1bdbb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31436549\"",
            "sdkmessagefilterid": "bac6bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "GrantAccess",
                "sdkmessageid": "c5bdbb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31429419\"",
            "sdkmessagefilterid": "f9c6bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "Merge",
                "sdkmessageid": "dbbdbb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31436817\"",
            "sdkmessagefilterid": "fcc6bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "ModifyAccess",
                "sdkmessageid": "dcbdbb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31437759\"",
            "sdkmessagefilterid": "42c7bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "Retrieve",
                "sdkmessageid": "f2bdbb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31432761\"",
            "sdkmessagefilterid": "d7c7bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "RetrieveMultiple",
                "sdkmessageid": "03bebb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31441514\"",
            "sdkmessagefilterid": "39c8bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "RetrievePrincipalAccess",
                "sdkmessageid": "04bebb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"10876821\"",
            "sdkmessagefilterid": "65c8bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "RetrieveSharedPrincipalsAndAccess",
                "sdkmessageid": "10bebb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31441786\"",
            "sdkmessagefilterid": "85c8bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "RevokeAccess",
                "sdkmessageid": "11bebb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31439673\"",
            "sdkmessagefilterid": "d9c8bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "SetState",
                "sdkmessageid": "1cbebb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31440023\"",
            "sdkmessagefilterid": "fbc8bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "SetStateDynamicEntity",
                "sdkmessageid": "1dbebb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        },
        {
            "@odata.etag": "W/\"31439008\"",
            "sdkmessagefilterid": "23c9bb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid": {
                "name": "Update",
                "sdkmessageid": "20bebb1b-ea3e-db11-86a7-000a3a5473e8"
            }
        }
    ]
}
```

---


> [!NOTE]
> Some of these messages are deprecated. `SetState` and `SetStateDynamicEntity` still exist, but you should use `Update` instead.

## Message support for tables

Some messages can only be used with specific tables. For example, you can only use the `RetrieveUnpublishedMultiple` message with a specific set of tables that contain data that can be published

This information is stored in the [SdkMessageFilter table](../reference/entities/sdkmessagefilter.md). You can query this table to determine which tables can be used for a specific message.

#### [SDK for .NET](#tab/sdk)

Use this static method to get a list of names of tables that can be used with a message:

```csharp
/// <summary>
/// Write the names of tables for a message to the console
/// </summary>
/// <param name="service">The authenticated IOrganizationService to use</param>
/// <param name="messageName">The name of the message</param>
static void OutputTablesForMessage(IOrganizationService service, string messageName) {

    var query = new QueryExpression(entityName: "sdkmessage")
    {
        Criteria = { 
            Conditions =
            {
                new ConditionExpression(
                        attributeName: "name",
                        conditionOperator: ConditionOperator.Equal,
                        value: messageName)
            }
        },
        LinkEntities = {
            new LinkEntity(
                linkFromEntityName:"sdkmessage",
                linkToEntityName: "sdkmessagefilter",
                linkFromAttributeName: "sdkmessageid",
                linkToAttributeName: "sdkmessageid",
                joinOperator: JoinOperator.Inner)
            {
                EntityAlias = "sdkmessagefilter",
                Columns = new ColumnSet("primaryobjecttypecode"),
            }
        }
    };

            EntityCollection results = service.RetrieveMultiple(query);
            List<string> names = new List<string>();

            foreach (var entity in results.Entities)
            {
                names.Add(((AliasedValue)entity["sdkmessagefilter.primaryobjecttypecode"]).Value as string);
            }

            names.Distinct().ToList().ForEach(name => Console.WriteLine(name));
}
```

If you use this method setting the `messageName` parameter to `RetrieveUnpublishedMultiple`, you will get results that include these table names:

**Output:**

```console
organizationui
systemform
savedquery
savedqueryvisualization
sitemap
hierarchyrule
appmodule
appconfig
appconfiginstance
webresource
mobileofflineprofile
mobileofflineprofileitem
mobileofflineprofileitemassociation
navigationsetting
appelement
appsetting
teammobileofflineprofilemembership
usermobileofflineprofilemembership
```

#### [Web API](#tab/webapi)

Use the following `GET` request to retrieve the tables supported by a message. The request below retrieves messages for the `RetrieveUnpublishedMultiple` message.  Replace the `@message` alias parameter value for the message you want to retrieve table names for.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/sdkmessages?$select=sdkmessageid
&$filter= name eq @message
&$expand=sdkmessageid_sdkmessagefilter($select=primaryobjecttypecode)
&@message='RetrieveUnpublishedMultiple'
Content-Type: application/json
```


**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sdkmessages(sdkmessageid,sdkmessageid_sdkmessagefilter(primaryobjecttypecode))",
    "value": [
        {
            "@odata.etag": "W/\"42343467\"",
            "sdkmessageid": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
            "sdkmessageid_sdkmessagefilter": [
                {
                    "@odata.etag": "W/\"10875729\"",
                    "primaryobjecttypecode": "savedquery",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "b9c7bb1b-ea3e-db11-86a7-000a3a5473e8"
                },
                {
                    "@odata.etag": "W/\"10875725\"",
                    "primaryobjecttypecode": "organizationui",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "bac7bb1b-ea3e-db11-86a7-000a3a5473e8"
                },
                {
                    "@odata.etag": "W/\"52381806\"",
                    "primaryobjecttypecode": "appsetting",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "7cbb24ef-4ce1-eb11-bacb-000d3a11527a"
                },
                {
                    "@odata.etag": "W/\"29691679\"",
                    "primaryobjecttypecode": "appelement",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "72cfb731-fec3-ea11-a812-000d3a5394f0"
                },
                {
                    "@odata.etag": "W/\"42343472\"",
                    "primaryobjecttypecode": "usermobileofflineprofilemembership",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "6d6b7818-41f3-4d41-a1c5-2e36f16f8cea"
                },
                {
                    "@odata.etag": "W/\"10875697\"",
                    "primaryobjecttypecode": "appconfiginstance",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "46c863b7-2cb6-46e3-9ae7-46132a966780"
                },
                {
                    "@odata.etag": "W/\"10875745\"",
                    "primaryobjecttypecode": "webresource",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "bbd24839-4249-4e7c-a239-6fa0fe2b5859"
                },
                {
                    "@odata.etag": "W/\"10875713\"",
                    "primaryobjecttypecode": "mobileofflineprofile",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "35b7fb00-7b92-49f8-840a-7668b13fa621"
                },
                {
                    "@odata.etag": "W/\"42343469\"",
                    "primaryobjecttypecode": "teammobileofflineprofilemembership",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "495eaf32-df68-4ac5-be6e-797b5454e106"
                },
                {
                    "@odata.etag": "W/\"10875721\"",
                    "primaryobjecttypecode": "mobileofflineprofileitemassociation",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "45971bcb-7da3-4a3e-832c-8f72f360ada5"
                },
                {
                    "@odata.etag": "W/\"10875705\"",
                    "primaryobjecttypecode": "appmodule",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "b78abd84-c055-4795-8ed4-c2832d54ae35"
                },
                {
                    "@odata.etag": "W/\"10875741\"",
                    "primaryobjecttypecode": "systemform",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "e342b0fc-dc2c-4241-b026-d86cf934a6ab"
                },
                {
                    "@odata.etag": "W/\"10875709\"",
                    "primaryobjecttypecode": "hierarchyrule",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "a33799de-e398-4a69-8560-dc34be151bbb"
                },
                {
                    "@odata.etag": "W/\"10875717\"",
                    "primaryobjecttypecode": "mobileofflineprofileitem",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "45940eee-c53e-4e5b-8810-e24ff8ba7a4a"
                },
                {
                    "@odata.etag": "W/\"10875702\"",
                    "primaryobjecttypecode": "navigationsetting",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "7543d474-ac6d-4126-a54c-e84ad2e12f90"
                },
                {
                    "@odata.etag": "W/\"10875695\"",
                    "primaryobjecttypecode": "appconfig",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "7ed190aa-444f-4b68-a4e2-ea797c329732"
                },
                {
                    "@odata.etag": "W/\"10875737\"",
                    "primaryobjecttypecode": "sitemap",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "e9a0c1a2-d815-4454-910c-eea88db72b7c"
                },
                {
                    "@odata.etag": "W/\"10875733\"",
                    "primaryobjecttypecode": "savedqueryvisualization",
                    "_sdkmessageid_value": "f6bdbb1b-ea3e-db11-86a7-000a3a5473e8",
                    "sdkmessagefilterid": "c2995c4d-ede4-437a-9f77-f41971c5437a"
                }
            ],
            "sdkmessageid_sdkmessagefilter@odata.nextLink": "[Organization URI]/api/data/v9.2/sdkmessages(f6bdbb1b-ea3e-db11-86a7-000a3a5473e8)/sdkmessageid_sdkmessagefilter?$select=primaryobjecttypecode"
        }
    ]
}
```

---

> [!NOTE]
> - For certain messages, you may find that placeholder values are returned, such as `DeletedEntity for objectTypeCode=11478` or `new_system_donotuseentity_rp53fd1p1ekxpa_t12_b71d6344c5`. These aren't valid table names. Disregard these values.
> 
> - This query will also return [Private tables](../entities.md#private-tables). In the example above: `organizationui`,`hierarchyrule`, `appelement`, and `appsetting` are private tables and not supported for use.


### See also

[Table operations using the Organization service](entity-operations.md)<br />
[Use ExecuteAsync to execute messages asynchronously](use-executeAsync.md)<br />
[Execute messages in a single database transaction](use-executetransaction.md)<br />
[Execute multiple requests using the Organization service](execute-multiple-requests.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

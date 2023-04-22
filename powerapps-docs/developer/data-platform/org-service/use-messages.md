---
title: "Use messages with the Organization service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Understand how messages are used to invoke operations using the organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
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
|[OrganizationRequest & OrganizationResponse classes](#organizationrequest--organizationresponse-classes)| Use these classes when you don't have SDK Request and Response classes. You might prefer to use this approach rather than generating SDK Request and Response classes when you know the message name and details of the input and output parameters.|
|[SDK Request & Response classes](#sdk-request--response-classes)|Using these classes is the most common way you use messages. Many messages already have classes defined in the SDK for .NET. For custom actions, you can generate classes.|
|[IOrganizationService methods](#iorganizationservice-methods)|The <xref:Microsoft.Xrm.Sdk.IOrganizationService> provides some methods for common data operations. These methods are the quickest and easiest ways to perform most common data operations.|

## OrganizationRequest & OrganizationResponse classes

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

## SDK Request & Response classes

The SDK for .NET contains definitions for common Dataverse messages in these namespaces:

|Namespace|Description|
|---------|---------|
|<xref:Microsoft.Xrm.Sdk.Messages?displayProperty=fullName>|Messages for common data operations and messages used to create and modify schema data, also known as metadata.|
|<xref:Microsoft.Crm.Sdk.Messages?displayProperty=fullName>|Messages for business logic and operations to support special capabilities to support ALM and apps. Some messages in this namespace support capabilities only found in Microsoft Dynamics 365 business applications. |

These classes contain properties for all the input and output parameters.

- The classes ending with *Request contain the properties for input parameters.

   These classes inherit from the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> class.

- The classes ending with *Response contain the properties for output parameters.

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
- [Create and use Custom APIs](../custom-api.md)
- [Event Framework](../event-framework.md)

## Private Messages

Microsoft Dataverse contains some messages that aren't intended for third party developers to use. Microsoft added these messages enable feature functionality, but third party solutions can also add them with the Custom API feature. The [SdkMessage.IsPrivate](../reference/entities/sdkmessage.md#BKMK_IsPrivate) property tells you which messages are private.

> [!CAUTION]
> You should not use private messages unless you created them as a Custom API. By marking a message as private, the solution publisher is explicitly calling out that they do not support other apps to use the message. They may remove the message or introduce breaking changes at any time. Use of these messages by anyone other than the solution publisher are not supported.
> Calling private messages from plug-ins is not supported.

More information: [Create and use Custom APIs](../custom-api.md)

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

**Request**

```http
GET [Organization Uri]/api/data/v9.2/sdkmessagefilters?$select=sdkmessagefilterid
&$filter= primaryobjecttypecode eq @table
&$expand=sdkmessageid($select=name)
&@table='account'
Content-Type: application/json
```


**Response**

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

### See also

[Table operations using the Organization service](entity-operations.md)<br />
[Use ExecuteAsync to execute messages asynchronously](use-executeAsync.md)<br />
[Execute messages in a single database transaction](use-executetransaction.md)<br />
[Execute multiple requests using the Organization service](execute-multiple-requests.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

---
title: Use Webhooks to Create External Handlers for Server Events
description: Learn how to use Webhooks to send Dataverse server events to your web application, parse request data, and build external handlers.
ms.collection: get-started
ms.date: 03/31/2026
ms.reviewer: pehecke
ms.topic: article
author: swylezol
ms.subservice: dataverse-developer
ms.author: swylezol
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---
# Use webhooks to create external handlers for server events

Use webhooks to send Microsoft Dataverse server events to an external web application. This article explains the request data Dataverse sends and how webhooks help you build external handlers for server events.

By using webhooks, developers and ISVs can integrate Dataverse data with their own custom code hosted on external services. By using the webhook model, you can secure your endpoint by using authentication header or query string parameter keys. This approach is simpler than the SAS authentication model that you might currently use for Azure Service Bus integration.

When deciding between the webhook model and the Azure Service Bus integration, keep these points in mind:

- Azure Service Bus works for high scale processing, and provides a full queuing mechanism if Dataverse is pushing many events.
- Webhooks can only scale to the point at which your hosted web service can handle the messages.
- Webhooks enable synchronous and asynchronous steps. Azure Service Bus only allows for asynchronous steps.
- Webhooks send POST requests with JSON payload and can be consumed by any programming language or web application hosted anywhere.
- Both webhooks and Azure Service Bus can be invoked from a plug-in or custom workflow activity.

## Get started

Using webhooks involves three parts:

- Creating or configuring a service to consume webhook requests.
- Registering webhook step on the Dataverse service.
- Invoking a webhook from a plug-in or custom workflow activity.

### Start by registering a test WebHook

To understand how to create and configure a service to consume a WebHook request from Dataverse, start by learning how to register a WebHook. For more information, see [Register a WebHook](register-web-hook.md).

After you register an example WebHook, use a request logging site to examine the contextual data that's passed. For more information, see [Test WebHook registration with request logging site](test-WebHook-registration.md).

> [!TIP]
> Completing the steps to register a test WebHook and examining the contextual data that is passed makes the rest of the information in this topic easier to understand. Complete these steps and return to this topic.

<a name="create-or-configure"></a>

## Create or configure a service to consume WebHook requests

Webhooks are simply a pattern that you can apply using a wide range of technologies. There are no required frameworks, platforms, or programming languages you must use. Use the skills and knowledge you have to deliver the appropriate solution.

[Azure Functions](https://azure.microsoft.com/services/functions/) provide an excellent way to deliver a solution using Webhooks, but it's not a requirement. This section doesn't provide guidance toward a specific solution. Instead, it describes the data that Dataverse passes to your service that enables your service to add value.

As demonstrated in [Test WebHook registration with request logging site](test-WebHook-registration.md), you can register a test WebHook step and use the request logging site to capture the specific kinds of data that your application can process.

### Data passed to the service

The request includes three types of data: query string, header data, and request body.

#### Query string

The only data you pass as a query string are the authentication values if you configure the WebHook to use the **WebhookKey** or **HttpQueryString** options, as described in [Authentication options](register-web-hook.md#authentication-options).

#### Header data

If you choose the **HttpHeader** authentication option, use the key/value pairs that your service requires.

You can expect your service to receive the following data:

|Key|Value Description|
|---------|---------|
|`x-ms-dynamics-organization`|The domain name of the environment sending the request|
|`x-ms-dynamics-entity-name`|The logical name of the table passed in the execution context data.|
|`x-ms-dynamics-request-name`|The name of the event that the WebHook step was registered for.|
|`x-ms-correlation-request-id`|Unique identifier for tracking any type of extension. The platform uses this property for infinite loop prevention. In most cases, you can ignore this property. When working with technical support, this value can be used to query telemetry to understand what occurred during the entire operation.
|`x-ms-dynamics-msg-size-exceeded`|Sent only when the HTTP payload size exceeds 256 KB.|

#### Request body

The body contains a string that represents the JSON value of an instance of the <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext> class. This is the same data that is passed to Azure Service Bus integrations.

The service you create must parse this data to extract the relevant items of information for your service to provide its function. How you choose to parse this data depends on the technology you're using and your preferences.

The following example shows the serialized JSON data passed for a step registered with the following properties:

|Property|Description|
|---------|---------|
|**Message**|Update|
|**Primary Entity**|contact|
|**Secondary Entity**|none|
|**Filtering Attributes**|firstname,lastname|
|**Run in User's Context**|Calling User|
|**Execution Order**|1|
|**Event Pipeline Stage of Execution**|PostOperation|
|**Execution Mode**|Asynchronous|

```json
{
    "BusinessUnitId": "e2b9dd85-e89e-e711-8122-000d3aa2331c",
    "CorrelationId": "aaaa0000-bb11-2222-33cc-444444dddddd",
    "Depth": 1,
    "InitiatingUserId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
    "InputParameters": [{
        "key": "Target",
        "value": {
            "__type": "Entity:http:\/\/schemas.microsoft.com\/xrm\/2011\/Contracts",
            "Attributes": [{
                "key": "firstname",
                "value": "James"
            }, {
                "key": "contactid",
                "value": "6d81597f-0f9f-e711-8122-000d3aa2331c"
            }, {
                "key": "fullname",
                "value": "James Glynn (sample)"
            }, {
                "key": "yomifullname",
                "value": "James Glynn (sample)"
            }, {
                "key": "modifiedon",
                "value": "\/Date(1506384247000)\/"
            }, {
                "key": "modifiedby",
                "value": {
                    "__type": "EntityReference:http:\/\/schemas.microsoft.com\/xrm\/2011\/Contracts",
                    "Id": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
                    "KeyAttributes": [],
                    "LogicalName": "systemuser",
                    "Name": null,
                    "RowVersion": null
                }
            }, {
                "key": "modifiedonbehalfby",
                "value": null
            }],
            "EntityState": null,
            "FormattedValues": [],
            "Id": "6d81597f-0f9f-e711-8122-000d3aa2331c",
            "KeyAttributes": [],
            "LogicalName": "contact",
            "RelatedEntities": [],
            "RowVersion": null
        }
    }],
    "IsExecutingOffline": false,
    "IsInTransaction": false,
    "IsOfflinePlayback": false,
    "IsolationMode": 1,
    "MessageName": "Update",
    "Mode": 1,
    "OperationCreatedOn": "\/Date(1506409448000-0700)\/",
    "OperationId": "4af10637-4ea2-e711-8122-000d3aa2331c",
    "OrganizationId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",
    "OrganizationName": "OrgName",
    "OutputParameters": [],
    "OwningExtension": {
        "Id": "75417616-4ea2-e711-8122-000d3aa2331c",
        "KeyAttributes": [],
        "LogicalName": "sdkmessageprocessingstep",
        "Name": null,
        "RowVersion": null
    },
    "ParentContext": {
        "BusinessUnitId": "e2b9dd85-e89e-e711-8122-000d3aa2331c",
        "CorrelationId": "aaaa0000-bb11-2222-33cc-444444dddddd",
        "Depth": 1,
        "InitiatingUserId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",
        "InputParameters": [{
            "key": "Target",
            "value": {
                "__type": "Entity:http:\/\/schemas.microsoft.com\/xrm\/2011\/Contracts",
                "Attributes": [{
                    "key": "firstname",
                    "value": "James"
                }, {
                    "key": "contactid",
                    "value": "6d81597f-0f9f-e711-8122-000d3aa2331c"
                }],
                "EntityState": null,
                "FormattedValues": [],
                "Id": "6d81597f-0f9f-e711-8122-000d3aa2331c",
                "KeyAttributes": [],
                "LogicalName": "contact",
                "RelatedEntities": [],
                "RowVersion": null
            }
        }, {
            "key": "SuppressDuplicateDetection",
            "value": false
        }],
        "IsExecutingOffline": false,
        "IsInTransaction": false,
        "IsOfflinePlayback": false,
        "IsolationMode": 1,
        "MessageName": "Update",
        "Mode": 1,
        "OperationCreatedOn": "\/Date(1506409448000-0700)\/",
        "OperationId": "4af10637-4ea2-e711-8122-000d3aa2331c",
        "OrganizationId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",
        "OrganizationName": "OneFarm",
        "OutputParameters": [],
        "OwningExtension": {
            "Id": "75417616-4ea2-e711-8122-000d3aa2331c",
            "KeyAttributes": [],
            "LogicalName": "sdkmessageprocessingstep",
            "Name": null,
            "RowVersion": null
        },
        "ParentContext": null,
        "PostEntityImages": [],
        "PreEntityImages": [],
        "PrimaryEntityId": "6d81597f-0f9f-e711-8122-000d3aa2331c",
        "PrimaryEntityName": "contact",
        "RequestId": null,
        "SecondaryEntityName": "none",
        "SharedVariables": [{
            "key": "ChangedEntityTypes",
            "value": [{
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "feedback",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "contract",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "salesorder",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "connection",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "socialactivity",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "postfollow",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "incident",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "invoice",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "entitlement",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "lead",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "opportunity",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "quote",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "socialprofile",
                "value": "Update"
            }, {
                "__type": "KeyValuePairOfstringstring:#System.Collections.Generic",
                "key": "contact",
                "value": "Update"
            }]
        }],
        "Stage": 30,
        "UserId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff"
    },
    "PostEntityImages": [{
        "key": "AsynchronousStepPrimaryName",
        "value": {
            "Attributes": [{
                "key": "fullname",
                "value": "James Glynn (sample)"
            }, {
                "key": "contactid",
                "value": "6d81597f-0f9f-e711-8122-000d3aa2331c"
            }],
            "EntityState": null,
            "FormattedValues": [],
            "Id": "6d81597f-0f9f-e711-8122-000d3aa2331c",
            "KeyAttributes": [],
            "LogicalName": "contact",
            "RelatedEntities": [],
            "RowVersion": null
        }
    }],
    "PreEntityImages": [],
    "PrimaryEntityId": "6d81597f-0f9f-e711-8122-000d3aa2331c",
    "PrimaryEntityName": "contact",
    "RequestId": null,
    "SecondaryEntityName": "none",
    "SharedVariables": [],
    "Stage": 40,
    "UserId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff"
}
```

> [!IMPORTANT]
> When the size of the entire HTTP payload exceeds 256 KB, the `x-ms-dynamics-msg-size-exceeded` header is included and the following <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext> properties are removed:
>
> - <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext.ParentContext>
> - <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext.InputParameters>
> - <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext.PreEntityImages>
> - <xref:Microsoft.Xrm.Sdk.RemoteExecutionContext.PostEntityImages>
>
>Some operations don't include these properties.

## Invoke a WebHook from a plug-in or workflow activity

Because a WebHook is a kind of service endpoint, you can invoke it without registering a step by using a plug-in or workflow activity. This approach works the same way as it does for an Azure Service Bus endpoint. You need to provide the [ServiceEndpointId](reference/entities/serviceendpoint.md#BKMK_ServiceEndpointId) to the <xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService> interface. For more information, see the following Azure Service Bus samples:

- [Sample: Azure aware custom plug-in](org-service/samples/azure-aware-custom-plugin.md)
- [Sample: Azure aware custom workflow activity](org-service/samples/azure-aware-custom-workflow-activity.md)

## Troubleshoot WebHook registrations

Webhooks are relatively simple. The service sends the request and evaluates the response. The system can't parse any data returned with the body of the response. It only looks at the response `StatusCode` value.

The timeout is 60 seconds. Generally, if no response is returned before the timeout period or if the response `StatusCode` value isn't within the `2xx` range to indicate success, the operation fails. The exception is when the error returned is in the following table:

|StatusCode|Description|
|-|-|
|`502`|Bad Gateway|
|`503`|Service Unavailable|
|`504`|Gateway Timeout|

These errors indicate a networking issue that might be resolved with another attempt. The WebHook service makes one more attempt only when these error codes are returned.

### Asynchronous Webhooks

If you register your web hook to run asynchronously, you can examine the System Job for details on the error. For more information, see [Query failed asynchronous jobs for a given step](register-web-hook.md#query-failed-asynchronous-jobs-for-a-given-step).

### Synchronous webhooks

[!INCLUDE [synchronous-WebHook-error](includes/synchronous-WebHook-error.md)]

> [!NOTE]
> When you register a webhook for a synchronous step, it sends the execution context data to the configured endpoint immediately. If an error occurs after the request is sent, the data operation rolls back but the request sent to the configured endpoint can't be recalled.

## Next steps

[Register a WebHook](register-web-hook.md)<br />
[Test WebHook registration with request logging site](test-WebHook-registration.md)

### See also

[Write a plug-in](write-plug-in.md)<br />
[Register a plug-in](register-plug-in.md)<br />
[Asynchronous service in Dataverse](asynchronous-service.md)<br />
[Sample: Azure aware custom plug-in](org-service/samples/azure-aware-custom-plugin.md)<br />
[Sample: Azure aware custom workflow activity](org-service/samples/azure-aware-custom-workflow-activity.md)<br />
[Azure Functions](https://azure.microsoft.com/services/functions/)<br />
[ServiceEndpoint table](reference/entities/serviceendpoint.md)<br />
[SdkMessageProcessingStep table](reference/entities/sdkmessageprocessingstep.md)<br />
[AsynchronousOperations table](reference/entities/asyncoperation.md)<br />
<xref:Microsoft.Xrm.Sdk.RemoteExecutionContext><br />
<xref:Microsoft.Xrm.Sdk.IServiceEndpointNotificationService><br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

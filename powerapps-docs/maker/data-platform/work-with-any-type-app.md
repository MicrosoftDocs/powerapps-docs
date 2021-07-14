---
title: "Work with any type of app | MicrosoftDocs"
description: Learn how Microsoft Dataverse provides multiple ways to integrate with any type of app, device, system, or service.
ms.custom: ""
ms.date: 06/16/2020
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "powerapps"
author: "mmercuri"
ms.subservice: dataverse-maker
ms.author: "mmercuri"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Work with any type of app 

Microsoft Dataverse provides multiple ways to integrate in any type of app (mobile, web, desktop), device, system, or service. For cloud solutions, there are ways to integrate regardless of the model in which your solution is deployed&mdash;infrastructure as a service (IaaS), platform as a service (PaaS), or software as a service (SaaS). For IaaS-based solutions, the integration approach also
works well if solutions are running inside of containers.

In some cases, integration with an app can be achieved by using business logic contained in Dataverse. In other cases, it will involve integration via events, the Dataverse OData API, or using plug-ins.

## Defining business logic

tables in Dataverse can use rich server-side logic and validation to ensure data quality and reduce repetitive code in each app that creates and uses data in a table.

- **Business rules**: Validate data across multiple columns and tables, and provide warning and error messages, regardless of the app used to create the data. More information: [Create a business rule for a table](./data-platform-create-business-rule.md)

- **Business process flows**: Guide users to ensure that they enter data consistently and follow the same steps every time. Business process flows are currently only supported for model-driven apps. More information: [Business processes flows overview](/power-automate/business-process-flows-overview)

- **Workflows**: Automate business processes without user interaction. More information: [Classic Dataverse workflows](/power-automate/workflow-processes)

- **Business logic with code**: Supports advanced developer scenarios to extend the app directly through code. More information: [Apply business logic using code](../../developer/data-platform/apply-business-logic-with-code.md)

## Integrating with apps by using events

A common approach of app integration is through the use of events. For example, an event such as adding a new row occurs in Dataverse, and this should be communicated to an associated system so that an action can be taken. For example, if a new support request was raised, it might trigger an SMS message to be sent to the assigned support staff.

This interactivity can also occur in the opposite direction&mdash;an update in an external system might result in data being added, updated, or deleted from a Dataverse environment.

The most popular approaches in Dataverse involve webhooks, Azure messaging (Service Bus, Event Hubs), Azure Logic Apps, or Power Automate.

![Events in Dataverse.](media/cds-events.png "Events in Dataverse")

### Webhooks

With Dataverse, you can send data about events that occur on the service to a web app by using webhooks. A webhook is a lightweight HTTP pattern for connecting web APIs and services with a publish-and-subscribe model. Webhook senders notify receivers about events by making requests to receiver endpoints with some information about the events.

Webhooks enable developers and ISVs to integrate Dataverse data with their own custom code hosted on external services. By using the webhook model, you can secure your endpoint by using authentication header or query string parameter keys. This is simpler than the shared access signature<!--Was SAS. Should be no caps, no abbreviation via Cloud Style Guide.--> authentication model used with Azure Service Bus integration.

- Webhooks can only scale to the point at which your hosted web service can handle the messages.

- Webhooks enable synchronous and asynchronous steps.

- Webhooks send POST requests with the JSON payload and can be consumed by any programming language or web app hosted anywhere.

- Webhooks can be invoked from a plug-in or custom workflow activity.

### Azure Service Bus

Service Bus provides a secure and reliable communication channel between Dataverse runtime data and external, cloud-based line-of-business apps. This capability is especially useful in keeping disparate Dataverse systems or other Dataverse servers synchronized with business data changes.

The sequence of events is as follows:

- A listener app is registered on a Service Bus solution endpoint and begins actively listening for the Dataverse remote execution context on the service bus.

- A user performs some operation in Dataverse that triggers execution of the registered out-of-the-box plug-in or a custom Azure-aware plug-in. The plug-in initiates a post, through an asynchronous service system job, of the current request data context to Service Bus.

- The claims posted by Dataverse are authenticated. Service Bus then relays the remote execution context to the listener. The listener processes the context information and performs some business-related task with that information. Service Bus notifies the asynchronous service of a successful post and sets the status of the related system job to Completed.

Service Bus relays the request message data context between Dataverse and the Service Bus solution listener apps. Service Bus also provides data security so that only authorized apps can access the posted Dynamics 365 data. Authorization of Dataverse to post the data
context to Service Bus, and for listener apps to read it, is managed by Azure shared access signatures.

More information: [Service Bus](https://azure.microsoft.com/services/service-bus/) and [Service Bus authentication and authorization](/azure/service-bus-messaging/service-bus-authentication-and-authorization)

## Logic Apps and Power Automate

Logic Apps, offered via Azure, and Power Automate, offered via Microsoft Power Platform, can trigger a workflow that can be used to integrate with application events and data on a schedule or by activity in a database, system, service, or SaaS.

![Logic Apps and Power Automate with Dataverse.](media/logic-apps-and-power-automate.png "Logic Apps and Power Automate with Dataverse")

These workflows can execute logic and interact with these systems using the hundreds of connectors to databases, PaaS, and SaaS.

For example, when a row is added to a relational database, such as SQL, this might trigger a workflow that can insert this data in Dataverse.

With the ability to create custom connectors by using Open API (formerly known as Swagger) definitions for a service, it's also straightforward to include services, functions, and code running in IaaS and Azure Kubernetes Service (AKS).

## Integrating Dataverse into apps with the OData API

All popular programming languages support a form of integration with REST-based APIs.

![Dataverse with the OData API.](media/cds-with-odata.png "Dataverse with the OData API")

The Dataverse Web API provides a development experience that can be used across a wide variety of programming languages, platforms, and devices. The Web API implements the OData (Open Data Protocol), version 4.0, an OASIS standard for building and consuming RESTful APIs over rich data sources. You can learn more about this protocol at [www.odata.org](https://www.odata.org/). For more information about this standard, see [www.oasis-open.org](https://www.oasis-open.org/standards#odatav4.0).

Dataverse takes an "API first" approach. This means that the service doesn't just provide a mechanism to query data, it also provides metadata from the service on business rules, constraints, and so on that you can use to build intelligent, responsive apps and services.

The API is secured by using OAuth. OAuth requires an idtable provider for authentication. For Dataverse, the idtable provider is Azure Active Directory (Azure AD). To authenticate with Azure AD by using a Microsoft work or school account, use the Azure AD Authentication Libraries (ADAL).

For more information about getting started with the Dataverse Web API, see [Use the Dataverse Web API](../../developer/data-platform/webapi/overview.md).

For more information about using the Dataverse Web API with OAuth, see [Use OAuth with Dataverse](../../developer/data-platform/authenticate-oauth.md).

## Plug-ins

The Dataverse provides the ability to write code that sits between the API and the data. This code, written in .NET, is referred to as a *plug-in*. Because the plug-in sits between the API and the data, it enforces the same logic on every app.

Plug-ins can be synchronous or asynchronous, and perform the following tasks: 

- Return errors to the user.

- Query Dataverse data to evaluate logic to perform.

- Perform data operations.

- Perform outbound HTTP requests.

Plug-ins are registered at points in the event pipeline, which are illustrated here.

<img src = "media/plug-in-event-pipeline.png" alt = "Plug-in event pipeline" width = "335" height = "433" >

Within the event pipeline, the following events can occur: 

- **Requests** and **Responses** can be **examined** and **rejected** or **manipulated** in several steps of the event pipeline.

- **Validation handlers** can throw custom exceptions to reject operations that your logic considers invalid.

- **Pre-operation handlers** can modify requests before the database operation.

- **Post-operation handlers** can modify responses.

- **Async handlers** perform automation after the response is returned.

One constraint with plug-ins is that they must be self-contained. If integration code requires references to other libraries, integration can be done by using Azure Functions.

### Azure Functions

Azure Functions provides a serverless code execution option for business and integration logic.

![Dataverse with Azure Functions.](media/azure-functions.png "Dataverse with Azure Functions")

Functions are triggered by a call from an external system, service, or code. For Dataverse, that trigger can come directly from Dataverse using Service Bus, a webhook, or a call from a plug-in. Additionally, the Azure Functions call can be initiated via a flow in either Logic Apps or Power Automate that involves the Common Data Service connector.

More information:
[Use plug-ins to extend business processes](../../developer/data-platform/plug-ins.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

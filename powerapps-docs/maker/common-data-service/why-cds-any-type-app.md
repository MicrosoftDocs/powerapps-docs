---
title: "Work with any type of app | MicrosoftDocs"
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
ms.author: "mmercuri"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Work with any type of app 

Common Data Service provides multiple ways to integrate in any type of app – mobile, web, desktop, device, system, or service. For cloud solutions, there are ways to integrate regardless of the model in which your solution is deployed – IaaS, PaaS, or SaaS. For IaaS based solutions, the integration approach also
works well if solutions are running inside of containers.

In some cases, integration with an app can be achieve using business logic contained within Common Data Service. In other cases it will involve integration via events, the Common Data Service OData API, or using plug-ins.

## Defining business logic

Entities within Common Data Service can leverage rich server-side logic and validation to ensure data quality and reduce repetitive code in each app that creates and uses data within an entity.

- **Business rules**: Validate data across multiple fields and entities and provide warning and error messages, regardless of the app used to create the data. More information: [Create a business rule](/powerapps/maker/common-data-service/data-platform-create-business-rule).

- **Business process flows**: Guide users to ensure they enter data consistently and follow the same steps every time. Business process flows are currently only supported for model-driven apps. More information: [Business processes flows overview](/power-automate/business-process-flows-overview).

- **Workflows**: Allow you to automate business processes without user interaction. More information: [Classic Common Data Service workflows](/power-automate/workflow-processes).

- **Business logic with code**: Supports advanced developer scenarios to extend the application directly through code. More information: [Apply business logic with code](/powerapps/developer/common-data-service/apply-business-logic-with-code).

## Integrating with applications using events

A common approach of application integration is through the use of events. For example, an event occurs within Common Data Service, such as adding a new record, and this should be communicated to an associated system so that an action could be taken. For example, if a new support request was raised, it might trigger an SMS message to be sent to the assigned support staff.

This interactivity can also occur in the opposite direction – an update in an external system may result in data being added, updated, or deleted from a Common Data Service environment.

The most populate approaches in Common Data Service involve webhooks, Azure Messaging (Service Bus, Event Hubs), Logic Apps, or Power Automate.

![Events in Common Data Service](media/cds-events.png)

### Webhooks

With Common Data Service, you can send data about events that occur on the service to a web application using webhooks. Webhooks is a lightweight HTTP pattern for connecting Web APIs and services with a publish and subscribe model. Webhook senders notify receivers about events by making requests to receiver endpoints with some information about the events.

Webhooks enable developers and ISV’s to integrate Common Data Service data with their own custom code hosted on external services. By using the webhook model, you can secure your endpoint by using authentication header or query string parameter keys. This is simpler than the SAS authentication model used with Azure Service Bus integration.

- Webhooks can only scale to the point at which your hosted web service can handle the messages.

- Webhooks enables synchronous and asynchronous steps.

- Webhooks send POST requests with JSON payload and can be consumed by any programming language or web application hosted anywhere.

- Webhooks can be invoked from a plug-in or custom workflow activity.

### Azure Service Bus

The Azure Service Bus provides a secure and reliable communication channel between Common Data Service runtime data and external cloud-based line-of-business (LOB) applications. This capability is especially useful in keeping disparate Common Data Service systems or other Common Data Service servers synchronized with business data changes.

The sequence of events are as follows:

- A listener application is registered on an Azure Service Bus solution endpoint and begins actively listening for the Common Data Service remote execution context on the service bus.

- A user performs some operation in Common Data Service that triggers execution of the registered OOB plug-in or a custom Azure-aware plug-in. The plug-in initiates a post, through an asynchronous service system job, of the current request data context to the service bus.

- The claims posted by Common Data Service are authenticated. The service bus then relays the remote execution context to the listener. The listener processes the context information and performs some business-related task with that information. The service bus notifies the asynchronous service of a successful post and sets the related system job to a completed status.

The service bus relays the request message data context between Common Data Service and Azure Service Bus solution listener applications. The service bus also provides data security so that only authorized applications can access the posted Dynamics 365 data. Authorization of Common Data Service to post the data
context to the service bus and for listener applications to read it is managed by Azure Shared Access Signatures (SAS).

For more information about the service bus, see [Service Bus](https://azure.microsoft.com/services/service-bus/). For more information about service bus authorization, see [Service Bus authentication and authorization](https://azure.microsoft.com/documentation/articles/service-bus-authentication-and-authorization/).

## Logic Apps and Power Automate

Logic Apps, offered via Azure, and Power Automate, offered via the Power Platform, can trigger a workflow that can be used to integrate with application events and data on a schedule or by activity in a database, system, service, or SaaS.

![Logic Apps and Power Automate with Common Data Service](media/logic-apps-and-power-automate.png)

These workflows can execute logic and interact with these systems using the hundreds of connectors to databases, PaaS, and SaaS.

For example, when a record is added to a relational database, such as SQL, this might trigger a workflow that could insert this data in Common Data Service.

With the ability to create custom connectors using Open API (formerly known as Swagger) definitions for a service, it’s also straightforward to include services, functions, and code running in IaaS and Azure Kubernetes Service (AKS).

## Integrating Common Data Service into applications with the OData API

All popular programming languages support a form of integration with REST-based application programming interfaces (APIs).

![Common Data Service with the OData API](media/cds-with-odata.png)

The Common Data Service Web API provides a development experience that can be used across a wide variety of programming languages, platforms, and devices. The Web API implements the OData (Open Data Protocol), version 4.0, an OASIS standard for building and consuming RESTful APIs over rich data sources. You can learn more about this protocol at [www.odata.org](https://www.odata.org/). Details about this standard are available at [www.oasis-open.org](https://www.oasis-open.org/standards#odatav4.0).

Common Data Service takes an *API first* approach. This means that the service doesn’t just provide a mechanism to query data, it also provides meta-data from the service on business rules, constraints, and so on, that enable you to build intelligent, responsive applications and services.

The API is secured using OAuth. OAuth requires an identity provider for authentication. For Common Data Service, the identity provider is Azure Active Directory (AAD). To authenticate with AAD using a Microsoft work or school account, use the Azure Active Directory Authentication Libraries (ADAL).

For more information about getting started with the Common Data Service Web API, see [Use the Common Data Service Web API](/powerapps/developer/common-data-service/webapi/overview).

For more information about using the Common Data Service Web API with OAUTH, see [Use OAuth with Common Data Service](/powerapps/developer/common-data-service/authenticate-oauth).

## Plug-ins

The Common Data Service provides the ability to write code that sits between the API and the data. This code, written in .NET, is referred to as a plug-in. As the plug in sits between the API and the data, it will enforce the same logic on every application.

Plug-ins can be synchronous or asynchronous and perform the following tasks: 

- Return errors to the user.

- Query Common Data Service data to evaluate logic to perform.

- Perform data operations.

- Perform outbound HTTP Requests.

Plug-ins are registered at points in the event pipeline, which are illustrated here.

![Plug-in event pipeline](media/plug-in-event-pipeline.png)

Within the event pipeline the following events can occur: 

- **Requests** and **Responses** can be **examined** and **rejected** or **manipulated** in several steps of the event pipeline.

- **Validation handlers** can throw custom exceptions to reject operations that your logic considers invalid.

- **Pre-operation handlers** can modify requests before the database operation.

- **Post-operation handlers** can modify responses.

- **Async handlers** perform automation after the response is returned.

One constraint with plug-ins is that they must be self-contained. If integration code requires references to other libraries, integration can be done using Azure Functions.

### Azure Functions

Azure Functions provide a serverless code execution option for business and integration logic.

![Common Data Service with Azure Functions](media/azure-functions.png)

Functions are triggered by a call from an external system, service or code. For Common Data Service, that trigger could be directly from Common Data Service using Service Bus, webhook, or a call from a plug-in. Additionally, the Azure Function call can be initiated via a flow in either Logic Apps or Power Automate that involves the Common Data Service connector.

More information:
[Use plug-ins to extend business processes](/powerapps/developer/common-data-service/plug-ins). 

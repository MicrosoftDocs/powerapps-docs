---
title: Use Web Services with model apps | Microsoft Docs
description: Learn how developers can use web services with model apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/26/2018
ms.author: jdaly
---

# Use Web Services with model apps

The CDS provides two web services you can use to interact with data. Choose the one which best matches the requirement and your skills. More information: [Developer Guide: Choose your development style for Dynamics 365 Customer Engagement](/dynamics365/customer-engagement/developer/choose-development-style)

## Web API
The Web API is an OData v4 RESTful endpoint. Use this for any programming language that supports HTTP requests and authentication using OAuth 2.0.

More information: [Developer Guide: Use the Dynamics 365 Customer Engagement Web API](/dynamics365/customer-engagement/developer/use-microsoft-dynamics-365-web-api)

## Organization Service

The Organization service is a core part of the CDS platform. It is a Windows Communication Foundation (WCF) service and currently exposes only a SOAP endpoint. 
.NET developers can use the SDK assemblies to perform data operations. Within a Plug-in, the Organization service via the SDK assemblies is the only option.
> [!NOTE]
> It is possible for developers to use the SOAP endpoint of the organization service without using the .NET SDK assemblies, but the RESTful nature of the Web API makes it a much superior alternative.

More information: [Developer Guide: Use the Dynamics 365 Organization service](/dynamics365/customer-engagement/developer/use-microsoft-dynamics-365-organization-service)

## About the web services and the platform

It is valuable to recognize that the organization service is what defines the platform. The Web API provides a RESTful programming experience but ultimately all data operations go through the underlying organization service. 

The organization service defines the supported operations as messages. Each message has a name. Within the SDK assemblies each message has a corresponding *&lt;message name&gt;*`Request` and *&lt;message name&gt;*`Response` class. The [IOrganizationService interface](/dotnet/api/microsoft.xrm.sdk.iorganizationservice) in the `Microsoft.Xrm.Sdk.dll` defines several helper methods for common CRUD operations as well as an [Execute method](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.execute) that can be used to invoke messages. All messages use the underlying [OrganizationRequest Class](/dotnet/api/microsoft.xrm.sdk.organizationrequest).

The Web API provides all the same operations as the organization service but presents them in an RESTful style using the OData v4 protocol. OData v4 provides for named operations via *functions* or *actions*. Almost every message available in the organization service is exposed as a corresponding named function or action. Those messages that correspond to CRUD operations are not available in the Web API because as a RESTful service they have implementations using GET, POST, PATCH, and DELETE HTTP methods.

The SOAP endpoint for the organization service was introduced in 2011 and we have announced that it is deprecated. This means that it will continue to work and be supported until we remove it. We have also announced that we will update the .NET SDK assemblies so that they will continue to work after the SOAP endpoint is removed. This means that there will be updated SDK assemblies available before the SOAP endpoint is removed and developers will be required to update their code to use these new assemblies at some point in the future.

## Discovery services
TODO: Add information about the discovery services

## Use Custom Actions

One of the declarative options available for processes is to create a *custom action*. A custom action is essentially creating a new message in the organization service. You can use custom actions to combine a set of operations into a named reusable operation. For example, you might create a new message called *new_Escalate* that combines a standard set of operations that are involved in notifying the correct people when an important customer is experiencing a serious issue.

When you define a custom action, you choose the signature of the operation by defining input parameters and properties to be included in any result that is returned. Custom actions can then be invoked from a declarative process using the designer or by code. 

The unique value of custom actions is that the specific operations they contain can be modified by someone who is not a developer using the designer without impacting other processes or code that calls it.  This remains true if the signature of the action does not change. If you need different input parameters or output properties, you should create a new, different custom action to avoid breaking any processes or code using an existing one.

When a custom action is defined in an environment, a new OData v4 Action is available using the Web API and within the organization service the custom action can be invoked using the [OrganizationRequest Class](/dotnet/api/microsoft.xrm.sdk.organizationrequest) directly or by using a strongly typed class generated using the *Code Generation tool (CrmSvcUtil.exe)*.

More information: 
- [Customization Guide: Actions overview](/dynamics365/customer-engagement/customize/actions)
- [Developer Guide: Create your own actions](/dynamics365/customer-engagement/developer/create-own-actions)
- [Developer Guide: Use Web API actions > Use a custom action](/dynamics365/customer-engagement/developer/webapi/use-web-api-actions#use-a-custom-action)

## Metadata Services

Both the Web API and the organization service include capabilities to perform CRUD operations on the entity schema. While you can perform these operations using code, generally you will use designers to add, update, or delete custom schema elements. Users must have administrator privileges to apply schema changes, but all users can read metadata.

A more common use for the metadata services is to retrieve metadata about the environment that your extension is running within. Because every environment can be different and schema metadata contains much of the information about how the environment is configured, you may need to retrieve this information to allow for your extensions to adapt to other customizations that are in effect in that environment.

Some examples:
- The number of options available in an optionset attribute can change. Rather than hard-code the values in your environment, consider whether different options are present. You can query the system to determine whether the current environment has different options.
- The display name for an entity can be changed. The default display name for the account entity is *Account*. This could be changed to *Company*. If you want to display a message to a user and refer to the name of an entity, you should not hard-code this but instead use the value that matches what the user is accustomed to seeing and use the display name retrieved from the entity metadata instead.

Developing a good working understanding of the metadata in the system can help you understand how the CDS platform works. The designers available to edit metadata cannot show all the details found in the metadata. You can install a model app called the *Metadata Browser* which will allow you to view all the hidden entities and metadata properties that are found in the system. 

More information: [Developer Documentation : Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata)

For more information about working with metadata programmatically see:
- [Developer Guide: Use the Web API with metadata](/dynamics365/customer-engagement/developer/webapi/use-web-api-metadata)
- [Developer Guide: Use the Organization service with Dynamics 365 metadata](/dynamics365/customer-engagement/developer/org-service/use-organization-service-metadata)

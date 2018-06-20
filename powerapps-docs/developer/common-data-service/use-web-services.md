---
title: Use Common Data Service for Apps web services| Microsoft Docs
description: Learn how developers can use Common Data Service for Apps web services.
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

# Use Common Data Service for Apps web services

Common Data Service for Apps provides two web services you can use to interact with data. Choose the one which best matches the requirement and your skills. More information: [Choose your development style for Common Data Service for Apps](/dynamics365/customer-engagement/developer/choose-development-style)

## Web API
The Web API is an OData v4 RESTful endpoint. Use this for any programming language that supports HTTP requests and authentication using OAuth 2.0.

More information: [Use the Common Data Service for Apps Web API](/dynamics365/customer-engagement/developer/use-microsoft-dynamics-365-web-api)

## Organization service

The Organization service is a core part of Common Data Service for Apps platform. It is a Windows Communication Foundation (WCF) service and currently exposes only a SOAP endpoint. 
.NET developers can use the SDK assemblies to perform data operations. Within a Plug-in, the Organization service via the SDK assemblies is the only option.
> [!NOTE]
> It is possible for developers to use the SOAP endpoint of the organization service without using the .NET SDK assemblies, but the RESTful nature of the Web API makes it a much superior alternative.

More information: [Use the CDS for Apps Organization service](/dynamics365/customer-engagement/developer/use-microsoft-dynamics-365-organization-service)

## About the web services and the platform

[!INCLUDE [cc_about-web-services-platform](../../includes/cc_about-web-services-platform.md)]

## Discovery services

Each Common Data Service for Apps user may be able to access multiple Common Data Service for Apps instances. Discovery services let you write code to provide users a list of instances they can connect to based on the Microsoft account they use. Each instance includes a URL that you can then use to connect to the instance they choose. 

A Discovery service is accessed through either the Web API or the Organization Service.

- For the Web API see: [Discover the URL for your organization using the Web API](/dynamics365/customer-engagement/developer/webapi/discover-url-organization-web-api)
- For the Organization Service see: [Discover the URL for your organization using the Organization Service](/dynamics365/customer-engagement/developer/org-service/discover-url-organization-organization-service)

## Use custom actions

One of the declarative options available for processes is to create a *custom action*. A custom action is essentially creating a new message in the organization service. You can use custom actions to combine a set of operations into a named reusable operation. For example, you might create a new message called *new_Escalate* that combines a standard set of operations that are involved in notifying the correct people when an important customer is experiencing a serious issue.

When you define a custom action, you choose the signature of the operation by defining input parameters and properties to be included in any result that is returned. Custom actions can then be invoked from a declarative process using the designer or by code. 

The unique value of custom actions is that the specific operations they contain can be modified by someone who is not a developer using the designer without impacting other processes or code that calls it.  This remains true if the signature of the action does not change. If you need different input parameters or output properties, you should create a new, different custom action to avoid breaking any processes or code using an existing one.

When a custom action is defined in an environment, a new OData v4 Action is available using the Web API and within the organization service the custom action can be invoked using the [OrganizationRequest Class](/dotnet/api/microsoft.xrm.sdk.organizationrequest) directly or by using a strongly typed class generated using the *Code Generation tool (CrmSvcUtil.exe)*.

More information: 
- [Common Data Service for Apps Customization Guide: Actions overview](/dynamics365/customer-engagement/customize/actions)
- [Create your own actions](/dynamics365/customer-engagement/developer/create-own-actions)
- [Use Web API actions > Use a custom action](/dynamics365/customer-engagement/developer/webapi/use-web-api-actions#use-a-custom-action)

## Metadata services

Both the Web API and the organization service include capabilities to perform CRUD operations on the entity schema. While you can perform these operations using code, generally you will use designers to add, update, or delete custom schema elements. Users must have administrator privileges to apply schema changes, but all users can read metadata.

A more common use for the metadata services is to retrieve metadata about the environment that your extension is running within. Because every environment can be different and schema metadata contains much of the information about how the environment is configured, you may need to retrieve this information to allow for your extensions to adapt to other customizations that are in effect in that environment.

Some examples:
- The number of options available in an optionset attribute can change. Rather than hard-code the values in your environment, consider whether different options are present. You can query the system to determine whether the current environment has different options.
- The display name for an entity can be changed. The default display name for the account entity is *Account*. This could be changed to *Company*. If you want to display a message to a user and refer to the name of an entity, you should not hard-code this but instead use the value that matches what the user is accustomed to seeing and use the display name retrieved from the entity metadata instead.

Developing a good working understanding of the metadata in the system can help you understand how Common Data Service for Apps platform works. The designers available to edit metadata cannot show all the details found in the metadata. You can install a model-driven app called the *Metadata Browser* which will allow you to view all the hidden entities and metadata properties that are found in the system. 

More information: [Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata)

For more information about working with metadata programmatically see:
- [Use the Web API with metadata](/dynamics365/customer-engagement/developer/webapi/use-web-api-metadata)
- [Use the Organization service with CDS for Apps metadata](/dynamics365/customer-engagement/developer/org-service/use-organization-service-metadata)
 
### See also

[Common Data Service for Apps Developer Overview](overview.md)


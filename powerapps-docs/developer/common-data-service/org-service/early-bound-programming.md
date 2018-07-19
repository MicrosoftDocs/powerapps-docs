---
title: "Early-bound and Late-bound programming using the Organization service (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Early-bound and Late-bound programming using the Organization service

<!-- 

Late-bound is the 'default mode' that can be used without running CrmSvcUtil.exe
This topic should describe the pros and cons of the different style. 

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/mix-early-late-bound-entities
-->

When you work with the Organization service assemblies you have two styles you can use: *early-bound* and *late-bound*.

## Early-Bound

Early-bound programming requires that you first generate a set of classes based on the metadata for a specific organization using the code generation tool (CrmSvcUtil.exe). More information: [Generate classes for early-bound programming using the Organization service](generate-early-bound-classes.md)

When you have generated early-bound entity classes using the code generation tool you will enjoy a better experience while you write code because classes and attribute properies using the respective `SchemaName` property values:

- <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SchemaName> 
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName>
- <xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase>.<xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.SchemaName>

Simply instantiate the class and let IntelliSense in Visual Studio provide the names of properties and relationships.

The classes generated for early-bound programming can also include definitions for any custom actions that are defined for the environment. This will provide you with a pair of request and response classes to use with these custom actions. More information: [Custom Actions](../custom-actions.md)

There is also an option to extend the code generation tool to change the output. One extension creates enums for each optionset option value. This provides a better experience because you don't have to look up the integer value for each option. More information: [Create extensions for the code generation tool](extend-code-generation-tool.md)

However, because the classes are generated using metadata from a specific instance, and each instance may have different entities and attributes, and these can change over time. You may need to write code to work for entities that are not present when you generate the strongly typed classes.

### Advantages:

 - IntelliSense makes code easier to write and read

### Disadvantages:

- You need to regenerate the classes as you modify the schema

## Late-Bound

Late-bound programming uses the <xref:Microsoft.Xrm.Sdk.Entity> class and you need to refer to entities, and attributes using their `LogicalName` property values: 
- <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalName> 
- <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName>

Relationships do not have a `LogicalName` property, so the <xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase>.<xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.SchemaName> property is used.

The main advantage for late-bound programming is that you don't need to generate the classes or include that generated file within your projects. The generated file can be quite large.

### Advantages:

 - You don't need to regenerate the entity classes
 - Very slightly more performant

### Disadvantages:

- No IntelliSense for entities, attributes, and relationships
- More, less readable code

## Mix early and late bound

Because all the generated classes inherit from the <xref:Microsoft.Xrm.Sdk.Entity> class used with late-bound programming, you can work with entities, attributes, and relationships not defined within classes.

<!-- TODO: So much debate and opinions about which to use e.g. https://stackoverflow.com/questions/15038699/what-are-the-disadvantages-of-early-bound/15040087 

Seems like the need to call the EnableProxyTypes is only needed for the proxy that is passed into plug-ins?

https://docs.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.client.organizationserviceproxy.enableproxytypes

Using CrmServiceClient I don't need it.
-->
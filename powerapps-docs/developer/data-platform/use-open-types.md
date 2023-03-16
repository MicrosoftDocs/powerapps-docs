---
title: "Use open types with Custom APIs (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use the Expando open type with Custom APIs." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 03/14/2023
ms.reviewer: jdaly
ms.topic: article
author: divkamath # GitHub ID
ms.subservice: dataverse-developer
ms.author: dikamath # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - PHecke
  - JimDaly
---
# Use open types with Custom APIs

An *open type* is a structured type that can have dynamic properties. Most types that are defined in the Dataverse SDK for .NET or the Web API $metadata service documents are *closed types*. With closed types, every property name and type value is known. If you use the wrong name, or set the value to the wrong type you get an error. Normally, this structure is a good thing, but sometimes your business logic requires a more flexible approach.

When you create a Dataverse message using Custom API, you can specify the names and types of each of the request parameters and response properties. There are currently 13 different types to choose from so you can create closed types that the system knows about and can validate for you. But closed types aren't dynamic or allow for complex and nested properties.

You could define a message with a single string parameter and expect callers to pass arbitrary JSON as the value, and you could return arbitrary JSON in a single string response property. But this pattern places a burden on the developer of the calling application to correctly compose the JSON to send and parse the JSON you return. As the creator of the message, you'll need to provide documentation and examples showing the correct structure and types. You also need to detect when these types are incorrect and return useful errors.

Dataverse open types provide a middle ground where you use existing Dataverse types and can compose nested properties to flexibly express the requirements of your business logic.

## How to use open types

To use open types you need a message that is configured for them. With Custom API, you specify that a request parameter or response property is open by setting the `Type` to **Entity** (3) or **EntityCollection** (4) *without* specifying a `LogicalEntityName`.

When you do this, you are telling Dataverse that the **Entity** is a collection of key/value pairs that can't be validated against any table definition, so it won't try. **EntityCollection** is just an array of **Entity**.

There are several ways you can use this, as the following sections explain.

### Use real entities

You can have an API with parameters or response properties that represent more than one possible Entity types that represent table rows. For example, you can have a `Customer` parameter that can accept either `Account` or `Contact` records. But in this case, the attribute names and types will not be validated by the system. You might get an error when you try to save or update such records unless you include your own validation.

<!-- Might be useful to expose some mechanism to validate known entities without trying to create or update them? -->

### Use Entity as a dictionary

The more common case is to use the Entity as a dictionary. In this case, it serves as a container for a set of string keys that can have values of any type.

The correct structure of the data to pass in this dictionary will depend on the author of the message. The Dataverse service documents or generated early-bound classes will not provide these details. It is imperative for the author of the message to provide clear documentation about how to pass parameters of this type.




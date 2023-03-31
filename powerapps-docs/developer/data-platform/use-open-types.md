---
title: "Use open types with Custom APIs (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use open types with Custom APIs." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/01/2023
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

An _open type_ is a structured type that can have dynamic properties. Most types that are defined in Dataverse are _closed types_. With closed types, every property name and type value is known. If you use the wrong name, or set the value to the wrong type you get an error. Normally, this structure is a good thing, but sometimes your business logic requires a more flexible approach.

When you create a Dataverse message using Custom API, you can specify the names and types of each of the request parameters and response properties. There are currently [13 different types to choose from](/power-apps/developer/data-platform/reference/entities/customapirequestparameter#type-choicesoptions) so you can create closed types that the system knows about and can validate for you. But closed types aren't dynamic or allow for complex and nested properties.

## Use JSON strings or open types

You don't need to use open types. You can define define request parameters and response properties as strings and require callers to pass JSON data as the value. You can return any kind of JSON data as the value of a string response property. When you do this, your plug-in code must deserialize the JSON received and serialize the JSON to return. Your code is responsible for validating the JSON data received and returning useful error messages when the data is invalid.

The advantage of using open types is that you can use existing Dataverse types to compose the data structures you want to use. Developers using your custom apis with the Dataverse SDK for .NET can use the [Entity](xref:Microsoft.Xrm.Sdk.Entity) class to compose requests and process responses.

In either case, Dataverse doesn't know the details of the data structures you are using. As the API developer, you are responsible for documenting these structures and providing any helper classes to enable callers to be successful using your API. More information: [Recommendations](#recommendations)

## How to use open types

To use open types you need a message that is configured for them. With Custom API you specify that a request parameter or response property is open by setting the `Type` to **Entity** (3) or **EntityCollection** (4) _without_ specifying a `LogicalEntityName`.

When you do this, you are telling Dataverse that the **Entity** is a collection of key/value pairs that can't be validated against any table definition, so it won't try. An **EntityCollection** without a `LogicalEntityName` is just an array of **Entity**.

> [!NOTE]
> Custom API defined as _functions_ can't use open types as request parameters, but may use them as response properties.

### Use Dataverse entities

While not actually an open type, it is worth mentioning that you can have a custom API with parameters or response properties that represent more than one possible closed entity types. For example, you can create a Custom API with a `Customer` parameter that can accept either `Account` or `Contact` entity instances. Your plug-in code can check the [Entity.LogicalName](xref:Microsoft.Xrm.Sdk.Entity.LogicalName) value to determine the type.

### Use Entity as a dictionary

The more common case is to use the Entity as a dictionary. In this case, the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection provide the way to specify a set of keys and values. The values can be any .NET type and can be nested. Other Entity class properties and methods are not used.

Let's say that your application uses data that comes from or will be sent to Microsoft Graph and represents the [educationSchool resource type](/graph/api/resources/educationschool?view=graph-rest-1.0). You might use an open type like the following examples.

# [SDK for .NET](#tab/sdk)

To define an open type with the SDK, simply use the [Entity](xref:Microsoft.Xrm.Sdk.Entity) class without specifying the entity name, then set the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection with the keys and the values.

```csharp
var educationSchool = new Entity() {
    Attributes =
    {
        { "id", Guid.NewGuid() },
        { "displayName","Redmond STEM Academy" },
        { "phone", "555-1234" },
        { "address",  new Entity() //physicalAddress resource type
            {
            Attributes =
                {
                    { "city","Redmond" },
                    { "countryOrRegion","United States" },
                    { "postalCode","98008" },
                    { "state","Washington" },
                    { "street","123 Maple St" },
                }
            }
        }
    }
};
```

# [Web API](#tab/webapi)

To specify an open type when using Web API, you must set the `@odata.type` annotation value to `Microsoft.Dynamics.CRM.expando`.

```json
{
  "@odata.type": "Microsoft.Dynamics.CRM.expando",
  "id@odata.type": "Guid",
  "id": "59fab58c-46f9-425c-b32d-43726fb6e95b",
  "displayName@odata.type": "String",
  "displayName": "Redmond STEM Academy",
  "phone@odata.type": "String",
  "phone": "555-1234",
  "address": {
    "@odata.type": "Microsoft.Dynamics.CRM.expando",
    "city@odata.type": "String",
    "city": "Redmond",
    "countryOrRegion@odata.type": "String",
    "countryOrRegion": "United States",
    "state@odata.type": "String",
    "state": "Washington",
    "street@odata.type": "String",
    "street": "123 Maple St"
  }
}
```

> [!NOTE]
> Notice that the `id` value has an `id@odata.type` annotation. This is necessary to specify that the value represents a <xref:System.Guid> rather than a <xref:System.String>. Unless specified, OData will expect that the simplest JSON type is intended.
>
> Each of the string values also has an annotation to specify that they are strings. This is a mitigation against a known issue in OData [https://github.com/OData/odata.net/issues/764](https://github.com/OData/odata.net/issues/764). If the string value contains an open bracket '[' or single quote ', the OData library will return an error like the following `Microsoft.OData.ODataException: Found an unbalanced bracket expression.`. Unless you are certain that the values sent will never include these characters, you must include the appropriate annotation to prevent this error.

---

### Use other known types

In addition to basic .NET types, you can also use certain types known to Dataverse. The SDK for .NET contains definitions of many classes that Dataverse knows about, and in the Web API these are listed among the [Web API Complex Type Reference](xref:Microsoft.Dynamics.CRM.ComplexTypeIndex).

## Recommendations

The correct structure of the data to pass in this dictionary will depend on the author of the message. The Dataverse service documents or generated early-bound classes will not provide these details. It is imperative for the author of the message to provide clear documentation about how to pass parameters of this type, or provide their own classes to represent the types they expect

## Known issues

The following are known issues using open types

It is possible to send data that represents an array to

## Frequently asked questions (FAQ)

## See also

[Odata.org Advanced Tutorial: Open Type](https://www.odata.org/getting-started/advanced-tutorial/#openType)

---
title: "Use open types with Custom APIs (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use open types with Dataverse Custom APIs." # 115-145 characters including spaces. This abstract displays in the search result.
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

An _open type_ is a structured type that can have dynamic properties. All types that are defined in Dataverse are _closed types_. With closed types, every property name and type value is known. If you use the wrong name, or set the value to the wrong type you get an error. Normally, this structure is a good thing, but sometimes your business logic requires a more flexible approach.

When you create a Dataverse message using Custom API, you must specify the names and types of each of the request parameters and response properties. There are currently [13 different types to choose from](/power-apps/developer/data-platform/reference/entities/customapirequestparameter#type-choicesoptions) so you can create closed types that the system knows about and can validate for you. But closed types aren't dynamic or allow for complex and nested properties.

Open types with custom APIs enable two scenarios:

1. [Structured dynamic data](#structured-dynamic-data). This data can't be described by a class, so there's no need to serialize or deserialize it.
1. [Custom closed types](#custom-closed-types). When you want a custom api to accept a request parameter or return a response property using a specific complex type that can't be expressed using the [options currently available](/power-apps/developer/data-platform/reference/entities/customapirequestparameter#type-choicesoptions).

It's important to understand the scenario that applies to your custom api to use open types correctly, but lets understand how to use open types first.

## How to use open types

To use open types, you need a message that is configured for them. With Custom API, you specify that a request parameter or response property is open by setting the `Type` to **Entity** (3) or **EntityCollection** (4) _without_ specifying a `LogicalEntityName`.

When you don't specify the `LogicalEntityName`, you're telling Dataverse that the **Entity** is a collection of key/value pairs that can't be validated against any table definition, so it doesn't try. An **EntityCollection** without a `LogicalEntityName` is just an array of **Entity**.

> [!NOTE]
> Custom API defined as _functions_ can't use open types as request parameters, but may use them as response properties.

### Use Dataverse entities

While not actually an open type, it's worth mentioning that you can have a custom API with parameters or response properties that represent more than one possible closed entity types. For example, you can create a Custom API with a `Customer` parameter that expects either `Account` or `Contact` entity instances. Dataverse allows *any* entity type. Your plug-in code must check the [Entity.LogicalName](xref:Microsoft.Xrm.Sdk.Entity.LogicalName) value to determine whether it's a type you expect.

### Use Entity as a dictionary

The more common case is to use the Entity as a dictionary. Use the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection to specify a set of keys and values. The values can be any .NET type and can be nested. Don't use any other [Entity](xref:Microsoft.Xrm.Sdk.Entity) class properties.

Let's say that your application uses data that comes from or will be sent to Microsoft Graph and represents the [educationSchool resource type](/graph/api/resources/educationschool). You might use an open type like the following examples.

# [SDK for .NET](#tab/sdk)

To use an open type with the SDK, use the [Entity](xref:Microsoft.Xrm.Sdk.Entity) class without specifying the entity name, then set the [Entity.Attributes](xref:Microsoft.Xrm.Sdk.Entity.Attributes) collection with the keys and the values.

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

To use an open type when using Web API, you must set the `@odata.type` annotation value to `Microsoft.Dynamics.CRM.expando`. This annotation tells Dataverse this is an [expando EntityType](xref:Microsoft.Dynamics.CRM.expando), which has no properties and inherits from the [crmbaseentity EntityType](xref:Microsoft.Dynamics.CRM.crmbaseentity). More information: [expando](webapi/web-api-entitytypes.md#expando)

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

Notice that the `id` value has an `id@odata.type` annotation. This annotation is necessary to specify that the value represents a <xref:System.Guid> rather than a <xref:System.String>. Unless specified, OData expects that the simplest JSON type is intended.

If the value is a number, it's `Int32`. If the value is `Decimal`, `Double`, `Int16`, or `Int64`, you must specify the type using the `<property name>@odata.type` annotation.

> [!NOTE]
> Notice that each of the string values also has an annotation to specify that they are strings. This is a mitigation against a known issue in OData [https://github.com/OData/odata.net/issues/764](https://github.com/OData/odata.net/issues/764). If the string value contains an open bracket '`[`' or single quote '`'`', the OData library will return an `Microsoft.OData.ODataException`. Unless you are certain that the values sent will never include these characters, you must include the `"<property name>@odata.type": "String"` annotation to prevent this error.

If the value is an array, you must always include an annotation using this pattern: `"<property name>@odata.type": "Collection(<type>)"`

For example:

```json
{
  "@odata.type": "Microsoft.Dynamics.CRM.expando",
   "stringArray": ["one","two","three"],
   "stringArray@odata.type": "Collection(String)",
   "intarray": [1,2,3],
   "intarray@odata.type": "Collection(Int32)"
}
```

> [!NOTE]
> Please see the known issue: [Error using Array data with Web API](#error-using-array-data-with-web-api)

---


### Use Dataverse types

In addition to basic .NET types, you can also use types known to Dataverse. The SDK for .NET contains definitions of many classes that Dataverse knows about, and in the Web API these types are listed among the Web API [Complex Type Reference](xref:Microsoft.Dynamics.CRM.ComplexTypeIndex) and [Enum Type Reference](xref:Microsoft.Dynamics.CRM.EnumTypeIndex).

When using the SDK, you can simply set the values.

When using Web API, you must specify the type using the Web API namespace: `Microsoft.Dynamics.CRM`. For example:

```json
{
  "@odata.type": "Microsoft.Dynamics.CRM.expando",
  "label@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
   "label": {      
      "Label": "Yes",
      "LanguageCode": 1033
   },
  "labelarray": [
    {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "test",
      "LanguageCode": 1033
    },
    {
      "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
      "Label": "prøve",
      "LanguageCode": 1030
    }
  ],
  "labelarray@odata.type": "Collection(Microsoft.Dynamics.CRM.LocalizedLabel)",
  "enumarray": ["DateOnly"],
  "enumarray@odata.type": "Collection(Microsoft.Dynamics.CRM.DateTimeFormat)"
}

```

## Structured dynamic data

Structured dynamic data can be defined using various formats that can be set as a string: JSON, XML, YAML, HTML. This kind of data can be easily set using a string parameter or response property. So why use open types?

||When to use?  |
|---------|---------|
|**Use String**|When the structured data is being passed through your custom api and sent to another service or consumed as a string by another application calling your custom api.|
|**Use Open Type**|When the plug-in that supports your custom api, or any plug-ins that extend your custom api, must read or change the structured data.|

Parsing a string value into an object such as [XDocument](xref:System.Xml.Linq.XDocument) or [JObject](https://www.newtonsoft.com/json/help/html/t_newtonsoft_json_linq_jobject.htm) so that you can manipulate it in your plug-in is a relatively expensive operation. When your plug-in, or any other plug-in that might extend the logic in your custom api, changes the data, they must convert the object back into a string. You can avoid these expensive operations by using open types.  

With open types, callers of your custom api can use the familiar dictionary structure that the [Entity](xref:Microsoft.Xrm.Sdk.Entity) class provides so your plug-in can interact with it in the same way you work with other Dataverse records.

If you are serializing or deserializing the string data to a class, your data isn't dynamic and you should review the next section.


## Custom closed types

Open types allow for dynamic and unstructured data. But you should consider whether your API has truly dynamic parameters or if you actually want to have a custom type.

Currently, you can't define a custom type that Dataverse knows about. But using open types you can define a closed-type class that Dataverse can process as an open type. Developers using your Custom API can use your classes to have a better, more productive experience using your custom api with fewer opportunities for errors.

For example, let's say that your custom api requires a parameter that tracks a course using an array of points that contain latitude and longitude information. You need a `Location` class.

# [SDK for .NET](#tab/sdk)

You can create a `Location` class that inherits from the [Entity](xref:Microsoft.Xrm.Sdk.Entity) class and contains the properties you need. For example:

```csharp
using Microsoft.Xrm.Sdk;

namespace MyCompany
{
    /// <summary>
    /// Specifies a location for use with my_CustomAPI
    /// </summary>
    public class Location : Entity
    {
        // Gets or sets the latitude of the Location.
        [AttributeLogicalName("Latitude")]
        public double Latitude
        {
            get
            {
                return GetAttributeValue<double>("Latitude");
            }
            set
            {
                SetAttributeValue("Latitude", value);
            }
        }

        // Gets or sets the longitude of the Location.
        [AttributeLogicalName("Longitude")]
        public double Longitude
        {
            get
            {
                return GetAttributeValue<double>("Longitude");
            }
            set
            {
                SetAttributeValue("Longitude", value);
            }
        }
    }
}
```

Because this type inherits from the `Entity` class, it can use the `Entity` [GetAttributeValue](xref:Microsoft.Xrm.Sdk.Entity.GetAttributeValue%2A) and [SetAttributeValue](xref:Microsoft.Xrm.Sdk.Entity.SetAttributeValue%2A) methods with to access the values in the `Attributes` collection. You can use this class within your plug-in code and share it with consumers a library or in sample code in your documentation.

The result is code that is easier to use and read.

**Before**

```csharp
var location = new Entity() { 
   Attributes =
   {
      { "Latitude", 47.66132951804776 },
      { "Longitude", -122.11446844957624},            
   }            
};

// OR 

var location = new Entity();
location["Latitude"] = 47.66132951804776;
location["Longitude"] = -122.11446844957624;
```

**After**

```csharp
var location = new Location { 
   Latitude = 47.66132951804776,
   Longitude = -122.11446844957624
};

// OR 

var location = new Location()
location.Latitude = 47.66132951804776;
location.Longitude = -122.11446844957624;
```

# [Web API](#tab/webapi)

Because Web API can be used with .NET and other programming languages, the specific method depends on the language, and the technologies you'll use to work with JSON.

When using [Json.NET](https://www.newtonsoft.com/json) with C#, you can define a `Location` class like this:

```csharp
using Newtonsoft.Json;

namespace MyCompany
{
    public class Location 
    {
        [JsonProperty("@odata.type")]
        public string ODataType => "Microsoft.Dynamics.CRM.expando";

        // Gets or sets the latitude of the Location.
        public double? Latitude { get; set; }

        [JsonProperty("Latitude@odata.type")]
        public static string LatitudeType => "Double";

        // Gets or sets the longitude of the Location.
        public double? Longitude { get; set; }

        [JsonProperty("Longitude@odata.type")]
        public static string LongitudeType => "Double";
    }
}

```

You can share this class with consumers a library or in sample code in your documentation.

When a developer uses this class, they don't need to worry about setting the `@odata.type` annotations.

```csharp
Location location = new() {
   Latitude = 47.66132951804776,
   Longitude = -122.11446844957624
};

// OR 

var location = new()
location.Latitude = 47.66132951804776;
location.Longitude = -122.11446844957624;
```

The `@odata.type` annotations are always included when the class instance is serialized.

```json
{
    "@odata.type": "Microsoft.Dynamics.CRM.expando",
    "Latitude": 47.66132951804776,
    "Latitude@odata.type": "Double",
    "Longitude": -122.11446844957624,
    "Longitude@odata.type": "Double"
}
```

---



## Known issues

The following are known issues using open types:

### Error using Array data with Web API

When sending data that contains an array using Web API, the following error occurs when the custom api has a plug-in:

```json
{
  "error": {
    "code": "0x80040224",
    "message": "Element 'http://schemas.datacontract.org/2004/07/System.Collections.Generic:value' contains 
     data from a type that maps to the name 'System.Collections.Generic:List`1'. The deserializer has no 
     knowledge of any type that maps to this name. Consider changing the implementation of the ResolveName 
     method on your DataContractResolver to return a non-null value for name 'List`1' and namespace 
     'System.Collections.Generic'.",
  }
}
```

This error doesn't occur when the client application is using the SDK for .NET or when no plug-in is set for the custom api.


## Frequently asked questions (FAQ)

Use the **Feedback** for **This page** button below to submit questions you have about open types.

## See also

[Create and use Custom APIs](custom-api.md)<br />
[Odata.org Advanced Tutorial: Open Type](https://www.odata.org/getting-started/advanced-tutorial/#openType)

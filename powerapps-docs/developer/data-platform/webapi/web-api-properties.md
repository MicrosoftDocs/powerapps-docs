---
title: "Web API Properties (Microsoft Dataverse)| Microsoft Docs"
description: "Describes OData Property elements defined for EntityTypes within the Dataverse Web API."
ms.custom: ""
ms.date: 11/24/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)" 
author: "JimDaly" # GitHub ID
ms.author: pehecke
manager: "sunilg"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API Properties

Within the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), each entity type that is not abstract will have `Property` elements.

Each `Property` element has the following attributes:

|Attribute  |Description  |
|---------|---------|
|`Name`|The name of the property. This value is case sensitive.|
|`Type`|The primitive type of the property. See Primitive types used by Dataverse|

When you retrieve the $metadata document with [Metadata annotations](web-api-service-documents.md#metadata-annotations) you can see some `Annotation` elements that can be useful. For example, the following `name` and `openrevenue` properties:

```xml
<Property Name="name" Type="Edm.String" Unicode="false">
    <Annotation Term="Org.OData.Core.V1.Description" String="Type the company or business name." />
</Property>
<Property Name="openrevenue" Type="Edm.Decimal" Scale="Variable">
    <Annotation Term="Org.OData.Core.V1.Description" String="Sum of open revenue against an account and its child accounts." />
    <Annotation Term="Org.OData.Core.V1.Computed" Bool="true" />
    <Annotation Term="Org.OData.Core.V1.Permissions">
        <EnumMember>Org.OData.Core.V1.PermissionType/Read</EnumMember>
    </Annotation>
</Property>
```
With the annotations in this example, you can know that the `openrevenue` field is read-only.

With [Metadata annotations](web-api-service-documents.md#metadata-annotations) applied, you will find these annotations for properties:

|Annotation Term  |Description  |
|---------|---------|
|`Org.OData.Core.V1.Description`|A description of the property|
|`Org.OData.Core.V1.Computed`|Whether the property is computed. You can't set this value because it is computed by Dataverse.|
|`Org.OData.Core.V1.Permissions`|Includes the types of permissions available for the property. This is only included when permissions are limited, and it always contains the value `<EnumMember>Org.OData.Core.V1.PermissionType/Read</EnumMember>` meaning that you can only read this value. |

> [!NOTE]
> `Org.OData.Core.V1.Computed` and `Org.OData.Core.V1.Permissions` annotations are frequently found together, but not always. Either of them means the property is read-only.

## Primitive types used by Dataverse

Properties for entity types used for business data will only include primitive types.

The following are primitive types currently used by Dataverse.


|Type|Description|
|---------|---------|
|Edm.Binary|Binary data. Used for file and image data.|
|Edm.Boolean|Binary-valued logic.|
|Edm.Date|Date without a time-zone offset.|
|Edm.DateTimeOffset|Date and time with a time-zone offset, no leap seconds|
|Edm.Decimal|Numeric values with fixed precision and scale|
|Edm.Double|IEEE 754 binary64 floating-point number (15-17 decimal digits)|
|Edm.Guid|16-byte (128-bit) unique identifier|
|Edm.Int16|Signed 16-bit integer. Used only for certain schema EntityType properties|
|Edm.Int32|Signed 32-bit integer|
|Edm.Int64|Signed 64-bit integer|
|Edm.String|Sequence of UTF-8 characters<br />This type may include the `Unicode="false"` facet.<br /><br />When this facet exists, the string property will only contain and accept string values with characters limited to the ASCII character set.<br /><br />If no value is specified, the Unicode facet defaults to true.|

## Lookup properties

You can find properties which use the following naming convention: `_<name>_value`. These are called *lookup properties*.

Lookup properties are computed, read-only properties that have an `Edm.Guid` value. You can use these lookup properties in a query filter to match all the records associated to the single record in the many-to-one relationship.

To change the value of a lookup property, you must change the single-valued navigation property that it represents. More information: [Lookup properties](web-api-navigation-properties.md#lookup-properties)

When you include lookup properties in a query, you can request annotations to be included that provide additional information about the data that is set for those underlying attributes which aren’t represented by a single-valued navigation property. More information: [Retrieve data about lookup properties](query-data-web-api.md#retrieve-data-about-lookup-properties).

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />
[Web API Service Documents](web-api-service-documents.md)<br />
[Web API EntityTypes](web-api-entitytypes.md)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

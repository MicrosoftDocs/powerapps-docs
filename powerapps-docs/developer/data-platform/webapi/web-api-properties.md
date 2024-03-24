---
title: Web API Properties
description: Learn about OData property elements that are defined for EntityTypes in the Microsoft Dataverse Web API.
ms.topic: conceptual
ms.date: 04/06/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.service: powerapps
applies_to: 
  - "Dynamics 365 (online)" 
search.audienceType: 
  - developer
contributors:
 - JimDaly
ms.custom: bap-template
---
# Web API properties

In the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), each entity type that isn't abstract has `Property` elements. Each `Property` element has the following attributes:

|Attribute  |Description  |
|---------|---------|
|`Name`|The name of the property; usually the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName> of the column and is always lower case. One exception to this rule is [Lookup properties](#lookup-properties).|
|`Type`|The primitive type of the property. See [Primitive types used by Dataverse](#primitive-types-used-by-dataverse)|

When you retrieve the $metadata document with [metadata annotations](web-api-service-documents.md#metadata-annotations) you can see some `Annotation` elements that can be useful. For example, the following `name` and `openrevenue` properties:

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

The following table describes the annotations that are returned with [metadata annotations](web-api-service-documents.md#metadata-annotations) applied.

|Annotation term  |Description  |
|---------|---------|
|`Org.OData.Core.V1.Description`|A description of the property|
|`Org.OData.Core.V1.Computed`|Whether the property is computed; read-only because it's computed by Dataverse.|
|`Org.OData.Core.V1.Permissions`|Includes the types of permissions available for the property. Only included when permissions are limited, and it always contains the value `<EnumMember>Org.OData.Core.V1.PermissionType/Read</EnumMember>` meaning it's read-only. |

> [!NOTE]
> `Org.OData.Core.V1.Computed` and `Org.OData.Core.V1.Permissions` annotations are frequently found together, but not always. Either of them means the property is read-only.

## Primitive types used by Dataverse

Properties for entity types that are used for business data include primitive types only. The following table describes the primitive types Dataverse uses.


|Type|Description|
|---------|---------|
|`Edm.Binary`|Binary data. Used for file and image data.|
|`Edm.Boolean`|Binary-valued logic.|
|`Edm.Date`|Date without a time zone offset.|
|`Edm.DateTimeOffset`|Date and time with a time zone offset, no leap seconds|
|`Edm.Decimal`|Numeric values with fixed precision and scale|
|`Edm.Double`|IEEE 754 binary64 floating-point number (15-17 decimal digits)|
|`Edm.Guid`|16-byte (128-bit) unique identifier|
|`Edm.Int16`|Signed 16-bit integer. Used only for certain schema EntityType properties|
|`Edm.Int32`|Signed 32-bit integer|
|`Edm.Int64`|Signed 64-bit integer|
|`Edm.String`|Sequence of UTF-8 characters<br />This type may include the `Unicode="false"` facet.<br /><br />When this facet exists, the string property will only contains and accepts string values with characters limited to the ASCII character set.<br /><br />If no value is specified, the Unicode facet defaults to true.|

## Lookup properties

Some properties use the following naming convention: `_<name>_value`. These properties are called *lookup properties*. Lookup properties are computed, read-only properties that have an `Edm.Guid` value. You can use these lookup properties in a query filter to match all the records associated to the single record in the many-to-one relationship.

OData represents lookup columns as [Single-valued navigation properties](web-api-navigation-properties.md#single-valued-navigation-properties) rather than properties. Dataverse provides lookup properties to simplify scenarios to retrieve data using the primary key of a related record. To change the value of a lookup property, you must change the single-valued navigation property that it represents. More information: [Lookup properties](web-api-navigation-properties.md#lookup-properties)

When you include lookup properties in a query, you can request annotations to be included that provide additional information about the data that is set for those underlying attributes that aren't represented by a single-valued navigation property. More information: [Lookup property data](query-data-web-api.md#lookup-property-data)

## Next steps

Learn about navigation properties.

> [!div class="nextstepaction"]
> [Navigation properties](web-api-navigation-properties.md)


### See also  

[Use the Dataverse Web API](overview.md)   
[Web API types and operations](web-api-types-operations.md)   
[Web API Service Documents](web-api-service-documents.md)   
[Web API EntityTypes](web-api-entitytypes.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

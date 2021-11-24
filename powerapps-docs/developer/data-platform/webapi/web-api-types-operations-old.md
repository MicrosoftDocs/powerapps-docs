---
title: "Web API types and operations (Microsoft Dataverse)| Microsoft Docs"
description: "Describes how you can find information you need from the Web API service and metadata documents, including documentation of the Web API system entity types, functions, and actions"
ms.custom: ""
ms.date: 11/24/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)" 
ms.assetid: d80cfb87-d4f1-4c75-bcc8-4f54d1351e26
caps.latest.revision: 27
author: "JimDaly" # GitHub ID
ms.author: pehecke
manager: "sunilg"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API types and operations


In order to use the Web API you need to find information about what is available for you to use. The service describes itself via service and metadata documents that you can access. This topic will introduce important concepts and describe how you can find the information you need using documentation generated from the service and metadata documents as well as the documentation of the system entity types, functions, and actions.

<a name="bkmk_terminology"></a>
  
## Terminology 

The Web API is implemented using the OData v4 standard which uses a specific set of terms you need to be familiar with. *Entity Data Model (EDM)* is the abstract data model that is used to describe the data exposed by an OData service. The following table is a selected list of terms defined in [OData Version 4.0 Part 1: Protocol Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html) which you should understand.  
  
|Term|Definition|  
|----------|----------------|  
|*Entity types*|Named structured types with a key. They define the named properties and relationships of an entity. Entity types may derive by single inheritance from other entity types.|  
|*Entities*|Instances of entity types (e.g. account, opportunity).|  
|*Entity sets*|Named collections of entities (e.g. accounts is an entity set containing account entities). An entity's key uniquely identifies the entity within an entity set|  
|*Complex types*|Keyless named structured types consisting of a set of properties. Complex types are commonly used as property values in model entities, or as parameters or return values for operations.|  
|*Enumeration types* or *Enum types*|Named primitive types whose values are named constants with underlying integer values.|  
|*Functions*|Operations that do not have side effects and may support further composition, for example, with additional filter operations, functions or an action|  
|*Actions*|Operations that allow side effects, such as data modification, and cannot be further composed in order to avoid non-deterministic behavior|  
  
<a name="bkmk_servicedocs"></a>
  
## Service documents

There are two service documents you can reference to learn more about the Web API.  
  
<a name="bkmk_serviceDocument"></a>

### Service document

The following query, typed into the address field of your browser, returns the *service document*, a complete list of all the entity sets that are available for your organization. Note that *[organization URI]* represents the URL for your organization.  
  
```  
  
[Organization URI]/api/data/v9.0  
  
```  
  
 The entity sets are returned in the form of a JSON array. Each item in the array has three properties as listed in this table.  
  
|Property|Description|  
|--------------|-----------------|  
|`name`|This is the name of the entity set. This data is from the <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `EntitySetName` property for the entity.|  
|`kind`|For the web API only Entity sets are listed.|  
|`url`|This value is the same as the name property and it represents the part of the resource path to retrieve data for the entity.|  
  
 This information can be retrieved using a `GET` request and may be useful to get a list of all entity sets available using the service.  
  
<a name="bkmk_csdl"></a>

### CSDL $metadata document
 
A `GET` request to the following URL will return a rather large (more than 3.5 MB) Common Schema Definition Language (CSDL) document, or *metadata document* that describes the data and operations exposed by the service.  
  
```http  
GET [Organization URI]/api/data/v9.0/$metadata  
```  
  
This document can be used as a data source to generate classes that will provide strongly typed objects for the service. But if you are not using generated classes, you may want to review documentation generated from this information instead. The [Web API Reference](/dynamics365/customer-engagement/web-api/about) uses information primarily from this document taken from a base environment with some common additional solutions installed.  
  
You can learn more about this document in [OData Version 4.0 Part 3: Common Schema Definition Language (CSDL) Plus Errata 02](https://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part3-csdl.html).  
  
> [!TIP]
>  Before your read the rest of this topic, download the `$metadata` for your organization and take a look at how the types, functions, and actions described are included in the `$metadata` and the supporting documentation.  
>   
>  You can view or download the document using your browser by navigating to the URL.  

<a name="bkmk_metannot"></a>

### Metadata annotations

The metadata document includes several types of `Annotation` elements which provide additional information about metadata elements and the capabilities of the service.  Starting with v9.x, these annotations are not included with the default metadata document unless explicitly requested. These annotations increase the size of the metadata document and are not always necessary.  
  
 To include annotations you have two options when requesting the metadata document:  
  
-   Append  the `?annotations=true` query string parameter to the URL.  
  
-   Add  the `Prefer: odata.include-annotations="*"` header to the request.  
  
Each `Annotation` element includes a `Term` attribute that describes the type of annotation. The definitions of all the possible annotations used by OData v4 can be found in [OData Vocabularies Version 4.0](https://docs.oasis-open.org/odata/odata-vocabularies/v4.0/csprd01/odata-vocabularies-v4.0-csprd01.html). The following table provides some examples used by the Web API.  
  
|Term|Description|  
|----------|-----------------|  
|`Org.OData.Core.V1.Description`|A description of an entity type or property.|  
|`Org.OData.Core.V1.Permissions`|A list of permissions available for a property when permissions are restricted.  Typically this will appear for properties with only a single `<EnumMember>Org.OData.Core.V1.PermissionType/Read</EnumMember>` child element to indicate that the property is read-only.|  
|`Org.OData.Core.V1.Computed`|Whether the property is computed. These are also usually read-only.|  
|`OData.Community.Keys.V1.AlternateKeys`|Contains a collection of elements that describe any alternate keys defined for an entity. More information:[Alternate keys](#bkmk_alternateKeys)|  
|`Org.OData.Capabilities.V1.IndexableByKey`|Whether an entityset supports key values according to OData URL conventions.|  
|`Org.OData.Capabilities.V1.SkipSupported`|Whether an entityset supports `$skip`.|  
|`Org.OData.Capabilities.V1.SearchRestrictions`|What kinds of restrictions on `$search` expressions are applied to an entityset.|  
|`Org.OData.Capabilities.V1.CountRestrictions`|What kinds of restrictions on `/$count` path suffix and $count=true system query option.|  
|`Org.OData.Capabilities.V1.NavigationRestrictions`|What kinds of restrictions on navigating properties according to OData URL conventions.|  
|`Org.OData.Capabilities.V1.ChangeTracking`|The change tracking capabilities of this service or entity set.|  
|`Org.OData.Capabilities.V1.ConformanceLevel`|The conformance level achieved by this service.|  
|`Org.OData.Capabilities.V1.FilterFunctions`|A list of functions and operators supported in `$filter`.|  
|`Org.OData.Core.V1.DereferenceableIDs`|Whether Entity-ids are URLs that locate the identified entity.|  
|`Org.OData.Core.V1.ConventionalIDs`|Whether Entity-ids follow OData URL conventions.|  
|`Org.OData.Capabilities.V1.AsynchronousRequestsSupported`|Whether the service supports the asynchronous request preference.|  
|`Org.OData.Capabilities.V1.BatchContinueOnErrorSupported`|Whether the service supports the continue on error preference.  This setting supports `$batch` requests.|  
|`Org.OData.Capabilities.V1.CrossJoinSupported`|Whether cross joins for the entity sets in this container are supported.|  
|`Org.OData.Capabilities.V1.SupportedFormats`|The media types of supported formats, including format parameters.|  
  
<a name="bkmk_entityTypes"></a>

## Entity types

The <xref:Microsoft.Dynamics.CRM.EntityTypeIndex> lists each of the system entity types exposed through the web API which store business data. An entity type is a named structured type with a key. It defines the named properties and relationships of an entity. Entity types may derive by single inheritance from other entity types. <xref:Microsoft.Dynamics.CRM.MetadataEntityTypeIndex> lists each of the entity types used to manage system metadata. Both are entity types but the way you work with them is different. See [Use the Web API with Microsoft Dataverse metadata](use-web-api-metadata.md) for information about using model entities. Each entity type is included within an `EntityType` element in the `$metadata`. The following is the definition of the <xref:Microsoft.Dynamics.CRM.account?text=account EntityType/> from the `$metadata` with properties and navigation properties removed.  
  
```xml  
<EntityType Name="account" BaseType="mscrm.crmbaseentity">  
  <Key>  
    <PropertyRef Name="accountid" />  
  </Key>  
  <!--Properties and navigation properties removed for brevity-->  
  <Annotation Term="Org.OData.Core.V1.Description" String="Business that represents a customer or potential customer. The company that is billed in business transactions." />  
</EntityType>  
```  
  
Each `EntityType` reference page in the Web API documentation uses information from the `$metadata` to show the following information when available.  
  
|Information|Description|  
|-----------------|-----------------|  
|**Description**|A description of the entity.<br /><br /> The <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `Description` property information is included in the `EntityType` element using the `Annotation` element with the `Term` attribute value of Org.OData.Core.V1.Description.|  
|**Collection URL**|The URL to access the collection of each type.<br /><br /> The <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `EntitySetName` property information is included using the `$metadata` `EntityContainer` element. The `Name` attribute of each `EntitySet` element controls how the data is accessed via the URL.|  
|**Base Type**|This is the entity type that the entity type inherits from.<br /><br /> The `BaseType` attribute of the `EntityType` element contains the name of the entity type. This name is prefixed with the alias for the Microsoft.Dynamics.CRM namespace: mscrm. More information:[Type inheritance](web-api-types-operations.md#bkmk_typeInheritance)|  
|**Display Name**|This information is not in the `$metadata`, it’s retrieved from the <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `DisplayName` property.|  
|**Primary Key**|The property value that contains the unique identifier to refer to an instance of an entity.<br /><br /> The <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `PrimaryIdAttribute` property value is included in the `EntityType` `Key` element. Each entity can have just one primary key.<br /><br /> Alternate keys are not listed here. More information:[Alternate keys](web-api-types-operations.md#bkmk_alternateKeys)|  
|**Primary Attribute**|Many entities require that a primary attribute value be set, so this is included for convenience.<br /><br /> This information is not in the `$metadata`, it’s retrieved from the metadata <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `PrimaryNameAttribute` property.|  
|**Properties**|See [Properties](web-api-types-operations.md#bkmk_properties).|  
|**Single-valued navigation properties**|See [Single-Valued navigation properties](web-api-types-operations.md#bkmk_singleValuedNavigationProperties).|  
|**Collection-valued navigation properties**|See [Collection-valued navigation properties](web-api-types-operations.md#bkmk_collectionvaluedNavProperties).|  
|**Operations bound to the entity type**|When an operation is bound to a specific entity type, it’s listed for convenience.|  
|**Operations that use the entity type**|This list shows any operations that may use the entity type. This is derived by collecting references to all operations that refer to the current type in the parameters or as a return value.|  
|**Entity types that inherit from the entity type**|This list includes any entity types that inherit directly from the entity type. See [Type inheritance](web-api-types-operations.md#bkmk_typeInheritance) for more information.|  
  
<a name="bkmk_changeentitysetname"></a>
 
### Change the name of an entity set
 
By default, the entity set name matches the <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `LogicalCollectionName` (<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>`LogicalCollectionName`) property value. If you have a custom entity that you want to address using a different entity set name, you can update the <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `EntitySetName` (<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.`EntitySetName`) property value to use a different name.  
  
<a name="bkmk_alternateKeys"></a>

### Alternate keys

Although Dataverse allows for creating alternate keys, only the primary key will be found in the default entities.  
  
 None of the system entities have alternate keys defined. If you define alternate keys for an entity, they will be included in the `$metadata` `EntityType` element as an `Annotation` like the following:  
  
```  
<Annotation Term="OData.Community.Keys.V1.AlternateKeys">  
  <Collection>  
    <Record Type="OData.Community.Keys.V1.AlternateKey">  
      <PropertyValue Property="Key">  
        <Collection>  
          <Record Type="OData.Community.Keys.V1.PropertyRef">  
            <PropertyValue Property="Alias" String="key name" />  
            <PropertyValue Property="Name" PropertyPath="key name" />  
          </Record>  
        </Collection>  
      </PropertyValue>  
    </Record>  
  </Collection>  
</Annotation>  
```  
  
Information about alternate keys can also be retrieved from the metadata using the <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/> `Keys` collection-valued navigation property using the Web API or the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.`Keys` property using the organization service.  
  
<a name="bkmk_typeInheritance"></a>
 
### Type inheritance

Inheritance allows for sharing of common properties and categorizing entity types into groups. All entity types in the web API inherit from two of the following entity types. All business entity types inherit from the <xref:Microsoft.Dynamics.CRM.crmbaseentity?text=crmbaseentity EntityType/> and all model entities inherit from the <xref:Microsoft.Dynamics.CRM.crmmodelbaseentity?text=crmmodelbaseentity EntityType/>.  
  
|Base entity|Description|  
|-----------------|-----------------|  
|<xref:Microsoft.Dynamics.CRM.crmbaseentity?text=crmbaseentity EntityType/>|All business entities inherit from this entity. It has no properties. It only serves as an abstract base entity.|  
|<xref:Microsoft.Dynamics.CRM.activitypointer?text=activitypointer EntityType/>|All activity entities inherit from this entity. It defines the common set of properties and navigation properties for activity entities.|  
|<xref:Microsoft.Dynamics.CRM.principal?text=principal EntityType/>|The <xref:Microsoft.Dynamics.CRM.systemuser?text=systemuser EntityType/> and <xref:Microsoft.Dynamics.CRM.team?text=team EntityType/> inherit a common ownerid property from this entity.|  
|<xref:Microsoft.Dynamics.CRM.crmmodelbaseentity?text=crmmodelbaseentity EntityType/>|Only <xref:Microsoft.Dynamics.CRM.MetadataBase?text=MetadataBase EntityType/> inherits directly from this entity. It has no properties. It only serves as an abstract base entity.|  
|<xref:Microsoft.Dynamics.CRM.MetadataBase?text=MetadataBase EntityType/>)|All metadata entities inherit from this entity. It provides the `MetadataId` and `HasChanged` properties for all metadata entities.|  
|<xref:Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType/>|All model entities that represent different types of attributes inherit from this entity.|  
|<xref:Microsoft.Dynamics.CRM.EnumAttributeMetadata?text=EnumAttributeMetadata EntityType/>|Those model entities that represent attributes that include a set of options inherit from this entity.|  
|<xref:Microsoft.Dynamics.CRM.OptionSetMetadataBase?text=OptionSetMetadataBase EntityType/>|This model entity type provides a common set of properties used by the <xref:Microsoft.Dynamics.CRM.BooleanOptionSetMetadata?text=BooleanOptionSetMetadata EntityType/> and <xref:Microsoft.Dynamics.CRM.OptionSetMetadata?text=OptionSetMetadata EntityType/> model entity types that inherit from it.|  
|<xref:Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType/>|This entity type provides a common set of properties used by the <xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata?text=ManyToManyRelationshipMetadata EntityType/> and <xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType/> model entity types that inherit from it.|  
  
<a name="bkmk_properties"></a>
 
## Properties

Each entity type may have declared properties that correspond to attributes. In the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex> and <xref:Microsoft.Dynamics.CRM.MetadataEntityTypeIndex> content, properties that are inherited from a base entity type are combined within the list of declared properties for each entity type. The inheritance is called out in the description for each property.  
  
In the `$metadata` `EntityType` elements each property is included in a `Property` element with a `Name` attribute value that corresponds to the properties you will set in code. The `Type` attribute value specifies the data type of the property. Properties for business entity types generally use OData primitive types.  
  
The following is an example of the <xref:Microsoft.Dynamics.CRM.account?text=account EntityType/> `name` property defined in the `$metadata`.  
  
```  
<Property Name="name" Type="Edm.String" Unicode="false">  
  <Annotation Term="Org.OData.Core.V1.Description" String="Type the company or business name." />  
</Property>  
```  
  
The description of the property is available in an `Annotation` element with the `Term` attribute property of Org.OData.Core.V1.Description. This description is taken from the <xref:Microsoft.Dynamics.CRM.AttributeMetadata?text=AttributeMetadata EntityType/> `Description` property value. Not all properties have a description.  
  
Each property may be computed. This means that the value may be set by the system. This is specified in an `Annotation` element with the `Term` attribute value of Org.OData.Core.V1.Computed.  
  
Each property may also have limitations on whether it may be updated. This is defined in an `Annotation` element with a `Term` attribute value Org.OData.Core.V1.Permissions. The only option set for this is Org.OData.Core.V1.PermissionType/Read, which indicates that the property is read only.  
  
<a name="bkmk_primitives"></a>

### Primitive types
 
OData supports a wide range of data types but Dataverse doesn’t use all of them. The following table describes how Dataverse Organization service types are mapped to OData primitive types.  
  
|Organization Service Type|Web API Type|Description|  
|-------------------------------|------------------|-----------------|  
|BigInt|Edm.Int64|Signed 64-bit integer|  
|Boolean|Edm.Boolean|Binary-valued logic|  
|CalendarRules|Single-valued navigation properties|Specific single-valued navigation properties to the <xref:Microsoft.Dynamics.CRM.calendarrule?text=calendarrule EntityType/>.|  
|Customer|Single-valued navigation properties|The customer of an entity with this type of property may be a single-valued navigation property set to either an account or contact entity type using the respective single-valued navigation properties. When either of the respective single-valued collection properties is set, the other is cleared.|  
|DateTime|Edm.DateTimeOffset|Date and time with a time-zone offset, no leap seconds <br />There is no DateTime type in OData.|  
|Decimal|Edm.Decimal|Numeric values with fixed precision and scale|  
|Double|Edm.Double|IEEE 754 binary64 floating-point number (15-17 decimal digits)|  
|EntityName|Edm.String|Sequence of UTF-8 characters|  
|Image|Edm.Binary|Binary data|  
|Integer|Edm.Int32|Signed 32-bit integer|  
|Lookup|Single-valued navigation property|A reference to a specific entity|  
|ManagedProperty|Not applicable|For internal use only.|  
|Memo|Edm.String|Sequence of UTF-8 characters|  
|Money|Edm.Decimal|Numeric values with fixed precision and scale|  
|Owner|Single-valued navigation property|A reference to the <xref:Microsoft.Dynamics.CRM.principal?text=principal EntityType/>. Both systemuser and team entity types inherit their ownerid property from the principal entity type.|  
|Picklist|Edm.Int32|Signed 32-bit integer|  
|State|Edm.Int32|Signed 32-bit integer|  
|Status|Edm.Int32|Signed 32-bit integer|  
|String|Edm.String|Sequence of UTF-8 characters|  
|Uniqueidentifier|Edm.Guid|16-byte (128-bit) unique identifier|  

<!-- TODO:
|PartyList|Collection-valued navigation property to the `activityparty` entity type.|The activitypartyparticipationtypemask property contains a value to represent the role of the participant. See [Activity Party Types](../activityparty-entity.md#ActivityPartyTypes) for more information.|   -->

<a name="bkmk_lookupProperties"></a>
 
### Lookup properties

For most single-valued navigation properties you will find a computed, read-only property that uses the following naming convention: `_<name>_value` where the `<name>` matches the name of the single-valued navigation property. The exception to this pattern is when a lookup attribute of the entity can accept multiple types of entity references. A common example is how the `incident` entity `customerid` attribute may be set to a reference that is either a `contact` or `account` entity. In the <xref:Microsoft.Dynamics.CRM.incident?text=incident EntityType/> [Single-valued navigation properties](/dynamics365/customer-engagement/web-api/incident?view=dynamics-ce-odata-9#Single-valued_navigation_properties) you will find `customerid_account` and `customerid_contact` as separate single-valued navigation properties to reflect the customer associated with an opportunity. If you set one of these single-valued navigation properties, the other will be set to null because they are both bound to the `customerid` attribute. In the <xref:Microsoft.Dynamics.CRM.incident?text=incident EntityType/> [Properties](/dynamics365/customer-engagement/web-api/incident?view=dynamics-ce-odata-9#Properties) you’ll find a `_customerid_value` lookup property that contains the same value that is set for whichever of the single-valued navigation properties contain a value.  
  
Generally, you should avoid using lookup properties and use the corresponding single-valued navigation properties instead. These properties have been included because they may be useful for certain integration scenarios. These properties are read-only and computed because they will simply reflect the changes applied using the corresponding single-valued navigation property.  
  
When you include lookup properties in a query, you can request annotations to be included that provide additional information about the data that is set for those underlying attributes which aren’t represented by a single-valued navigation property. More information:[Retrieve data about lookup properties](query-data-web-api.md#bkmk_lookupProperty)  
  
<a name="bkmk_navprops"></a>

## Navigation properties

In OData, navigation properties allow you to access data related to the current entity. When you retrieve an entity you can choose to expand navigation properties to include the related data. There are two types of navigation properties: single-valued and collection-valued.  
  
<a name="bkmk_singleValuedNavigationProperties"></a>
 
### Single-valued navigation properties

These properties correspond to Lookup attributes that support many-to-one relationships and allow setting a reference to another entity. In the `$metadata` `EntityType` element, these are defined as a `NavigationProperty` element with at `Type` attribute set to a single type. The following is an example of the <xref:Microsoft.Dynamics.CRM.account?text=account EntityType/> `createdby` single-valued navigation property in the `$metadata`:  
  
```xml  
<NavigationProperty Name="createdby" Type="mscrm.systemuser" Nullable="false" Partner="lk_accountbase_createdby">  
 <ReferentialConstraint Property="_createdby_value" ReferencedProperty="systemuserid" />  
</NavigationProperty>  
```  
  
Every navigation property that represents a single-valued navigation property will have a corresponding collection-valued navigation property indicated by the `Partner` attribute value. Each single-valued navigation property also has a `ReferentialConstraint` element with `Property` attribute value that represents the computed read-only lookup property that can be used to retrieve corresponding GUID value of the related entity. More information:[Lookup properties](web-api-types-operations.md#bkmk_lookupProperties)  
  
<a name="bkmk_collectionvaluedNavProperties"></a>

### Collection-valued navigation properties

These properties correspond to one-to-many or many-to-many relationships. In the `$metadata` `EntityType` element, these are defined as a `NavigationProperty` element with at `Type` attribute set to a collection of a type. The following represents the <xref:Microsoft.Dynamics.CRM.account?text=account EntityType/> `Account_Tasks` collection-valued navigation property which represents a one-to-many relationship:  
  
```xml  
<NavigationProperty Name="Account_Tasks" Type="Collection(mscrm.task)" Partner="regardingobjectid_account_task" />  
```  
  
When the collection-valued navigation property represents a many-to-many relationship, the name of the navigation property and the name of the partner will be the same. The following represents the <xref:Microsoft.Dynamics.CRM.account?text=account EntityType/> `accountleads_association` collection-valued navigation property which represents a many-to-many relationship:  
  
```xml  
<NavigationProperty Name="accountleads_association" Type="Collection(mscrm.lead)" Partner="accountleads_association" />  
```  
  
The difference between one-to-many and many-to-many relationships is not important when using the Web API. The way you associate entities is the same regardless of the type of relationship. Although many-to-many relationships still use intersect entities behind the scenes, only a few special system intersect entities are included within the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex>. For example, <xref:Microsoft.Dynamics.CRM.campaignactivityitem?text=campaignactivityitem EntityType/> is technically an intersect entity, but it is included because it has more properties than an ordinary intersect entity.  
  
An ordinary intersect entity has only the four basic properties required to maintain the many-to-many relationship. When you create a custom many-to-many relationship between entities, an ordinary intersect entity will be created to support the relationship. Because you should use navigation properties to perform operations involving many-to-many relationships, ordinary intersect entities are not documented but are still available using the Web API. These intersect entity types are accessible using an entity set name that uses the following naming convention: *\<intersect entity logical name>*+’collection’. For example, you can retrieve information from the contactleads intersect entity type using `[Organization URI]/api/data/v9.0/contactleadscollection`. You should only use these ordinary intersect entities in situations where you wish to apply change tracking.  
  
<a name="bkmk_actions"></a>

## Actions

*Actions* are operations that allow side effects, such as data modification, and cannot be further composed in order to avoid non-deterministic behavior.  
  
 The <xref:Microsoft.Dynamics.CRM.ActionIndex> topic lists each of the available system actions. More information:[Use Web API actions](use-web-api-actions.md).  
  
<a name="bkmk_functions"></a>
 
## Functions

*Functions* are operations that do not have side effects and may support further composition, for example, with additional filter operations, functions or an action  
  
 There are two types of functions defined in the Web API:  
  
-   The <xref:Microsoft.Dynamics.CRM.FunctionIndex> lists each of the available system functions.  
  
-   The <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex> topic lists functions which are intended to be used as criteria in a query.  
  
 More information:[Use Web API functions](use-web-api-functions.md)  
  
<a name="bkmk_complexTypes"></a>
 
## Complex types

*Complex types* are keyless named structured types consisting of a set of properties. Complex types are commonly used as property values in model entities, or as parameters or return values for operations.  
  
<xref:Microsoft.Dynamics.CRM.ComplexTypeIndex> lists all the system complex types. The following is the <xref:Microsoft.Dynamics.CRM.WhoAmIResponse?text=WhoAmIResponse ComplexType" /> from the $metadata.  
  
```xml  
<ComplexType Name="WhoAmIResponse">  
  <Property Name="BusinessUnitId" Type="Edm.Guid" Nullable="false" />  
  <Property Name="UserId" Type="Edm.Guid" Nullable="false" />  
  <Property Name="OrganizationId" Type="Edm.Guid" Nullable="false" />  
</ComplexType>  
```  
  
<a name="bkmk_EnumTypes"></a>
 
## Enumeration types
 
*Enumeration types* or *EnumTypes* are named primitive types whose values are named constants with underlying integer values.  
  
<xref:Microsoft.Dynamics.CRM.EnumTypeIndex> lists all the system enumeration types. *Enumeration types* are named primitive types whose values are named constants with underlying integer values. The following is the <xref:Microsoft.Dynamics.CRM.AccessRights?text=AccessRights EnumType" /> from the $metadata.  
  
```  
<EnumType Name="AccessRights">  
  <Member Name="None" Value="0" />  
  <Member Name="ReadAccess" Value="1" />  
  <Member Name="WriteAccess" Value="2" />  
  <Member Name="AppendAccess" Value="4" />  
  <Member Name="AppendToAccess" Value="16" />  
  <Member Name="CreateAccess" Value="32" />  
  <Member Name="DeleteAccess" Value="65536" />  
  <Member Name="ShareAccess" Value="262144" />  
  <Member Name="AssignAccess" Value="524288" />  
</EnumType>  
```  

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Authenticate to Dataverse with the Web API](authenticate-web-api.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br/>

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
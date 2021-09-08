---
title: "Retrieve and detect changes to table definitions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The classes in the Query namespace, and the RetrieveMetadataChangesRequest and RetrieveMetadataChangesResponse classes, let you build efficient queries and capture changes to table and column definitions (metadata) as they occur over time." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/10/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Retrieve and detect changes to table definitions

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The classes in the <xref:Microsoft.Xrm.Sdk.Metadata.Query> namespace, and the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> and <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse> classes, let you build efficient queries and capture changes to table and column definitions (metadata) as they occur over time.  
  
 All code examples referenced in this document are found in [Query and detect definition (metadata) changes](samples/query-metadata-changes.md).
  
<a name="BKMK_MetadataStrategies"></a> 
  
## Strategies for using definitions

 Table and column definitions lets you create applications that adapt as the Microsoft Dataverse data model changes. Definitions are important for the following types of application:  
  
-   UI for client applications  
  
-   Integration tools that have to map Dataverse data to external systems  
  
-   Development tools  
  
 Using the classes in the <xref:Microsoft.Xrm.Sdk.Metadata.Query> namespace you can implement designs that will exist somewhere between a lightweight query and a persistent metadata cache.  
  
### Lightweight query
  
 An example of a lightweight query is when you have a custom web resource UI that provides a select control to display the current choice in a Dataverse choices (picklist) column. You do not want to hard-code these choices because you would have to update that code if the available choices are ever changed. Instead you can construct a query to just retrieve those choice values and labels from the definition.  
  
 You do not have to cache this data because you can use the <xref:Microsoft.Xrm.Sdk.Metadata.Query> classes to retrieve this data directly from the Dataverse application cache.  
  
### Persistent definition (metadata) cache
  
 When you have an application that must be able to work while disconnected from the Dataverse server, or that is sensitive to limited network bandwidth between the client and the server, such as a mobile application, you will want to implement a persistent metadata cache.  
  
 With a persistent metadata cache your application will have to query all the necessary metadata the first time it connects. Then you will save that data in the application. The next time the application connects to the server you can retrieve just the difference since your last query, which should be much less data to transmit, and then merge the changes into your metadata cache when your application is loading.  
  
 How frequently you should poll for metadata changes depends on the expected volatility of metadata for your application and how long your application will remaining running. There is no event available that you can use to detect when metadata changes occur. There is a limit to the number of days that deleted metadata changes are saved and a request for changes that occurs beyond that limit will require a full re-initialization of the metadata cache. For more information see [Deleted metadata expiration](/dynamics365/customer-engagement/developer/retrieve-detect-changes-metadata#BKMK_DeletedMetadataExpiration).  
  
 When there are no changes the query should respond quickly and there will be no data to transmit back. However, if there are changes, especially if there are deleted metadata items that have to be removed from your cache, you can expect that the request may take some additional time to finish. More information: [Performance when retrieving deleted metadata](/dynamics365/customer-engagement/developer/retrieve-detect-changes-metadata#BKMK_PerformanceRetrievingDeletedMetadata)  
  
<a name="BKMK_RetrieveJusttheMetadataYouNeed"></a>

## Retrieve only the definitions you need

 Metadata is frequently retrieved or synchronized when an application starts and can affect the time the application takes to load. This is particularly true for mobile applications retrieving metadata for the first time. Retrieving only the metadata you need is very important to create an application that performs well.  
  
 The <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression> class provides a structure consistent with the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class you use to create complex queries to retrieve table data. Unlike the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest>, <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest>,  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest>, or <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRelationshipRequest> classes, the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> contains a `Query` parameter that accepts an <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression> instance that you can use to specify specific criteria for the data to return in addition to which properties you want. You can use <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> to return the full set of metadata that you get using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest>, or just a label for a specific attribute.  
  
### Specify your filter criteria  

 The <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression>.<xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Criteria> property accepts a <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression> that contains a collection of <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionExpression> objects that allow for defining conditions for filtering entity properties based on their value. These conditions use a <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionOperator> that allows for the following operators:  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionOperator>.Equals  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionOperator>.NotEquals  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionOperator>.In  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionOperator>.NotIn  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionOperator>.GreaterThan  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataConditionOperator>.LessThan  
  
 The <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression> also includes a <xref:Microsoft.Xrm.Sdk.Query.LogicalOperator> to represent whether to apply `And` or `Or` logic when you evaluate the conditions.  
  
 Not all properties can be used as filter criteria. Only properties that represent simple data types, enumerations, <xref:Microsoft.Xrm.Sdk.BooleanManagedProperty> or <xref:Microsoft.Xrm.Sdk.Metadata.AttributeRequiredLevelManagedProperty> types can be used in a <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression>. When a <xref:Microsoft.Xrm.Sdk.BooleanManagedProperty> or <xref:Microsoft.Xrm.Sdk.Metadata.AttributeRequiredLevelManagedProperty> is specified, only the `Value` property is evaluated.  
  
 The following table lists <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata> properties that cannot be used in a <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression>:  
  
|Properties|Properties (cont'd)|Properties (cont'd)|Properties (cont'd)|  
|-|-|-|-|  
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.Attributes>|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.Description>|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.DisplayCollectionName>|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.DisplayName>|  
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ManyToManyRelationships>|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ManyToOneRelationships>|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.OneToManyRelationships>|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.Privileges>|  
  
 The following code example shows a <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression> that will return a set of non-intersect, user-owned tables not included in a list of tables to exclude:  
  
 ```csharp
   // An array of SchemaName values for non-intersect, user-owned entities that should not be returned.
     String[] excludedEntities = {
"WorkflowLog",
"Template",
"CustomerOpportunityRole",
"Import",
"UserQueryVisualization",
"UserEntityInstanceData",
"ImportLog",
"RecurrenceRule",
"QuoteClose",
"UserForm",
"SharePointDocumentLocation",
"Queue",
"DuplicateRule",
"OpportunityClose",
"Workflow",
"RecurringAppointmentMaster",
"CustomerRelationship",
"Annotation",
"SharePointSite",
"ImportData",
"ImportFile",
"OrderClose",
"Contract",
"BulkOperation",
"CampaignResponse",
"Connection",
"Report",
"CampaignActivity",
"UserEntityUISettings",
"IncidentResolution",
"GoalRollupQuery",
"MailMergeTemplate",
"Campaign",
"PostFollow",
"ImportMap",
"Goal",
"AsyncOperation",
"ProcessSession",
"UserQuery",
"ActivityPointer",
"List",
"ServiceAppointment"};

     //A filter expression to limit entities returned to non-intersect, user-owned entities not found in the list of excluded entities.
     MetadataFilterExpression EntityFilter = new MetadataFilterExpression(LogicalOperator.And);
     EntityFilter.Conditions.Add(new MetadataConditionExpression("IsIntersect", MetadataConditionOperator.Equals, false));
     EntityFilter.Conditions.Add(new MetadataConditionExpression("OwnershipType", MetadataConditionOperator.Equals, OwnershipTypes.UserOwned));
     EntityFilter.Conditions.Add(new MetadataConditionExpression("SchemaName", MetadataConditionOperator.NotIn, excludedEntities));
     MetadataConditionExpression isVisibleInMobileTrue = new MetadataConditionExpression("IsVisibleInMobile", MetadataConditionOperator.Equals, true);
     EntityFilter.Conditions.Add(isVisibleInMobileTrue);
```
  
### Specify the properties you want
  
 The <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Properties> property accepts a <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataPropertiesExpression>. You can set <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataPropertiesExpression>.<xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataPropertiesExpression.AllProperties> to `true` if you want to return all the properties or you can provide a collection of strings to the <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataPropertiesExpression>.<xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataPropertiesExpression.PropertyNames> to define which properties you want to include in the results.  
  
 The strongly typed objects returned will include all properties, but only those that you request will have data. All other properties will be null, with the following few exceptions: every item of metadata will include the <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.MetadataId> ,`LogicalName` and <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.HasChanged> values if they exist for that item. You do not have to specify them in the <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Properties> you request.  
  
 If you are not using managed code and are actually parsing the `responseXML` returned from the XMLHttpRequest you will get elements for each property but only those you request will contain data. The following XML shows the contact table metadata XML that will be returned when `IsVisibleInMobile` is the only property requested.  
  
```xml  
<a:EntityMetadata>  
 <c:MetadataId>608861bc-50a4-4c5f-a02c-21fe1943e2cf</c:MetadataId>  
 <c:HasChanged i:nil="true"/>  
 <c:ActivityTypeMask i:nil="true"/>  
 <c:Attributes i:nil="true"/>  
 <c:AutoRouteToOwnerQueue i:nil="true"/>  
 <c:CanBeInManyToMany i:nil="true"/>  
 <c:CanBePrimaryEntityInRelationship i:nil="true"/>  
 <c:CanBeRelatedEntityInRelationship i:nil="true"/>  
 <c:CanCreateAttributes i:nil="true"/>  
 <c:CanCreateCharts i:nil="true"/>  
 <c:CanCreateForms i:nil="true"/>  
 <c:CanCreateViews i:nil="true"/>  
 <c:CanModifyAdditionalSettings i:nil="true"/>  
 <c:CanTriggerWorkflow i:nil="true"/>  
 <c:Description i:nil="true"/>  
 <c:DisplayCollectionName i:nil="true"/>  
 <c:DisplayName i:nil="true"/>  
 <c:IconLargeName i:nil="true"/>  
 <c:IconMediumName i:nil="true"/>  
 <c:IconSmallName i:nil="true"/>  
 <c:IsActivity i:nil="true"/>  
 <c:IsActivityParty i:nil="true"/>  
 <c:IsAuditEnabled i:nil="true"/>  
 <c:IsAvailableOffline i:nil="true"/>  
 <c:IsChildEntity i:nil="true"/>  
 <c:IsConnectionsEnabled i:nil="true"/>  
 <c:IsCustomEntity i:nil="true"/>  
 <c:IsCustomizable i:nil="true"/>  
 <c:IsDocumentManagementEnabled i:nil="true"/>  
 <c:IsDuplicateDetectionEnabled i:nil="true"/>  
 <c:IsEnabledForCharts i:nil="true"/>  
 <c:IsImportable i:nil="true"/>  
 <c:IsIntersect i:nil="true"/>  
 <c:IsMailMergeEnabled i:nil="true"/>  
 <c:IsManaged i:nil="true"/>  
 <c:IsMappable i:nil="true"/>  
 <c:IsReadingPaneEnabled i:nil="true"/>  
 <c:IsRenameable i:nil="true"/>  
 <c:IsValidForAdvancedFind i:nil="true"/>  
 <c:IsValidForQueue i:nil="true"/>  
 <c:IsVisibleInMobile>  
  <a:CanBeChanged>false</a:CanBeChanged>  
  <a:ManagedPropertyLogicalName>canmodifymobilevisibility</a:ManagedPropertyLogicalName>  
  <a:Value>false</a:Value>  
 </c:IsVisibleInMobile>  
 <c:LogicalName>contact</c:LogicalName>  
 <c:ManyToManyRelationships i:nil="true"/>  
 <c:ManyToOneRelationships i:nil="true"/>  
 <c:ObjectTypeCode i:nil="true"/>  
 <c:OneToManyRelationships i:nil="true"/>  
 <c:OwnershipType i:nil="true"/>  
 <c:PrimaryIdAttribute i:nil="true"/>  
 <c:PrimaryNameAttribute i:nil="true"/>  
 <c:Privileges i:nil="true"/>  
 <c:RecurrenceBaseEntityLogicalName i:nil="true"/>  
 <c:ReportViewName i:nil="true"/>  
 <c:SchemaName i:nil="true"/>  
</a:EntityMetadata>  
  
```  
  
 In a future release further efficiencies may be achieved by not returning elements with null values for properties that were not requested. If you write code to parse this XML you should expect that the XML returned for the same query could be reduced to only the following XML.  
  
```xml  
<a:EntityMetadata>  
 <c:MetadataId>608861bc-50a4-4c5f-a02c-21fe1943e2cf</c:MetadataId>  
 <c:IsVisibleInMobile>  
  <a:CanBeChanged>false</a:CanBeChanged>  
  <a:ManagedPropertyLogicalName>canmodifymobilevisibility</a:ManagedPropertyLogicalName>  
  <a:Value>false</a:Value>  
 </c:IsVisibleInMobile>  
 <c:LogicalName>contact</c:LogicalName>  
</a:EntityMetadata>  
```  
  
 Definitions are returned in a hierarchical structure just as it is using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest>. To access a specific column or relationship you must create a query that returns the table they are part of. If you want to retrieve data about a specific column, you must include the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.Attributes> property in your <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression>.<xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Properties>. For the table relationships to be returned, you must include one or more of the following <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata> properties:  <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ManyToManyRelationships>,  <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ManyToOneRelationships>, or <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.OneToManyRelationships>.  
  
 The following code example will return the `Attributes` property for requested tables:  
  
```csharp
//A properties expression to limit the properties to be included with entities
MetadataPropertiesExpression EntityProperties = new MetadataPropertiesExpression()
{
 AllProperties = false
};
EntityProperties.PropertyNames.AddRange(new string[] { "Attributes" });
```

### Retrieve column definitions

 The <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression>.<xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression.AttributeQuery> property accepts an <xref:Microsoft.Xrm.Sdk.Metadata.Query.AttributeQueryExpression> that defines <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Criteria> and <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Properties> for columns to be returned for the tables that match the <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression><xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Criteria> and <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Properties>.  
  
 The following table lists <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> properties that cannot be used in a <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataFilterExpression>  
  
|Properties|Properties (cont'd)|  
|-|-|  
|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.Description>|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.DisplayName>|  
|<xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata.OptionSet>|<xref:Microsoft.Xrm.Sdk.Metadata.LookupAttributeMetadata.Targets>|  
  
 The following code example will limit columns (attributes) returned to only those that have a choice (option set) and will only return the <xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata.OptionSet> and <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.AttributeType> properties for those columns:  
  
```csharp
//A condition expression to return optionset attributes
MetadataConditionExpression[] optionsetAttributeTypes = new MetadataConditionExpression[] { 
new MetadataConditionExpression("AttributeType", MetadataConditionOperator.Equals, AttributeTypeCode.Picklist),
new MetadataConditionExpression("AttributeType", MetadataConditionOperator.Equals, AttributeTypeCode.State),
new MetadataConditionExpression("AttributeType", MetadataConditionOperator.Equals, AttributeTypeCode.Status),
new MetadataConditionExpression("AttributeType", MetadataConditionOperator.Equals, AttributeTypeCode.Boolean)
};

//A filter expression to apply the optionsetAttributeTypes condition expression
MetadataFilterExpression AttributeFilter = new MetadataFilterExpression(LogicalOperator.Or);
AttributeFilter.Conditions.AddRange(optionsetAttributeTypes);

//A Properties expression to limit the properties to be included with attributes
MetadataPropertiesExpression AttributeProperties = new MetadataPropertiesExpression() { AllProperties = false };
AttributeProperties.PropertyNames.Add("OptionSet");
AttributeProperties.PropertyNames.Add("AttributeType");
```
  
### Retrieve relationship definitions
  
 The <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression>.<xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression.RelationshipQuery> property accepts a <xref:Microsoft.Xrm.Sdk.Metadata.Query.RelationshipQueryExpression> to specify the table relationship <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Criteria> and <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Properties> you want for the tables that match the <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression><xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Criteria> and <xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Properties>.  
  
 Use the <xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase.RelationshipType> property in your criteria to specify whether you want to return many-to-many relationships or one-to-many relationships.  
  
 The following table lists relationship metadata properties that cannot be used in a MetadataFilterExpression:  
  
|Properties|  
|-|  
|<xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.AssociatedMenuConfiguration>|  
|<xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.CascadeConfiguration>|  
|<xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity1AssociatedMenuConfiguration>|  
|<xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata.Entity2AssociatedMenuConfiguration>|  
  
### Retrieve labels
  
 Finally, the <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression>.<xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression.LabelQuery> property accepts a <xref:Microsoft.Xrm.Sdk.Metadata.Query.LabelQueryExpression> that lets you specify one or more integer `LCID` values for to determine which localized labels to return. Valid locale ID values can be found at [Locale ID (LCID) Chart](/openspecs/office_standards/ms-oe376/6c085406-a698-4e12-9d4d-c3b0ee3dbc4a). If an organization has many language packs installed the labels for all languages will be returned unless you specify a <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression.LabelQuery>.  
  
 The following example defines a <xref:Microsoft.Xrm.Sdk.Metadata.Query.LabelQueryExpression> that will limit labels to only those representing the users preferred language.  
  
```csharp

private Guid _userId;
private int _languageCode;
```

```csharp

_userId = ((WhoAmIResponse)_service.Execute(new WhoAmIRequest())).UserId;
_languageCode = RetrieveUserUILanguageCode(_userId);
```

```csharp

protected int RetrieveUserUILanguageCode(Guid userId)
{
 QueryExpression userSettingsQuery = new QueryExpression("usersettings");
 userSettingsQuery.ColumnSet.AddColumns("uilanguageid", "systemuserid");
 userSettingsQuery.Criteria.AddCondition("systemuserid", ConditionOperator.Equal, userId);
 EntityCollection userSettings = _service.RetrieveMultiple(userSettingsQuery);
 if (userSettings.Entities.Count > 0)
 {
  return (int)userSettings.Entities[0]["uilanguageid"];
 }
 return 0;
}
```

```csharp

//A label query expression to limit the labels returned to only those for the user's preferred language
LabelQueryExpression labelQuery = new LabelQueryExpression();
labelQuery.FilterLanguages.Add(_languageCode);
```
  
<a name="BKMK_RetrievingNeworChangedMetadata"></a> 
  
## Retrieve new or changed definitions

 The <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse> class returns a strongly typed <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadataCollection> that contains the requested data. The <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse> class also provides a <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse.ServerVersionStamp> value that you can pass to the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp> property in later requests. When a value is included for the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp> property, only data that matches the <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression> and has changed since the `ClientVersionStamp` was retrieved will be returned. The only exception to this is when your <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression>.<xref:Microsoft.Xrm.Sdk.Metadata.Query.MetadataQueryExpression.Properties> includes <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.Privileges>. Privileges will always be returned regardless of the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp>. This way your application can determine whether any important changes have occurred that you care about since you last queried the metadata. You can then merge any new or changed metadata into your persistent metadata cache so that your application will be able to avoid the performance issues with downloading metadata you may not need.  
  
 The <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.HasChanged> property provides a way to detect which child elements in a metadata item have changed. Because all the metadata is returned as part of the containing metadata item, when the label of a <xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata> has changed, the containing <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>, <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>, and <xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata> properties are returned. However, the <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.HasChanged> property will be false for those containing metadata items. Only the <xref:Microsoft.Xrm.Sdk.Metadata.OptionMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.HasChanged> property will be true.  
  
 The following example makes an initial request by defining an <xref:Microsoft.Xrm.Sdk.Metadata.Query.EntityQueryExpression> and executing a request with a <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp> set to null.  
  
```csharp
//An entity query expression to combine the filter expressions and property expressions for the query.
EntityQueryExpression entityQueryExpression = new EntityQueryExpression()
{

 Criteria = EntityFilter,
 Properties = EntityProperties,
 AttributeQuery = new AttributeQueryExpression()
 {
  Criteria = AttributeFilter,
  Properties = AttributeProperties
 },
 LabelQuery = labelQuery

};

//Retrieve the metadata for the query without a ClientVersionStamp
RetrieveMetadataChangesResponse initialRequest = getMetadataChanges(entityQueryExpression, null, DeletedMetadataFilters.OptionSet);

```

```csharp
protected RetrieveMetadataChangesResponse getMetadataChanges(
 EntityQueryExpression entityQueryExpression,
 String clientVersionStamp,
 DeletedMetadataFilters deletedMetadataFilter)
{
 RetrieveMetadataChangesRequest retrieveMetadataChangesRequest = new RetrieveMetadataChangesRequest()
 {
  Query = entityQueryExpression,
  ClientVersionStamp = clientVersionStamp,
  DeletedMetadataFilters = deletedMetadataFilter
 };

 return (RetrieveMetadataChangesResponse)_service.Execute(retrieveMetadataChangesRequest);

}
```

<a name="BKMK_RetrieveInformationaboutDeletedMetadata"></a>

## Retrieve information about deleted definitions

 The <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse.DeletedMetadata> property will return a <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataCollection> when the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp> and <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.DeletedMetadataFilters> properties are set on the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest>. The <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataCollection> contains the <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.MetadataId> values of any <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>,  <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> or <xref:Microsoft.Xrm.Sdk.Metadata.RelationshipMetadataBase> objects that have been deleted from the system in a time limit. For more information, see [Deleted metadata expiration](/dynamics365/customer-engagement/developer/retrieve-detect-changes-metadata#BKMK_DeletedMetadataExpiration).  
  
 Use the <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters> enumeration with the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.DeletedMetadataFilters> to limit the information to only those types of metadata you are interested in. The <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters> enumeration provides the following options:  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters>.Entity (Default)  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters>.Attribute  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters>.Relationship  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters>.Label  
  
-   <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters>.OptionSet  
  
 You will also use <xref:Microsoft.Xrm.Sdk.Metadata.Query.DeletedMetadataFilters> enumeration as a key to the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse.DeletedMetadata> to filter the `GUID` values found in the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesResponse.DeletedMetadata> property.  
  
 When you design a metadata cache you will want to use the <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.MetadataId> for each item so that you can identify deleted metadata items and remove them.  
  
<a name="BKMK_DeletedMetadataExpiration"></a>

### Deleted definition expiration

 Any metadata items that are deleted are tracked for a limited period of time specified by the `Organization.ExpireSubscriptionsInDays` value. By default this value is 90 days. If the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest>.<xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp> value indicates that the last metadata query was from before the expiration date, the service will throw an `ExpiredVersionStamp` error (0x80044352), When you are retrieving data to refresh and existing metadata cache you should always try to catch this error and be prepared to re-initialize your metadata cache with the results from a second request passed without a <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp>. The `ExpiredVersionStamp` error is also thrown when changes on the server, such as changes to the `ExpireSubscriptionsInDays` value, affect accurately tracking the deleted metadata.  
  
 The following example passes a <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp> and catches the `ExpiredVersionStamp`. If the error is caught the cache is reinitialized by passing in a new request with the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest.ClientVersionStamp> set to `null`.  
  
```csharp

protected String updateOptionLabelList(EntityQueryExpression entityQueryExpression, String clientVersionStamp)
{
 //Retrieve metadata changes and add them to the cache
 RetrieveMetadataChangesResponse updateResponse;
 try
 {
  updateResponse = getMetadataChanges(entityQueryExpression, clientVersionStamp, DeletedMetadataFilters.OptionSet);
  addOptionLabelsToCache(updateResponse.EntityMetadata, true);
  removeOptionLabelsFromCache(updateResponse.DeletedMetadata, true);

 }
 catch (FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault> ex)
 {
  // Check for ErrorCodes.ExpiredVersionStamp (0x80044352)
  // Will occur when the timestamp exceeds the Organization.ExpireSubscriptionsInDays value, which is 90 by default.
  if (ex.Detail.ErrorCode == unchecked((int)0x80044352))
  {
   //reinitialize cache
   _optionLabelList.Clear();

   updateResponse = getMetadataChanges(entityQueryExpression, null, DeletedMetadataFilters.OptionSet);
   //Add them to the cache and display the changes
   addOptionLabelsToCache(updateResponse.EntityMetadata, true);

  }
  else
  {
   throw ex;
  }

 }
 return updateResponse.ServerVersionStamp;
}
```

  
<a name="BKMK_PerformanceRetrievingDeletedMetadata"></a>

### Performance when retrieving deleted definitions

 When a metadata item is deleted it is saved in the database and not in the Dataverse metadata cache. Although the deleted metadata is limited to just the <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.MetadataId> and the type of metadata item, accessing the database is an operation that will require more server resources than just querying for changes.  
  
### See also

 [Extend Dynamics 365 Customer Engagement (on-premises)](/dynamics365/customer-engagement/developer/extend-dynamics-365-server)   
 [Offline use of the Dynamics 365 services](/dynamics365/customer-engagement/developer/org-service/offline-use-services)   
 [Query and detect definition (metadata) changes](samples/query-metadata-changes.md)   
 [Use the Organization service with metadata](/dynamics365/customer-engagement/developer/org-service/use-organization-service-metadata)   
 [Customize entity metadata](/dynamics365/customer-engagement/developer/customize-entity-metadata)   
 [Customize entity attribute metadata](/dynamics365/customer-engagement/developer/customize-entity-attribute-metadata)   
 [Customize entity relationship metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
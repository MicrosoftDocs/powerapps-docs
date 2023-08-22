---
title: "Choices columns (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about choices columns that allow storing multiple choices in a single column." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 01/09/2023
ms.reviewer: jdaly
ms.topic: article
author: NHelgren # GitHub ID
ms.subservice: dataverse-developer
ms.author: nhelgren # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Choices columns

Customizers can define a column that allows selection of multiple options. The <xref:Microsoft.Xrm.Sdk.Metadata.MultiSelectPicklistAttributeMetadata> class defines a column type that inherits from the <xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata> class. Just like the <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> class, this column includes an <xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata.Options?text=OptionSetMetadata.Options> property that contains the valid options for the column. The difference is that the values you get or set are an <xref:Microsoft.Xrm.Sdk.OptionSetValueCollection> type that contains an array of integers representing the selected options. Formatted values for this column are a semi-colon separated string containing the labels of the selected options.

> [!NOTE]
> Only the publisher of a managed solution can import changes that delete an option from a global option set. This includes Microsoft published solutions such as the out of box global option sets. In order to make a change to the option sets, an Upgrade must be made to the solution that added the option set. More information: [Upgrade or update a solution](../../maker/data-platform/update-solutions.md). Users can manually delete an option in their environment if they are unable to modify the solution or contact the solution publisher, but this must be done on every environment manually.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

With the Web API, this column is defined using the <xref:Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata?text=MultiSelectPicklistAttributeMetadata EntityType>.

Just like choices columns, there's technically no upper limit on the number of options that can be defined. Usability considerations should be applied as the limiting factor. However only 150 options can be selected for a single column. Also, a default value can't be set.

## Setting choices values

The following examples show how to set choices values for a column named `sample_outdooractivities` added to the `contact` table.

### [Web API](#tab/webapi)

With the Web API, you set the values by passing a string containing comma separated number values:

**Request:**

```http
POST [organization uri]/api/data/v9.0/contacts HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
    "@odata.type": "Microsoft.Dynamics.CRM.contact",
    "firstname": "Wayne",
    "lastname": "Yarborough",
    "sample_outdooractivities": "1, 9"
}
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [organization uri]/api/data/v9.0/contacts(0c67748a-b78d-e711-811c-000d3a75bdf1)
```

### [SDK for .NET](#tab/sdk)

With the SDK for .NET, use the <xref:Microsoft.Xrm.Sdk.OptionSetValueCollection> to set values for this column:

```csharp

string conn = $@"
    Url = {url};
    AuthType = OAuth;
    UserName = {userName};
    Password = {password};
    AppId = 51f81489-12ee-4a9e-aaae-a2591f45987d;
    RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97;
    LoginPrompt=Auto;
    RequireNewInstance = True";

var service = new CrmServiceClient(conn);
// var service = new ServiceClient(conn);

OptionSetValueCollection activities = new OptionSetValueCollection();
activities.Add(new OptionSetValue(1)); //Swimming
activities.Add(new OptionSetValue(9)); //Camping

Contact contact = new Contact();
contact["firstname"] = "Wayne";
contact["lastname"] = "Yarborough";
contact["sample_outdooractivities"] = activities;

service.Create(contact);
```

---

## Query data from choices

Two new condition operators have been added to support querying values in choices:

|Web API|FetchXml|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>|
|---------|---------|---------|
|<xref:Microsoft.Dynamics.CRM.ContainValues>|`contain-values`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.ContainValues>|
|<xref:Microsoft.Dynamics.CRM.DoesNotContainValues>|`not-contain-values`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.DoesNotContainValues>|

> [!NOTE]
> These operators depend on full-text indexing to be applied on the database tables that store the multiple values. There is some latentcy after new records are created and the full-text index takes effect. You may need to wait several seconds after new records are created before filters using these operators can evaluate the values.

Other existing condition operators that can be used with this type of column include the following:

|Web API|FetchXml|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>|
|---------|---------|---------|
|`eq`|`eq`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.Equal>|
|`ne`|`neq`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.NotEqual>|
|`not null`|`not-null`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.NotNull>|
|`eq null`|`null`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.Null>|
|<xref:Microsoft.Dynamics.CRM.In>|`in`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.In>|
|<xref:Microsoft.Dynamics.CRM.NotIn>|`not-in`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.NotIn>|


The following examples show using the `ContainValues` and `DoesNotContainValues` operators against the following data set on choices column named `sample_outdooractivities` on the `contact` table.

### Choices `sample_outdooractivities` values

|Value|Label|
|-----|-----|
|1|Swimming|
|2|Hiking|
|3|Mountain Climbing|
|4|Fishing|
|5|Hunting|
|6|Running|
|7|Boating|
|8|Skiing|
|9|Camping|

### Contact table values

|`fullname`| 'sample_outdooractivities'|
|--------|-------------------|
|Wayne Yarborough|1,9|
|Monte Orton|2|
|Randal Maple|4|
|Hiram Mundy|2,3,8,9|
|Barbara Weber|1,4,7|
|Georgette Sullivan|4,5,9|
|Verna Kennedy|2,4,9|
|Marvin Bracken|1,2,8,9|


#### [Web API](#tab/webapi)

This example shows the use of the <xref:Microsoft.Dynamics.CRM.ContainValues> query function to return all the contacts who like hiking. Notice how the text of the options is returned as annotations due to the `odata.include-annotations="OData.Community.Display.V1.FormattedValue"` preference applied.


**Request:**

```http
GET [organization uri]/api/data/v9.0/contacts?$select=fullname,sample_outdooractivities&$filter=Microsoft.Dynamics.CRM.ContainValues(PropertyName='sample_outdooractivities',PropertyValues=%5B'2'%5D) HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
Content-Length: 1092

{
    "@odata.context": "[organization uri]/api/data/v9.0/$metadata#contacts(fullname,sample_outdooractivities)",
    "value": [{
        "@odata.etag": "W/\"529811\"",
        "fullname": "Monte Orton",
        "sample_outdooractivities@OData.Community.Display.V1.FormattedValue": "Hiking",
        "sample_outdooractivities": "2",
        "contactid": "cdbcc48e-0b8d-e711-811c-000d3a75bdf1"
    }, {
        "@odata.etag": "W/\"529823\"",
        "fullname": "Hiram Mundy",
        "sample_outdooractivities@OData.Community.Display.V1.FormattedValue": "Hiking; Mountain Climbing; Skiing; Camping",
        "sample_outdooractivities": "2,3,8,9",
        "contactid": "d7bcc48e-0b8d-e711-811c-000d3a75bdf1"
    }, {
        "@odata.etag": "W/\"529838\"",
        "fullname": "Verna Kennedy",
        "sample_outdooractivities@OData.Community.Display.V1.FormattedValue": "Hiking; Fishing; Camping",
        "sample_outdooractivities": "2,4,9",
        "contactid": "e6bcc48e-0b8d-e711-811c-000d3a75bdf1"
    }, {
        "@odata.etag": "W/\"529843\"",
        "fullname": "Marvin Bracken",
        "sample_outdooractivities@OData.Community.Display.V1.FormattedValue": "Swimming; Hiking; Skiing; Camping",
        "sample_outdooractivities": "1,2,8,9",
        "contactid": "ebbcc48e-0b8d-e711-811c-000d3a75bdf1"
    }]
}
```

#### [SDK for .NET](#tab/sdk)

```csharp
//Retrieve contacts who like hiking
//Using Query Expression
int[] hikingValue = new int[] { 2 };
ConditionExpression condition = 
    new ConditionExpression(
    "sample_outdooractivities", 
    ConditionOperator.ContainValues, 
    hikingValue);

FilterExpression filter = new FilterExpression();
filter.AddCondition(condition);

QueryExpression likesHikingQuery = 
    new QueryExpression("contact");
likesHikingQuery.ColumnSet.AddColumns("fullname", "sample_outdooractivities");
likesHikingQuery.Criteria.AddFilter(filter);

EntityCollection hikers = service.RetrieveMultiple(likesHikingQuery);

Console.WriteLine("\nContacts who like Hiking");
Console.WriteLine("=========================");
foreach (Contact contact in hikers.Entities)
{
    string values = (contact["sample_outdooractivities"] == null) ? 
        "null" : 
        contact.FormattedValues["sample_outdooractivities"];
    Console.WriteLine("{0} {1}", contact.FullName, values);
}

    /*OUTPUT:
    Contacts who like Hiking
    =========================
    Monte Orton Hiking
    Hiram Mundy Hiking; Mountain Climbing; Skiing; Camping
    Verna Kennedy Hiking; Fishing; Camping
    Marvin Bracken Swimming; Hiking; Skiing; Camping
    */
```

---

### Example code using FetchXml

The following code shows the use of FetchXml with Web API and SDK for .NET.

#### [Web API](#tab/webapi)
This example shows the use of the `not-contain-values` operator in the following `FetchXml` query using the Web API.

```xml
<fetch distinct='false' no-lock='false' mapping='logical'>
    <entity name='contact'>
        <attribute name='fullname' />
        <attribute name='sample_outdooractivities' />
            <filter type='and'>
                <condition attribute='sample_outdooractivities' operator='not-contain-values'>
                    <value>2</value>
                </condition>
            </filter>
    </entity>
</fetch>
```

**Request:**

```http
GET [organization uri]/api/data/v9.0/contacts?fetchXml=%253Cfetch%2520distinct%253D'false'%2520no-lock%253D'false'%2520mapping%253D'logical'%253E%253Centity%2520name%253D'contact'%253E%253Cattribute%2520name%253D'fullname'%2520%252F%253E%253Cattribute%2520name%253D'sample_outdooractivities'%2520%252F%253E%253Cfilter%2520type%253D'and'%253E%253Ccondition%2520attribute%253D'sample_outdooractivities'%2520operator%253D'not-contain-values'%253E%253Cvalue%253E2%253C%252Fvalue%253E%253C%252Fcondition%253E%253C%252Ffilter%253E%253C%252Fentity%253E%253C%252Ffetch%253E HTTP/1.1
Accept: application/json
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
    "@odata.context": "[organization uri]/api/data/v9.0/$metadata#contacts(fullname,sample_outdooractivities,contactid)",
    "value": [{
        "@odata.etag": "W/\"529806\"",
        "fullname": "Wayne Yarborough",
        "sample_outdooractivities@OData.Community.Display.V1.FormattedValue": "Swimming; Camping",
        "sample_outdooractivities": "1,9",
        "contactid": "c8bcc48e-0b8d-e711-811c-000d3a75bdf1"
    }, {
        "@odata.etag": "W/\"529816\"",
        "fullname": "Randal Maple",
        "sample_outdooractivities@OData.Community.Display.V1.FormattedValue": "Fishing",
        "sample_outdooractivities": "4",
        "contactid": "d2bcc48e-0b8d-e711-811c-000d3a75bdf1"
    }, {
        "@odata.etag": "W/\"529828\"",
        "fullname": "Barbara Weber",
        "sample_outdooractivities@OData.Community.Display.V1.FormattedValue": "Swimming; Fishing; Boating",
        "sample_outdooractivities": "1,4,7",
        "contactid": "dcbcc48e-0b8d-e711-811c-000d3a75bdf1"
    }, {
        "@odata.etag": "W/\"529833\"",
        "fullname": "Georgette Sullivan",
        "sample_outdooractivities@OData.Community.Display.V1.FormattedValue": "Fishing; Hunting; Camping",
        "sample_outdooractivities": "4,5,9",
        "contactid": "e1bcc48e-0b8d-e711-811c-000d3a75bdf1"
    }]
}
```

#### [SDK for .NET](#tab/sdk)

This sample shows the use of the `not-contain-values` using <xref:Microsoft.Dynamics.CRM.FetchExpression> using <xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A?text=IOrganizationService.RetrieveMultiple>.

```csharp
//Retrieving contacts who do not like hiking:
//Using Fetch Expression
string fetchXml = @"<fetch distinct='false' no-lock='false' mapping='logical'>
                     <entity name='contact'>
                      <attribute name='fullname' />
                      <attribute name='sample_outdooractivities' />
                       <filter type='and'>
                        <condition attribute='sample_outdooractivities' operator='not-contain-values'>
                         <value>2</value>
                        </condition>
                       </filter>
                      </entity>
                     </fetch>";
FetchExpression doesNotLikeHiking = new FetchExpression(fetchXml);

EntityCollection nonHikers = service.RetrieveMultiple(doesNotLikeHiking);

Console.WriteLine("\nContacts who do not like Hiking");
Console.WriteLine("===============================");
foreach (Contact contact in nonHikers.Entities)
{
    string values = (contact["sample_outdooractivities"] == null) ? "null" : contact.FormattedValues["sample_outdooractivities"];
    Console.WriteLine("{0} {1}", contact.FullName, values);
}

    /* OUTPUT
    Contacts who do not like Hiking
    ===============================
    Wayne Yarborough Swimming; Camping
    Randal Maple Fishing
    Barbara Weber Swimming; Fishing; Boating
    Georgette Sullivan Fishing; Hunting; Camping 
    */
```

---

## Create choices with code

The easiest way to create choices is to use the column editor in the customization tools. More information: [How to create and edit columns](../../maker/data-platform/create-edit-fields.md)

But if you need to automate creation of this kind of column you can use C# code like the following with the SDK for .NET that creates choices to allow choices of outdoor activities to the `contact` table. More information: [Create columns](org-service/metadata-attributemetadata.md#create-columns)

```csharp
private const int _languageCode = 1033; //English

MultiSelectPicklistAttributeMetadata outDoorActivitiesAttribute = new MultiSelectPicklistAttributeMetadata()
{
SchemaName = "sample_OutdoorActivities",
LogicalName = "sample_outdooractivities",
DisplayName = new Label("Outdoor activities", _languageCode),
RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
Description = new Label("Outdoor activities that the contact likes.", _languageCode),
OptionSet = new OptionSetMetadata()
    {
        IsGlobal = false,
        OptionSetType = OptionSetType.Picklist,
        Options = {
            new OptionMetadata(new Label("Swimming",_languageCode),1),
            new OptionMetadata(new Label("Hiking",_languageCode),2),
            new OptionMetadata(new Label("Mountain Climbing",_languageCode),3),
            new OptionMetadata(new Label("Fishing",_languageCode),4),
            new OptionMetadata(new Label("Hunting",_languageCode),5),
            new OptionMetadata(new Label("Running",_languageCode),6),
            new OptionMetadata(new Label("Boating",_languageCode),7),
            new OptionMetadata(new Label("Skiing",_languageCode),8),
            new OptionMetadata(new Label("Camping",_languageCode),9)}
    }
};

CreateAttributeRequest createAttributeRequest = new CreateAttributeRequest
{
    EntityName = "contact",
    Attribute = outDoorActivitiesAttribute
};

var response = (CreateAttributeResponse)service.Execute(createAttributeRequest);

```

### See also

[Column definitions](entity-attribute-metadata.md)<br />
[Create a table row using the Web API](webapi/create-entity-web-api.md)<br />
[Query Data using the Web API](webapi/query-data-web-api.md)<br />
[Work with column definitions](org-service/metadata-attributemetadata.md)<br />
[Sample: Work with columns definitions](org-service/samples/work-with-attributes.md)<br />
[Late-bound and early-bound programming using the Organization Service](org-service/early-bound-programming.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

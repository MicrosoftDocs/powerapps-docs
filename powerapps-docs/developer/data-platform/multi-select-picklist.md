---
title: Use Choices Columns to Store Multiple Selected Options
description: "Learn how to define, set, and query choices columns that store multiple selected options in a single column using the Web API or SDK for .NET. Get started now."
ms.date: 10/29/2026
ms.reviewer: jdaly
ms.topic: article
ai-usage: ai-assisted
author: MsSQLGirl
ms.author: jukoesma
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Use choices columns to store multiple options

Customizers can define a choices column that allows selection of multiple options. This article explains how to set, query, and create choices columns by using the Web API and the SDK for .NET. The <xref:Microsoft.Xrm.Sdk.Metadata.MultiSelectPicklistAttributeMetadata> class defines a column type that inherits from the <xref:Microsoft.Xrm.Sdk.Metadata.EnumAttributeMetadata> class. Just like the <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> class, this column includes an [OptionSetMetadata.Options](xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadata.Options) property that contains the valid options for the column. The difference is that the values you get or set are an <xref:Microsoft.Xrm.Sdk.OptionSetValueCollection> type that contains an array of integers representing the selected options. Formatted values for this column are a semicolon-separated string containing the labels of the selected options.

With the Web API, you define this column by using the [MultiSelectPicklistAttributeMetadata entity type](xref:Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata).

Just like choices columns, there's technically no upper limit on the number of options that you can define. Apply usability considerations as the limiting factor. However, you can select only 150 options for a single column. Also, you can't set a default value.

## Set choices column values

The following examples show how to set choices values for a column named `sample_outdooractivities` that you add to the `contact` table.

### [Web API](#tab/webapi)

By using the Web API, set the values by passing a string containing comma-separated number values:

**Request:**

```http
POST [organization uri]/api/data/v9.2/contacts HTTP/1.1
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
OData-EntityId: [organization uri]/api/data/v9.2/contacts(00aa00aa-bb11-cc22-dd33-44ee44ee44ee)
```

### [SDK for .NET](#tab/sdk)

By using the SDK for .NET, use the <xref:Microsoft.Xrm.Sdk.OptionSetValueCollection> to set values for this column:

```csharp
public static Guid CreateContactWithChoicesColumnSetExample(IOrganizationService service) {

   OptionSetValueCollection activities = new OptionSetValueCollection();
   activities.Add(new OptionSetValue(1)); //Swimming
   activities.Add(new OptionSetValue(9)); //Camping

   Entity contact = new Entity("contact");
   contact["firstname"] = "Wayne";
   contact["lastname"] = "Yarborough";
   contact["sample_outdooractivities"] = activities;

   return service.Create(contact);

}
```

---

## Query data from choices columns

Two condition operators support querying values in choices:

|Web API|FetchXml|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator>|
|---------|---------|---------|
|<xref:Microsoft.Dynamics.CRM.ContainValues>|`contain-values`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.ContainValues>|
|<xref:Microsoft.Dynamics.CRM.DoesNotContainValues>|`not-contain-values`|<xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.DoesNotContainValues>|

> [!NOTE]
> These operators depend on full-text indexing to be applied on the database tables that store the multiple values. There's some latency after new records are created and the full-text index takes effect. You might need to wait several seconds after new records are created before filters using these operators can evaluate the values.

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

See [Create choices columns with code](#create-choices-columns-with-code) for sample code to create this column.

### Contact table values

|`fullname`| `sample_outdooractivities`|
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

This example shows how to use the <xref:Microsoft.Dynamics.CRM.ContainValues> query function to return all the contacts who like hiking. The response includes the text of the options as annotations because of the `odata.include-annotations="OData.Community.Display.V1.FormattedValue"` preference applied.


**Request:**

```http
GET [organization uri]/api/data/v9.2/contacts?$select=fullname,sample_outdooractivities&$filter=Microsoft.Dynamics.CRM.ContainValues(PropertyName='sample_outdooractivities',PropertyValues=%5B'2'%5D) HTTP/1.1
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
    "@odata.context": "[organization uri]/api/data/v9.2/$metadata#contacts(fullname,sample_outdooractivities)",
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

### [SDK for .NET](#tab/sdk)

This example shows how to use the <xref:Microsoft.Xrm.Sdk.Query.ConditionOperator.ContainValues> member to return all the contacts who like hiking. The response includes the text of the options as formatted value.

```csharp
public static void WriteContactsWhoLikeHikingExample(IOrganizationService service)
{
    ArgumentNullException.ThrowIfNull(service);

    var likesHikingQuery = new QueryExpression("contact")
    {
        ColumnSet = new ColumnSet("fullname", "sample_outdooractivities"),
        Criteria = new FilterExpression
        {
            Conditions =
            {
                new ConditionExpression(
                    "sample_outdooractivities",
                    ConditionOperator.ContainValues,
                    new int[] { 2 })
            }
        }
    };

    var hikers = service.RetrieveMultiple(likesHikingQuery);

    Console.WriteLine("\nContacts who like Hiking");
    Console.WriteLine("=========================");
    foreach (var contact in hikers.Entities)
    {
        var fullname = contact.GetAttributeValue<string>("fullname") ?? "(no name)";
        var values = contact.FormattedValues.TryGetValue("sample_outdooractivities", out var formattedValue)
            ? formattedValue
            : "null";

        Console.WriteLine($"{fullname} {values}");
    }
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

This example shows the use of the `not-contain-values` operator in the following `FetchXml` query by using the Web API.

```xml
<fetch>
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
GET [organization uri]/api/data/v9.2/contacts?fetchXml=%253Cfetch%2520distinct%253D'false'%2520no-lock%253D'false'%2520mapping%253D'logical'%253E%253Centity%2520name%253D'contact'%253E%253Cattribute%2520name%253D'fullname'%2520%252F%253E%253Cattribute%2520name%253D'sample_outdooractivities'%2520%252F%253E%253Cfilter%2520type%253D'and'%253E%253Ccondition%2520attribute%253D'sample_outdooractivities'%2520operator%253D'not-contain-values'%253E%253Cvalue%253E2%253C%252Fvalue%253E%253C%252Fcondition%253E%253C%252Ffilter%253E%253C%252Fentity%253E%253C%252Ffetch%253E HTTP/1.1
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
    "@odata.context": "[organization uri]/api/data/v9.2/$metadata#contacts(fullname,sample_outdooractivities,contactid)",
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

This sample shows the use of the `not-contain-values` operator by using <xref:Microsoft.Dynamics.CRM.FetchExpression> with [IOrganizationService.RetrieveMultiple](xref:Microsoft.Xrm.Sdk.IOrganizationService.RetrieveMultiple%2A).

```csharp
public static void RetrieveContactsWhoDoNotLikeHikingExample(IOrganizationService service)
{
    ArgumentNullException.ThrowIfNull(service);

    var fetchXml = """
        <fetch>
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
        """;

    var doesNotLikeHiking = new FetchExpression(fetchXml);
    var nonHikers = service.RetrieveMultiple(doesNotLikeHiking);

    Console.WriteLine("\nContacts who do not like Hiking");
    Console.WriteLine("===============================");
    foreach (var contact in nonHikers.Entities)
    {
        var fullname = contact.GetAttributeValue<string>("fullname") ?? "(no name)";
        var values = contact.FormattedValues.TryGetValue("sample_outdooractivities", out var formattedValue)
            ? formattedValue
            : "null";

        Console.WriteLine($"{fullname} {values}");
    }
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

## Create choices columns with code

The easiest way to create choices is to use the column editor in the customization tools. [Learn how to create and edit columns](../../maker/data-platform/create-edit-fields.md).

If you need to automate creation of this kind of column, use the following examples with the Web API or SDK for .NET. Both examples create a choices column for outdoor activities in the `contact` table. [Learn more about creating columns](org-service/metadata-attributemetadata.md#create-columns).

### [Web API](#tab/webapi)

Sends a `POST` request with [MultiSelectPicklistAttributeMetadata entity type](xref:Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata) payload  to the `/Attributes` collection of the `contact` table to create a column as part of a solution with the unique name `mySampleSolutionUniqueName`. [Learn to associate a solution component with a solution](optional-parameters.md#associate-a-solution-component-with-a-solution)

**Request:**

```http
POST [organization uri]/api/data/v9.2/EntityDefinitions(LogicalName='contact')/Attributes HTTP/1.1
Accept: application/json
MSCRM.SolutionUniqueName: mySampleSolutionUniqueName
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0

{
    "@odata.type": "Microsoft.Dynamics.CRM.MultiSelectPicklistAttributeMetadata",
    "SchemaName": "sample_OutdoorActivities",
    "DisplayName": {
        "LocalizedLabels": [
            {
                "Label": "Outdoor activities",
                "LanguageCode": 1033
            }
        ]
    },
    "RequiredLevel": {
        "Value": "None"
    },
    "Description": {
        "LocalizedLabels": [
            {
                "Label": "Outdoor activities that the contact likes.",
                "LanguageCode": 1033
            }
        ]
    },
    "OptionSet": {
        "IsGlobal": false,
        "OptionSetType": "Picklist",
        "Options": [
            {
                "Value": 1,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Swimming", "LanguageCode": 1033 }
                    ]
                }
            },
            {
                "Value": 2,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Hiking", "LanguageCode": 1033 }
                    ]
                }
            },
            {
                "Value": 3,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Mountain Climbing", "LanguageCode": 1033 }
                    ]
                }
            },
            {
                "Value": 4,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Fishing", "LanguageCode": 1033 }
                    ]
                }
            },
            {
                "Value": 5,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Hunting", "LanguageCode": 1033 }
                    ]
                }
            },
            {
                "Value": 6,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Running", "LanguageCode": 1033 }
                    ]
                }
            },
            {
                "Value": 7,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Boating", "LanguageCode": 1033 }
                    ]
                }
            },
            {
                "Value": 8,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Skiing", "LanguageCode": 1033 }
                    ]
                }
            },
            {
                "Value": 9,
                "Label": {
                    "LocalizedLabels": [
                        { "Label": "Camping", "LanguageCode": 1033 }
                    ]
                }
            }
        ]
    }
}
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [organization uri]/api/data/v9.2/EntityDefinitions(LogicalName='contact')/Attributes(00aa00aa-bb11-cc22-dd33-44ee44ee44ee)
```

### [SDK for .NET](#tab/sdk)

Uses [CreateAttributeRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest) to create a [MultiSelectPicklistAttributeMetadata](xref:Microsoft.Xrm.Sdk.Metadata.MultiSelectPicklistAttributeMetadata) column on the contact table as part of a solution with the unique name `mySampleSolutionUniqueName`. [Learn to associate a solution component with a solution](optional-parameters.md#associate-a-solution-component-with-a-solution)


```csharp
public static Guid CreateOutdoorActivitiesOptionSetExample(IOrganizationService service)
{
    ArgumentNullException.ThrowIfNull(service);

    const int languageCode = 1033; // English

    static OptionMetadata CreateOption(string label, int value, int localeId) =>
        new(new Label(label, localeId), value);

    var outdoorActivitiesAttribute = new MultiSelectPicklistAttributeMetadata
    {
        SchemaName = "sample_OutdoorActivities",
        LogicalName = "sample_outdooractivities",
        DisplayName = new Label("Outdoor activities", languageCode),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        Description = new Label("Outdoor activities that the contact likes.", languageCode),
        OptionSet = new OptionSetMetadata
        {
            IsGlobal = false,
            OptionSetType = OptionSetType.Picklist,
            Options =
            {
                CreateOption("Swimming", 1, languageCode),
                CreateOption("Hiking", 2, languageCode),
                CreateOption("Mountain Climbing", 3, languageCode),
                CreateOption("Fishing", 4, languageCode),
                CreateOption("Hunting", 5, languageCode),
                CreateOption("Running", 6, languageCode),
                CreateOption("Boating", 7, languageCode),
                CreateOption("Skiing", 8, languageCode),
                CreateOption("Camping", 9, languageCode)
            }
        }
    };

    var createAttributeRequest = new CreateAttributeRequest
    {
        EntityName = "contact",
        Attribute = outdoorActivitiesAttribute,
        SolutionUniqueName = "mySampleSolutionUniqueName"
    };

    var response = (CreateAttributeResponse)service.Execute(createAttributeRequest);
    return response.AttributeId;
}

```

---



### See also

[Column definitions](entity-attribute-metadata.md)<br />
[Create a table row using the Web API](webapi/create-table-row.md)<br />
[Query Data using the Web API](webapi/query/overview.md)<br />
[Work with column definitions](org-service/metadata-attributemetadata.md)<br />
[Sample: Work with columns definitions](org-service/samples/work-with-attributes.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

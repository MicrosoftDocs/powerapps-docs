---
title: Filter rows using OData
description: Learn how to use OData to filter rows when you retrieve data from Microsoft Dataverse Web API.
ms.date: 05/28/2025
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Filter rows using OData


Use the `$filter` [query option](overview.md#odata-query-options) to filter a collection of resources.

Dataverse evaluates each resource in the collection using the expression set for `$filter`. Only records where the expression evaluates to `true` are returned in the response. Records aren't returned if the expression evaluates to `false` or `null`, or if the user doesn't have read access to the record.

The following table describes the operators and functions you can use in `$filter` expressions.


| |Description| More information|
|---|---|---|
|**Comparison operators**|Use the `eq`,`ne`,`gt`,`ge`,`lt`, and `le` operators to compare a property and a value.|[Comparison operators](#comparison-operators)|
|**Logical operators**|Use `and`, `or`, and `not` to create more complex expressions. |[Logical operators](#logical-operators)|
|**Grouping operators**|Use parentheses: `()`, to specify the precedence to evaluate a complex expression. |[Grouping operators](#grouping-operators)|
|**OData query functions**|Evaluate string values using `contains`, `endswith`, and `startswith` functions. |[Use OData query functions](#use-odata-query-functions)|
|**Dataverse query functions**|Use more than 60 specialized functions designed for business applications. |[Dataverse query functions](#dataverse-query-functions)|
|**Lambda expressions**|Create expressions based on values of related collections. |[Filter using values of related collections](#filter-using-values-of-related-collections)|

## Comparison operators

The following table describes the operators you can use to compare a property and a value.

|Operator|Description|Example|  
|---|---|---|
|`eq`|Equal|`$filter=revenue eq 100000`|  
|`ne`|Not Equal|`$filter=revenue ne 100000`|  
|`gt`|Greater than|`$filter=revenue gt 100000`|  
|`ge`|Greater than or equal|`$filter=revenue ge 100000`|  
|`lt`|Less than|`$filter=revenue lt 100000`|  
|`le`|Less than or equal|`$filter=revenue le 100000`|  

### Column comparison

You can use comparison operators to compare property values in the same row. Only comparison operators can be used to compare values in the same row, and the column types must match. For example, the following query returns any contacts where `firstname` equals `lastname`:

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname&$filter=firstname eq lastname
```

## Logical operators

The following table describes the logical operators you can use to create more complex expressions.

|Operator|Description|Example|  
|---|---|---|
|`and`|Logical and|`$filter=revenue lt 100000 and revenue gt 2000`|  
|`or`|Logical or|`$filter=contains(name,'(sample)') or contains(name,'test')`|  
|`not`|Logical negation|`$filter=not contains(name,'sample')`|  

## Grouping operators

Use parentheses `()` with logical operators to specify the precedence to evaluate a complex expression; for example:

`$filter=(contains(name,'sample') or contains(name,'test')) and revenue gt 5000`

## Dataverse query functions

Use more than 60 specialized functions designed for business applications. These functions provide special capabilities, as described in the following table.

|Group|Functions|
|---|---|
|**Dates** |<xref:Microsoft.Dynamics.CRM.InFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.InFiscalPeriodAndYear>, <xref:Microsoft.Dynamics.CRM.InFiscalYear>, <xref:Microsoft.Dynamics.CRM.InOrAfterFiscalPeriodAndYear>, <xref:Microsoft.Dynamics.CRM.InOrBeforeFiscalPeriodAndYear>,<br /><xref:Microsoft.Dynamics.CRM.Last7Days>, <xref:Microsoft.Dynamics.CRM.LastFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.LastFiscalYear>, <xref:Microsoft.Dynamics.CRM.LastMonth>, <xref:Microsoft.Dynamics.CRM.LastWeek>, <xref:Microsoft.Dynamics.CRM.LastXDays>, <xref:Microsoft.Dynamics.CRM.LastXFiscalPeriods>, <xref:Microsoft.Dynamics.CRM.LastXFiscalYears>,<br /><xref:Microsoft.Dynamics.CRM.LastXHours>, <xref:Microsoft.Dynamics.CRM.LastXMonths>, <xref:Microsoft.Dynamics.CRM.LastXWeeks>, <xref:Microsoft.Dynamics.CRM.LastXYears>, <xref:Microsoft.Dynamics.CRM.LastYear>, <xref:Microsoft.Dynamics.CRM.Next7Days>, <xref:Microsoft.Dynamics.CRM.NextFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.NextFiscalYear>,<br /><xref:Microsoft.Dynamics.CRM.NextMonth>, <xref:Microsoft.Dynamics.CRM.NextWeek>, <xref:Microsoft.Dynamics.CRM.NextXDays>, <xref:Microsoft.Dynamics.CRM.NextXFiscalPeriods>, <xref:Microsoft.Dynamics.CRM.NextXFiscalYears>, <xref:Microsoft.Dynamics.CRM.NextXHours>, <xref:Microsoft.Dynamics.CRM.NextXMonths>,<br /><xref:Microsoft.Dynamics.CRM.NextXWeeks>, <xref:Microsoft.Dynamics.CRM.NextXYears>, <xref:Microsoft.Dynamics.CRM.NextYear>, <xref:Microsoft.Dynamics.CRM.OlderThanXDays>, <xref:Microsoft.Dynamics.CRM.OlderThanXHours>, <xref:Microsoft.Dynamics.CRM.OlderThanXMinutes>, <xref:Microsoft.Dynamics.CRM.OlderThanXMonths>,<br /><xref:Microsoft.Dynamics.CRM.OlderThanXWeeks>, <xref:Microsoft.Dynamics.CRM.OlderThanXYears>, <xref:Microsoft.Dynamics.CRM.On>, <xref:Microsoft.Dynamics.CRM.OnOrAfter>, <xref:Microsoft.Dynamics.CRM.OnOrBefore>, <xref:Microsoft.Dynamics.CRM.ThisFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.ThisFiscalYear>, <xref:Microsoft.Dynamics.CRM.ThisMonth>, <xref:Microsoft.Dynamics.CRM.ThisWeek>, <xref:Microsoft.Dynamics.CRM.ThisYear>, <xref:Microsoft.Dynamics.CRM.Today>, <xref:Microsoft.Dynamics.CRM.Tomorrow>, <xref:Microsoft.Dynamics.CRM.Yesterday>|
|**Id Values**|<xref:Microsoft.Dynamics.CRM.EqualBusinessId>, <xref:Microsoft.Dynamics.CRM.EqualUserId>, <xref:Microsoft.Dynamics.CRM.NotEqualBusinessId>, <xref:Microsoft.Dynamics.CRM.NotEqualUserId>|
|**Hierarchy**|<xref:Microsoft.Dynamics.CRM.Above>, <xref:Microsoft.Dynamics.CRM.AboveOrEqual>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserHierarchy>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserHierarchyAndTeams>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserTeams>, <br /><xref:Microsoft.Dynamics.CRM.EqualUserTeams>, <xref:Microsoft.Dynamics.CRM.NotUnder>, <xref:Microsoft.Dynamics.CRM.Under>, <xref:Microsoft.Dynamics.CRM.UnderOrEqual><br />More information: [Query hierarchical data](../../query-hierarchical-data.md)|
|**Choices columns**|<xref:Microsoft.Dynamics.CRM.ContainValues>, <xref:Microsoft.Dynamics.CRM.DoesNotContainValues><br />More information: [Query data from choices](../../multi-select-picklist.md#query-data-from-choices)|
|**Between**|<xref:Microsoft.Dynamics.CRM.Between>, <xref:Microsoft.Dynamics.CRM.NotBetween>|
|**In**|<xref:Microsoft.Dynamics.CRM.In>, <xref:Microsoft.Dynamics.CRM.NotIn>|
|**Language**|<xref:Microsoft.Dynamics.CRM.EqualUserLanguage>|

> [!NOTE]
> The [Contains function](xref:Microsoft.Dynamics.CRM.Contains) is for use with columns that have full-text indexing. Only the Dynamics 365 KBArticle (article) table has columns that have full-text indexing. Use the OData `contains` function instead.

The <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex?displayProperty=fullName> has the complete list. Each article provides a syntax example you can copy.

You must use the function's *fully qualified name* and append the [Service namespace](../web-api-service-documents.md#service-namespace) (`Microsoft.Dynamics.CRM`) to the name of the function.

Each function has a `PropertyName` parameter that specifies the property to be evaluated. The function may have more parameters, such as `PropertyValue`, `PropertyValues`, or `PropertyValue1` and `PropertyValue2`. When these parameters exist, you must supply a value, or values, to compare to the `PropertyName` parameter.

The following example shows uses the [Between function](xref:Microsoft.Dynamics.CRM.Between) to search for accounts with between 5 and 2,000 employees.  
  
```http 
GET [Organization URI]/api/data/v9.2/accounts?$select=name,numberofemployees
&$filter=Microsoft.Dynamics.CRM.Between(PropertyName='numberofemployees',PropertyValues=["5","2000"])  
```  

## Filter using string values

Keep the following points in mind when you filter on string values:

- All filters using string values are case insensitive.
- You must URL encode special characters in filter criteria. More information: [URL encode special characters](#url-encode-special-characters)
- You may use wildcard characters, but avoid using them incorrectly. More information: [Use wildcard characters](#use-wildcard-characters)
- You can use OData query functions: `contains`, `startswith`, and `endswith`. More information: [Use OData query functions](#use-odata-query-functions)
- You must manage single quotes when you use filters that accept an array of string values. More information: [Manage single quotes](#manage-single-quotes)

### URL encode special characters

If the string you are using as a value in a filter function includes a special character, you need to URL encode it. For example, if you use this function: `contains(name,'+123')`, it will not work because `+` is a character that can't be included in a URL. If you URL encode the string, it will become `contains(name,'%2B123')` and you will get results where the column value contains `+123`.

The following table shows the URL encoded values for common special characters.

|Special<br />character|URL encoded<br />character|
|---|---|
|`$`|`%24`|
|`&`|`%26`|
|`+`|`%2B`|
|`,`|`%2C`|
|`/`|`%2F`|
|`:`|`%3A`|
|`;`|`%3B`|
|`=`|`%3D`|
|`?`|`%3F`|
|`@`|`%40`|


### Use wildcard characters

When composing filters using strings, you can apply the following wildcard characters:

|Characters  |Description  |T-SQL documentation and examples  |
|---|---|---|
|`% ` |Matches any string of zero or more characters. This wildcard character can be used as either a prefix or a suffix.|[Percent character (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/percent-character-wildcard-character-s-to-match-transact-sql)|
|`_`  |Use the underscore character to match any single character in a string comparison operation that involves pattern matching.|[_ (Wildcard - Match One Character) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-match-one-character-transact-sql)|
|`[]` |Matches any single character within the specified range or set that is specified between brackets.|[[ ] (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-to-match-transact-sql)|
|`[^]`|Matches any single character that isn't within the range or set specified between the square brackets.|[[^] (Wildcard - Character(s) Not to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-not-to-match-transact-sql)|

More information: [Use wildcard characters in conditions for string values](../../wildcard-characters.md)

#### Leading wildcards not supported

It's important not to use leading wild cards because they aren't supported. Queries that use these anti-patterns introduce performance problems because the queries can't be optimized. Here are some examples of leading wildcards:

```
startswith(name,'%value')
endswith(name,'value%')
```

[Learn more about errors returned when leading wildcards are used](/power-apps/developer/data-platform/webapi/query/optimize-performance#avoid-leading-wild-cards-in-filter-conditions)

### Use OData query functions

The following table describes the OData query functions you can use to filter on string values:

|Function|Example|  
|---|---|  
|`contains`|`$filter=contains(name,'(sample)')`|  
|`endswith`|`$filter=endswith(name,'Inc.')`|  
|`startswith`|`$filter=startswith(name,'a')`|

You can use these functions with the logical operator `not` to negate the result.

### Manage single quotes

Some filters accept an array of string values, such as the [In Query function](xref:Microsoft.Dynamics.CRM.In). When you specify values in these filters that contain single quote, or apostrophe, characters, such as `O'Brian` or `Men's clothes`, you must use double quotes around the values; for example:

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
&$filter=Microsoft.Dynamics.CRM.In(PropertyName=@p1,PropertyValues=@p2)
&@p1='lastname'
&@p2=["OBrian","OBryan","O'Brian","O'Bryan"]
```

If you don't, you get the following error: `Invalid JSON. A comma character ',' was expected in scope 'Array'. Every two elements in an array and properties of an object must be separated by commas.`

If the filter is for a single value, replace the single quote character with two consecutive single quote characters; for example:

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
&$filter=lastname eq 'O''Bryan'
```

If you don't, you get an error like this: `There is an unterminated literal at position 21 in 'lastname eq 'O'Bryan''.`

## Filter based on related data values

You can filter rows returned based on values in related tables. How you filter depends on the type of relationship.

### Filter on lookup property

For one-to-many relationships, a [filtered collection](overview.md#filtered-collections) returns the same results as using an `eq` `$filter` on the [Lookup property](../web-api-properties.md#lookup-properties) for the relationship. For example, this filtered collection:

```http
GET [Organization URI]/api/data/v9.2/systemusers(<systemuserid value>)/user_accounts?$select=name
```

Is the same as this filter on a lookup property.

```http
GET [Organization URI]/api/data/v9.2/accounts?$filter=_owninguser_value eq <systemuserid value>&$select=name
```

### Filter using lookup column property values

You can filter based on values in [single-valued navigation properties](../web-api-navigation-properties.md#single-valued-navigation-properties) that represent lookup columns. Use this pattern:

`<single-valued navigation property>/<property name>`

The following example returns account records based on the value of the `primarycontactid/fullname` column:

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$filter=primarycontactid/fullname eq 'Susanna Stubberod (sample)'
&$select=name,_primarycontactid_value
Accept: application/json  
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_primarycontactid_value)",
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

You can also compare values further up the hierarchy of [single-valued navigation properties](../web-api-navigation-properties.md#single-valued-navigation-properties).

The following example returns the first account where the contact record represents the `primarycontactid`, where 'System Administrator' created the record, using `primarycontactid/createdby/fullname` in the `$filter`.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$filter=primarycontactid/createdby/fullname eq 'System Administrator'
&$select=name,_primarycontactid_value
&$expand=primarycontactid(
$select=fullname,_createdby_value;
$expand=createdby($select=fullname))
&$top=1
Accept: application/json  
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_primarycontactid_value,primarycontactid(fullname,_createdby_value,createdby(fullname)))",
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "primarycontactid": {
                "fullname": "Susanna Stubberod (sample)",
                "_createdby_value@OData.Community.Display.V1.FormattedValue": "System Administrator",
                "_createdby_value": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd",
                "createdby": {
                    "fullname": "System Administrator",
                    "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                    "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
                }
            }
        }
    ]
}
```

### Filter using values of related collections

Use the *Lambda operators* `any` and `all` to evaluate values in a collection to filter the results.

- `any`: Returns `true` if the expression applied is true for any member of the collection; otherwise, it returns false.

  - The `any` operator without an argument returns `true` if the collection isn't empty.

- `all`: Returns true if the expression applied is true for all members of the collection; otherwise, it returns false.

The syntax looks like this:

`<collection>/[any | all](o:<expression to evaluate>)`

In this case, `o` is the variable that represents items in the collection. The convention is to use the first letter of the type.
In the expression, use `o/<property or collection name>` to refer to a property or collection of a given item.

You can include conditions on multiple collection-valued navigation properties and nested collections. You can't include conditions on collection-valued navigation properties that are nested in a lookup navigation property. For example, `$filter=primarycontactid/new_contact_account/any(a:a/accountid eq '{GUID}')` isn't supported.

More information: [Lambda Operators at odata.org](https://www.odata.org/getting-started/basic-tutorial/#lambda)

#### Lambda operator examples

The following example retrieves all [account](xref:Microsoft.Dynamics.CRM.account) records that have at least one email with "sometext" in the subject:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Emails/any(e:contains(e/subject,'sometext'))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

The following example retrieves all [account](xref:Microsoft.Dynamics.CRM.account) records that have all associated tasks closed:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Tasks/all(t:t/statecode eq 1)
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

The following example retrieves all [account](xref:Microsoft.Dynamics.CRM.account) records that have at least one email with "sometext" in the subject and whose state code is active:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Emails/any(e:contains(e/subject,'sometext') and 
e/statecode eq 0)
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

The following example creates a nested query using `any` and `all` operators:

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=(contact_customer_accounts/any(c:c/jobtitle eq 'jobtitle' and 
c/opportunity_customer_contacts/any(o:o/description ne 'N/A'))) and 
endswith(name,'Inc.')
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

## Condition limits

You can include no more than 500 total conditions in a query. Otherwise, you see this error:

> Name: `TooManyConditionsInQuery`<br />
> Code: `0x8004430C`<br />
> Number: `-2147204340`<br />
> Message: `Number of conditions in query exceeded maximum limit.`

You need to reduce the number of conditions to execute the query. You might be able to reduce the number of conditions by using the [In](xref:Microsoft.Dynamics.CRM.In) or [NotIn](xref:Microsoft.Dynamics.CRM.NotIn) query functions that can be used with numbers, unique identifiers, and strings up to 850 characters.

## Next steps

Learn how to page results.

> [!div class="nextstepaction"]
> [Page results](page-results.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
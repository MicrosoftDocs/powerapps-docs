---
title: "Use Microsoft Dataverse Web API functions"
description: "Learn how to use Web API functions with Microsoft Dataverse. Discover how to pass parameters, use bound and unbound functions, and compose queries to retrieve data efficiently."
ms.topic: how-to
ms.date: 03/27/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---
# Use Web API functions

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Functions are reusable operations that you can perform by using the Web API. The Web API includes two types of functions:

- **Functions**: Use a `GET` request with the functions listed in the <xref:Microsoft.Dynamics.CRM.FunctionIndex> to perform operations that have no side effects. These functions generally retrieve data, either a collection or a complex type. Each function has a corresponding message in the organization service.

- **Query functions**: Use the functions listed in the <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex> to evaluate properties and values in the composition of a query. Each query function has a corresponding <xref:Microsoft.Xrm.Sdk.Query.ConditionOperator> value.
  
<a name="bkmk_passParametersToFunctions"></a>

## Passing parameters to a function
  
For functions that require parameters, pass the values by using parameter aliases.

For example, when you use the <xref:Microsoft.Dynamics.CRM.GetTimeZoneCodeByLocalizedName> function, you must include the `LocalizedStandardName` and `LocaleId` parameter values. You can use the following inline syntax:
  
```http
GET/GetTimeZoneCodeByLocalizedName(LocalizedStandardName='Pacific Standard Time',LocaleId=1033)  
```  
  
However, a couple of issues can cause requests to fail unless you send these requests by using parameter aliases:

- You get a `400 Bad Request - Invalid URL` error if you exceed the [Maximum OData segment length](compose-http-requests-handle-errors.md#maximum-odata-segment-length).
- There's an issue using DateTimeOffset values with the inline syntax, as explained in the following article: [DateTimeOffset as query parameter #204](https://github.com/OData/WebApi/issues/204).
  
Avoid these issues by passing the values in by using parameter aliases, as shown in the following code sample:
  
```http
GET /GetTimeZoneCodeByLocalizedName(LocalizedStandardName=@p1,LocaleId=@p2)?@p1='Pacific Standard Time'&@p2=1033  
```  
  
When you use a parameter value multiple times, [parameter aliases](query/overview.md#use-parameter-aliases-with-query-options) allow you to reuse it to reduce the length of the URL.
  
<a name="bkmk_passCrmEntityReference"></a>

## Pass record reference to a function

Certain functions require passing a reference to an existing record. For example, the following functions have a parameter that requires a <xref:Microsoft.Dynamics.CRM.crmbaseentity> entity type:  
  
:::row:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.CalculateRollupField>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.IncrementKnowledgeArticleViewCount>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.InitializeFrom>
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.IsValidStateTransition>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.RetrieveDuplicates>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.RetrieveLocLabels>
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.RetrieveRecordWall>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.ValidateRecurrenceRule>
   :::column-end:::
:::row-end:::
  
When you pass a reference to an existing record, add the `@odata.id` annotation to the Uri for the record. For example, if you're using the <xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess> function, you can use the following Uri to specify retrieving access to a specific contact record:  
  
```http
GET /systemusers(af9b3cf6-f654-4cd9-97a6-cf9526662797)/Microsoft.Dynamics.CRM.RetrievePrincipalAccess(Target=@tid)?@tid={'@odata.id':'contacts(aaaabbbb-0000-cccc-1111-dddd2222eeee)'}
```  
  
The `@odata.id` annotation can be either the full URI or a relative URI.
  
<a name="bkmk_boundAndUnboundFunctions"></a>
 
## Bound and unbound functions

You can bind only functions found in <xref:Microsoft.Dynamics.CRM.FunctionIndex> or functions you create as a [custom API](../custom-api.md). Query functions are never bound.  
  
<a name="bkmk_boundFunctions"></a>

### Bound functions

In the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document), when a `Function` element represents a bound function, it has an `IsBound` attribute with the value `true`. The first `Parameter` element defined in the function represents the entity that the function is bound to. When the `Type` attribute of the parameter is a collection, the function is bound to an entity collection.

The following example is the definition of the <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivileges> function and <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegesResponse> complex type in the CSDL.
  
```xml
<ComplexType Name="RetrieveUserPrivilegesResponse">
  <Property Name="RolePrivileges" Type="Collection(mscrm.RolePrivilege)" />
</ComplexType
<Function Name="RetrieveUserPrivileges" IsBound="true">
    <Parameter Name="entity" Type="mscrm.systemuser" Nullable="false" />
    <ReturnType Type="mscrm.RetrieveUserPrivilegesResponse" Nullable="false" />
</Function>
```  
  
This bound function is equivalent to the [SDK for .NET RetrieveUserPrivilegesRequest class](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegesRequest). In the Web API, this function is bound to the <xref:Microsoft.Dynamics.CRM.systemuser> entity type that represents the [SDK for .NET RetrieveUserPrivilegesRequest.UserId property](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegesRequest.UserId) property. Instead of returning an instance of the [SDK for .NET RetrieveUserPrivilegesResponse class](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegesResponse), this function returns a <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegesResponse> complex type. When a function returns a complex type, its definition usually appears directly above the definition of the function in the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document).  
  
To invoke a bound function, append the full name of the function to the URL and include any named parameters in parentheses following the function name. The full function name includes the namespace `Microsoft.Dynamics.CRM`. Functions that aren't bound must not use the full name.  
  
> [!IMPORTANT]
> Invoke a bound function by using a URI to set the first parameter value. You can't set it as a named parameter value.  
  
The following example uses the <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivileges> function, which is bound to the `systemuser` table.  
  
 **Request:**

```http
GET [Organization URI]/api/data/v9.2/systemusers(da455fec-68b7-ec11-9840-000d3a13d713)/Microsoft.Dynamics.CRM.RetrieveUserPrivileges
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response:**
 
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
  "@odata.context": "[Organization URI]/api/data/v8.2/$metadata#Microsoft.Dynamics.CRM.RetrieveUserPrivilegesResponse",
  "RolePrivileges": [
    {
      "Depth": "Global",
      "PrivilegeId": "20db4bf7-60c4-4eb9-ab95-0949766fef1a",
      "BusinessUnitId": "dfe37870-c8ac-ec11-9841-0022482088be",
      "PrivilegeName": "prvCreateflowsession"
    },
    {
      "Depth": "Global",
      "PrivilegeId": "d8db8e4c-5b76-48eb-b5ec-171b8c661917",
      "BusinessUnitId": "dfe37870-c8ac-ec11-9841-0022482088be",
      "PrivilegeName": "prvWriteworkflowbinary"
    },
    ... <full list of privileges removed for brevity>
    {
      "Depth": "Global",
      "PrivilegeId": "b234db9f-27a2-4d12-8b51-fc34fbef9d87",
      "BusinessUnitId": "dfe37870-c8ac-ec11-9841-0022482088be",
      "PrivilegeName": "prvWriteflowsession"
    }
  ]
}
 
```  
  
<a name="bkmk_unboundFunctions"></a>
 
### Unbound functions

The <xref:Microsoft.Dynamics.CRM.WhoAmI> function isn't bound to an entity. It's defined in the [CSDL $metadata document](web-api-service-documents.md#csdl-metadata-document) without an `IsBound` attribute.  
  
```xml
<ComplexType Name="WhoAmIResponse">  
  <Property Name="BusinessUnitId" Type="Edm.Guid" Nullable="false" />  
  <Property Name="UserId" Type="Edm.Guid" Nullable="false" />  
  <Property Name="OrganizationId" Type="Edm.Guid" Nullable="false" />  
</ComplexType>  
<Function Name="WhoAmI">  
  <ReturnType Type="mscrm.WhoAmIResponse" Nullable="false" />  
</Function>  
```  
  
This function corresponds to the [SDK for .NET WhoAmIRequest class](xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest) and returns a <xref:Microsoft.Dynamics.CRM.WhoAmIResponse> complex type that corresponds to the [SDK for .NET WhoAmIResponse class](xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse). This function doesn't have any parameters.  
  
When you invoke an unbound function, use just the function name, as shown in the following example:
  
 **Request:**

```http
GET [Organization URI]/api/data/v9.2/WhoAmI HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
{  
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",  
 "BusinessUnitId": "11bb11bb-cc22-dd33-ee44-55ff55ff55ff",  
 "UserId": "22cc22cc-dd33-ee44-ff55-66aa66aa66aa",  
 "OrganizationId": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"  
}  
```  
  
<a name="bkmk_composeQueryWithFunctions"></a>

## Compose a query with functions

You can use functions in two ways to control the data returned by queries. Certain functions allow you to control the columns or conditions that they return. You can also use query functions to evaluate conditions in a query.
  
<a name="bkmk_composableFunctions"></a>
  
### Composable functions

Some functions listed in <xref:Microsoft.Dynamics.CRM.FunctionIndex> return a collection of entities. A subset of these functions are *composable*, which means that you can include a `$select` or `$filter` system query option to control which columns are returned in the results. These functions have an `IsComposable` attribute in the CSDL. Each of these functions has a companion message in the SDK that accepts either a [SDK for .NET ColumnSet class](xref:Microsoft.Xrm.Sdk.Query.ColumnSet) or [SDK for .NET QueryBase class](xref:Microsoft.Xrm.Sdk.Query.QueryBase) type parameter. The OData system query options provide the same functionality, so these functions don't have the same parameters as their companion messages in the SDK for .NET . The following table shows a list of composable functions:  
  
:::row:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.RetrieveAllChildUsersSystemUser>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.RetrieveBusinessHierarchyBusinessUnit>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple>
   :::column-end:::
:::row-end:::
:::row:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.SearchByBodyKbArticle>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.SearchByKeywordsKbArticle>
   :::column-end:::
   :::column:::
      <xref:Microsoft.Dynamics.CRM.SearchByTitleKbArticle>
   :::column-end:::
:::row-end:::
  
<a name="bkmk_queryevaluationFunctions"></a>
  
### Query functions

Use the functions listed in the <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex> to compose a query. You can use them in a manner similar to the [OData query functions](query/filter-rows.md#use-odata-query-functions), but there are some important differences. You must use the full name of the function and include the names of the parameters.
  
The following example uses the <xref:Microsoft.Dynamics.CRM.LastXHours> query function to return all account entities modified in the past 12 hours:
  
```http
GET /accounts?$select=name,accountnumber&$filter=Microsoft.Dynamics.CRM.LastXHours(PropertyName=@p1,PropertyValue=@p2)&@p1='modifiedon'&@p2=12  
```  

#### Limitations of query functions

One limitation of query functions is that you can't use the `not` operator to negate query functions.

For example, the following query, which uses <xref:Microsoft.Dynamics.CRM.EqualUserId>, fails with the error: `Not operator along with the Custom Named Condition operators is not allowed`.

```http
GET /systemusers?$select=fullname,systemuserid&$filter=not Microsoft.Dynamics.CRM.EqualUserId(PropertyName=@p1)&@p1='systemuserid'
```

Several query functions have a companion negated query function. For example, <xref:Microsoft.Dynamics.CRM.NotEqualUserId> negates <xref:Microsoft.Dynamics.CRM.EqualUserId>, so the following query returns the expected results:

```http
GET /systemusers?$select=fullname,systemuserid&$filter=Microsoft.Dynamics.CRM.NotEqualUserId(PropertyName=@p1)&@p1='systemuserid'
```

Other query functions can be negated in different ways. For example, rather than trying to negate the <xref:Microsoft.Dynamics.CRM.Last7Days> query function like this (which fails with the same error as mentioned previously):

```http
GET /accounts?$select=name&$filter=not Microsoft.Dynamics.CRM.Last7Days(PropertyName=@p1)&@p1='createdon'
```

Use the <xref:Microsoft.Dynamics.CRM.OlderThanXDays> query function like this:

```http
GET /accounts?$select=name&$filter=Microsoft.Dynamics.CRM.OlderThanXDays(PropertyName=@p1,PropertyValue=@p2)&@p1='createdon'&@p2=7
```

### See also

[Web API functions and actions Sample (C#)](samples/webapiservice-functions-and-actions.md)   
[Web API functions and actions Sample (Client-side JavaScript)](samples/functions-actions-client-side-javascript.md)   
[Web API Functions and Actions Sample (PowerShell)](samples/functions-actions-powershell.md)   
[Query data using the Web API](query/overview.md)   
[Use Web API actions](use-web-api-actions.md)   

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

---
title: Use Web API functions
description: Learn how to use functions, which are reusable operations used with a GET request to retrieve data from Microsoft Dataverse Web API.
ms.topic: how-to
ms.date: 04/26/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
ms.custom: bap-template
---
# Use Web API functions

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Functions are reusable operations that you can perform using the Web API. There are two types of functions in the Web API:

- **Functions**: Use a `GET` request with the functions listed in the <xref:Microsoft.Dynamics.CRM.FunctionIndex> to perform operations that have no side-effects. These functions generally retrieve data, either a collection or a complex type. Each function has a corresponding message in the organization service.

- **Query functions**: Use the functions listed in the <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex> to evaluate properties and values in the composition of a query. Each query function has a corresponding <xref:Microsoft.Xrm.Sdk.Query.ConditionOperator> value.
  
<a name="bkmk_passParametersToFunctions"></a>

## Passing parameters to a function
  
For those functions that require parameters, the best practice is to pass the values using parameters.

For example, when you use the <xref:Microsoft.Dynamics.CRM.GetTimeZoneCodeByLocalizedName> function, you must include the `LocalizedStandardName` and `LocaleId` parameter values. You could use the following inline syntax:
  
```http
GET [Organization URI]/api/data/v9.0/GetTimeZoneCodeByLocalizedName(LocalizedStandardName='Pacific Standard Time',LocaleId=1033)  
```  
  
However, there's an issue using DateTimeOffset values with the inline syntax, as explained in the following article: [DateTimeOffset as query parameter #204](https://github.com/OData/WebApi/issues/204).  
  
Avoid the `DateTimeOffset` issue by passing the values in as parameters, as shown in the following code sample:
  
```http
GET [Organization URI]/api/data/v9.0/GetTimeZoneCodeByLocalizedName(LocalizedStandardName=@p1,LocaleId=@p2)?@p1='Pacific Standard Time'&@p2=1033  
```  
  
When a parameter value is used multiple times, [parameter aliases](query-data-web-api.md#use-parameter-aliases-with-query-options) allow you to reuse it to reduce the length of the URL.
  
<a name="bkmk_passCrmEntityReference"></a>

## Pass record reference to a function

Certain functions require passing a reference to an existing record. For example, the following functions have a parameter that requires a <xref:Microsoft.Dynamics.CRM.crmbaseentity> entity type:  
  
|Functions|&nbsp;|&nbsp;|  
|-|-|-|  
|<xref:Microsoft.Dynamics.CRM.CalculateRollupField>|<xref:Microsoft.Dynamics.CRM.IncrementKnowledgeArticleViewCount>|<xref:Microsoft.Dynamics.CRM.InitializeFrom>|  
|<xref:Microsoft.Dynamics.CRM.IsValidStateTransition>|<xref:Microsoft.Dynamics.CRM.RetrieveDuplicates>|<xref:Microsoft.Dynamics.CRM.RetrieveLocLabels>|  
|<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess>|<xref:Microsoft.Dynamics.CRM.RetrieveRecordWall>|<xref:Microsoft.Dynamics.CRM.ValidateRecurrenceRule>|  
  
When you pass a reference to an existing record, use the `@odata.id` annotation to the Uri for the record. For example if you're using the <xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess> function you can use the following Uri to specify retrieving access to a specific contact record:  
  
```http
GET [Organization URI]/api/data/v9.0/systemusers(af9b3cf6-f654-4cd9-97a6-cf9526662797)/Microsoft.Dynamics.CRM.RetrievePrincipalAccess(Target=@tid)?@tid={'@odata.id':'contacts(9f3162f6-804a-e611-80d1-00155d4333fa)'}
```  
  
The `@odata.id` annotation can be either the full URI or a relative URI.
  
<a name="bkmk_boundAndUnboundFunctions"></a>
 
## Bound and unbound functions

Only functions found in <xref:Microsoft.Dynamics.CRM.FunctionIndex>, or created as a [custom API](../custom-api.md) may be bound. Query functions are never bound.  
  
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
  
This bound function is equivalent to the <xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegesRequest> class used by the SDK for .NET. In the Web API this function is bound to the <xref:Microsoft.Dynamics.CRM.systemuser> entity type that represents the [RetrieveUserPrivilegesRequest.UserId property](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegesRequest.UserId) property. Instead of returning an instance of the <xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegesResponse> class, this function returns a <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegesResponse> complex type. When a function returns a complex type, its definition usually appears directly above the definition of the function in the CSDL.  
  
To invoke a bound function, append the full name of the function to the URL and include any named parameters in parentheses following the function name. The full function name includes the namespace `Microsoft.Dynamics.CRM`. Functions that aren't bound must not use the full name.  
  
> [!IMPORTANT]
> Invoke a bound function using a URI to set the first parameter value. You can't set it as a named parameter value.  
  
The following example uses the <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivileges> function, which is bound to the `systemuser` table.  
  
 **Request:**

```http
GET [Organization URI]/api/data/v9.2/systemusers(da455fec-68b7-ec11-9840-000d3a13d713)/Microsoft.Dynamics.CRM.RetrieveUserPrivileges HTTP/1.1
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

The <xref:Microsoft.Dynamics.CRM.WhoAmI> function isn't bound to an entity. It's defined in the CSDL without an `IsBound` attribute.  
  
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
  
This function corresponds to the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> class and returns a <xref:Microsoft.Dynamics.CRM.WhoAmIResponse> complex type that corresponds to the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIResponse> class used by the SDK for .NET. This function doesn't have any parameters.  
  
When you invoke an unbound function, use just the function name, as shown in the following example:
  
 **Request:**

```http
GET [Organization URI]/api/data/v9.0/WhoAmI() HTTP/1.1  
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
 "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.WhoAmIResponse",  
 "BusinessUnitId": "ded5a64f-f06d-e511-80d0-00155db07cb1",  
 "UserId": "d96e9f55-f06d-e511-80d0-00155db07cb1",  
 "OrganizationId": "4faf1f34-f06d-e511-80d0-00155db07cb1"  
}  
```  
  
<a name="bkmk_composeQueryWithFunctions"></a>

## Compose a query with functions

There are two ways that functions can be used to control the data returned with queries. Certain functions allow for control over the columns or conditions that they return, and you can use query functions to evaluate conditions in a query.
  
<a name="bkmk_composableFunctions"></a>
  
### Composable functions

Some functions listed in <xref:Microsoft.Dynamics.CRM.FunctionIndex> return a collection of entities. A subset of these functions are *composable*, which means that you can include a `$select` or `$filter` system query option to control which columns are returned in the results. These functions have an `IsComposable` attribute in the CSDL. Each of these functions has a companion message in the SDK that accept either a <xref:Microsoft.Xrm.Sdk.Query.ColumnSet> or <xref:Microsoft.Xrm.Sdk.Query.QueryBase> type parameter. The OData system query options provide the same functionality so these functions don't have the same parameters as their companion messages in the SDK. The following table shows a list of those composable functions in this release.  
  
|Functions|&nbsp;|&nbsp;|  
|-|-|-|  
|<xref:Microsoft.Dynamics.CRM.RetrieveAllChildUsersSystemUser>|<xref:Microsoft.Dynamics.CRM.RetrieveBusinessHierarchyBusinessUnit>|<xref:Microsoft.Dynamics.CRM.RetrieveUnpublishedMultiple>|
|<xref:Microsoft.Dynamics.CRM.SearchByBodyKbArticle>|<xref:Microsoft.Dynamics.CRM.SearchByKeywordsKbArticle>|<xref:Microsoft.Dynamics.CRM.SearchByTitleKbArticle>|  
  
<a name="bkmk_queryevaluationFunctions"></a>
  
### Query functions

Functions listed in the <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex> are intended to be used to compose a query. You can use them in a manner similar to the [OData query functions](query-data-web-api.md#use-odata-query-functions), but there are some important differences. You must use the full name of the function and include the names of the parameters. 
  
The following example uses the <xref:Microsoft.Dynamics.CRM.LastXHours> query function to return all account entities modified in the past 12 hours:
  
```http
GET [Organization URI]/api/data/v9.0/accounts?$select=name,accountnumber&$filter=Microsoft.Dynamics.CRM.LastXHours(PropertyName=@p1,PropertyValue=@p2)&@p1='modifiedon'&@p2=12  
```  

#### Limitations of query functions

One of the limitations of query functions is that you can't use the `not` operator to negate query functions.

For example, the following query, which uses <xref:Microsoft.Dynamics.CRM.EqualUserId>, fails with the error: `Not operator along with the Custom Named Condition operators is not allowed`.

```http
GET [Organization URI]/api/data/v9.1/systemusers?$select=fullname,systemuserid&$filter=not Microsoft.Dynamics.CRM.EqualUserId(PropertyName=@p1)&@p1='systemuserid'
```

Several query functions have a companion negated query function. For example, <xref:Microsoft.Dynamics.CRM.NotEqualUserId> negates <xref:Microsoft.Dynamics.CRM.EqualUserId>, so the following query returns the expected results:

```http
GET [Organization URI]/api/data/v9.1/systemusers?$select=fullname,systemuserid&$filter=Microsoft.Dynamics.CRM.NotEqualUserId(PropertyName=@p1)&@p1='systemuserid'
```

Other query functions can be negated in different ways. For example, rather than trying to negate the <xref:Microsoft.Dynamics.CRM.Last7Days> query function like this (which fail with the same error as mentioned previously):

```http
GET [Organization URI]/api/data/v9.1/accounts?$select=name&$filter=not Microsoft.Dynamics.CRM.Last7Days(PropertyName=@p1)&@p1='createdon'
```

Use the <xref:Microsoft.Dynamics.CRM.OlderThanXDays> query function like this:

```http
GET [Organization URI]/api/data/v9.1/accounts?$select=name&$filter=Microsoft.Dynamics.CRM.OlderThanXDays(PropertyName=@p1,PropertyValue=@p2)&@p1='createdon'&@p2=7
```

### See also

[Web API functions and actions Sample (C#)](samples/webapiservice-functions-and-actions.md)   
[Web API functions and actions Sample (Client-side JavaScript)](samples/functions-actions-client-side-javascript.md)   
[Perform operations using the Web API](perform-operations-web-api.md)   
[Compose HTTP requests and handle errors](compose-http-requests-handle-errors.md)   
[Query data using the Web API](query-data-web-api.md)   
[Create a table row using the Web API](create-entity-web-api.md)   
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)   
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)   
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)   
[Use Web API actions](use-web-api-actions.md)   
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)   
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)   
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]

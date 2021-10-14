---
title: "Implement all types of queries when filtering results using PreOperation RetrieveMultiple | MicrosoftDocs"
description: "For best performance and consistent results for all applications you must implement filtering for all types of queries that can be used with plug-ins that are registered for the PreOperation stage of RetrieveMultiple"
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: ryjones
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 09/23/2019
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Implement all types of queries when filtering results using PreOperation RetrieveMultiple

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

**Category**: Design, Performance, Security, Supportability

**Impact potential**: Medium

<a name='symptoms'></a>

## Symptoms

RetrieveMultiple calls from different application display different results.

- For example: same views in legacy applications show different results in new applications.

<a name='guidance'></a>

## Guidance

> [!NOTE]
> The `Retrieve` and `RetrieveMultiple` messages are typically the most commonly used messages. Plug-ins for these messages can significantly impact system performance. Generally, you should avoid using plug-ins for these messages if the requirements can be achieved some other way. More information: [Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](limit-registration-plugins-retrieve-retrievemultiple.md)

Plug-ins registered on the `RetrieveMultiple` message are typically intended to filter the results returned by queries for an entity. There are two strategies to do this using a plug-in registered on either the `PostOperation` or `PreOperation` stages.

### PostOperation filtering

In the `PostOperation` stage, evaluate the records returned in the <xref:Microsoft.Xrm.Sdk.IExecutionContext.OutputParameters> `BusinessEntityCollection` <xref:Microsoft.Xrm.Sdk.EntityCollection.Entities> property and remove entities that should not be returned.

This approach will potentially change the expected number of records returned in each page of results and can result in inconsistent experiences when the data is displayed in an application.

### PreOperation filtering

In the `PreOperation` stage, evaluate the <xref:Microsoft.Xrm.Sdk.IExecutionContext.InputParameters>  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest.Query> property and adjust the query to filter what will be returned before it is executed.

When using this approach you must implement the appropriate filtering for the different possible types of queries, most importantly: <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> and <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>. If you implement just one of these, different applications that use the other type of query will not apply your changes.

Although the `QueryExpressionToFetchXml` and `FetchXmlToQueryExpression` messages provide the capability to convert one query type to another, because of the performance impact of including additional calls within `RetrieveMultiple`, we recommend that you do not use these messages in this context. Rather, implement your filtering using the equivalent logic in both. 

There is a third type of query that can also be used with `RetrieveMultiple`: <xref:Microsoft.Xrm.Sdk.Query.QueryByAttribute>. This type of query does not provide for complex filtering and it isn't possible to include more complex filtering logic within a plug-in. Fortunately, this type of query is not frequently used. Depending on the sensitivity of the filtering you add, you may choose to reject queries of this type by throwing an <xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException>.

## Example

See [Sample: Modify query in PreOperation stage](../../org-service/samples/modify-query-preoperation-stage.md) for an example of the strategy we recommend.

## Problematic patterns

If a plug-in is written to change the records returned in a specific application which uses just one type of query used by that application, either <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> or <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>, the results may not be consistent in other applications or if the application changes the type of query used. Plug-ins should be written to provide the same result regardless of the application.

<a name='additional'></a>

## Additional information

When using the Web API, GET requests on a collection are converted to <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> unless the query uses FetchXml as described in [Retrieve and execute predefined queries](../../webapi/retrieve-and-execute-predefined-queries.md). In that case the queries use <xref:Microsoft.Xrm.Sdk.Query.FetchExpression>.

The legacy web client for model-driven apps is being replaced by Unified Interface. Unified Interface uses the FetchXml defined in the [SavedQuery.FetchXml](../../reference/entities/savedquery.md#BKMK_FetchXml) or [UserQuery.FetchXml](../../reference/entities/userquery.md#BKMK_FetchXml) properties. For better performance, Unified Interface does not convert the FetchXml data to a <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> before executing these queries as the legacy web client did. Therefore, queries that were modified in plug-in code for the legacy web client which used  <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> will not apply the same changes now that the query to support views is being passed using <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> unless the plug-in code is written to apply same logic to <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> queries. 

<a name='seealso'></a>

### See also

[Sample: Modify query in PreOperation stage](../../org-service/samples/modify-query-preoperation-stage.md)<br />
[Query data using the Organization service](../../org-service/entity-operations-query-data.md)<br />
[Use FetchXML to construct a query](../../use-fetchxml-construct-query.md)<br />
[Build queries with QueryExpression](../../org-service/build-queries-with-queryexpression.md)<br />
[Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](limit-registration-plugins-retrieve-retrievemultiple.md)<br />
[Unified Interface Community](https://community.dynamics.com/365/unified-interface/)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
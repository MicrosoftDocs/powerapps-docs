---
title: "Sample: Generic virtual table data provider plug-in (Microsoft Dataverse) | Microsoft Docs"
description: "Sample demonstrates how to implement a generic custom Dynamics 365 virtual table plug-in."
ms.custom: ""
ms.date: 04/09/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "samples"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: d329dade-16c5-46e9-8dec-4b8efb996d24
author: "Sunil-Garg" # GitHub ID
ms.author: "pehecke"
manager: "ryjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Sample: Generic virtual table data provider plug-in

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

## Demonstrates

This sample shows a minimal implementation for a generic Microsoft Dataverse virtual table data provider plug-in, **DropboxRetrieveMultiplePlugin**, for the [Dropbox](https://www.dropbox.com/) file-sharing service. It uses the "bare metal" approach, translating the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> through the creation of the custom visitor class, **DropBoxExpressionVisitor**. It returns a collection of the files that satisfy the search criteria as an <xref:Microsoft.Xrm.Sdk.EntityCollection>. 

> [!NOTE]
> This sample requires the use of ILMERGE to combine the plug-in and Dropbox assemblies prior to registering the assembly with Dataverse. Use of ILMERGE is not officially supported. A future update to this sample will remove the need to use ILMERGE. 

## Getting started

In order to build this sample, you must first install the [Dropbox.Api](https://www.nuget.org/packages/Dropbox.Api/) and [Microsoft.CrmSdk.Data](https://www.nuget.org/packages/Microsoft.CrmSdk.Data/) NuGet packages in your solution.  You'll also need a DropBox account and pass a real access token when creating an instance of the **DropboxClient**.

Add the following using statements to your code:

```csharp
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Query;
using Dropbox.Api;
using Dropbox.Api.Files;
```

## Sample code  

```csharp  

public class DropBoxExpressionVisitor : QueryExpressionVisitorBase
{
    public string SearchKeyWords { get; private set; }

    public override QueryExpression Visit(QueryExpression query)
    {
        // Very simple visitor that extracts search keywords
        var filter = query.Criteria;
        if (filter.Conditions.Count > 0)
        {
            foreach (ConditionExpression condition in filter.Conditions)
            {
                if (condition.Operator == ConditionOperator.Like && condition.Values.Count > 0)
                {
                    string exprVal = (string)condition.Values[0];

                    if (exprVal.Length > 2)
                    {
                        this.SearchKeyWords += " " + exprVal.Substring(1, exprVal.Length - 2);
                    }
                }
            }
            return query;
        }
    }
}

public class DropboxRetrieveMultiplePlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var qe = (QueryExpression)context.InputParameters["Query"];
        if (qe != null)
        {
            var visitor = new DropBoxExpressionVisitor();
            qe.Accept(visitor);
            using (var dbx = new DropboxClient(AccessToken))
            {
                if (visitor.SearchKeyWords != string.Empty)
                {
                    var searchCriteria = new SearchArg(string.Empty, visitor.SearchKeyWords);
                    var task = Task.Run(() => this.SearchFile(dbx, searchCriteria));
                    context.OutputParameters["BusinessEntityCollection"] = task.Result;
                }
            }
        }
    }

    public async Task<EntityCollection> SearchFile(DropboxClient dbx, SearchArg arg)
    {
        EntityCollection ec = new EntityCollection();
        var list = await dbx.Files.SearchAsync(arg);
        foreach (var item in list.Matches)
        {
            if (item.Metadata.IsFile)
            {
                Entity e = new Entity("new_dropbox");
                e.Attributes.Add("new_dropboxid", Guid.NewGuid());
                e.Attributes.Add("new_filename", item.Metadata.AsFile.Name);
                e.Attributes.Add("new_filesize", item.Metadata.AsFile.Size);
                e.Attributes.Add("new_modifiedon", item.Metadata.AsFile.ServerModified);
                ec.Entities.Add(e);
            }
        }
        return ec;
    }
}

``` 

### See also

[Get started with virtual tables](get-started-ve.md)<br />
[API considerations of virtual tables](api-considerations-ve.md)<br />
[Custom virtual table data providers](custom-ve-data-providers.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
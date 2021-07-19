---
title: "Remove unsupported code that uses reflection in custom workflow activities | MicrosoftDocs"
description: "You must remove the code snippet mentioned in this topic if you find it in custom workflow activities"
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
ms.date: 08/15/2019
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Remove unsupported code that uses reflection in custom workflow activities

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

**Category**: Reliability

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

Workflow activities containing unsupported code that uses reflection will break in the coming months unless it is removed.

Workflow extensions will fail throwing the error `Could not load file or assembly 'Microsoft.Crm.Workflow, Version=`. The version number might be different but typically it is `6.0.0.0`.


<a name='guidance'></a>

## Guidance

You should not include and should proactively look for and remove code within custom workflow activities like the following:

```
var type = Type.GetType("Microsoft.Crm.Workflow.SynchronousRuntime.WorkflowContext, Microsoft.Crm.Workflow, Version=6.0.0.0");
type.GetProperty("ProxyTypesAssembly").SetValue(serviceFactory, typeof(YourServiceContext).Assembly, null); 
```

If you find code like this that is using reflection within a custom workflow activity you should remove it, recompile and update the assembly that contains it.

<a name='problem'></a>

## Problematic patterns

Today, this code serves no purpose. It appears to have been added by developers seeking to workaround an issue when using strong (early-bound) types around 7 years ago. 

Snippets including this code can be found in many forum posts unrelated to the issue. It is mentioned as a solution in this post on Stack Overflow [How to EnableProxyTypes on a service accessed from the IWorkflowContext in CRM 2011?](https://stackoverflow.com/questions/9230117/how-to-enableproxytypes-on-a-service-accessed-from-the-iworkflowcontext-in-crm-2/45948206)

The underlying issue about supporting strong types has been fixed, but this code has remained in the code base for custom workflow activities. This code has never been supported, but it didn't break anything. In the coming months, it will start to cause any custom workflow which include it to break.


<a name='additional'></a>

## Additional information

Currently reflection is not allowed. This code references an internal assembly that was included in a white list so that internal code could reflect on it. This is why it does not currently throw an error. But when general restrictions are lifted in the future, this will cause the workflow activity to break.

In order to provide greater capabilities within custom workflow activities without breaking people's business logic, we need everyone to review their code base and remove references like this.

<a name='seealso'></a>

### See also

[Workflow extensions](../../workflow/workflow-extensions.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
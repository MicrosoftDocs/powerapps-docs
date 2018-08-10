---
title: "Add metadata to a custom workflow activity (Common Data Service for Apps) | Microsoft Docs"
description: "Learn about adding metadata to a custom workflow activity by adding input and output parameters, and input and output attributes for the parameters."
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
      - "Dynamics 365 (online)"
ms.assetid: 06607e30-352c-4f27-a82e-adad48ca0f34
caps.latest.revision: 35
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Add metadata to a custom workflow activity

The assembly that contains the custom workflow activity definition is annotated using the .NET attributes to provide the metadata that Common Data Service for Apps uses at runtime to link your code to the workflow engine. For more information about .NET attributes, see [Extending Metadata Using Attributes](/dotnet/standard/attributes/index).  
  
Before you start adding metadata to your custom workflow activity definition, ensure that you’re aware of the CDS for Apps types and attributes that are supported for the custom workflow activities. More information: [Process Classes, Attributes, and CDS for Apps Types](process-classes-attributes-and-types.md) 
  
<a name="AddingInput"></a>

## Add input parameters

While specifying the input parameter in your workflow class, you can also specify a default value for the parameter. The following sample shows the definition of an input parameter.  
  
```csharp  
[Input("DateTime input")]  
[Default("2004-07-09T02:54:00Z")]  
public InArgument<DateTime> Date { get; set; }  
```  
  
This input parameter is annotated with the .NET attribute `Input`. The <xref:Microsoft.Xrm.Sdk.Workflow.InputAttribute> class derives from the <xref:Microsoft.Xrm.Sdk.Workflow.ParameterAttribute> class, which takes a parameter (<xref:Microsoft.Xrm.Sdk.Workflow.ParameterAttribute>.<xref:Microsoft.Xrm.Sdk.Workflow.ParameterAttribute.Name>) to specify the name of the input attribute. This name appears in the process form assistant in the web application. This lets you map an attribute as an input parameter to the process.  
  
In addition, you can make the input parameter required. More information:  [RequiredArgumentAttribute](process-classes-attributes-and-types.md#RequiredArgumentAttribute)  
  
<a name="Output"></a>

## Add output parameters

Output parameters are added in the same manner as the input parameters. The following sample shows the definition of an output parameter.  
  
```csharp  
[Output("Money output only")]  
[Default("23.3")]  
public OutArgument<Money> MoneyOutput { get; set; }  
```  
  
This output parameter is annotated with the .NET attribute `Output`. The <xref:Microsoft.Xrm.Sdk.Workflow.OutputAttribute> class derives from the <xref:Microsoft.Xrm.Sdk.Workflow.ParameterAttribute> class, which takes a parameter (<xref:Microsoft.Xrm.Sdk.Workflow.ParameterAttribute>.<xref:Microsoft.Xrm.Sdk.Workflow.ParameterAttribute.Name>) to specify the name of the output attribute. This name appears in the process form assistant in the web application. This lets you map an attribute as an output.  
  
<a name="InAndOut"></a>

## Add input and output attributes for the same parameter

You can use the input and output attributes for the same parameter. In the following code example, `IntParameter` is the input as well as the output parameter.  
  
```csharp  
[Input("Int input")]  
[Output("Int output")]  
[Default("2322")]  
public InOutArgument<int> IntParameter { get; set; }  
```  
  
<a name="Additional"></a>

## Additional attributes

Some types, such as `EntityReference` and `OptionSetValue`, require additional attributes apart from the `Input`, `Output`, and `Default` attributes. The additional attributes are: `ReferenceTarget` and `AttributeTarget`. The following sample shows the definition of a parameter of the `EntityReference` type.  
  
```csharp  
[Input("EntityReference input")]  
[Output("EntityReference output")]  
[ReferenceTarget("account")]  
[Default("3B036E3E-94F9-DE11-B508-00155DBA2902", "account")]  
public InOutArgument<EntityReference> AccountReference { get; set; }  
```  
  
For a list of supported types and attributes, see [Process Classes, Attributes, and CDS for Apps Types](process-classes-attributes-and-types.md).  
  
<a name="Execute"></a>

## Add the Execute method

Your custom workflow activity must have an `Execute` method, as shown in the following example.  
  
```csharp  
protected override void Execute(CodeActivityContext context)  
{  
   if (AccountReference.Get(context).Id != new Guid("3B036E3E-94F9-DE11-B508-00155DBA2902"))     
      throw new InvalidPluginExecutionException("Unexpected default value");  
}  
```  
  
### See also

[Custom workflow activities (workflow assemblies)](../custom-workflow-activities-workflow-assemblies.md)   
[Creating a Custom Workflow Activity](create-custom-workflow-activity.md)   
[Using the IOrganization Web Service within a Custom Workflow Activity](use-iorganization-web-service-custom-workflow-activity.md)   
[Sample: Create a Custom Workflow Activity](sample-create-custom-workflow-activity.md)   
[Process Classes, Attributes, and CDS for Apps Types](process-classes-attributes-and-types.md)

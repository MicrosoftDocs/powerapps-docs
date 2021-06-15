---
title: "Create extensions for the code generation tool (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The SDK download package includes an extension to the CrmSvcUtil code generation tool that you can use to generate enumerations for all choices (optionset) values including global choices, picklist, state, and status values." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Create extensions for the code generation tool

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can extend the functionality of the code generation tool by specifying additional command-line parameters and parameter values. To specify a parameter, add the following to the command line: /\<*parametername*>:\<*class name*>,\<*assembly name*>. Note that assembly name does not include the .dll extension. As an alternative, you can add the equivalent value to the config file in the format “<add key=”\<*parametername*>” value=”\<*class name*>,\<*assembly name*>” />”.  

The following table lists the parameters that you can use.  

|Parameter name|Interface Name|Description|  
|--------------------|--------------------|-----------------|  
|/codecustomization|ICustomizeCodeDomService|Called after the CodeDOM generation has been completed, assuming the default instance of `ICodeGenerationService`. It is useful for generating additional classes, such as the constants in picklists.|  
|/codewriterfilter|ICodeWriterFilterService|Called during the process of CodeDOM generation, assuming the default instance of `ICodeGenerationService`, to determine whether a specific object or property should be generated.|  
|/codewritermessagefilter|ICodeWriterMessageFilterService|Called during the process of CodeDOM generation, assuming the default instance of `ICodeGenerationService`, to determine whether a specific message should be generated. This should not be used for requests/responses as these are already generated in Microsoft.Crm.Sdk.Proxy.dll and Microsoft.Xrm.Sdk.dll.|  
|/metadataproviderservice|IMetadataProviderService|Called to retrieve the metadata from the server. This may be called multiple times during the generation process, so the data should be cached.|  
|/codegenerationservice|ICodeGenerationService|Core implementation of the CodeDOM generation. If this is changed, the other extensions may not behave in the manner described.|  
|/namingservice|INamingService|Called during the CodeDOM generation to determine the name for objects, assuming the default implementation.|

The implementation of these interfaces must have one of the following constructors:

`MyNamingService`()<br />
`MyNamingService`(`INamingService``defaultService`)<br />
`MyNamingService`(`IDictionary`<`string`, `string`> `parameters`)<br />
`MyNamingService`(`INamingService``defaultService`, `IDictionary`<`string`, `string`> `parameters`)

The `Microsoft.Crm.Services.Utility` namespace is defined in CrmSvcUtil.exe. Add a reference to CrmSvcUtil.exe in your Visual Studio code generation tool extension projects.

<a name="Generate_Enums"></a>

## Sample extension to generate enumerations for choices (option sets)

The following sample code demonstrates how to write an extension.  

```csharp
using System;

using Microsoft.Crm.Services.Utility;
using Microsoft.Xrm.Sdk.Metadata;

/// <summary>
/// Sample extension for the CrmSvcUtil.exe tool that generates early-bound
/// classes for custom entities.
/// </summary>
public sealed class BasicFilteringService : ICodeWriterFilterService
{
    public BasicFilteringService(ICodeWriterFilterService defaultService)
    {
        this.DefaultService = defaultService;
    }

    private ICodeWriterFilterService DefaultService { get; set; }

    bool ICodeWriterFilterService.GenerateAttribute(AttributeMetadata attributeMetadata, IServiceProvider services)
    {
        return this.DefaultService.GenerateAttribute(attributeMetadata, services);
    }

    bool ICodeWriterFilterService.GenerateEntity(EntityMetadata entityMetadata, IServiceProvider services)
    {
        if (!entityMetadata.IsCustomEntity.GetValueOrDefault()) { return false; }
        return this.DefaultService.GenerateEntity(entityMetadata, services);
    }

    bool ICodeWriterFilterService.GenerateOption(OptionMetadata optionMetadata, IServiceProvider services)
    {
        return this.DefaultService.GenerateOption(optionMetadata, services);
    }

    bool ICodeWriterFilterService.GenerateOptionSet(OptionSetMetadataBase optionSetMetadata, IServiceProvider services)
    {
        return this.DefaultService.GenerateOptionSet(optionSetMetadata, services);
    }

    bool ICodeWriterFilterService.GenerateRelationship(RelationshipMetadataBase relationshipMetadata, EntityMetadata otherEntityMetadata,
    IServiceProvider services)
    {
        return this.DefaultService.GenerateRelationship(relationshipMetadata, otherEntityMetadata, services);
    }

    bool ICodeWriterFilterService.GenerateServiceContext(IServiceProvider services)
    {
        return this.DefaultService.GenerateServiceContext(services);
    }
}

```

Download the sample: [CrmSvcUtilExtensions](https://github.com/microsoft/Dynamics365-Apps-Samples/tree/master/samples-from-msdn/BasicFilteringService) and  [GeneratePickListEnums](https://github.com/microsoft/Dynamics365-Apps-Samples/tree/master/samples-from-msdn/GeneratePicklistEnums). 

The **GeneratePicklistEnums** sample extension outputs a source code file that contains enumerations for all option sets, state codes, and status codes. For an example of how to use these enumerations, see the `SampleCode\CS\QuickStart` sample.  

In addition, it includes a helper code file that contains the enumerations generated for all out-of-the-box values. These enumerations can be used in your code by adding the file `SampleCode\CS\HelperCode\OptionSets.cs` or `SampleCode\VB\HelperCode\OptionSets.vb` to your project.

Each enumeration can be used to test or set the value for a property. Typically this property is a table column (entity attribute) but there are a few that are used for other properties.

### Usage Example

The following example shows how to use one of these enumerations to set a value in an account.

```csharp
// Instantiate an account object. Note the use of the option set enumerations defined
// in OptionSets.cs.
Account account = new Account { Name = "Fourth Coffee" };
account.AccountCategoryCode = new OptionSetValue((int)AccountAccountCategoryCode.PreferredCustomer);
account.CustomerTypeCode = new OptionSetValue((int)AccountCustomerTypeCode.Investor);

// Create an account record named Fourth Coffee.
// Save the record reference so we can delete it during cleanup later.
Guid accountId = service.Create(account);
```

### See Also

 [Generate early-bound classes for the Organization service](generate-early-bound-classes.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
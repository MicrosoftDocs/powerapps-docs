---
title: "Develop IPlugin implementations as stateless | MicrosoftDocs"
description: "Members of classes that implement IPlugin are exposed to potential thread-safety issues, which could lead to data inconsistency or performance problems."
services: ''
suite: powerapps
documentationcenter: na
author: jowells
ms.reviewer: phecke
manager: austinj
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 9/05/2019
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Develop IPlugin implementations as stateless

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

**Category**: Design, Performance

**Potential risk**: High

<a name='symptoms'></a>

## Symptoms

Members of classes that implement the <xref href="Microsoft.Xrm.Sdk.IPlugin?text=IPlugin interface" /> are exposed to potential thread-safety issues which could lead to:

- Data inconsistencies
- Slower plug-in executions

<a name='guidance'></a>

## Guidance

When implementing <xref:Microsoft.Xrm.Sdk.IPlugin>, do not use member fields and properties and write the <xref:Microsoft.Xrm.Sdk.IPlugin.Execute*> method as a stateless operation.  All per invocation state information should be accessed via the execution context only.  

Do not attempt to store any execution state data in member fields or properties for use during the current or next plug-in invocation unless that data was obtained from the configuration parameter provided to the overloaded constructor.

Do not use code that registers to AppDomain events. Plugin logic should not rely on any AppDomain events or properties, since the internal implementation of the plugin infrastructure can change the execution behavior at any point of time. This can cause failures even if the code worked at some point in time.

Read-only, static, and constant members are inherently thread-safe and can also be used reliably within a plug-in class. The following are some examples on how to maintain thread-safe plug-ins:

- Constant field members

    ```csharp
    public class Valid_ClassConstantMember : IPlugin
    {
        public const string validConstantMember = "Plugin registration not valid for {0} message.";

        public void Execute(IServiceProvider serviceProvider)
        {
            var context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));

            if (context.MessageName.ToLower() != "create")
                throw new InvalidPluginExecutionException(String.Format(Valid_ClassConstantMember.validConstantMember, context.MessageName));
        }
    }
    ```

- Storing configuration data assigned or set in plug-in class constructor
    ```csharp
    public class Valid_ClassFieldConfigMember : IPlugin
    {
        private string validConfigField;

        public Valid_ClassFieldConfigMember(string unsecure, string secure)
        {
            this.validConfigField = !String.IsNullOrEmpty(secure)
                ? unsecure
                : secure;
        }

        public void Execute(IServiceProvider serviceProvider)
        {
            if (!String.IsNullOrEmpty(this.validConfigField))
            {
                var message = ValidHelperMethod();
            }
        }

        private string ValidHelperMethod()
        {
            return String.Format("{0} is the config value.", this.validConfigField);
        }
    }
    ```

- Stateless method implementation

    ```csharp
    public class Valid_ClassStatelessMethodMember : IPlugin
    {
        public void Execute(IServiceProvider serviceProvider)
        {
            var context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
    
            if (ValidMemberMethod(context))
            {
                //Then continue with execution
            }
        }
    
        private bool ValidMemberMethod(IPluginExecutionContext context)
        {
            if (context.MessageName.ToLower() == "create")
                return true;
            else
                return false;
        }
    }
    ```

<a name='problem'></a>

## Problematic patterns

> [!WARNING]
> These patterns should be avoided.

- Assigning plug-in class field member during plug-in execution
 
    ```csharp
    public class Violation_ClassAssignFieldMember : IPlugin
    {
        //The instance member used in multiple violation patterns
        internal IOrganizationService service = null;
        internal IPluginExecutionContext context = null;
    
        public void Execute(IServiceProvider serviceProvider)
        {
            this.context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
            var factory = (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    
            //The violation
            this.service = factory.CreateOrganizationService(this.context.UserId);
    
            //Invoke another violation in method member
            AccessViolationProperties();
        }
    
        private void AccessViolationProperties()
        {
            //Accessing the context and service fields exposes this IPlugin implementation to thread-safety issues
            var entity = new Entity("task");
            entity["regardingid"] = new EntityReference(this.context.PrimaryEntityName, this.context.PrimaryEntityId);
    
            var id = this.service.Create(entity);
        }
    }
    ```

- Setting plug-in class property member during plug-in execution

    ```csharp
    public class Violation_ClassAssignPropertyMember : IPlugin
    {
        //The instance member used in multiple violation patterns
        internal IOrganizationService Service { get; set; }
        internal IPluginExecutionContext Context { get; set; }
    
        public void Execute(IServiceProvider serviceProvider)
        {
            this.Context = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
            var factory = (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    
            //The violation
            this.Service = factory.CreateOrganizationService(context.UserId);
    
            //Invoke another violation in method member
            AccessViolationProperties();
        }
    
        private void AccessViolationProperties()
        {
            //Accessing the Context and Service properties exposes this IPlugin implementation to thread-safety issues
            var entity = new Entity("task");
            entity["regardingid"] = new EntityReference(this.Context.PrimaryEntityName, this.Context.PrimaryEntityId);
    
            var id = this.Service.Create(entity);
        }
    }
    ```

<a name='additional'></a>

## Additional information

After Microsoft Dataverse instantiates the plug-in class, the platform caches that plug-in instance for performance reasons. The length of time that a plug-in instance is held in cache is managed by the platform.  Certain operations, such as changing a plug-in's registration properties, will trigger a notification to the platform to refresh the cache.  In these scenarios, the plug-in will be reinitialized.

Because the platform caches plug-in class instances, the constructor is not called for every invocation of plug-in execution.  For this reason, IPlugin implementations should not depend on the timing of operations in the constructor apart from obtaining static configuration data. 

Another reason IPlugins should be stateless is that multiple system threads could execute the same, shared, plug-in instance concurrently.  This opens up members of classes that implement IPlugin to potential thread-safety issues, which could lead to data inconsistency or performance problems.

<a name='seealso'></a>

### See also

[Write a plug-in](../../write-plug-in.md)<br />
[CRM Team Blog: Thread Safety in Plug-ins](https://cloudblogs.microsoft.com/dynamics365/no-audience/2008/11/18/member-static-variable-and-thread-safety-in-plug-in-for-crm-4-0/)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]

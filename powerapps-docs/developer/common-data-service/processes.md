# Processes

<!-- Needs major attention
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/automate-business-processes-customer-engagement
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/process-architecture
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/process-categories
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/workflow-process-entities
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/supported-types-triggers-entities-actions-processes
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/custom-workflow-activities-workflow-assemblies
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/model-business-process-flows
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-work-business-process-flows
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/create-real-time-workflows
https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/create-own-actions -->

## Use custom actions

One of the declarative options available for processes is to create a *custom action*. A custom action is essentially creating a new message in the organization service. You can use custom actions to combine a set of operations into a named reusable operation. For example, you might create a new message called *new_Escalate* that combines a standard set of operations that are involved in notifying the correct people when an important customer is experiencing a serious issue.

When you define a custom action, you choose the signature of the operation by defining input parameters and properties to be included in any result that is returned. Custom actions can then be invoked from a declarative process using the designer or by code. 

The unique value of custom actions is that the specific operations they contain can be modified by someone who is not a developer using the designer without impacting other processes or code that calls it.  This remains true if the signature of the action does not change. If you need different input parameters or output properties, you should create a new, different custom action to avoid breaking any processes or code using an existing one.

When a custom action is defined in an environment, a new OData v4 Action is available using the Web API and within the organization service the custom action can be invoked using the [OrganizationRequest Class](/dotnet/api/microsoft.xrm.sdk.organizationrequest) directly or by using a strongly typed class generated using the *Code Generation tool (CrmSvcUtil.exe)*.

More information: 
- [Common Data Service for Apps Customization Guide: Actions overview](/dynamics365/customer-engagement/customize/actions)
- [Create your own actions](/dynamics365/customer-engagement/developer/create-own-actions)
- [Use Web API actions > Use a custom action](/dynamics365/customer-engagement/developer/webapi/use-web-api-actions#use-a-custom-action)
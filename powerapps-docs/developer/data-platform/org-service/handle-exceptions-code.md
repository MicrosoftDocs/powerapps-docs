---
title: "Handle exceptions in your code (Microsoft Dataverse) | Microsoft Docs"
description: "This article discusses the exceptions that are returned from a Microsoft Dataverse web service method call. The sample in this article highlights the common faults and exceptions that your application design should handle."
ms.custom: intro-internal
ms.date: 06/02/2021
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

# Handle exceptions in your code

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

There are a number of exceptions that can be returned from a Microsoft Dataverse web service method call. Your application design must catch and appropriately handle these exceptions. In the SDK .NET assemblies, all web service method calls use a communication channel to the server based on the Windows communication foundation technology. In WCF terms, exceptions returned from the channel are called *faults*.  

<a name="BKMK_Common"></a>   

## Common exceptions and faults  

The following code is used in most Dataverse Web Services samples. It highlights the common faults and exceptions that your application design should handle.  
  
```csharp
catch (FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault> ex)
{
    Console.WriteLine("The application terminated with an error.");
    Console.WriteLine("Timestamp: {0}", ex.Detail.Timestamp);
    Console.WriteLine("Code: {0}", ex.Detail.ErrorCode);
    Console.WriteLine("Message: {0}", ex.Detail.Message);
    Console.WriteLine("Inner Fault: {0}",
        null == ex.Detail.InnerFault ? "No Inner Fault" : "Has Inner Fault");
}
catch (System.TimeoutException ex)
{
    Console.WriteLine("The application terminated with an error.");
    Console.WriteLine("Message: {0}", ex.Message);
    Console.WriteLine("Stack Trace: {0}", ex.StackTrace);
    Console.WriteLine("Inner Fault: {0}",
        null == ex.InnerException.Message ? "No Inner Fault" : ex.InnerException.Message);
}
catch (System.Exception ex)
{
    Console.WriteLine("The application terminated with an error.");
    Console.WriteLine(ex.Message);

    // Display the details of the inner exception.
    if (ex.InnerException != null)
    {
        Console.WriteLine(ex.InnerException.Message);

        FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault> fe = ex.InnerException
            as FaultException<Microsoft.Xrm.Sdk.OrganizationServiceFault>;
        if (fe != null)
        {
            Console.WriteLine("Timestamp: {0}", fe.Detail.Timestamp);
            Console.WriteLine("Code: {0}", fe.Detail.ErrorCode);
            Console.WriteLine("Message: {0}", fe.Detail.Message);
            Console.WriteLine("Trace: {0}", fe.Detail.TraceText);
            Console.WriteLine("Inner Fault: {0}",
                null == fe.Detail.InnerFault ? "No Inner Fault" : "Has Inner Fault");
        }
    }
}
```
  
> [!NOTE]
> If you’re accessing the Discovery web service, your code should catch <xref:Microsoft.Xrm.Sdk.DiscoveryServiceFault> instead of the <xref:Microsoft.Xrm.Sdk.OrganizationServiceFault> fault shown previously.  
  
In addition to these exceptions and faults, your code must handle the following exceptions:  
  
- [SecurityTokenValidationException](/dotnet/api/system.identitymodel.tokens.securitytokenvalidationexception)  
- [ExpiredSecurityTokenException](/dotnet/api/system.servicemodel.security.expiredsecuritytokenexception)  
- [SecurityAccessDeniedException](/dotnet/api/system.servicemodel.security.securityaccessdeniedexception)  
- [MessageSecurityException](/dotnet/api/system.servicemodel.security.messagesecurityexception)  
- [SecurityNegotiationException](/dotnet/api/system.servicemodel.security.securitynegotiationexception)  
  
When connecting to Dataverse, a `SecurityAccessDeniedException` exception can be thrown if you use a valid Microsoft account and your account is not associated with any Dataverse organization. A `MessageSecurityException` can be thrown if your Microsoft account isn’t valid or there was an authentication failure.  
  
<a name="BKMK_BusinessRuleErrors"></a>

## Custom errors from business rules
 
With Dataverse, customizers can create business rules that are evaluated on the server. Customizers can throw error messages based on conditions set in the business rule. Developers should be sure to include robust error handling in their code to catch and handle these exceptions.  
  
The following is an example of the trace log produced when one of these errors is returned from a business rule named **Name of Entity Scope Business Rule returning Error** and the error message is **custom error message**.  
  
```csharp
Unhandled Exception: System.ServiceModel.FaultException`1[[Microsoft.Xrm.Sdk.OrganizationServiceFault, Microsoft.Xrm.Sdk, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]]: custom error messageDetail:   
<OrganizationServiceFault xmlns:i="https://www.w3.org/2001/XMLSchema-instance" xmlns="https://schemas.microsoft.com/xrm/2011/Contracts">  
  <ErrorCode>-2147220891</ErrorCode>  
  <ErrorDetails xmlns:d2p1="https://schemas.datacontract.org/2004/07/System.Collections.Generic">  
    <KeyValuePairOfstringanyType>  
      <d2p1:key>OperationStatus</d2p1:key>  
      <d2p1:value xmlns:d4p1="https://www.w3.org/2001/XMLSchema" i:type="d4p1:string">0</d2p1:value>  
    </KeyValuePairOfstringanyType>  
    <KeyValuePairOfstringanyType>  
      <d2p1:key>SubErrorCode</d2p1:key>  
      <d2p1:value xmlns:d4p1="https://www.w3.org/2001/XMLSchema" i:type="d4p1:string">-2146233088</d2p1:value>  
    </KeyValuePairOfstringanyType>  
  </ErrorDetails>  
  <Message>custom error message</Message>  
  <Timestamp>2014-09-04T17:43:16.8197965Z</Timestamp>  
  <InnerFault i:nil="true" />  
  <TraceText>  
  
[Microsoft.Crm.ObjectModel: Microsoft.Crm.ObjectModel.SyncWorkflowExecutionPlugin]  
[cf6a25a9-5a34-e411-80b9-00155dd8c20f: ]  
Starting sync workflow 'Name of Entity Scope Business Rule returning Error', Id: c76a25a9-5a34-e411-80b9-00155dd8c20f  
Entering ConditionStep1_step:   
Entering SetMessage_step:   
Sync workflow 'Name of Entity Scope Business Rule returning Error' terminated with error 'custom error message'  
  
</TraceText>  
</OrganizationServiceFault>  
```  
  
More information: [Create a business rule for a table](../../../maker/data-platform/data-platform-create-business-rule.md)  
  
<a name="BKMK_AdditionalInfo"></a>

## Additional information about exceptions

When an uncaught exception is thrown that contains sensitive information that the user doesn’t have permission to see, the sensitive information in the exception is hidden from the user and a reference number is provided. This reference number refers to the related server event log entry and server trace entry. A system administrator can look up those entries and find more information about the exception.  
  
### See also  

 [Web service error codes](web-service-error-codes.md)   
 [Handle exceptions in plug-ins](../handle-exceptions.md)   
 [.NET Framework Developer Center](/dotnet/framework/development-guide)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
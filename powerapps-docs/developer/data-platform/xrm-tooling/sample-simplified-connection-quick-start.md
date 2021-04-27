---
title: "Sample: Simplified connection quick start (Developer Guide for Microsoft Dataverse) | MicrosoftDocs"
description: "This sample shows you how to connect to the Microsoft Dataverse web services using the CrmServiceClient and perform basic create, update, retrieve, and delete operations on a table. "
ms.custom: 
ms.date: 04/12/2021
author: Nkrb
ms.service: powerapps
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: samples
applies_to: 
  - Microsoft Dataverse (online)
ms.assetid: a4fb3634-948e-4bac-a32f-f626c78d83a0
caps.latest.revision: 29
ms.author: nabuthuk
manager: kvivek
search.audienceType: 
  - developer
search.app: 
  - D365CE
  - PowerApps
---
# Sample: Simplified connection quick start using Microsoft Dataverse

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This sample shows how to connect to the Dataverse web services using the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> and perform basic create, update, retrieve, and delete operations on a table. For more information about the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>, see [Use CrmServiceClient constructors to connect to Dataverse](use-crmserviceclient-constructors-connect.md).

## Requirements

The complete sample code can be found here [Sample: Quick start for Dataverse](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/Xrm%20Tooling/QuickStartCS) 

You must modify the `app.config` file with connection information for your Dataverse instance before running the sample. 

## Demonstrates

This sample authenticates the user with the Dataverse web services by using the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> and methods. After obtaining a reference to the Organization web service, the sample performs basic create, update, retrieve, and delete operations on an `account` table. The sample also handles common exceptions. No helper code is used to establish a connection to the Organization web service.  

In addition, this sample supports `OAuth` authentication and advanced connection diagnostics. For more information on using diagnostics, see [Configure tracing for XRM Tooling](configure-tracing-xrm-tooling.md).

## Example

The following shows a sample `app.config file`. To use this, remove the comment characters “<!- -” at the beginning of the \<add … /> line and the “- ->” at the end on the line for the line that is relevant to your server and organization. Next, modify the data values as appropriate for your configuration.

```xml
<?xml version="1.0" encoding="utf-8"?>  
<configuration>  
  <connectionStrings>  
    <!-- Online using Microsoft 365 -->  
    <!-- <add name="Server=CRM Online, organization=contoso, user=someone"  
         connectionString="Url=https://contoso.crm.dynamics.com; Username=someone@contoso.onmicrosoft.com; Password=password; authtype=Office365"/> -->  
  </connectionStrings>  
  <startup>  
    <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.6.2" />  
  </startup>  
<system.diagnostics>  
    <trace autoflush="true"/>  
    <sources>  
      <source name="Microsoft.Xrm.Tooling.Connector.CrmServiceClient" switchName="Microsoft.Xrm.Tooling.Connector.CrmServiceClient" switchType="System.Diagnostics.SourceSwitch">  
        <listeners>  
          <add name="console" type="System.Diagnostics.ConsoleTraceListener"/>  
          <add name="fileListener"/>  
        </listeners>  
      </source>  
      <source name="Microsoft.Xrm.Tooling.CrmConnectControl" switchName="Microsoft.Xrm.Tooling.CrmConnectControl" switchType="System.Diagnostics.SourceSwitch">  
        <listeners>  
          <add name="console" type="System.Diagnostics.ConsoleTraceListener"/>  
          <add name="fileListener"/>  
        </listeners>  
      </source>  
      <source name="CrmSvcUtil" switchName="CrmSvcUtil" switchType="System.Diagnostics.SourceSwitch">  
        <listeners>  
          <add name="console" type="System.Diagnostics.ConsoleTraceListener"/>  
          <add name="fileListener"/>  
        </listeners>  
      </source>  
    </sources>  
    <switches>  

      <!--Possible values for switches: Off, Error, Warning, Information, Verbose  
                        Verbose:      includes Error, Warning, Info, Trace levels  
                        Information:  includes Error, Warning, Info levels  
                        Warning:      includes Error, Warning levels  
                        Error:        includes Error level-->  

      <add name="Microsoft.Xrm.Tooling.CrmConnectControl" value="Off"/>  
      <add name="Microsoft.Xrm.Tooling.Connector.CrmServiceClient" value="Error"/>  
      <add name="CrmSvcUtil" value="Off"/>  
    </switches>  

    <sharedListeners>  
      <add name="fileListener" type="System.Diagnostics.TextWriterTraceListener" initializeData="CrmSvcUtil.log"/>  
    </sharedListeners>  

  </system.diagnostics>  
  <runtime>  
    <assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">  
      <dependentAssembly>  
        <assemblyIdentity name="Microsoft.Xrm.Sdk" publicKeyToken="31bf3856ad364e35" culture="neutral" />  
        <bindingRedirect oldVersion="0.0.0.0-7.0.0.0" newVersion="8.0.0.0" />  
      </dependentAssembly>  
      <dependentAssembly>  
        <assemblyIdentity name="Microsoft.Xrm.Sdk.Deployment" publicKeyToken="31bf3856ad364e35" culture="neutral" />  
        <bindingRedirect oldVersion="0.0.0.0-7.0.0.0" newVersion="8.0.0.0" />  
      </dependentAssembly>  
      <dependentAssembly>  
        <assemblyIdentity name="Microsoft.ServiceBus" publicKeyToken="31bf3856ad364e35" culture="neutral" />  
        <bindingRedirect oldVersion="0.0.0.0-2.4.0.0" newVersion="2.4.0.0" />  
      </dependentAssembly>  
    </assemblyBinding>  
  </runtime>  
</configuration>  
```

## Another Example

```csharp
using Microsoft.Crm.Sdk.Messages;
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Query;
using Microsoft.Xrm.Tooling.Connector;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PowerApps.Samples
{
   public partial class SampleProgram
    {
        [STAThread] // Added to support UX
        static void Main(string[] args)
        {
            CrmServiceClient service = null;

            try
            {
                service = SampleHelpers.Connect("Connect");
                if (service.IsReady)
                {
                    #region Sample Code
                    ////////////////////////////////////
                    #region Set up
                    SetUpSample(service);
                    #endregion Set up
                    #region Demonstrate
                    // Obtain information about the logged on user from the web service.
                    Guid userid = ((WhoAmIResponse)service.Execute(new WhoAmIRequest())).UserId;
                    SystemUser systemUser = (SystemUser)service.Retrieve("systemuser", userid,
                        new ColumnSet(new string[] { "firstname", "lastname" }));
                    Console.WriteLine("Logged on user is {0} {1}.", systemUser.FirstName, systemUser.LastName);

                    // Retrieve the version of Microsoft Dynamics CRM.
                    RetrieveVersionRequest versionRequest = new RetrieveVersionRequest();
                    RetrieveVersionResponse versionResponse =
                        (RetrieveVersionResponse)service.Execute(versionRequest);
                    Console.WriteLine("Microsoft Dynamics CRM version {0}.", versionResponse.Version);

                    // Instantiate an account object. Note the use of option set enumerations defined in OptionSets.cs.
                    // Refer to the Entity Metadata topic in the SDK documentation to determine which attributes must
                    // be set for each entity.
                    Account account = new Account { Name = "Fourth Coffee" };
                    account.AccountCategoryCode = new OptionSetValue((int)AccountAccountCategoryCode.PreferredCustomer);
                    account.CustomerTypeCode = new OptionSetValue((int)AccountCustomerTypeCode.Investor);

                    // Create an account record named Fourth Coffee.
                    _accountId = service.Create(account);

                    Console.Write("{0} {1} created, ", account.LogicalName, account.Name);

                    // Retrieve the several attributes from the new account.
                    ColumnSet cols = new ColumnSet(
                        new String[] { "name", "address1_postalcode", "lastusedincampaign" });

                    Account retrievedAccount = (Account)service.Retrieve("account", _accountId, cols);
                    Console.Write("retrieved, ");

                    // Update the postal code attribute.
                    retrievedAccount.Address1_PostalCode = "98052";

                    // The address 2 postal code was set accidentally, so set it to null.
                    retrievedAccount.Address2_PostalCode = null;

                    // Shows use of a Money value.
                    retrievedAccount.Revenue = new Money(5000000);

                    // Shows use of a Boolean value.
                    retrievedAccount.CreditOnHold = false;

                    // Update the account record.
                    service.Update(retrievedAccount);
                    Console.WriteLine("and updated.");

                #region Clean up
                CleanUpSample(service);
                    #endregion Clean up
                }
                #endregion Demonstrate
                #endregion Sample Code
                else
                {
                    const string UNABLE_TO_LOGIN_ERROR = "Unable to Login to Dynamics CRM";
                    if (service.LastCrmError.Equals(UNABLE_TO_LOGIN_ERROR))
                    {
                        Console.WriteLine("Check the connection string values in cds/App.config.");
                        throw new Exception(service.LastCrmError);
                    }
                    else
                    {
                        throw service.LastCrmException;
                    }
                }
            }
            catch (Exception ex)
            {
                SampleHelpers.HandleException(ex);
            }

            finally
            {
                if (service != null)
                    service.Dispose();

                Console.WriteLine("Press <Enter> to exit.");
                Console.ReadLine();
            }
        }
            }
}

```

### See also

[Use connection strings in XRM tooling to connect to Dataverse](use-connection-strings-xrm-tooling-connect.md)<br />
[Sample: Quick start for XRM Tooling API](sample-quick-start-xrm-tooling-api.md)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
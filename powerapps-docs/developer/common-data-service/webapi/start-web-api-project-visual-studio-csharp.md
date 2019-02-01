---
title: "Enhanced quick Start(Common Data Service for Apps)| Microsoft Docs"
description: "Create a new project in Visual Studio to build a console application that uses Common Data Service for Apps Web API"
ms.custom: ""
ms.date: 1/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 08377156-32c7-492a-8e66-50a47a330dc6
caps.latest.revision: 14
author: "brandonsimons" # GitHub ID
ms.author: "jdaly"
manager: ""
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Enhanced quick start

This topic demonstrates how to re-factor the code in [Quick start](quick-start-console-app-csharp.md) topic by adding re-usable [HttpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) and error handling methods. Complete the steps in the [Quick start](quick-start-console-app-csharp.md) topic to create a new Visual Studio project before you start enhancing the code.

<a name="bkmk_addAllRequiredResources"></a>

## Add all required resources to your project

The following process explains how to add all the required managed references and additional class files to your project. Consider this as a base set of resources that most managed code applications will need for invoking Web API operations.  
  
### Edit the application configuration file

In **Solution Explorer**, open the **App.config** file for editing. Add the following and then save the file.  You need to pass the CDS for Apps url and user credentials in the `App.config` file to connect to the CDS for Apps instance.

```xml  
  
<?xml version="1.0" encoding="utf-8"?>
<configuration>
<connectionStrings>
  <!--Online using Office 365-->
  <add name="Connect" connectionString="Url=https://yourorgname.crm.dynamics.com;Username=yourname@yourorg.onmicrosoft.com;Password=pasword;authtype=Office365; RequireNewInstance=True"/>
</connectionStrings>
<system.diagnostics>
<trace autoflush="true" />
<sources>
   <source name="Microsoft.Xrm.Tooling.Connector.CrmServiceClient" switchName="Microsoft.Xrm.Tooling.Connector.CrmServiceClient" switchType="System.Diagnostics.SourceSwitch">
   <listeners>
      <add name="console" type="System.Diagnostics.ConsoleTraceListener" />
	  <add name="fileListener" />
   </listeners>
</source>
<source name="Microsoft.Xrm.Tooling.CrmConnectControl" switchName="Microsoft.Xrm.Tooling.CrmConnectControl" switchType="System.Diagnostics.SourceSwitch">
   <listeners>
      <add name="console" type="System.Diagnostics.ConsoleTraceListener" />
	  <add name="fileListener" />
   </listeners>
</source>
</sources>
<switches>
 <add name="Microsoft.Xrm.Tooling.Connector.CrmServiceClient" value="Error" />
 <add name="Microsoft.Xrm.Tooling.CrmConnectControl" value="Error" />
 <add name="Microsoft.IdentityModel.Clients.ActiveDirectory" value="Error" />
</switches>
<sharedListeners>
    <add name="fileListener" type="Microsoft.Xrm.Tooling.Connector.DynamicsFileLogTraceListener, Microsoft.Xrm.Tooling.Connector" />
	<add name="fileListener" type="Microsoft.Xrm.Tooling.Connector.DynamicsFileLogTraceListener, Microsoft.Xrm.Tooling.Connector" BaseFileName="PowerApps-Sample-Log" Location="LocalUserApplicationDirectory" MaxFileSize="52428800" />
</sharedListeners>
</system.diagnostics>
<startup>
<supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.6.1" />
</startup>
<runtime>
<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
  <dependentAssembly>
    <assemblyIdentity name="Microsoft.Xrm.Sdk" publicKeyToken="31bf3856ad364e35" culture="neutral" />
	<bindingRedirect oldVersion="0.0.0.0-9.0.0.0" newVersion="9.0.0.0" />
  </dependentAssembly>
<dependentAssembly>
    <assemblyIdentity name="Microsoft.Xrm.Sdk.Workflow" publicKeyToken="31bf3856ad364e35" culture="neutral" />
	<bindingRedirect oldVersion="0.0.0.0-9.0.0.0" newVersion="9.0.0.0" />
</dependentAssembly>
    <dependentAssembly>
	    <assemblyIdentity name="Microsoft.Xrm.Tooling.Connector" publicKeyToken="31bf3856ad364e35" culture="neutral" />
		<bindingRedirect oldVersion="0.0.0.0-3.0.0.0" newVersion="3.0.0.0" />
    </dependentAssembly>
<dependentAssembly>
     <assemblyIdentity name="Microsoft.Crm.Sdk.Proxy" publicKeyToken="31bf3856ad364e35" culture="neutral" />
	 <bindingRedirect oldVersion="0.0.0.0-9.0.0.0" newVersion="9.0.0.0" />
</dependentAssembly>
</assemblyBinding>
</runtime>
</configuration

```
  
<a name="bkmk_addCodeToCallHelperLibrary"></a>

### Add the helper code

Next step in the process is to add a new helper class file to the project and copy paste the [SampleHelper](https://github.com/Microsoft/PowerApps-Samples/blob/master/cds/webapi/C%23/SampleHelpers.cs) code.

The [Web API samples (C#)](https://github.com/Microsoft/PowerApps-Samples/blob/master/cds/webapi/C%23) uses the `SampleHelper` file which contains methods to assist with supplemental operations, such as application configuration, Common Data Service for Apps server authentication, exception handling, web communication and `OAuthMessageHandler` class which manages the renewal of the tokens. This file is shared with all the Web API (C#) samples.

Because the Common Data Service for Apps Web API is based on REST principles, it does not require client-side assemblies to access.

#### Add code to call the helper library
  
1. Add a new class file to the project and name it as `SampleMethod`. Add the following helper methods to it. The `SampleMethod` class file is added to show a pattern to encapsulate method calls into re-usable methods to be used in `Program.cs`. This class file is shared commonly with all the [Web API sample (C#)](https://github.com/Microsoft/PowerApps-Samples/blob/master/cds/webapi/C%23). 

```csharp
using Newtonsoft.Json.Linq;
using System;
using System.Net.Http;

namespace PowerApps.Samples
{
  public partial class SampleProgram
   {
	 public static WhoAmIResponse WhoAmI(HttpClient client)
	  {
		WhoAmIResponse returnValue = new WhoAmIResponse();

         //Send the WhoAmI request to the Web API using a GET request. 
HttpResponseMessage response = client.GetAsync("WhoAmI"HttpCompletionOption.ResponseHeadersRead).Result;

if (response.IsSuccessStatusCode)
 {
	//Get the response content and parse it.
	JObject body = JObject.Parse(response.Content.ReadAsStringAsync().Result);
	returnValue.BusinessUnitId = (Guid)body["BusinessUnitId"];
	returnValue.UserId = (Guid)body["UserId"];
	returnValue.OrganizationId = (Guid)body["OrganizationId"];
		}

 else
   {
       throw new Exception(string.Format("The WhoAmI request failed with a status of '{0}'",
        response.ReasonPhrase));
       }
          return returnValue;

        }

    }

public class WhoAmIResponse
 {
   public Guid BusinessUnitId { get; set; } 
   public Guid UserId { get; set; }
   public Guid OrganizationId { get; set; }

    }
```

2. Now go to `Program.cs` file, add the following code.  
  
```csharp

using Newtonsoft.Json.Linq;
using System;
using System.Configuration;
using System.Net.Http;

namespace PowerApps.Samples 
{
public partial class SampleProgram
{ 
static void Main(string[] args)
  {
     try
      {
 //Get configuration data from App.config connectionStrings
string connectionString = ConfigurationManager.ConnectionStrings["Connect"].ConnectionString;
 
using (HttpClient client = SampleHelpers.GetHttpClient(connectionString, SampleHelpers.clientId, SampleHelpers.redirectUrl, "v9.0"))
 {
    WhoAmIResponse response = WhoAmI(client);
         Console.WriteLine("Your system user ID is: {0}", response.UserId);
      }

 else
  {
      Console.WriteLine("The request failed with a status of '{0}'",response.ReasonPhrase);

        } 
}

 }

catch (Exception ex)
   {
     SampleHelpers.DisplayException(ex);
     throw;
   }

finally
  {
	Console.WriteLine("Press <Enter> to exit the program.");
	Console.ReadLine();

  }
}
}
}
```

3. Save all the files in the solution.
  
<a name="bkmk_nextSteps"></a>

### Next steps

 At this point the solution can be built without errors. The solution represents a skeletal frame that is ready to accept custom code, including calls to the Common Data Service for Apps Web API.  
  
> [!TIP]
> Before you leave this topic, consider saving your project as a project template. You can then reuse that template for future learning projects and save yourself some time and effort in setting up new projects. To do this, while your project is open in Microsoft Visual Studio, in the **File** menu select **Export template**. Follow the [Export Template Wizard](https://docs.microsoft.com/en-us/visualstudio/ide/how-to-create-project-templates) instructions to create the template.  
  
### See also

[Web API samples (C#)](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23)<br/>
[Perform operations using the Web API](perform-operations-web-api.md)

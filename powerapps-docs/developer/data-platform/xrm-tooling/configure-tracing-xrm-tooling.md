---
title: "Configure tracing for XRM tooling (Microsoft Dataverse)| Microsoft Docs"
description: "Learn how you can configure tracing for components such as operation calls, warnings, exceptions, and other significant events in XRM Tooling"
ms.custom: ""
ms.date: 03/27/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: d7586a5a-40da-427e-bbeb-4f8a371a8dcf
caps.latest.revision: 8
author: "MattB-msft"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Configure tracing for XRM tooling

You can enable tracing to record data related to process milestones across all components of XRM tooling, such as operation calls, warnings, exceptions, and other significant events. This information can be used for troubleshooting operational and performance issues in your Windows client applications. Tracing in XRM tooling is built on top of [System.Diagnostics.Tracing](/dotnet/api/system.diagnostics.tracing). To enable tracing for an assembly or component, for example Microsoft.Xrm.Tooling.Connector, you must define the following three things for each component in your code or in the application configuration file (*\<AppName>*.exe.config):  
  
- A trace source  
- A trace listener  
- A trace level other than **Off**. These are the other values that you can specify: **Error**, **Warning**, **Info**, and **Verbose**.  
Here is the configuration for enabling tracing for a component in XRM tooling. For example, the following configuration only enables tracing for the Microsoft.Xrm.Tooling.CrmConnectControl component:  
  
```xml  
</configuration>  
  <system.diagnostics>  
    <trace autoflush="true" />  
    <sources>  
      <source name="DynamicsCrm.CrmConnectControl"  
        switchName="DynamicsCrm.CrmConnectControl"  
        switchType="System.Diagnostics.SourceSwitch">  
        <listeners>  
          <add name="console" type="System.Diagnostics.DefaultTraceListener" />  
          <remove name="Default"/>  
          <add name ="fileListener"/>  
        </listeners>  
      </source>  
    </sources>  
    <switches>  
      <!--   
            Possible values for switches: Off, Error, Warning, Info, Verbose  
                Verbose:    includes Error, Warning, Info, Trace levels  
                Info:       includes Error, Warning, Info levels  
                Warning:    includes Error, Warning levels  
                Error:      includes Error level  
        -->  
      <add name="DynamicsCrm.CrmConnectControl" value="Verbose"/>  
    </switches>  
    <sharedListeners>  
      <add name="fileListener" type="System.Diagnostics.TextWriterTraceListener" initializeData="XRMLoginControl.log"/>  
      <add name="eventLogListener" type="System.Diagnostics.EventLogTraceListener" initializeData="XRMLogin"/>  
    </sharedListeners>  
  </system.diagnostics>  
</configuration>  
```  
  
If you want to enable tracing for all of the components in XRM tooling, you can do that as well. Here is the configuration for a combined tracing of all three of the components in XRM tooling:  
  
```xml  
<configuration>  
  <system.diagnostics>  
    <trace autoflush="true" />  
    <sources>  
      <source name="Microsoft.Xrm.Tooling.Connector.CrmServiceClient"  
              switchName="Microsoft.Xrm.Tooling.Connector.CrmServiceClient"  
              switchType="System.Diagnostics.SourceSwitch">  
        <listeners>  
          <add name="console" type="System.Diagnostics.DefaultTraceListener" />  
          <remove name="Default"/>  
          <add name ="fileListener"/>  
        </listeners>  
      </source>  
  
      <source name="Microsoft.Xrm.Tooling.CrmConnectControl"  
              switchName="Microsoft.Xrm.Tooling.CrmConnectControl"  
              switchType="System.Diagnostics.SourceSwitch">  
        <listeners>  
          <add name="console" type="System.Diagnostics.DefaultTraceListener" />  
          <remove name="Default"/>  
          <add name ="fileListener"/>  
        </listeners>  
      </source>  
  
      <source name="Microsoft.Xrm.Tooling.WebResourceUtility"  
        switchName="Microsoft.Xrm.Tooling.WebResourceUtility"  
        switchType="System.Diagnostics.SourceSwitch">  
        <listeners>  
          <add name="console" type="System.Diagnostics.DefaultTraceListener" />  
          <remove name="Default"/>  
          <add name ="fileListener"/>  
        </listeners>  
      </source>  
    </sources>  
    <switches>  
      <!--   
            Possible values for switches: Off, Error, Warning, Info, Verbose  
                Verbose:    includes Error, Warning, Info, Trace levels  
                Info:       includes Error, Warning, Info levels  
                Warning:    includes Error, Warning levels  
                Error:      includes Error level  
        -->  
      <add name="Microsoft.Xrm.Tooling.Connector.CrmServiceClient" value="Verbose" />  
      <add name="Microsoft.Xrm.Tooling.CrmConnectControl" value="Verbose"/>  
      <add name="Microsoft.Xrm.Tooling.WebResourceUtility" value="Verbose" />  
  
    </switches>  
    <sharedListeners>  
      <add name="fileListener" type="System.Diagnostics.TextWriterTraceListener" initializeData="XRMToolingLogs.log"/>        
      <add name="eventLogListener" type="System.Diagnostics.EventLogTraceListener" initializeData="XRMTooling" />  
    </sharedListeners>  
  
  </system.diagnostics>  
</configuration>  
```  
  
### See also

[Build Windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
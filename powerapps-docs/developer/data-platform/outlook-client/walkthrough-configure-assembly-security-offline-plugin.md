---
title: "Walkthrough: Configure assembly security for an offline plug-in (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The topic provides a walkthrough on configuring assembly security for an offline plug-in." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "sriharibs-msft" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Walkthrough: Configure assembly security for an offline plug-in

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

The Microsoft Dataverse platform applies an additional security restriction to registered offline plug-in assemblies. When Dynamics 365 for Microsoft Office Outlook with Offline Access is installed, an AllowList key is added to the system registry on the client computer. For each assembly containing an offline plug-in that you register, you must add a registry sub-key under the AllowList key with the key name derived from the assembly's public key token. Failure to add this key results in the offline plug-in not being executed by the platform even though the plug-in is registered. This walkthrough describes how to add this sub-key for a plug-in assembly.  
  
### Get the public key token  
  
1.  Load the assembly containing the offline plug-in into the Plug-in Registration tool. For more information about how to use the tool, see [Register a plug-in](../register-plug-in.md).  
  
2.  Select the plug-in assembly in the tree view of the tool.  
  
3.  Copy (Ctrl+C) the value in the **Public Key Token** field into the paste buffer.  
  
### Add an AllowList key  
  
1.  Run the registry editor by selecting **Start**, then select **Run** and type `regedit.exe`.  
  
2.  In the tree view pane, navigate to the **AllowList** key. The complete path of the key is `HKEY_CURRENT_USER\Software\Microsoft\MSCRMClient\AllowList`.  
  
3.  Select the **AllowList** key and right click to display the context menu.  
  
4.  Select **New** then click **Key** to create a new sub-key.  
  
5.  Paste the public key token value into the name of the new sub-key.  
  
6.  Close the registry editor.  
  
### See also  
 [Plug-in Development](/dynamics365/customer-engagement/developer/plugin-development)   
 [Sample: Create a basic plug-in](../org-service/samples/basic-followup-plugin.md)   
 [Register and Deploy Plug-ins](/dynamics365/customer-engagement/developer/register-deploy-plugins)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
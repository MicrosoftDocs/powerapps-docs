---
title: "Walkthrough: Register an Azure-aware plug-in using the Plug-in Registration Tool (Common Data Service for Apps) | Microsoft Docs"
description: "The walkthrough demonstrates how to register a service endpoint step using the Plug-in Registration Tool. "
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: b5ef50fa-8085-f425-3968-804d012fc840
author: brandonsimons" # GitHub ID
ms.author: jdaly" # MSFT alias of Microsoft employees only
manager: ryjones" # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Tutorial: Register an Azure-aware plug-in using the Plug-in Registration Tool

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/walkthrough-register-azure-aware-plug-in-using-plug-in-registration-tool -->

This walkthrough demonstrates how to register a service endpoint step using the Plug-in Registration Tool. Once configured, Dynamics 365 (online) Common Data Service for Apps can post the execution context of the current operation to a Azure solution endpoint. For this walkthrough, the step is registered to post the execution context of the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> message for an `Account` entity to the Azure Service Bus.  
  
 The following prerequisites must be completed before you start this walkthrough:  
  
-   Access to the Plug-in Registration Tool. [!INCLUDE[proc-download-plugin-registration-tool](../../includes/proc-download-plugin-registration-tool.md)]
  
-   Your Dynamics 365 system user account must have the System Customizer or System Administrator role. For more information, see [How Role-Based Security Can Be Used to Control Access to Entities In Dynamics 365](security-dev/how-role-based-security-control-access-entities.md).<!-- topic not found-->
  
-   Have access to a Azure platform service namespace that is configured for SAS authorization, to which Dynamics 365 will post a message.  
  
  
-   If you plan to use any other Azure messaging entity other than a queue, for example a relay, there must be a listener application actively listening to the specified solution endpoint for Dynamics 365 to successfully post to the Azure Service Bus. For more information, see [Write a Listener for an Azure Solution](write-listener-application-azure-solution.md).  
  
-   A configured service endpoint with SAS authorization is available in the target organization. More information: [Walkthrough: Configure Microsoft Azure (SAS) for integration with Dynamics 365](walkthrough-configure-azure-sas-integration.md).  
  
## Steps  
 This walkthrough contains the following steps:  
  
1.  [Connect to the Dynamics 365 server](#BKMK_Connect)  
  
2.  [Register a service endpoint step for an event](#BKMK_Register)  
  
3.  [Test the endpoint registration](#BKMK_Test)  
  
<a name="BKMK_Connect"></a>   
## Connect to the Dynamics 365 server  
 Follow the steps below to connect to the Dynamics 365 server using the Plug-in Registration tool.  
  
1.  Run the Plug-in Registration tool.  
  
2.  Click **Create New Connection**.  
  
3.  In the **Login** dialog box, select the deployment type radio button corresponding to the Dynamics 365 server you intend to register a service endpoint with. The **On-premises** radio button includes an IFD deployment and the **Office 365** button is for the Microsoft Online Services provider of Dynamics 365 (online).  
  
    |||  
    |-|-|  
    |![Login form for an online deployment](media/crm-v6s-pr.png "Login form for an online deployment")<br />Login form for an online deployment|![Login window for an on&#45;premises deployment](media/crm-v6s-pr-login-onprem.png "Login window for an on-premises deployment")<br />Login form for an on-premises deployment|  
  
4.  If you check **Display list of available organizations**, you are presented with a list of organizations that you belong to after you click **Login**. This enables you to choose the organization that you want to register the service endpoint with. Otherwise, your default organization is used.  
  
5.  Enter the indicated information about the server and login account, and then click **Login**.  
  
<a name="BKMK_Register"></a>   
## Register a service endpoint step for an event  
 Follow the steps below to register a step for an event on the service endpoint.  
  
1.  Select an existing service endpoint in the tab of the tab of the target organization.  
  
2.  Navigate to the **Register** menu and click **Register New Step**.  
  
3.  Fill out the **Register New Step** dialog box for an account create event as shown in the following figure.  
  <!-- To-Do: Image is not present and need to fix it-->

 ![Creating a service endpoint step](media/crm-v6s-pr-service-endpoint-step.png "Creating a service endpoint step")
  
4.  Click **Register New Step**.  
  
 Dynamics 365 will now post the current message containing the execution context to the service bus whenever an account is created. The post is performed asynchronously and is not executed immediately.  
  
<a name="BKMK_Test"></a>   
## Test the endpoint registration  
 After you register the endpoint you can test it. A listener must be running or a queue available on the target endpoint for the service bus post from the plug-in to happen.  
  
1.  Open the Dynamics 365 web application for the same organization that you registered the service endpoint under.  
  
2.  Click the **Create** button ![Create button](media/crm-v6s-wa-create-icon.PNG "Create button"), and then click **Account**.  
  
3.  Enter an account name, for example `Adventure Works Cycle`, into the **Account Name** field, and then click **Save**.  
  
4.  Wait about 10 minutes for the Azure Service Bus post to occur.  
  
5.  Click **Settings > System Jobs**.  
  
6.  Open the system job that has the same name that you specified for your service endpoint. Check the status to see if the post was successful, is waiting, or failed.  
  
 You can now unregister the endpoint, if so desired, by selecting it in the tool’s tree view and click **Unregister**.  
  
### See also  
 [Azure Extensions for Dynamics 365](azure-extensions.md) <!-- To-Do: The file is not found to fix the link-->
 
 [Introduction to Microsoft Azure Integration with Dynamics 365](azure-integration.md)
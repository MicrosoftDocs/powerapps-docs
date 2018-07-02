---
title: "Get started with model-driven app making in PowerApps | MicrosoftDocs"
description: "Learn how you can get started building and customizing model-driven apps"
ms.custom: ""
ms.date: 06/18/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: d6bd269e-0000-44e9-b686-a6240a101ec7
caps.latest.revision: 14
ms.author: "matp"
manager: "kvivek"
---
# Get started with app making and customization

You can tailor a model-driven app to more closely fit your organization’s industry, nomenclature, and unique business processes. You can implement many customizations without writing any code.  
  
 The following table shows some examples of customizations:  
  
|Customization|Definition|Reason for the customization|  
|-------------------|----------------|----------------------------------|  
|Entity|An item with properties that you track, such as a contact or account. For an entity you might track properties such as *company name*, *location*, *products*, *email*, and *phone*.|Create or modify the name or properties of an entity that your organization wants to track.|
|Field|A property of an entity, such as *company name*.|Define entity properties that you want to track.|  
|Form|A set of data-entry fields for a given entity that matches the items that your organization tracks for the entity, for example, a set of data-entry fields that track a customer’s previous orders along with specific requested reorder dates.|Create a new form based on an existing form, and then customize the form to suit your organization’s needs.|
|Business process flow|An online process that walks users through a standard business process.|Standardize your business processes with the same stages and steps for each type of customer interaction. Business processes help everyone follow best practices.
|Dashboard|Provides an overview of actionable business data|Create a dashboard that provides lists and charts that shows a team's performance at a glance.
|Interface|The buttons, labels, and controls of the user interface.|If the users in your organization find the term *Commit* more familiar than the term *Go*, for example, you can change all the **Go** buttons to be **Commit** buttons.|
|Workflow|A set of rules that run on demand or are triggered to run automatically.|Create or modify workflows to run in accordance with the way your organization works. For example, a custom workflow could automatically send an email notification to an account owner when a specific condition or combination of conditions is reached.|  

<a name="BKMK_PublishingCustomizations"></a>   
## Publishing customizations  
 Certain customizations that make changes to the user interface require that they be published before people can use them in the application. Publishing provides a way for you to save your work before you have finished and then come back and finish at a later time. Publishing is only required when you change a solution component. When you create or delete a solution component, publishing occurs automatically. Before you export a solution, you’ll be prompted to publish customizations. This is because any unpublished customizations won’t be included in the solution.  
  
 When you perform customizations that will appear in Dynamics 365 for tablets you should always explicitly publish your customizations to make sure that every item is synchronized with the Dynamics 365 for tablets application.  
  
> [!NOTE]
>  Publishing customizations can interfere with normal system operation. In a production environment we recommend that you schedule publishing customizations when it’s least disruptive to users.  
  
 The following solution components require publishing when they are updated:  
  
-   Application Ribbon  
  
-   Entity  
  
-   Entity Relationship  
  
-   Field  
  
-   Form  
  
-   Message  
  
-   Option Set  
  
-   Site Map  
  
-   Web Resource  
  
> [!NOTE]
>  When using Dynamics 365 App for Outlook it can take at least an hour for customization changes to take effect. You can make the changes appear immediately in Internet Explorer by clearing the cache. To do this, go to **Tools** > **Internet Options** and under **Browsing history** select the **Delete** button. Uncheck all browsing history items except “Temporary Internet files and website files” and “Cookies and website data” and then select **Delete**.  
  
## See also  
 [Customization concepts](../common-data-service/overview.md)  
 [Using solutions](../common-data-service/use-solutions-for-your-customizations.md)  
 [Create a custom theme or brand](../common-data-service/change-color-scheme-add-logo-match-organizations-brand.md)  

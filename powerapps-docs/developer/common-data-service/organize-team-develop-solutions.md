---
title: "Organize your team to develop solutions (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This document lists down some strategies to use when multiple developers are working on the same solution" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "shmcarth" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Organize your team to develop solutions

When multiple developers have to work on the same solution, you may want to create an environment where each developer can create customizations that will not interfere with the work of other developers. You may also need to move your solution from development environments to test environments and user acceptance testing (UAT) environments.  
  
<a name="BKMK_StrategiesForTeamDev"></a>   
## Strategies for team development  
 Some strategies to manage team development of solutions are as follows:  
  
-   [Single Organization: One Master Solution](organize-team-develop-solutions.md#BKMK_SingleOrgMasterSolution)  
  
-   [Single Organization: Multiple Developer Solutions + Master Solution](organize-team-develop-solutions.md#BKMK_SingleOrgMultipleDeveloper)  
  
-   [One Organization per Developer](organize-team-develop-solutions.md#BKMK_OneOrgPerDev)  
  
<a name="BKMK_SingleOrgMasterSolution"></a>   
### Single organization: One master solution  
 Multiple developers can work on a single organization; however, they have to be careful to work on separate components. This is easier when any prerequisite managed solutions (shared libraries) are installed first.  
  
<a name="BKMK_SingleOrgMultipleDeveloper"></a>   
### Single organization: Multiple developer solutions + master solution  
 In a single organization, you can create separate unmanaged solutions for each developer. Each solution contains a sub set of a master solution. Each solution component exists in only one unmanaged solution. Developers do not add existing solution components to the unmanaged solutions assigned to them. This provides a clear separation of components that are being modified. You do not have to merge changes because each developer’s solution contains a reference to components that are contained in the master solution.  
  
<a name="BKMK_OneOrgPerDev"></a>   
### One organization per developer  

 Each developer can work on their own organization. To check their changes into CDS for Apps, they must export their solution as an unmanaged solution. The solution from each developer’s organization is then imported into a master solution. Use the master solution to export the managed solution.  
  
<a name="BKMK_DeployingSolutionsFromDevThroughToProduction"></a>   
## Deploy solutions from development through test and production environments  
 In development organizations, solutions are deployed into various test and staging environments for analysis before they are deployed into a production environment. The white paper [Deploying Microsoft Dynamics CRM 2011 and CRM Online Solutions from Development through Test and Production Environments](http://go.microsoft.com/fwlink/p/?LinkId=232288) explores how to deploy real-world Dynamics 365 solutions across test and production environments in reliable and repeatable ways by using automation. The paper also highlights specific constraints that exist when you deploy and test solutions in CDS for Apps.  
  
### See also  
 [Planning for Solution Development](plan-solution-development.md)   
 [Modularize your Solutions](organize-solutions.md)   
 [White Paper: Deploying Dynamics 365 Customer Engagement and CRM Online Solutions from Development through Test and Production Environments](http://www.microsoft.com/download/en/details.aspx?displaylang=en&id=27824)
---
title: Model-driven apps Developer Overview | Microsoft Docs
description: Learn how developers can add value to model-driven apps.
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: faisalmo
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/11/2018
ms.author: jdaly
---
# Model-driven apps Developer Overview

PowerApps offers users, businesses, partners, independent software vendors (ISVs), and systems integrators (SIs) a powerful platform for building line-of-business apps. The new addition to PowerApps in this release are model-driven apps built using the new Common Data Service for Apps. The Common Data Service for Apps now contains the core functionality of the Dynamics 365 Customer Engagement  applications. With model-driven apps, you can build apps that use the same extensibility capabilities as those applications.

Model-driven apps are primarly a no-code or low-code component focused approach to app development. The value developers can provide is by extending the application. Before you start writing code begin with learning how to build a model-driven app. 

## Get Started
If you are already experienced with the Dynamics 365 Customer Engagement apps, you will find that you will be able to apply your experience building model-driven apps. There are some new designers available to you, but generally the concepts are the same.

> [!NOTE]
> Model-driven apps connect to the Common Data Service for Apps. For information about how developers can add value at the service level, see [Common Data Service for Apps Developer Overview](../../common-data-service/developer/overview.md).
> Content in this section will refer only to extensions developers can do that apply to the experience for users of model-drven apps. 

If you are new to the Dynamics 365 Customer Engagement applications, the following topics provide a high-level overview of the important concepts to help developers get started working with model-driven apps.
 <!-- This isn't in my fork Matt P is adding -->
- [Overview of building a model-driven app](../model-driven-app-overview.md)


> [!NOTE]
> Because the Common Data Service for Apps in this preview release is an instance of Dynamics 365 Customer Engagement, you will find more complete information for developers in the [Dynamics 365 Customer Engagement Developer Guide](/dynamics365/customer-engagement/developer/developer-guide). These topics will provide an overview with links to the developer guide and other guides for more information.


## Community Tools for model driven apps

The Dynamics 365 community creates tools! Many of the most popular ones are distributed via in the [XrmToolBox](https://www.xrmtoolbox.com/). XrmToolBox is a Windows application that connects to Common Data Service for Apps, providing tools to ease customization, configuration and operation tasks. It is shipped with more than 30 plugins to make administration, customization or configuration tasks easier and less time consuming.

The following is a selected list of community tools distributed via the XrmToolBox you can use when working with model-driven apps

|Tool  |Description  |
|---------|---------|
|[Easy Translator](https://www.xrmtoolbox.com/plugins/MsCrmTools.Translator/)|Exports and Imports translations with contextual information|
|[Export to Excel](https://www.xrmtoolbox.com/plugins/Ryr.XrmToolBox.ExportToExcel/)|Easily export records from the selected view/fetchxml to Excel.|
|[Iconator](https://www.xrmtoolbox.com/plugins/MscrmTools.Iconator/)|Manage custom entities icons in a single screen|
|[Ribbon Workbench 2016](https://www.xrmtoolbox.com/plugins/RibbonWorkbench2016/)|Edit the Dynamics CRM Ribbon or Command Bar from inside the XrmToolbox|
|[View Designer](https://www.xrmtoolbox.com/plugins/Cinteros.XrmToolBox.ViewDesigner/)|Easy UI to design view layouts and alter queries using FetchXML Builder|
|[View Layout Replicator](https://www.xrmtoolbox.com/plugins/MsCrmTools.ViewLayoutReplicator/)|Apply same layout to multiple views of the same entity in a single operation|
|[WebResources Manager](https://www.xrmtoolbox.com/plugins/MsCrmTools.WebResourcesManager/)|Manage your web resources easily|

Another tool that is not distributed via the XrmToolBox is Jason Lattimer's [CRM REST Builder](https://github.com/jlattimer/CRMRESTBuilder). This tool generates JavaScript code for use with the Web API.

> [!NOTE]
> Tools created by the community are not supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.





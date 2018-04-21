---
title: What's new in PowerApps | Microsoft Docs
description: Updates to PowerApps, organized by release date
documentationcenter: na
author: skjerland
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: canvas
ms.date: 04/09/2018
ms.author: sharik

---
# What's new in PowerApps
For information about known limitations, see [Common issues and resolutions](common-issues-and-resolutions.md).


> [!NOTE]
> Releases are rolled out over several days. New or updated functionality may not appear immediately.

## Announcing the Business Applications Spring '18 release notes

Discover the latest updates to our business applications, as well as a host of new capabilities for building your own applications and extensions on top of our platform. [Download the Spring '18 release notes PDF](https://aka.ms/businessappsreleasenotes), which covers Dynamics 365, PowerApps, Microsoft Flow, and Power BI.

**Coming soon:** We'll keep updating the release notes PDF as features ship, and we'll also make them available on a web page.

## Apr. 9
* Cut (Ctrl+X), copy (Ctrl+C), and paste (Ctrl+V) controls&mdash;including the controls' styles, formulas, and properties&mdash;across apps in a web browser.

## Mar. 21
1. Create [model-driven apps](../model-driven-apps/model-driven-app-overview.md), which start with your data model and build up from the shape of your core business data and processes in Common Data Service for Apps to model forms, views, and other components. Model-driven apps automatically generate great UI that is responsive across devices.
2. [Create a database](../../administrator/create-database.md) on the latest version of CDS for Apps in an environment.
3. CDS for Apps now includes:
    - **Additional data types** support more complex entity definitions and provide richer experiences. (Applies to canvas and model-driven apps.)
    - [Create and customize entities](../common-data-service/data-platform-create-entity.md) in CDS for Apps right from the PowerApps site. The **refreshed experience** includes improved performance, a more user-friendly UI, and helpful features such as in-line creation of option sets. (Applies to canvas and model-driven apps.)
    - Create **server-side business rules** for validating data entered into CDS for Apps. (Applies to canvas and model-driven apps.)
    - Create **calculated and rollup fields** in CDS for Apps entities directly from the PowerApps site. (Applies to canvas and model-driven apps.)  
    - Developers can use the CDS for Apps **Software Development Kit** (SDK) to create code-based customizations for CDS for Apps.
    - Advanced users can access data stored in CDS for Apps through a new **OData Web API**.
    - [Import data](../common-data-service/data-platform-cds-newentity-pq.md) into CDS for Apps with **Power Query**. Use Power Query on the web to directly import data to CDS for Apps from multiple sources

## Mar. 5
1. Add (and delete) [attachments](controls/control-attachments.md) to SharePoint lists.
2. Open external [PDF](controls/control-pdf-viewer.md) files in a web browser. (Experimental feature)

## Feb. 12
* The volume control for embedded [video](controls/control-audio-video.md) and [audio](controls/control-audio-video.md) playback is now inline. To mute playback, instead of clicking or tapping a button, users must now use the volume control to lower the volume.

## Feb. 7
1. Removed the Zoom, Brightness, and Contrast properties from the [Camera](controls/control-camera.md) and [Barcode scanner](controls/control-barcodescanner.md) controls.
2. Fixed the issue where Clear buttons on [Text input](controls/control-text-input.md) controls limit the space alloted for user input. As a result of this fix, the [Clear](controls/control-text-input.md#additional-properties) property of a Text input control is supported only in Microsoft Edge (latest version) and Internet Explorer 11 web browsers.
3. Added accessibility enhancements to [multimedia](add-images-pictures-audio-video.md) controls.

## Jan. 31
1. Add closed captions to [Video](controls/control-audio-video.md) controls.
2. Improved error handling in [PDF Viewer](controls/control-pdf-viewer.md) controls.

## Jan. 18
1. PowerApps for iOS and Android now supports integration with Microsoft Authenticator.
2. A [combo box](controls/control-combo-box.md) replaces the [SharePoint lookup control](sharepoint-lookup-fields.md) in forms and a new [data card](working-with-cards.md) template for single-select lookup fields is selected by default in PowerApps Studio.
3. Within a [combo box](controls/control-combo-box.md), see all items in a long list with enhanced Read mode.
4. Control the size of the local record limit store up to a maximum of 2000 records in [non-delegable queries](delegation-overview.md#non-delegable-limits). (Experimental feature)

## Jan. 5
* Act on data right from your Power BI report or dashboard by integrating a [PowerApps custom visual (preview release)](https://powerapps.microsoft.com/blog/powerbi-powerapps-visual/), which pulls contextual data from your Power BI report.

## Dec. 8
1. [Condition templates](working-with-rules.md) for rules infer common properties of a control (such as **Text** or **Value**).
2. Stop displaying the [**Defining actions** confirmation dialog box](working-with-rules.md) when defining rule actions.

## Nov. 13
1. Select multiple values for the same field in SharePoint lists.
2. [View and download attachments](controls/control-attachments.md) in SharePoint lists.
3. [Customize SharePoint list forms](customize-list-form.md) using PowerApps.

## Nov. 10
* [Rename rules](working-with-rules.md) in an app and show rules when the selected control is in the rule condition.

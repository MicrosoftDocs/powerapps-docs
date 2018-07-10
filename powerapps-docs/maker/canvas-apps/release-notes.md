---
title: What's new | Microsoft Docs
description: Updates to PowerApps, organized by release date
documentationcenter: na
author: AFTOwen

ms.service: powerapps
ms.topic: conceptual
ms.component: canvas
ms.date: 05/21/2018
ms.author: anneta

---
# What's new in PowerApps
> [!IMPORTANT]
> **Announcing the release notes**<br>
> Wondering about upcoming and recently released capabilities in PowerApps?<br>
[View the release notes](https://docs.microsoft.com/business-applications-release-notes/april18/powerapps/overview). We've captured all the details, end to end, top to bottom, which you can use for planning.

For information about known limitations, see [Common issues and resolutions](common-issues-and-resolutions.md).

> [!NOTE]
> Releases are rolled out over several days. New or updated functionality may not appear immediately.

## May 30
1. [Rich-text editor control](controls/control-richtexteditor.md) (experimental) - allows end users to format text inside a WYSIWYG editing area. 

## May 21
1. Allow app users to import and export data from Excel or CSV files stored locally by using the **Get Data from Excel file** and **Export Data** features now available for upgraded Common Data Service (CDS) for Apps environments. 
1. Allow app users to [open entities in Excel](../common-data-service/data-platform-excel-addin.md) to create, update, and delete data stored within CDS for Apps by using the Excel add-in for PowerApps. 
1. [Create and publish Power BI reports](../common-data-service/data-platform-powerbi-connector.md) by using Power BI Desktop connected to CDS for Apps. 

## April 23
* Download [attachments](controls/control-attachments.md) in Internet Explorer within SharePoint custom list forms.

## April 9
* Cut (Ctrl+X), copy (Ctrl+C), and paste (Ctrl+V) controls&mdash;including the controls' styles, formulas, and properties&mdash;across apps in a web browser.

## March 21
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

## March 5
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

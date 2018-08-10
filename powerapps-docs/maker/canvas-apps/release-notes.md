---
title: What's new | Microsoft Docs
description: Updates to PowerApps, organized by release date
author: AFTOwen
manager: kvivek

ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer:
ms.date: 05/21/2018
ms.author: anneta

---
# What's new in PowerApps

> [!IMPORTANT]
>
> **Announcing the release notes**
>
> Wondering about upcoming and recently released capabilities in PowerApps?
>[View the release notes](https://docs.microsoft.com/business-applications-release-notes/april18/powerapps/overview). We've captured all the details, end to end, top to bottom, which you can use for planning.

For information about known limitations, see [Common issues and resolutions](common-issues-and-resolutions.md).

> [!NOTE]
> Releases are rolled out over several days. New or updated functionality may not appear immediately.

## July 30

* Automatically [format your code](https://powerapps.microsoft.com/en-us/blog/automatically-format-your-formula/) (blog) in the formula bar for canvas apps.

## July 16

1. Easier to configure [security for Common Data Service for Apps](share-app.md##manage-entity-permissions).
2. Improved [Tree view](https://powerapps.microsoft.com/blog/tree-view-now-even-better-with-expand-all-collapse-all-and-more/) (blog) for canvas apps in PowerApps Studio.

## July 9

1. Identify mistakes and [accessibility issues](accessibility-checker.md) in canvas apps with [AppChecker](https://powerapps.microsoft.com/blog/new-app-checker-helps-you-fix-errors-and-make-accessible-apps/) (blog).
2. Start canvas apps faster with the [**Concurrent** function](functions/function-concurrent.md).

## June 18

* [Select, edit, move, and test controls more easily](https://powerapps.microsoft.com/blog/say-goodbye-to-miss-clicks-on-the-canvas/) (blog) in canvas apps.

## June 11

1. [Import and export data from Common Data Services for Apps, and open that data in Excel](https://powerapps.microsoft.com/blog/cds-for-apps-excel-importexport/) (blog).
1. [**Notify** function](functions/function-showerror.md) shows banner messages in canvas apps.

## June 4

1. [Embed an app as a SharePoint webpart](https://powerapps.microsoft.com/blog/embedding-powerapps-in-office-and-beyond/) (blog).
1. [Specify a custom size for a tablet canvas app](https://powerapps.microsoft.com/blog/embedding-powerapps-in-office-and-beyond/) (blog).
1. Add [comments to formulas](https://powerapps.microsoft.com/blog/comment-your-powerapps-code/) (blog) in canvas apps.
1. [PowerShell cmdlets for administrators](https://docs.microsoft.com/powerapps/administrator/powerapps-powershell).
1. [Rich-text editor control](controls/control-richtexteditor.md) (experimental) - allows end users to format text inside a WYSIWYG editing area of a canvas app.

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

    * **Additional data types** support more complex entity definitions and provide richer experiences. (Applies to canvas and model-driven apps.)\

    * [Create and customize entities](../common-data-service/data-platform-create-entity.md) in CDS for Apps right from the PowerApps site. The **refreshed experience** includes improved performance, a more user-friendly UI, and helpful features such as in-line creation of option sets. (Applies to canvas and model-driven apps.)
    * Create **server-side business rules** for validating data entered into CDS for Apps. (Applies to canvas and model-driven apps.)
    * Create **calculated and rollup fields** in CDS for Apps entities directly from the PowerApps site. (Applies to canvas and model-driven apps.)  
    * Developers can use the CDS for Apps **Software Development Kit** (SDK) to create code-based customizations for CDS for Apps.
    * Advanced users can access data stored in CDS for Apps through a new **OData Web API**.
    * [Import data](../common-data-service/data-platform-cds-newentity-pq.md) into CDS for Apps with **Power Query**. Use Power Query on the web to directly import data to CDS for Apps from multiple sources

## March 5

1. Add (and delete) [attachments](controls/control-attachments.md) to SharePoint lists.
2. Open external [PDF](controls/control-pdf-viewer.md) files in a web browser. (Experimental feature)

## Feb. 12

* The volume control for embedded [video](controls/control-audio-video.md) and [audio](controls/control-audio-video.md) playback is now inline. To mute playback, instead of clicking or tapping a button, users must now use the volume control to lower the volume.

## Feb. 7

1. Removed the Zoom, Brightness, and Contrast properties from the [Camera](controls/control-camera.md) and [Barcode scanner](controls/control-barcodescanner.md) controls.
2. Fixed the issue where Clear buttons on [Text input](controls/control-text-input.md) controls limit the space alloted for user input. As a result of this fix, the [Clear](controls/control-text-input.md#additional-properties) property of a Text input control is supported only in Microsoft Edge (latest version) and Internet Explorer 11 web browsers.
3. Added accessibility enhancements to [multimedia](add-images-pictures-audio-video.md) controls.
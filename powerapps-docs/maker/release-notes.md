---
title: What's new in PowerApps | Microsoft Docs
description: Updates to PowerApps, organized by release date
services: ''
suite: powerapps
documentationcenter: na
author: skjerland
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/13/2018
ms.author: sharik

---
# What's new in PowerApps
For information about known limitations, see [Common issues and resolutions](common-issues-and-resolutions.md).

> [!NOTE]
> Releases are rolled out over several days. New or updated functionality may not appear immediately.

## Feb. 12
* The volume control for embedded [video](controls/control-audio-video.md) and [audio](controls/control-audio-video.md) playback is now inline. To mute playback, instead of clicking or tapping a button, users must now use the volume control to lower the volume.

## Feb. 7
1. Removed the Zoom, Brightness, and Contrast properties from the [Camera](controls/control-camera.md) and [Barcode scanner](controls/control-barcodescanner.md) controls.
2. Fixed the issue where Clear buttons on [Text input](../controls/control-text-input.md) controls limit the space alloted for user input. As a result of this fix, the [Clear](../../controls/control-text-input.md#additional-properties) property of a Text input control is supported only in Microsoft Edge (latest version) and Internet Explorer 11 web browsers.
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
2. [View and download attachment](controls/control-attachments.md) in SharePoint lists.
3. [Customize SharePoint list forms](customize-list-form.md) using PowerApps.

## Nov. 10
* [Rename rules](working-with-rules.md) in an app and show rules when the selected control is in the rule condition.

## Oct. 30
1. [Show all rules](working-with-rules.md) in an app, not just those for the selected control.
2. Add icons that app creators requested the most.
3. Improved performance of apps on Android and iOS devices.

## Sept. 20
1. After you [save an app](save-publish-app.md) for the first time, additional changes are saved every two minutes automatically by default.
2. Easily [create rules](working-with-rules.md) for conditional formatting without writing expressions - just set your condition and then design the results right on the PowerApps canvas.
3. More easily configure forms, galleries, and data tables with a full-height data pane that pops out when a control is added.
4. Get contextual quick-tips to help you create an app, whether starting from a blank app, a template, a data source, or SharePoint.

## Sept. 6
1. For apps that you create, [track usage](../administrator/app-analytics.md) in an embedded dashboard from Power BI.
2. Use a delimiter to break a text string into parts by using the **[Split](../functions/function-split.md)** function.

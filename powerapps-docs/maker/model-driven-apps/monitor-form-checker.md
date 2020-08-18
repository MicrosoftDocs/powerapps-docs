---
title: Monitor and troubleshoot model-driven app form behavior in Power Apps | MicrosoftDocs
description: "Learn how to use the news control to get the latest news about your customers"
ms.custom: ""
ms.date: 08/11/2020
ms.reviewer: "matp"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
author: "mspilde"
ms.author: "mspilde"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Use Monitor to troubleshoot model-driven app form behavior (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Monitor can help you debug and diagnose problems, which help you build faster, more reliable apps. Monitor provides a deep view into how an app runs by providing a log of all activities in your app as the app runs.

When you filter on model-driven app form-related events in Monitor, you can get information about related tables, entities, controls, and components on a form in Monitor as your app runs.  

There are many situations that you may encounter where access to the information provided by Monitor will help you better understand why a form behaves a certain way. Many form issues are based on business rules, JavaScript, form events, or client API that admins and makers have set.  Monitor can also help identify if the issue you experience is designed out-of-the-box or is due to a customization. It provides details that can help you answer the following questions:

- Why records aren’t showing in the related menu of an entity?
- Why is a control not editable?
- Why is a record in a read-only state?

## Filter Monitor for form-related issues

1. Sign in to [Power Apps](https://make.powerapps.com/), select **Apps**, select the app you want, and then select **Monitor** on the command bar. Follow the instructions on your screen to run the app and join the monitoring session.

   You can also start a Monitor session from a model-driven app. To do this, append *&monitor=true* to the end of the URL in the browser. This displays the **Monitor** command on the model-driven app global command bar.  Select **Monitor** to launch a monitoring session in a new tab.
   ![Add URL parameter to run Monitor from a model-driven app](media/run-monitor-from-app.png)

2. On the browser window running Monitor, select the three horizontal lines on the **Category** column to open the filter options.

   > [!div class="mx-imgBorder"] 
   > ![Filter on form events in Monitor](media/monitor-filter-formchecker.png)

3. Enter *formchecker* in the topmost **Filter** box. Don’t make any other changes and select **Apply**. 

   <img src="media/monitor-formchecker-filter.png" alt="Enter formchecker filter" height="255" width="405"> 

4. Click or tap anywhere outside the filter dialog to close the dialog and refresh the list in Monitor. You can expand the **Category** column to see the full name of the events that are tracked by selecting and holding the right-side of the column and dragging to the right. As you use the app and open and use a form, Monitor updates the list of events.
<!--Replace with updated screenshot that displays FormChecker not uci_formchecker"
   > [!div class="mx-imgBorder"] 
   >![Monitored form events displayed](media/monitor-formchecker-events.png)  -->

## Use Monitor to understand form behavior

For each record, you can open and view detailed information about the form event. For example, imagine you have a question about the options in the related menu tab of a form. You go to that form in the app and select the appropriate form component. In this example, the **RelatedMenu** record in the **Operation** column is selected. Next, the **Details** tab, and then **…** are selected ti display additional information. 

> [!div class="mx-imgBorder"] 
> ![Monitoring related menu ](media/monitor-formchecker-related-menu.png)

To see the full details, select **+** next to the line that displays the word **data** in the title, which is line **5** in the previous screenshot. The expanded details displays all items in the related menu with information that can help you understand why an entity is, or is not, included in the related menu options. There are many types of events that are monitored including the standard form events like onload, onsave, onclose, and so on.

As you continue to use the app that is being monitored, Monitor updates the information in the list of events. For forms, there are many different scenarios that you can troubleshoot and find additional information on the form, control, or entity, you are working with. 

## Supported form checking areas and events

Supported areas for form monitoring include:

|App area  |Description  |
|---------|---------|
|Control state   | Details about the state of the visible, enabled, and label source of a control when the form is loaded.     |
|Related menu   | Details about the state of related menu items. Examples:  <br /> Why is a menu item not displaying? <br /> Where does the menu item come from?     |
|Tab / section / control state change   | Details on who (via callstack) has caused a form component such as a tab, section, or control, to change the component’s visibility and enabled state.        |
|Navigation     | Details about who’s causing navigation or unexpected dialogs by tracing the callstack of these Xrm.Navigation client API methods: openAlertDialog(), openConfirmDialog(), openDialog(), openErrorDialog(), navigateTo(), openForm(), openTaskFlow(), openUrl(), openWebResource()         |
|Unsupported customizations    |  Details about unsupported client API access before the form is ready. Examples: <br /> Accessing parent.Xrm.Page in iFrame before form is fully loaded. <br /> Accessing Xrm.Page in form web resource outside of form handler contexts using window.setTimeout() to periodically call Form client API. <br /> Accessing Xrm.Page in updateView() method of PCF control code.  |

Examples of the supported form-related events in Monitor:
- FormEvents.onsave
- XrmNavigation
- FormEvents.onload
- FormControls
- TabStateChange.visible
- RelatedMenu
- ControlStateChange.disabled
- ControlStateChange.visible
- SectionStateChange.visible
- UnsupportedClientApi


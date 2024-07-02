---
title: Get the session or app ID
description: Learn about how to get a session ID or a canvas-app ID for troubleshooting.
author: tahoon
ms.subservice: troubleshoot
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 7/2/2024
ms.author: tahoon
search.audienceType: 
  - maker
contributors:
  - mduelae
---
# How to write a good Power Apps bug report

If an app isn't behaving as expected, it could be an issue with its configuration, the Power Apps system, or a system outside of Power Apps.

Depending on where the issue lies, you can seek assistance from these people or organizations:

| Type of issue | Who can help best |
| ------------- | ----------------- |
| App | Creators of the app, administrators |
| Power Apps | Microsoft |
| External data sources and integrations | Those who are responsible for the external system |


## Differences between app bugs and Power Apps bugs

An app bug is an unexpected behavior in a particular app. In comparison, a Power Apps bug is an unexpected behavior in the system that creates, runs, or manages the app. It's not always easy to tell the difference because an app bug can sometimes be caused by an underlying Power Apps bug. Here are some distinguishing signs.

| App bug | Power Apps bug |
| ------- | -------------- |
| Explains how to reproduce an issue in a specific app | Explains how to create an app that reproduces an issue |
| Requires access to specific data connections | Any data connection can be used to repro the issue, which may require a specific configuration of the data source |
| Affects only a single app in a single organization | Affects apps in multiple organizations, or has the potential to do so |
| Complicated app with components not relevant to the issue | [Minimal repro app](/troubleshoot/power-platform/power-apps/create-and-use-apps/minimal-canvas-app-repro) that clearly shows an issue with just a few components |
| Mentions custom features and code  | Mentions specific Power Apps features |
| Microsoft documentation does not exist for the affected feature | Microsoft documentation exists for affected feature and explains its expected behavior |

### Example app bugs
#### Canvas app does not show invoices
1. Log into Contoso app with app link.
1. Home screen opens. Click on button that says _My Invoices_.
1. Invoice screen opens. The list of invoices are displayed.
- Expected behavior: Invoices created by the user are displayed.
- Actual behavior: No invoices are shown.

#### Model-driven app does not show invoices
1. Log into Contoso app in a particular environment.
1. Dashboard page opens. Click Invoices on the site map.
1. Invoice page appears, with the view set to _My active invoices_. The list of invoices are displayed.
- Expected behavior: Invoices created by the user are displayed.
- Actual behavior: No invoices are shown.

These describe app bugs. The features, user interface, and tables are specific to the app and organization. For example, invoice isn't a built-in table in Power Apps. There isn't a specialized feature in canvas apps for filtering records by a certain user; the app maker has to write Power Fx expressions or configure data connectors. Similarly, the maker has to configure Views in model-driven apps to display desired records.

There isn't sufficient information in either bug reports to determine if there's a Power Apps issue. The creators of the app are best-suited to investigate app issues.

Suppose the creators investigate and believe the cause to be a Power Apps bug. They might then report them as follows.

### Example Power Apps bugs
#### Canvas app Filter function returns no results when filter text contains asterisk character
1. A minimal repro app is attached to demonstrate the issue. Open it.
1. This app contains a simple collection, `TestTable` with data `[{Name: "a"},  {Name: "*b"}]`.
1. There are 2 **[Table](./controls/modern-controls/modern-control-table.md)** controls in the app. Both controls are configured to show the Name column.
   1. Table1 has **Items** set to `Filter(TestTable, Name="a")`.
   1. Table2 has **Items** set to `Filter(TestTable, Name="*b")`.
- Expected behavior: Table1 shows the record `{Name: "a"}`, because it matches the **Filter** function's condition `Name="a"`. Table2 shows the record `{Name: "*b"}`, because it matches the **Filter** function's condition `Name="*b"`.
- Actual behavior: Table1 shows expected record but Table2 doesn't show any records.
- Notes: Same behavior is observed with other dataset controls like Gallery, when **Items** are set to the same expressions.

#### Model-driven app View returns no results when filter condition contains asterisk character
1. Create a View for any table.
1. Remove all filters for the View.
1. Add a filter for the primary column, matching text starting with _*b_.
1. Add this view and the table to any model-driven app.
1. Save and publish all changes.
1. Run the app.
2. Add a few records with different values for the primary column. Ensure one starts with _*b_.
3. Go to that table's page.
4. Change to the newly created view.
- Expected behavior: Grid shows records with primary column values that starts with _*b_.
- Actual behavior: No records shown.
- Notes: When the filter condition doesn't use an asterisk, like _b_, the filter works as expected.

These describe issues with specific Power Apps features: the **[Filter](/power-platform/power-fx/reference/function-filter-lookup)** function for the canvas app and [View filters](../model-driven-apps/create-edit-view-filters.md) for the model-driven app. They provide enough information for anybody to reproduce the issue easily. They mention investigative actions to isolate the issue.

If you suspect a Power Apps bug, here are other tips on writing a good bug report so that Microsoft can assist you more effectively.

## What makes a good Power Apps bug report

A good bug report frames an issue as a Power Apps bug, not an app bug. Follow these guidelines, where applicable, to help others understand and resolve the issue quickly.

### Have a descriptive title
The title should mention
1. a specific Power Apps feature,
1. the unexpected behavior,
1. and the conditions that cause it to happen.

Example of a bad title: "Gallery control is blank"

Example of a good title: "Filter function returns no results when filter text contains asterisk character"

### Attach a simplified app, not the original app

For issues with running an app, provide a [minimal repro app](/troubleshoot/power-platform/power-apps/create-and-use-apps/minimal-canvas-app-repro) for canvas apps, or a [vanilla repro solution](/troubleshoot/power-platform/power-apps/create-and-use-apps/vanilla-model-driven-app-repro) for model-driven apps.

The most important goal is that **anyone should be able to reproduce the issue on their own device**. With a minimal or vanilla repro app, you show that it's a Power Apps bug instead of an app bug. Microsoft can resolve it swiftly. Without these repro apps, resolution may be delayed or the bug report may not be accepted.

A minimal or vanilla repro app isn't always feasible or needed for these issues:
- Getting and saving data from a specific data source
- Issues with specific users like permissions
- Licensing
- Offline operation
- General server issues

Regardless, you should simplify your app as much as possible and [isolate the issue for canvas](/troubleshoot/power-platform/power-apps/create-and-use-apps/isolate-canvas-app-issues) or [model-driven apps](/troubleshoot/power-platform/power-apps/create-and-use-apps/isolate-model-app-issues).

### Attach a network trace

For data and server issues, examining network communications between the client and server helps [isolate the problematic layer](/troubleshoot/power-platform/power-apps/create-and-use-apps/isolate-common-issues). A record of network calls is known as a network trace.

You can either use [Monitor](../monitor-overview.md) or [browser development tools](/azure/azure-web-pubsub/howto-troubleshoot-network-trace#collect-a-network-trace-in-the-browser-browser-based-apps-only) to record a network trace.

Be sure to start recording just before reproducing the issue and end it right after. This minimizes irrelevant information in the trace.

### Provide detailed steps to reproduce the issue

If you've created a minimal or vanilla repro app, describe how to reproduce the issue in that app. Don't describe the app where you originally found the problem.

Mention the observed behavior and the expected behavior.

#### Provide screenshots or videos

For user interface issues, a screenshot or video can better clarify the steps to reproduce than a written description.

#### Link to official documentation

Links to Microsoft documentation clarify the affected feature and its expected behavior.

For issues with professional development features, provide a link to the documentation for the API function that's not working.

### Simplify code samples

If the issue involves coding and other professional development features, simplify the code first. Usually, just a few lines of code are needed to demonstrate a Power Apps bug. Deploy it in a fresh environment with no other customizations. Verify the issue occurs and attach a snippet of the problematic code.

Such professional development features include:
* [Power Apps code components](./developer/component-framework/overview)
* [Custom form scripts](/power-apps/developer/model-driven-apps/client-scripting) in model-driven apps
* [Power Fx or JavaScript commands](/power-apps/maker/model-driven-apps/command-designer-overview) in model-driven apps
* [Web resources](/power-apps/developer/model-driven-apps/web-resources) in model-driven apps

Mention specific configuration steps so that others can reproduce the issue on their own environment.

### Provide system info

An issue might happen only on a specific version of Power Apps, browser, or environment. Provide the [session ID](/power-apps/maker/canvas-apps/get-sessionid) so that Microsoft can get these details.

### Add notes from your investigation

You might have tried different configurations to eliminate possible causes. Mention these in the bug report. This helps others understand the issue better and avoid repeating the same steps.


## Submitting a Power Apps bug

Before reporting a bug, [check if it's a known issue](/power-platform/admin/view-known-issues). If not, you can [create a support request](/power-platform/admin/get-help-support) to report it.


## See also

- [General Power Apps debugging strategies](isolate-common-issues.md)

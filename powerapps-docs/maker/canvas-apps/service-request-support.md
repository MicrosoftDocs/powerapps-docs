---
title: Create an effective support request
description: Learn how to write a clear Power Apps support request so Microsoft support can help you quickly.
author: tahoon
ms.subservice: troubleshoot
ms.topic: how-to
ms.custom: canvas
ms.reviewer: 
ms.date: 7/2/2024
ms.author: tahoon
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Create an effective support request

If an app isn't behaving as expected, it could be an issue with your Power Apps configuration or a system outside of Power Apps.

Depending on the issue, you can get help from the following individuals or organizations:

| Type of issue | Who can help best |
| ------------- | ----------------- |
| App | Creators of the app, administrators |
| Power Apps | Microsoft |
| External data sources and integrations | Users responsible for the external system |

## Differences between app bugs and Power Apps bugs

An *app* bug is unexpected behavior in a particular app. In comparison, a *Power Apps* bug is unexpected behavior in the system that creates, runs, or manages the app. An underlying Power Apps bug might cause an app bug, making it difficult to determine if the bug is an app or Power Apps bug.

Here are some distinguishing signs.

| App bug | Power Apps bug |
| ------- | -------------- |
| Able to reproduce an issue in a specific app | Able to create an app that reproduces an issue |
| Requires access to *specific* data connections | *Any* data connection reproduces the issue, which might require a specific configuration of the data source |
| Affects only a single app in a single organization | Affects apps in multiple organizations or has the potential to affect them |
| Complicated app with components not relevant to the issue | [Minimal repro app](/troubleshoot/power-platform/power-apps/create-and-use-apps/minimal-canvas-app-repro) that shows an issue with a few components |
| Mentions custom features and code  | Mentions specific Power Apps features |
| Microsoft documentation doesn't exist for the affected feature | Microsoft documentation exists for the affected feature and explains its expected behavior |

### Example app bugs

The following examples show app bugs and how users can describe them as steps to app owners, so owners can reproduce and resolve the bugs.

1. Canvas app doesn't show invoices.
   1. Sign in to your canvas app, such as Contoso.
   1. On your Home screen, select **My Invoices**.
      - Expected behavior: Invoices created by the user are displayed.
      - Actual behavior: No invoices are shown.

1. Model-driven app doesn't show invoices.
   1. Sign in to the Contoso app in your environment.
   1. On the **Dashboard** page, select **Invoices** on the site map.
   1. On the **Invoices** page, set the view to **My active invoices**. The list of invoices are displayed.
      - Expected behavior: Invoices created by the user are displayed.
      - Actual behavior: No invoices are shown.

Bugs can have great variance because features, user interfaces, and tables are specific to an app and organization, making the cause of bugs different for everyone. For example, **invoice** isn't a built-in table in Power Apps. There isn't a specialized feature in canvas apps for filtering records by a certain user, therefore the app maker must write Power Fx expressions or configure data connectors. Similarly, the maker must configure **Views** in model-driven apps to display desired records.

There isn't sufficient information in either of the examples to determine if there's a Power Apps issue. The creators of the app are best suited to investigate app issues.

### Example Power Apps bugs

If app creators investigate and find what they classify as a Power Apps bug, they might report them similarly to the following examples.

1. **Canvas app Filter function returns no results when filter text contains asterisk character**

   1. A minimal repro app is attached to demonstrate the issue.
   1. This app contains a simple collection: `TestTable` with data `[{Name: "a"},  {Name: "*b"}]`.
   1. There are two **[Table](./controls/modern-controls/modern-control-table.md)** controls in the app. Both controls are configured to show the **Name** column.
   1. **Table1** has **Items** set to `Filter(TestTable, Name="a")`.
   1. **Table2** has **Items** set to `Filter(TestTable, Name="*b")`.
      - Expected behavior: **Table1** shows the record `{Name: "a"}`, matching the **Filter** function's condition `Name="a"`. **Table2** shows the record `{Name: "*b"}`, matching the **Filter** function's condition `Name="*b"`.
      - Actual behavior: **Table1** shows expected record but **Table2** doesn't show any records.
      - Notes: Same behavior is observed with other dataset controls like **Gallery**, when **Items** are set to the same expressions.

1. **Model-driven app View returns no results when filter condition contains asterisk character**

   1. Create a **View** for any table.
   1. Remove all filters for the view.
   1. Add a filter for the primary column, matching text that starts with _*b_.
   1. Add this view and the table to any model-driven app.
   1. Save and publish all changes.
   1. Run the app.
   1. Add a few records with different values for the primary column. Ensure one column starts with _*b_.
   1. Go to the table's page.
   1. Change the view to the newly created view.
      - Expected behavior: Grid shows records with primary column values that start with _*b_.
      - Actual behavior: No records shown.
      - Notes: When the filter condition doesn't use an asterisk, like _b_, the filter works as expected.

These Power Apps bugs describe issues with specific Power Apps features: the **[Filter](/power-platform/power-fx/reference/function-filter-lookup)** function for the canvas app and [View filters](../model-driven-apps/create-edit-view-filters.md) for the model-driven app.

A good support request provides enough information for anybody to reproduce the issue easily. The author might mention the result of their investigative actions or troubleshooting they tried when attempting to isolate the issue. For example, the author might mention the issue only occurs in the Chrome browser but not in Firefox.

## What makes a good Power Apps support request

A good support request frames an issue as a Power Apps bug, not an app bug. Follow these guidelines, where applicable, to help Microsoft understand and resolve the issue quickly.

### Have a descriptive title

The title should mention:

1. A specific Power Apps feature
1. The unexpected behavior
1. The conditions that cause the bug to happen

Example of a bad title: "Gallery control is blank"

Example of a good title: "Filter function returns no results when filter text contains asterisk character"

### Attach a simplified app, not the original app

For issues with running an app, provide a [minimal repro app](/troubleshoot/power-platform/power-apps/create-and-use-apps/minimal-canvas-app-repro) for canvas apps, or a [vanilla repro solution](/troubleshoot/power-platform/power-apps/create-and-use-apps/vanilla-model-driven-app-repro) for model-driven apps.

> [!IMPORTANT]
> The goal of a good support request is to include enough information so that anyone can reproduce the issue on their own device.
>
> If you can show that the bug is a Power Apps bug instead of an app bug, with a minimal or vanilla repro app, Microsoft can resolve it swiftly. Without these repro apps, the resolution might be delayed or the support request might not be accepted.

#### Exceptions

A minimal or vanilla repro app isn't always feasible or needed for these issues:

- Data access and saves from a specific data source
- Specific user data, such as user permissions
- Licensing
- Offline operation
- General server issues

Regardless, simplify your app as much as possible and [isolate the issue for canvas](/troubleshoot/power-platform/power-apps/create-and-use-apps/isolate-canvas-app-issues) or [model-driven apps](/troubleshoot/power-platform/power-apps/create-and-use-apps/isolate-model-app-issues).

### Attach a network trace

For data and server issues, examining network communications between the client and server helps [isolate the problematic layer](/troubleshoot/power-platform/power-apps/create-and-use-apps/isolate-common-issues). A record of network calls is known as a network trace.

You can either use [Monitor](../monitor-overview.md) or [browser development tools](/azure/azure-web-pubsub/howto-troubleshoot-network-trace#collect-a-network-trace-in-the-browser-browser-based-apps-only) to record a network trace.

Be sure to start recording just before reproducing the issue and end the recording right after you successfully reproduced it. This brief interval minimizes irrelevant information in the trace that might cause delays in Microsoft's handling of the support request.

### Provide detailed steps to reproduce the issue

If you created a minimal or vanilla repro app, describe *how to reproduce the issue* in that app. Don't describe issues with the app where you originally found the problem.

Mention the observed behavior and the expected behavior.

#### Provide screenshots or videos

For user interface issues, screenshots or videos can more quickly clarify the steps to reproduce the bug, rather than a written description.

#### Link to official documentation

Include links to Microsoft documentation to clarify the affected feature and its expected behavior.

For issues with professional development features, provide a link to the documentation for the API function that doesn't work.

### Simplify code samples

If the issue involves coding and other professional development features, simplify the code first. Usually, just a few lines of code are needed to demonstrate a Power Apps bug. Deploy the app in a fresh environment with no other customizations. Verify the issue occurs and attach a snippet of the problematic code.

Examples of professional development features in Power Apps:

- [Power Apps components](../../developer/component-framework/overview.md)
- [Custom form scripts](../../developer/model-driven-apps/client-scripting.md) in model-driven apps
- [Power Fx or JavaScript commands](../model-driven-apps/command-designer-overview.md) in model-driven apps
- [Web resources for model-driven apps](../../developer/model-driven-apps/web-resources.md)

Mention specific configuration steps so that others can reproduce the issue in their own environment.

### Provide system info

An issue might happen only on a specific version of Power Apps, a browser, or an environment. Provide the [session ID](/power-apps/maker/canvas-apps/get-sessionid) so that Microsoft can use these details.

### Add notes from your investigation

You might try different configurations to eliminate possible causes. Mention these configurations in the support request. This inclusion helps others understand the issue better and avoid repeating the same steps.

## Submitting a Power Apps support request

Before submitting a support request, [check if the bug is a known issue](/power-platform/admin/view-known-issues). If the bug isn't already known, you can [create a support request](/power-platform/admin/get-help-support) to report the bug.

## See also

- [General Power Apps debugging strategies](/troubleshoot/power-platform/power-apps/create-and-use-apps/isolate-common-issues)

---
title: "Customize Model-Driven Apps Using Code"
description: "Learn how to customize model-driven apps using supported Power Apps tools and code, understand upgradeability, and avoid unsupported customization methods."
author: sriharibs-msft
ms.author: srihas
ms.date: 08/10/2026
ms.reviewer: jdaly
ms.subservice: mda-developer
search.audienceType:
  - developer
contributors: 
  - JimDaly
---
# Customize model-driven apps by using code

Learn how to customize model-driven apps by using supported Power Apps tools and documented code. This article helps you identify supported and upgradeable methods so you can avoid customization problems during updates and upgrades.

Customizations made using methods other than those described here are unsupported and could cause problems during updates and upgrades to model-driven apps. For more information, see [Unsupported customizations](#unsupported-customizations) later in this topic.

Customizations made by using methods other than those described in this article are unsupported and could cause problems during updates and upgrades to model-driven apps. For more information, see [Unsupported customizations](#unsupported-customizations) later in this article.


## Customizations using Power Apps

Technical articles published on Microsoft sites such as this one support the topics they cover, but they might not support upgradeability.

The following customization methods can be used to produce fully supported customizations:

- Customization in Power Apps or solution explorer. For more information, see [Overview of building model-driven apps](../../maker/model-driven-apps/model-driven-app-overview.md)
- Settings in the web application. For more information, see [Administer model-driven apps](../../maker/model-driven-apps/model-driven-app-overview.md).
- Reporting Services. For more information, see [Reporting and analytics guide for model-driven apps](../../maker/model-driven-apps/add-reporting-to-app.md).

> [!NOTE]
> The behavior of model-driven apps depends on customizations applied to the associated Microsoft Dataverse. For more information, see [Supported customizations for Dataverse](../data-platform/supported-customizations.md).
> *Fully supported* means that developer support can provide assistance for customizations and that application support can help customers running those modifications.


## Customizations applied using code

The documentation on this site for developers, technical articles, sample code published on this site, and information released by the Dataverse Developer Support Team are included in the area of customizations applied using code. The specific actions and levels of supportability and upgradeability are described later in this topic.

### Client-side JavaScript

You can use JavaScript within model-driven apps in three areas:

- **Form Script event handlers**: You can configure form event handlers to call functions defined in JavaScript web resources.
- **Command bar (ribbon) commands**: You can use the `<CustomRule>` or `<JavaScriptFunction>` elements to define actions that call functions defined within JavaScript web resources.
- **Web resources and IFRAMEs**: You can use JavaScript web resources within HTML web resources. IFRAMES configured to allow cross-site scripting, or scripts within HTML web resources included in a form, can interact with the documented `Xrm.Page` or `Xrm.Utility` methods within the form via the parent reference.

All interaction with the application pages must use only the methods documented in the [Client API Reference for model-driven apps](clientapi/reference.md). Directly accessing the Document Object Model (DOM) of any model-driven apps page isn't supported. Don't use jQuery in form scripts and commands. For more information, see [Client scripting in model-driven apps using JavaScript](client-scripting.md).

You can open model-driven apps forms, views, dialogs, and reports by using the methods documented in [Open forms, views, dialogs, and reports with a URL](open-forms-views-dialogs-reports-url.md).

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

### Ribbon customization

You can use `RibbonDiffXml` to add, remove, or hide ribbon elements. You can reuse ribbon commands defined by model-driven apps; however, Microsoft reserves the right to change or deprecate the available commands. You can't reuse JavaScript functions defined within ribbon commands.

## Unsupported customizations

Modifications to Model-driven apps that you make without using either the methods described in this documentation or Power Apps tools aren't supported. Updates or upgrades of model-driven apps don't preserve these modifications. Anything that's not documented in this documentation and supporting documents isn't supported. Unsupported modifications can cause problems when you update through the addition of hot fixes or service packs or upgrade model-driven apps.

The following list includes unsupported action types that are frequently asked about:

- Reusing any model-driven apps JavaScript code. This code might change or be overwritten during an upgrade.
- Editing a solutions file to edit any solution components other than ribbons, forms, SiteMap, or saved queries isn't supported. For more information, see [When to edit the customizations file](when-edit-customization-file.md).
    - Defining new solution components by editing the solutions file isn't supported.
    - Editing web resource files exported with a solution isn't supported.
    - Except for the steps documented in [Maintain managed solutions](/power-platform/alm/maintain-managed-solutions), editing the contents of a managed solution isn't supported.

- Displaying a form within an IFrame embedded in another form isn't supported.

### See also

[Supported customizations for Dataverse](../data-platform/supported-customizations.md)<br/>
[Apply business logic using client scripting in model-driven apps using JavaScript](client-scripting.md)<br/>
[Customize commands and the ribbon](customize-commands-ribbon.md)<br/>
[Web resources in model-driven apps](web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

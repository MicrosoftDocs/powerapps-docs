---
title: "Get started with model-driven apps customization using code | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can customize model-driven apps by using tools that are available in Power Apps or that are described in the documentation. " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/15/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "Nkrb" # GitHub ID
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
---
# Get started with Model-driven apps customization using code

You can customize model-driven apps by using tools that are available in Power Apps or that are described in the documentation. These customizations are supported and can be upgraded.

Customizations made using methods other than those described here are unsupported and could cause problems during updates and upgrades to model-driven apps. For more information, see [Unsupported customizations](#unsupported-customizations) later in this topic.

Topics covered in technical articles published on Microsoft sites such as this one are supported, but might not be upgradable.


## Customizations using Power Apps

There are a variety of tools included with model-driven apps that you can use to customize them. Customizations made using the model-driven apps tools are fully supported and fully upgradeable.

The following customization methods can be used to produce fully supported customizations:

- Customization in Power Apps or solution explorer. For more information, see [Overview of building model-driven apps](../../maker/model-driven-apps/model-driven-app-overview.md)

- Settings in the web application. For more information, see [Administer model-driven apps](../../maker/model-driven-apps/model-driven-app-overview.md).

- Reporting Services. For more information, see [Reporting and analytics guide for model-driven apps](../../maker/model-driven-apps/add-reporting-to-app.md).

> [!NOTE]
> The behavior of model-driven apps depend on customizations applied to the associated Microsoft Dataverse. More information: [Supported customizations for Dataverse](../data-platform/supported-customizations.md)
> *Fully supported* means that developer support can provide assistance for customizations and that application support can help customers running those modifications.


## Customizations applied using code

The documentation on this site for developers, technical articles, sample code published on this site, and information released by the Dataverse Developer Support Team are included in the area of customizations applied using code. The specific actions and levels of supportability and upgradeability are described later in this topic.

### Client-side JavaScript

You can use JavaScript within model-driven apps in three areas:

- **Form Script event handlers**: You can configure form event handlers to call functions defined in JavaScript web resources.

- **Command bar (ribbon) commands**: You can use the `<CustomRule>` or `<JavaScriptFunction>` elements to define actions that call functions defined within JavaScript web resources.

- **Web resources and IFRAMEs**: You can use JavaScript web resources within HTML web resources. IFRAMES configured to allow cross-site scripting, or scripts within HTML web resources included in a form may interact with the documented `Xrm.Page` or `Xrm.Utility` methods within the form via the parent reference.

All interaction with the application pages must only be performed through the methods documented in the [Client API Reference for model-driven apps](clientapi/reference.md). Directly accessing the Document Object Model (DOM) of any Model-driven apps page is not supported. The use of jQuery in form scripts and commands is not recommended. More information: [Client scripting in model-driven apps using JavaScript](client-scripting.md).

You can open model-driven apps forms, views, dialogs, and reports using the methods documented in [Open forms, views, dialogs, and reports with a URL](open-forms-views-dialogs-reports-url.md).

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

### Ribbon customization

Use of `RibbonDiffXml` to add, remove, or hide ribbon elements is supported. Reuse of ribbon commands defined by Model-driven apps is supported; however, we reserve the right to change or deprecate the available commands. Reuse of JavaScript functions defined within ribbon commands is not supported.

## Unsupported customizations

Modifications to Model-driven apps that are made without using either the methods described in this documentation or Power Apps tools are not supported and are not preserved during updates or upgrades of model-driven apps. Anything that is not documented in this documentation and supporting documents is not supported. Additionally, unsupported modifications could cause problems when you update through the addition of hot fixes or service packs or upgrade model-driven apps.

The following is a list of unsupported action types that are frequently asked about:

- The reuse of any model-driven apps JavaScript code. This code may change or be overwritten during an upgrade.
- Editing a solutions file to edit any solution components other than ribbons, forms, SiteMap, or saved queries is not supported. For more information, see [When to edit the customizations file](when-edit-customization-file.md).
    - Defining new solution components by editing the solutions file is not supported.
    - Editing web resource files exported with a solution is not supported.
    - Except for the steps documented in [Maintain managed solutions](/power-platform/alm/maintain-managed-solutions), editing the contents of a managed solution is not supported.

- Displaying a form within an IFrame embedded in another form is not supported.

### See also

[Supported customizations for Dataverse](../data-platform/supported-customizations.md)<br/>
[Apply business logic using client scripting in model-driven apps using JavaScript](client-scripting.md)<br/>
[Customize commands and the ribbon](customize-commands-ribbon.md)<br/>
[Web resources in model-driven apps](web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
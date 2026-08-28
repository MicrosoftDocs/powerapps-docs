---
title: Build and edit model-driven apps with AI code generation tools (preview)
description: Learn how to use AI code generation tools to build and edit model-driven apps in Power Apps from natural-language requirements.
author: jasongre
ms.author: jasongre
ms.reviewer: matp
ms.date: 08/27/2026
ms.topic: how-to
ms.service: powerapps
ms.subservice: mda-maker
search.audienceType:
- maker
- developer
ms.collection:
- bap-ai-copilot
applies_to:
- PowerApps
---

# Build and edit model-driven apps with AI code generation tools (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Use the model app builder skill with an AI code generation tool, such as GitHub Copilot CLI or Claude Code, to build and edit model-driven apps from natural-language requirements. Start by describing the business process or app you need instead of creating each table, form, view, and other component individually.

The skill turns your requirements into an application plan that you can review before it makes changes. The skill then creates the model-driven app and its supporting Microsoft Dataverse artifacts in your Power Platform environment. You can continue to refine the app with natural-language instructions or use the standard designers in [Power Apps](https://make.powerapps.com).

> [!IMPORTANT]
> The model app builder skill is a preview capability under active development. Its app spec schema and command-line options might change between releases. Review the proposed plan before approving and validate the generated app before using in production.

## What you can do with the model app builder skill

Use the skill to:

- Create a model-driven app from a description of a business scenario.
- Plan the app around user personas and the jobs they need to accomplish.
- Review the app spec and build plan before the skill writes artifacts to your environment.
- Create supporting tables, columns, relationships, forms, views, charts, and sample data.
- Create generative pages for experiences that go beyond standard forms and views.
- Create a sitemap with custom icons for each table.
- Add JavaScript validation rules to forms.
- Add security roles based on the planned personas and data access needs.
- Edit an existing model-driven app by describing the changes you want.
- Verify the deployed app against the approved specification.

The skill chooses standard model-driven app artifacts where they fit the scenario. The skill can use generative pages for experiences that require a more tailored user interface beyond forms and views, like dashboards, guided workflows, and data exploration. Sitemap icons and JavaScript validation logic are created as web resources and connected to the appropriate app components during implementation.

## How the model app builder skill works

The skill uses an interactive, multistep authoring process:

1. Describe the business scenario. Explain the app or process you want to support. The skill can ask follow-up questions to clarify the users, data, workflows, and desired experience.
1. Review the app spec. The skill presents an app spec that can include personas, jobs to be done, tables, relationships, forms, views, charts, JavaScript validation rules, generative page intents, and the app sitemap with a proposed icon for each table. Review and refine the specification before continuing.
1. Review the build plan. The skill validates the app spec and presents a dry-run plan in the conversation, grouped by build phase. No app artifacts are created until you approve the plan.
1. Generate app artifacts. After approval, the skill builds the Dataverse schema, app, pages, and supporting artifacts. It creates web resources for the planned sitemap icons and JavaScript validation logic and wires them to the appropriate app components.
1. Verify the app. When verification is enabled, the skill compares the deployed app with the approved app spec.
1. Continue iterating. Describe targeted changes in the AI code generation tool or open the generated artifacts in Power Apps.

> [!IMPORTANT]
> Review and test new or edited artifacts for correctness, security, accessibility, and compliance with your organization's standards before sharing the app.

## Prerequisites

Install and configure the following software before you use the skill.

| Component | Minimum version | More information |
|-----------|-----------------|------------------|
| Node.js | Current long-term support (LTS) version | [Download Node.js](https://nodejs.org/) |
| Power Platform CLI (PAC CLI) | 2.7.0 or later | [Install Power Platform CLI](/power-platform/developer/cli/introduction) |
| Azure CLI | Latest | [Install Azure CLI](/cli/azure/install-azure-cli) |
| GitHub Copilot CLI, Claude Code, or another supported AI code generation tool | Latest | [GitHub Copilot CLI](https://github.com/features/copilot/cli/) or [Claude Code](https://claude.ai/code) |

You also need:

- A Power Platform environment where you have permission to create and modify Dataverse and model-driven app artifacts.
- An authenticated PAC CLI profile connected to the target environment. More information: [Authenticate Power Platform CLI](/power-platform/developer/cli/reference/auth)
- An authenticated Azure CLI session. Run `az login` with the same identity used by the active PAC CLI profile.

## Install the plugin

Run the installer to set up all Power Platform plugins in either PowerShell or a Windows command window.

```powershell
iwr https://raw.githubusercontent.com/microsoft/power-platform-skills/main/scripts/install.js -OutFile install.js; node install.js; del install.js
```

```dos
curl -fsSL https://raw.githubusercontent.com/microsoft/power-platform-skills/main/scripts/install.js | node
```

The installer detects supported AI code generation tools, registers the Power Platform Skills marketplace, installs the plugins, and enables automatic updates.

After installation, restart your AI code generation tool if needed.

To install only the Power Apps plugin for GitHub Copilot CLI or Claude Code:

1. Add the Power Platform Skills marketplace: `/plugin marketplace add microsoft/power-platform-skills`
1. Install the Power Apps plugin: `/plugin install model-apps@power-platform-skills`
1. Restart your AI code generation tool if needed.

> [!NOTE]
> For Claude Code, you can install the plugin with different scopes, such as global, local, or user. Depending on the scope, you need to be in the correct directory for Claude Code to use the plugin. More information: [Extend Claude with skills](https://code.claude.com/docs/en/skills#share-skills)

> [!TIP]
> Turn on automatic updates for the marketplace and skills. The model app builder skill is updated frequently during preview.

> [!NOTE]
> If you only need to create or edit generative pages in an existing model-driven app, use the separate generative pages skill. More information: [Create and edit generative pages with AI code generation tools](generative-page-external-tools.md)

## Create a model-driven app

1. Start a conversation with your AI code generation tool.
1. Invoke `/app-builder`, or describe the app you want to create. For example:

   - "Build an app to manage supplier onboarding and contract approvals."
   - "Create a model-driven app for tracking service requests across multiple teams."
   - "Build an equipment inspection app for field technicians and dispatchers."

1. Answer the skill's questions about the business process, users, data, workflows, and app experience.
1. Review the proposed app spec. Check that the personas, jobs to be done, tables, relationships, forms, views, charts, JavaScript validation rules, generative pages, navigation, and planned sitemap icons support the business scenario. Ask the skill to revise the specification as needed.
1. Review the dry-run build plan. Approve the plan only when its proposed changes match your intent.
1. Allow the skill to build the app and supporting artifacts.
1. Choose the optional verification step to reconcile the deployed app with the approved app spec.
1. Open the app in Power Apps, test its primary user scenarios, and inspect the generated artifacts.

## Edit an existing model-driven app

Use the same skill to make targeted changes to an existing app.

1. Invoke `/app-builder` and identify the app you want to update. For example:

   - "Update the Field Service app to support equipment inspections."
   - "Add an Invoices table and related forms and views to the Supplier Management app."
   - "Add a generative page that gives dispatchers an overview of overdue work orders."

1. Confirm the existing app that the skill should retrieve.
1. Review the editable app spec created from the deployed app.
1. Review the proposed changes and dry-run plan before approving the build.
1. Build, verify, and test the updated app.

## Continue customizing and extending in Power Apps

Artifacts created by the model app builder skill are standard Power Apps and Dataverse artifacts. After initial generation, you can continue to iterate and refine the app using the skill, or you can use [Power Apps](https://make.powerapps.com) and its designers to modify generated artifacts or create new artifacts manually. For example, you can:

- Refine forms, views, charts, and navigation.
- Update tables, columns, and relationships.
- Add or edit generative pages.
- Create new tables, forms, views, charts, pages, and other app components.
- Adjust security roles and sharing.
- Extend the app with other Power Platform customization tools.

> [!NOTE]
> The model app builder skill doesn't currently support every model-driven app artifact or concept. Use Power Apps designers and other Power Platform tools to add or modify unsupported components.

Changes made outside the skill can affect later AI-assisted edits. Before approving another build, review the app spec and build plan to ensure they preserve your manual customizations.

## Best practices

- Start with the business process, intended users, and their goals. Provide detailed requirements when you know exactly what you want, or use a broader description to give the skill more room to propose a design.
- Review and refine the app spec until it accurately reflects the app you want. Investing time in the plan reduces rework during implementation.
- Consider the skill's suggestions for rounding out the app, including supporting data, experiences, navigation, and validation.
- Test the primary tasks for every persona represented in the app spec.

## Related content

- [Steps to building a model-driven app](app-building-steps.md)
- [Overview of the model-driven app designer](app-designer-overview.md)
- [Create and edit generative pages with AI code generation tools](generative-page-external-tools.md)
- [Power Platform CLI reference](/power-platform/developer/cli/reference/index)
- [Model app builder skill on GitHub](https://github.com/microsoft/power-platform-skills/blob/main/plugins/model-apps/README.md#app-builder)

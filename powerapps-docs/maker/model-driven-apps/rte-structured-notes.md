---
title: Configure structured content in the rich text editor (preview)
description: Configure Copilot-powered templates to generate consistent, formatted content in the rich text editor in model-driven apps.
ms.topic: how-to
ms.date: 07/10/2026
ms.author: laalexan
author: lalexms
ms.reviewer: mpeart
ms.service: powerapps
ms.subservice: mda-maker
ms.preview: true
---

# Configure structured content in the rich text editor (preview)

> [!NOTE]
> This feature is currently in public preview and might change before it becomes generally available.

Structured content in the rich text editor (RTE) enables users to generate consistent, formatted responses by using Copilot-powered templates directly within supported experiences in model-driven apps. This capability helps standardize communications and improve productivity by reducing manual content creation.

After administrators configure structured content templates, users can apply templates to free-form content in records that use the rich text editor control. At runtime, Copilot generates structured output.

## Prerequisites

To use structured content in the rich text editor, the administrator must make sure the following prerequisites are met:

- The Copilot control is added to the rich text editor. Learn more in [Add the Copilot control to the rich text editor](/power-apps/maker/model-driven-apps/copilot-control).
- Pay-as-you-go billing is set up. Learn more in [Manage consumption-based billing and capacity](/dynamics365/customer-service/administer/setup-pay-as-you-go).
- Cross-geo settings are enabled. Learn more in [Move data across regions for Copilots, AI agents, and generative AI features](/power-platform/admin/geographical-availability-copilot).

## Turn on the structured content feature

A single admin setting controls the structured content feature. When you turn it on in one model-driven admin app, it applies to all model-driven apps in the environment.

1. Sign in to the admin center for your model-driven app, such as the Copilot Service admin center.
1. In the navigation pane, go to **Productivity** > **Prompt-based templates**.
1. Select the **Structured content for the rich text editor** checkbox.
1. Select **Save**.

## Configure structured templates

Administrators configure structured content templates so that users can generate structured responses. Templates determine how free-form content is organized when Copilot generates structured output.

To configure structured templates, complete the following steps:

1. In the admin configuration area, select **Productivity** > **Prompt-based templates** > **Create or Edit templates**.
1. Select **New**.
1. Enter the following details:
   - **Name**: The name of the template shown to users.
   - **Description**: Optional admin-facing information about the template.
   - **Structuring prompt**: Natural language instructions that tell Copilot how to organize the content.
1. Select **Save**.

> [!NOTE]
> If your organization uses custom rules for structured templates, other user privileges might be required. Out-of-box rules automatically apply required privileges.

## Runtime experience

After administrators configure structured templates, users can apply templates while creating or editing content in supported experiences.

To generate structured content by using Copilot:

1. Open a supported experience that contains a rich text editor field.
1. Enter or paste the content that you want to structure.
1. In the editor, select the **Write with Copilot** icon.
1. Select a structured template.
1. Select **Rewrite**.
1. Review the structured output.
1. If the output looks correct, apply the rewritten content.

> [!IMPORTANT]
> Always review AI-generated content before using it.

## Usage and billing

Structured content generation is a utilization-based feature.

During public preview, a grace period is available for evaluation and development purposes. After general availability, usage might be billed based on Copilot consumption.

## Error messages

Errors can occur when creating, testing, or using structured templates if any of the following scenarios are true:

- You disable Copilot after enabling the feature.
- You exhaust your Copilot usage credits.
- Required prerequisites aren't configured.

Contact your administrator if the issue persists.

## Related information

- [Add the rich text editor control to a model-driven app](rich-text-editor-control.md)
- [Add the Copilot control to the rich text editor](copilot-control.md)

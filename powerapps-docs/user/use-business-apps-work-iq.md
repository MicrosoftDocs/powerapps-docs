---
title: Use Business Applications in Work IQ (preview)
description: Learn how to use Work IQ to find and work with data in Power Apps model-driven apps.
author: shwetamurkute
ms.component: pa-user
ms.topic: how-to
ms.date: 09/25/2026
ms.subservice: end-user
ms.author: smurkute
ms.reviewer: smurkute
ms.service: powerapps
ai-usage: ai-assisted
search.audienceType:
  - enduser
ms.collection:
  - bap-ai-copilot
---

# Use Business Applications in Work IQ (preview)

[This article is prerelease documentation and is subject to change.]

Power Apps model-driven apps are available as Business Applications in Work IQ. You can use natural-language prompts to find and work with business data without opening the model-driven app. Work IQ applies Copilot reasoning to the data and app components that you already have permission to access.

You can work with Business Applications by using an agent, or through a chat experience powered by Work IQ Model Context Protocol (MCP). Start a conversation, select an environment and app when prompted, and then describe the information or action you need. Work IQ uses the app's views, forms, and tables to complete the request.

> [!IMPORTANT]
>
> - This feature is in preview.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520). They're available before an official release so that customers can get early access and provide feedback.

> [!NOTE]
>
> Copilot Credits apply to this feature. For information about billing, see the [Power Platform licensing guide](https://go.microsoft.com/fwlink/?linkid=2085130).

## Prerequisites

- You need access to the Work IQ experience where you want to use Business Applications.
- A Power Platform administrator must enable Work IQ for the environment in the Power Platform admin center.
- For the model-driven app, the **Enable M365 Copilot in model-driven apps** setting (`m365copilotmodelappenabled`) must be set to **Default** or **On**. For configuration instructions, see [Enable Microsoft 365 Copilot in a single model-driven app](../maker/model-driven-apps/add-microsoft-365-copilot.md#enable-microsoft-365-copilot-in-a-single-model-driven-app).
- You need permission to access the Power Platform environment, model-driven app, and business data involved in your request.

Work IQ respects your existing Power Platform security permissions. You can only select environments and applications, view data, and perform actions that your permissions allow.

## Work with a Business Applications

1. Start a conversation in an experience that supports Business Applications in Work IQ.
2. Select a Power Platform environment from the environments available to you.
3. Select the model-driven app that contains the business data you want to use.
4. Enter a prompt that describes the records you want to find or the action you want to perform.
5. Review the response. For an operation that changes data, review the proposed values, make any needed changes, and explicitly confirm the operation before it's submitted.

For example, ask Work IQ to list records from an app view, show the details of a record, create a record with the values in your prompt, or update an existing record. You can continue the conversation to refine a request or analyze the returned business data.

## Supported app components and capabilities

| Component | Capabilities |
|---|---|
| Views and record lists | - List records from the table's default system view, or name another system view in your prompt. <br> - The selected view determines the records and fields that are returned. <br> - Add filters in your prompt to further refine the view results. |
| Forms and record details | - Read, create, and update records by using the default main form, or name another main form in your prompt. Create and update operations aren't available for forms that use unsupported JavaScript event handlers. For more information, see [Known limitations](#known-limitations). <br> - Work IQ uses the fields on the first tab of the selected form. <br> - Before deleting a record, Work IQ presents the record's fields so you can verify that you selected the correct record. |
| Form fill and confirmation | - For create and update operations, Work IQ maps values from your prompt to the corresponding form fields. <br> - Review, add, or change values before you confirm and submit the operation. <br> - Delete operations also require explicit confirmation. <br> - After a create or update operation, use the record link in the response to open the record in the model-driven app. |
| Form behavior and validation | - Create and update operations enforce form control metadata, including whether a field is writable, required, or read-only. <br> - Form-scoped and table-scoped business rules are evaluated and enforced. <br> - Table security determines whether you can change, read, or access the data. |

## Known limitations

- You can't create or update a record when the selected form has JavaScript `OnLoad`, `OnChange`, or `OnSave` event handlers. Work IQ can't enforce these handlers in the headless experience. Use the link in the response to open the form or record in the model-driven app, and make the change there.
- Custom controls and subgrids aren't supported.

## Related information

- [Work IQ overview](/microsoft-365/copilot/extensibility/work-iq/)
- [Use Microsoft 365 Copilot in model-driven apps](use-microsoft-365-copilot-model-driven-apps.md)

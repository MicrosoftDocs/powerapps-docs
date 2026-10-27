---
title: Build canvas apps with the authoring agent in Power Apps canvas studio (preview)
description: Learn how to use the authoring agent in Power Apps canvas studio to plan, build, and refine canvas apps from a natural-language description.
author: tashasev
ms.author: tashas
ms.reviewer: joshuapa
ms.topic: how-to
ms.date: 10/22/2026
ms.subservice: canvas-maker
ms.collection: 
    - bap-ai-copilot
ms.update-cycle: 180-days
search.audienceType:
  - maker
contributors:
  - tashas
  - joshuapa
ai-usage: ai-assisted
---

# Build canvas apps with the authoring agent in Power Apps canvas studio (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The authoring agent in Power Apps canvas studio builds and edits canvas apps from a description you write in plain language. You describe the app you have in mind, the agent proposes a plan, and after you approve it, the agent builds the screens, controls, and Power Fx formulas directly in the app you have open. The result is a regular canvas app that you can keep refining using AI or by hand in studio.

> [!IMPORTANT]
>
> - This preview feature is available only in the United States.
> - Only English language is supported.
> - Preview features aren't meant for production use and might have restricted functionality. Microsoft provides these features before an official release so that customers can get early access and provide feedback.
> - AI-generated content might be incorrect. Review the plan and the generated app before you share it with users.

## Prerequisites

- A Power Apps environment where you can create and edit canvas apps.
- Your administrator must enable the authoring agent preview capability.
- A GitHub account that you can connect to the authoring agent. The authoring agent uses GitHub to run the canvas app authoring tools, and GitHub bills that account for usage.

## Enable GitHub account connections
Enabling GitHub account connections requires tenant administrator permissions. When you enable this feature, you make the authoring agent available, but makers still need to sign in by using a GitHub account to use the capability. Usage is billed through your existing GitHub billing plan.

1. In the [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/), go to **Manage** > **Tenant Settings**.
1. Locate the setting for **Agentic Coauthoring in Power Apps using GitHub**.
1. Read the terms carefully. Enable the setting to indicate that you accept the terms for this feature.

## Open the authoring agent and connect GitHub

1. In [Power Apps](https://make.preview.powerapps.com), create a canvas app or open an existing one for editing.
1. Add the data sources your app needs. For example, select **Add data** and add your Dataverse tables or SharePoint lists.
1. On the left rail, select **Authoring agent**.

   :::image type="content" source="media/canvas-authoring-agent/01-open-authoring-agent.png" alt-text="Screenshot of Power Apps Studio with the Authoring agent pane open, showing Connect your GitHub account with the Connect GitHub button and terms of use." lightbox="media/canvas-authoring-agent/01-open-authoring-agent.png":::

1. The first time you open the pane, select **Connect GitHub**, and then sign in to GitHub using the GitHub authentication modal.

After you connect, the pane shows your connected GitHub account and suggested prompts to help you get started.

:::image type="content" source="media/canvas-authoring-agent/03-agent-pane-suggested-prompts.png" alt-text="Screenshot of the connected Authoring agent pane with suggested prompts, the message box, and the model name." lightbox="media/canvas-authoring-agent/03-agent-pane-suggested-prompts.png":::

The authoring agent pane includes:

| Element | Description |
|---|---|
| Suggested prompts | Starting points such as **Build a team task tracking app**, **Build an inventory management app**, and **Build an employee onboarding app**. |
| Message box | Where you describe what to build or change. The placeholder reads **Ask the agent to build or edit your app**. |
| Model | The model the agent uses, for example **GPT-5.6 Terra**. |
| Token usage | Shows token usage for your session. |
| Disconnect account | Shown under the "..." ellipsis. Disconnects your GitHub account from the authoring agent. |

## Describe your app

1. In the message box, describe the app you want. Be specific about who uses the app, what they need to do, and which data they work with.

    For example:

    *"Create an app for attendees for an internal event. Attendees should be able to search for sessions by date/time, speaker name, session title, and topic area. They should be able to see event session details and add them to an itinerary. Attendees should be able to view and manage their itinerary by day. They should be able to see speaker profile information. They should also be able to see general information about the event like address, directions, attire, etc."*

    :::image type="content" source="media/canvas-authoring-agent/05-prompt-entered.png" alt-text="Screenshot of a detailed app description entered in the Authoring agent message box." lightbox="media/canvas-authoring-agent/05-prompt-entered.png":::

1. Select the send button.

The agent starts working. A **Task in progress** list shows each step as the agent reviews your app, explores your data, and plans the screens and design. Select a step to expand its details, or select **Show all** to see every step. While the agent works, the send button changes to a stop button. You can stop the in-progress agent if needed.  

:::image type="content" source="media/canvas-authoring-agent/06-task-in-progress.png" alt-text="Screenshot of the Task in progress list in the Authoring agent pane while the agent plans the app, showing completed tasks and some still in progress." lightbox="media/canvas-authoring-agent/06-task-in-progress.png":::

## Review and approve the plan

Before it changes your app, the agent shows a **Canvas App Plan**. The plan describes:

- The screens it plans to create and what each one does.
- How it will use data in your app.
- Any assumptions or limitations. Using the prompt above as an example, if the agent can't verify how to identify the signed-in user in your data, it says so and explains the approach it intends to take instead.

Read the plan carefully, especially the assumptions, and then choose how to continue:

1. Under **Allow this action?**, select one of the following options:
    - **Yes, continue**: Allow the agent to build the app as planned.
    - **Suggest changes**: Tell the agent how to revise its approach by using the text input area. 
1. Select **Submit**.

:::image type="content" source="media/canvas-authoring-agent/07-plan-approval.png" alt-text="Screenshot of the Canvas App Plan and the Allow this action approval card with Yes, continue and Suggest changes options." lightbox="media/canvas-authoring-agent/07-plan-approval.png":::

## Let the agent build your app

After you approve the plan, the agent builds the app. It writes the app's screens, controls, and formulas, checks its work, and fixes any errors it finds before it finishes. Progress messages in the pane tell you what the agent is doing, including when it finds and repairs problems.

While the agent applies changes, Studio might show **Loading** and refresh the canvas. Larger apps can take several minutes to build. You might see app checker errors on the canvas while the agent is still working. Wait until the task is complete before you review the results.

When the agent finishes, the pane shows **Task completed** and a summary of what it built, including any limitations to be aware of.

:::image type="content" source="media/canvas-authoring-agent/09-finished-app-task-completed.png" alt-text="Screenshot of the completed task summary in the Authoring agent pane next to the generated session search screen on the canvas." lightbox="media/canvas-authoring-agent/09-finished-app-task-completed.png":::

## Review and refine the generated app

The generated app is a regular canvas app. Use the tools provided in canvas studio to review and refine it:

- Open **Tree view** to see the generated screens and controls. The agent uses responsive containers, modern controls, and descriptive control names.
- Select controls to inspect and edit their properties and Power Fx formulas.
- Preview the app to try it as a user would by using the **Play** button.
- Ask the agent for more changes by describing them in the message box.
- Save and publish the app when you're ready.

To give feedback on a response, use the thumbs up or thumbs down button below it. 

## Tips for better results

- **Add your data first.** The agent builds on the data sources already in your app.
- **Describe users and tasks, not just screens.** Say who uses the app and what they need to accomplish.
- **Read the assumptions in the plan.** If the agent can't verify something, such as how to identify the current user or a field it needs, it tells you. Use **Suggest changes** to correct its approach before it builds.
- **Expect to refine.** Treat the result as a strong starting point, and review it before you share the app.

## Known limitations

- AI-generated content might be incorrect. Always review the plan and the generated app.
- The canvas updates when the agent applies its changes, so you might not see the app take shape until the agent is well into the build.
- The agent can't add data to the app or edit data in the app.
- The agent can't add images to the app.
- The agent can't save, publish, or share the app.
- You can't use the agent to create something that Power Apps doesn't support.
- You can't change the model used in the studio integration.
- This capability is available only in the United States.
- Only English is supported.

## Frequently asked questions

### How does the authoring agent use my data?

When you connect your GitHub account, the following notice appears in the authoring agent pane:

*"This feature uses your GitHub account, and GitHub will bill the account for this usage. Your prompts and application context will be sent to GitHub to be processed and stored under the GitHub terms applicable to your or your organization's GitHub account and either the GitHub General Privacy Statement or GitHub DPA."*

To learn more about how GitHub processes data, use the links provided in the pane.

### Why does the authoring agent need my GitHub account?

The authoring agent uses GitHub to run the canvas app authoring tools. Your prompts and application context are processed under the GitHub terms that apply to your account, and GitHub bills your account for usage.

### Can I use the authoring agent with an existing app?

Yes, the authoring agent can be used with any pre-existing canvas app in environments that meet eligibility requirements for the authoring agent.  

### How is this different from the Canvas Authoring MCP plugin?

The Canvas Authoring MCP plugin lets you author canvas apps from your own coding agent, such as GitHub Copilot CLI or Claude Code. The authoring agent brings agentic authoring directly into Power Apps Studio. While some canvas app makers are comfortable using coding agents, others prefer to work directly in canvas studio. 

## Related information

- [Create and edit canvas apps with AI code generation tools](/power-apps/maker/canvas-apps/create-canvas-external-tools)
- [Overview of modern controls and themes in canvas apps](/power-apps/maker/canvas-apps/controls/modern-controls/overview-modern-controls)
- [Building responsive canvas apps](/power-apps/maker/canvas-apps/build-responsive-apps)
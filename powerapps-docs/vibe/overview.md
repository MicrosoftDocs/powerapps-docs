---
title: Overview of the new Power Apps vibe experience
description: Discover the new AI-native Power Apps vibe code experience. Build apps with generated code, automate workflows, and integrate data seamlessly—no coding expertise is required.
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.date: 01/29/2026
ms.topic: concept-article
ms.custom: CXT 
---

#  Overview of the new Power Apps vibe experience (preview)

[This article is prerelease documentation and is subject to change.]

The new Power Apps vibe experience is an AI-native platform that builds solutions to business problems, including requirements, data, and full apps with generated code. You can automate workflows, integrate data sources seamlessly, and accelerate app development without extensive coding knowledge.

## Why choose Power Apps vibe?

The vibe experience transforms how you build business applications by combining three key capabilities in a single, integrated workspace:

- **Rapid prototyping**: Go from idea to working app in minutes, not weeks. Simply describe your business needs in natural language, and AI generates a complete solution including data models, business logic, and user interface.

- **Unified development**: Instead of switching between separate tools for planning, data modeling, and app building, work with everything in one place. Make changes to your plan, data, or app, and see updates automatically reflected across all components.

- **AI-powered assistance**: Get intelligent suggestions, code generation, and guided problem-solving throughout the development process. The AI understands your business context and helps you make better architectural decisions.

**Ideal for**: Business analysts, citizen developers, and professional developers who want to build line-of-business applications quickly without getting bogged down in technical implementation details.

**Common use cases**: Employee onboarding apps, inventory management systems, project tracking tools, customer feedback applications, and departmental workflow solutions.

Watch this video to see the vibe experience in action. The video demonstrates how to create a complete business application from a simple text description:
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=085271a3-bec6-4740-89df-044f984466d2]

After watching the video, explore the detailed walkthrough in [Create apps, data, and plans together](create-app-data-plan.md) to understand the full development process.

> [!IMPORTANT]
>
> - This feature is in preview.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites 

- An tenent admin must enable Copilot for the tenant. To enable Copilot, admins should:
  1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
  1. In the navigation pane, go to **Settings** to open the **Tenant settings**  page. 
  1. Set the toggle for **Copilot in Power Apps (preview)** to **On**.
  1. Select **Save** to apply the changes.
  
  For more information, see [Tenant settings](/power-platform/admin/tenant-settings).
- This capability isn't available in a default environment.
- This capability is currently available only in the US, Australia, Asia, and India region, and only in English. For more information, see [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).

### Troubleshooting connectivity issues

If you're experiencing connection errors or cannot access environments:

- **Verify environment region**: Ensure you have access to an environment located in the US, Australia, Asia, or India region. You can check your environment region in the [Power Platform admin center](https://admin.powerplatform.microsoft.com):
   1. Sign in to the Power Platform admin center
   1. In the navigation pane, select **Manage** > **Environments**
   1. Locate the **Region** column to see where your environments are hosted

For additional support with connectivity issues, contact [Power Platform support](https://powerapps.microsoft.com/support/).


## Access Power Apps vibe

You can access the new vibe experience in one of two ways:

- Go to [https://vibe.powerapps.com](https://vibe.preview.powerapps.com/) and sign in to start using the new experience.

- Alternatively, sign in to [Power Apps](https://make.preview.powerapps.com/). At the top, select **Try new experience (Preview)** to enable it.

   :::image type="content" source="media/overview/new-experience.png" alt-text="Screenshot of Try new experience preview button in Power Apps interface":::

   > [!NOTE]
   > If you access the new experience through [Power Apps](https://make.preview.powerapps.com/), you need to enable it each time you sign in.

## Navigation

The left navigation shows the following items:


:::image type="content" source="media/overview/left-navigation-pane.png" alt-text="Screenshot of the left navigation pane in the new Power Apps experience.":::

Legend:

1. **Home**: Returns you to the main landing page.
1. **Plans**: Access and manage your plans.
1. **Apps**: Open, play, or edit apps you created or that others shared with you.
1. **Profile**: Access the environment picker, session details, notifications, and settings.


## Enter your prompt to build apps

Describe your idea using natural language.

:::image type="content" source="media/overview/enter-prompt.png" alt-text="Screenshot of the prompt writing interface with enhance prompt button.":::


Legend:

1. **Enter prompt**: Type a description of what you want to build.

1. **Enhance prompt**: (Optional) Use this button to add more detail to your prompt before generating your app.

1. **Suggestions**: Want to experiment? Select one of the suggestions to explore the new app-building experience.

## Next steps

 [Create apps, data, and plans together (preview)](create-app-data-plan.md)

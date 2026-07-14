---
title: "Quickstart: Build a code app with GitHub Copilot"
description: Build, deploy, and share a code app from a natural-language prompt by using the GitHub Copilot CLI with the code apps plugin.
#customer intent: As a developer, I want to know how to build, deploy, and share a code app from a natural-language prompt by using the GitHub Copilot CLI with the code apps plugin.
ms.topic: quickstart
ms.collection: bap-ai-copilot
ms.author: jordanchodak
ms.reviewer: jdaly
author: jordanchodakWork
ms.date: 06/24/2026
---

# Quickstart: Build a code app with GitHub Copilot

This quickstart shows you how to go from a natural-language prompt to a deployed code app by using the [GitHub Copilot CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli/about-github-copilot-in-the-cli) with the code apps plugin.

## Prerequisites

- [Node.js](https://nodejs.org/) (LTS version) with a terminal of your choice.
- GitHub Copilot enabled for your account or tenant. To set up Copilot, see [Get started with GitHub Copilot](https://docs.github.com/en/copilot/getting-started-with-github-copilot).
- The [GitHub Copilot CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli/installing-github-copilot-in-the-cli) installed and authenticated. This quickstart uses the standalone `copilot` CLI, which supports plugins via `/plugin` slash commands.

   > [!TIP]
   > The code apps plugin also works with [Claude Code](https://www.anthropic.com/claude-code) and other coding agents through [Open Plugins](https://open-plugins.com/). This quickstart uses GitHub Copilot for the step-by-step walkthrough, but the same plugin, prompts, and CLI commands apply; start a session with `claude` instead of `copilot` and continue with the rest of the steps as written.

You don't need to install the code apps CLI separately; the plugin checks and installs dependencies for you the first time you run a skill.

## Install the code apps plugin

Start the Copilot CLI in any terminal:

```bash
copilot
```

In the Copilot session, add the Power Platform plugin marketplace and install the plugin:

```bash
/plugin marketplace add microsoft/power-platform-skills
```

Then install the code apps preview plugin:

```bash
/plugin install code-apps-preview@power-platform-skills
```

The plugin adds code apps skills to Copilot: create app, add connector, deploy, and more. It also orchestrates CLI commands on your behalf.

Close the terminal window after intallation, then re-open Copilot CLI with:

```bash
copilot
```

## Invoke the create-app skill

In your new Copilot session, run the create-app skill:

```bash
/code-apps-preview:create-app
```
Before doing anything else, the agent validates needed prerequisites by checking dependencies, installing anything missing, and confirming you're authenticated against the right tenant. Then, Copilot acknowledges the skill and prompts you to describe the app you want.

## Describe the app in natural language

Type a natural-language description of the app. Include your environment ID that you want the app to be deployed to. For example:

> *Create an app to visualize my organization's hierarchy as represented in Microsoft Entra. Show the hierarchy as a display tree where the leader of the company is at the top, with their direct reports below. Add a layer for each level of employees. The tree initially shows the top two layers. When a person is selected, the app refreshes to show who reports to them.*
>
> *For each user, include a "view profile" button. When clicked, show full name, title, work location, email, and phone number.*
> *Deploy to environment: &lt;environment&gt;*

## Approve the plan and watch the agent build

The agent identifies the needed data sources, the UI, and the interactions. It asks a few questions, then presents a plan for your approval.

When you approve the plan, the agent runs the code apps CLI to:

- Scaffold the project files
- Initialize the app
- Add connectors
- Implement functionality and UI, using the connectors

If you didn't supply your Power Platform environment ID in your prompt, the agent might pause to ask for your environment. Follow the instructions to provide it.

When the agent finishes building, it might ask if you want to deploy. Answer **yes** to make the app live.

## Play and share your app

Your app is now running for users as a code app, governed by Entra ID, [Conditional Access](/entra/identity/conditional-access/policy-block-by-location#create-a-conditional-access-policy), and data loss prevention (DLP), with telemetry and operational health flowing into the admin center. Optionally, iterate with the agent to edit your app the way you want. When ready, open [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) to share the app.

Congratulations! You built, deployed, and shared a code app end-to-end by using GitHub Copilot. You and your users can now view and play the app at [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 

## What just happened?

You didn't scaffold a project, wire up data, or run infrastructure commands. You described what you wanted. The Copilot agent ran the code apps CLI to build and deploy, and the Power Platform provides identity, data governance, audit trail, operational telemetry, and secure sharing. That's the value the platform delivers around your code, so you can stay focused on describing the app you want to build.

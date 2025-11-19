---
title: Connect to Dataverse with model context protocol FAQ
description: Frequently asked questions about using Microsoft Dataverse with a model context protocol server. 
author: ShefaaliP
ms.component: cds
ms.topic: how-to
ms.date: 11/17/2025
ms.subservice: dataverse-maker
ms.author: spatankar
ms. reviewer: matp
search.audienceType: 
  - maker
---
# Connect to Dataverse with model context protocol FAQ

This article provides answers to frequently asked questions about using Microsoft Dataverse with a model context protocol (MCP) server.

## Claude doesn't show Dataverse MCP server at all. What should I do?

Check the claude_desktop_config.json file and verify that the values are correct for your Dataverse environment. Make sure there are no extra spaces or characters in the GUID. Use a JSON editor that validates JSON format to ensure syntax correctness.

## Why do you make a distinction between exit and close Claude desktop?

Because **Exit** and **Close** have different effects. Exit really removes the Claude desktop app from memory and when you start it again, it’s a fresh start. Close just closes the experience but the app is still running.

## I don’t see any authentication experience to reauthorization

Exit Claude desktop and reopen it. Make sure you don’t have any connectivity problems. If the problem persists, check if there are any files in `C:\Users\<user>\AppData\Local\Microsoft.PowerPlatform.Dataverse.MCP\authCache`. If so, delete all, exit Claude desktop, and then reopen Claude desktop.

## I want to sign in with a different account but I don’t get prompted anymore

Exit Claude desktop. Delete the folder `C:\Users\<user>\AppData\Local\Microsoft.PowerPlatform.Dataverse.MCP\authCache`, then Reopen Claude desktop. You're prompted again for authentication.

## I can’t authenticate. What is the problem?

Verify that the GUID for the tenant and URL for the connection are indeed from environment you’ve set up. Go to https://make.powerapps.com and select the environment you’ve set up and verify that the tenant ID value matches the one in your Claude config file for Dataverse MCP server.

Go to https://make.powerautomate.com and ensure you're in the right environment. Go to your connection and ensure that the URL for your connection matches the URL in the Claude config file for Dataverse MCP server.

## I want to review MCP logs to observe what's happening. Where do I find them?

Open the Claude desktop logs at the following locations:

- Claude basic logs: `C:\Users\<user>\AppData\Roaming\Claude\logs`
- Claude verbose logs: `C:\Users\<user>\AppData\Local\Microsoft.PowerPlatform.Dataverse.MCP\logs`

## When using Claude why do I experience out of token or that the conversation is too long and recommends to start a new conversation message?

This is a limitation with the Claude free plan. Consider upgrading to a Claude paid plan. More information: [Claude pricing](https://www.anthropic.com/pricing)

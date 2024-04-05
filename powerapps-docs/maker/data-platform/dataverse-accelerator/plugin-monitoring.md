---
title: Plugin monitoring | Microsoft Docs
description:  Efficiently monitor Dataverse plugin performance and health status in real-time.
author: denise-msft
ms.author: demora
ms.service: powerapps
ms.topic: how-to
ms.date: 04/03/2024
ms.custom: template-how-to
contributors:
- dikamath
---

# Monitoring for developing Dataverse plugins and Custom APIs (preview)

Plugin monitoring introduces an enhanced Trace Log Viewer, providing a modern interface to surface the existing plugin trace log table in Dataverse environments. This feature is designed to streamline development and debugging processes for both low-code and pro-code plugins and Custom APIs. Seamless integration with Dataverse Custom APIs, Dataverse low code plugins, and pro-code plugin run history empowers makers to efficiently monitor and troubleshoot plugin performance.

## Prerequisites

- To access trace logs, users must have at least read privileges to the Plugin Trace Log privilege.
- To enable trace logs, System administrator security role is required.

## Key features

- **Centralized log viewer:** Access and view trace logs from Dataverse Custom APIs, low code plugins, and pro-code plugin executions in an environment from one central location.
- **Filtering capabilities:** Conveniently filter log history to quickly find logs relevant to debugging needs.
- **Seamless integration:** Integrated seamlessly with Dataverse Accelerator, ensuring availability in all environments.

## Installation

To install the Dataverse Accelerator and access the Plugin Monitoring feature, please refer to the [Dataverse Accelerator documentation](./dataverse-accelerator.md), which provides step-by-step installation instructions.

## Usage instructions

Here are the steps to use the Plugin monitoring trace viewer:

### Run the Plugin monitoring page

1. Log in to your Dataverse environment with appropriate credentials.
1. Play the Dataverse Accelerator app
1. Navigate to the **Plugin monitoring** feature, either using the left navigation or the feature card.

### Enable log capturing (for administrators)

If log capturing is not enabled in your environment, system administrators or users with appropriate security roles privilege can enable it.

1. The landing page will display an error state with two options:
    1. Enable all logs
    1. Exception logs only

Access the settings and locate the option to enable log capturing for plugins.

### View logs

Upon enabling logs, you'll start to see a list of existing plugin trace logs.

Logs may be categorized based on the type of plugin (Custom APIs, low code plugins, or pro-code plugins) and execution history.

### Filter logs

Utilize the filtering capabilities to quickly find logs relevant to your debugging needs.

Filter options include filtering by plugin type, execution status (success, failure), date range, or specific keywords.

### Read log details

Click on a specific log entry to view detailed information about the plugin execution. Log details include timestamp, plugin name, execution status, input/output parameters, error messages, and more.

## Best practices

1. **Read log details**
   - Click on a specific log entry to view detailed information about the plugin execution.
   - Log details may include timestamp, plugin name, execution status, input/output parameters, error messages, and more.

1. **Monitor Plugin Performance:**
   - Regularly monitor plugin performance by reviewing trace logs in the Trace Log Viewer.
   - Keep an eye on execution status, error messages, and any anomalies that may indicate performance issues or bugs.

1. **Troubleshoot Issues:**
   - Use the information provided in the trace logs to troubleshoot any issues that arise during plugin execution.
   - Analyze error messages, input/output parameters, and execution details to identify the root cause of the problem.

1. **Take Action:**
   - Based on the insights gathered from trace logs, take appropriate action to address any performance issues or bugs identified.
   - This may involve adjusting plugin configurations, updating code logic, or seeking assistance from other team members or support resources.

1. **Regularly Review Logs:**
   - Make it a habit to regularly review trace logs to ensure ongoing monitoring of plugin performance.
   - Address any issues or anomalies promptly to maintain the overall stability and reliability of your Dataverse environment.

## FAQs

1. **What privileges are required to access the Trace Log Viewer?**
   - Users must have at least read privileges to access and view trace logs.

1. **Who can enable log capturing within the environment?**
   - System administrators with the appropriate security role are able to enable log capturing within their environment.

1. **Can I filter log history to find specific logs?**
   - Yes, the Trace Log Viewer provides filtering capabilities, allowing users to conveniently find logs relevant to their debugging needs.

1. **Is the Plugin Monitoring feature available in all environments?**
   - Yes, the feature is delivered through the Dataverse Accelerator and is available in all environments.

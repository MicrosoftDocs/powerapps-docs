---
title: "Tutorial: Debug a plug-in (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to debug a Microsoft Dataverse plug-in with Plug-in Profiler and replay execution in Visual Studio to find issues fast." 
ms.date: 03/30/2026
ms.reviewer: "pehecke"
ms.topic: tutorial
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
  - PHecke
---
# Tutorial: debug a plug-in

This tutorial shows you how to debug a plug-in in Microsoft Dataverse by using Plug-in Profiler. Use it to replay execution in Visual Studio and troubleshoot faster.

- [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md)
- Tutorial: Debug a plug-in (This tutorial)
- [Tutorial: Update a plug-in](tutorial-update-plug-in.md)

For detailed explanations of supporting concepts and technical details, see:

- [Use plug-ins to extend business processes](plug-ins.md)
- [Write a plug-in](write-plug-in.md)
- [Register a plug-in](register-plug-in.md)
- [Debug Plug-ins](debug-plug-in.md)

## Goal

Because the plug-in executes on a remote server, you can't attach a debugger to the plug-in process. The plug-in profiler captures a profile of an executing plug-in and allows you to replay the execution of the plug-in by using Visual Studio on your local computer.

## Prerequisites

- All the prerequisites for  [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md) apply. See [Prerequisites](tutorial-write-plug-in.md#prerequisites). The exception is that Visual Studio 2019 or later is required to install and use Power Platform Tools.
- If you didn't complete the previous tutorial, you can use the general steps in this tutorial with a different registered plug-in.

## Install plug-in profiler

You can run the Plug-in Profiler from two tools: the Plug-in Registration Tool and Power Platform Tools for Visual Studio. This tutorial provides instructions for using both tools.

#### [Plug-in Registration Tool](#tab/prt)

1. If you don't already have the Plug-in Registration tool installed and open, follow the steps in [Tutorial: Write and register a plug-in](tutorial-write-plug-in.md) to open it. Complete the [Connect using the Plug-in Registration tool](tutorial-write-plug-in.md#connect-using-the-plug-in-registration-tool) section.

1. In the Plug-in Registration tool, select **Install Profiler**.

    :::image type="content" source="media/tutorial-debug-plug-in-install-profiler.png" alt-text="Screenshot of the Plug-in Registration Tool with Install Profiler selected to begin plug-in profiling.":::

#### [Power Platform Tools](#tab/pptools)

1. Follow the instructions in [Install Power Platform Tools](tools/devtools-install.md).

---

When you complete the preceding steps, you add a new managed solution named **Plug-in Profiler** to your Microsoft Dataverse development environment.

## Start profiling

Follow these steps to begin profiling a plug-in's execution.

#### [Plug-in Registration Tool](#tab/prt)

1. In the Plug-in Registration tool, select the **(Step) BasicPlugin.FollowupPlugin: Create of account** step that you registered earlier, and select **Start Profiling**.

    :::image type="content" source="media/tutorial-debug-plug-in-start-profiling.png" alt-text="Screenshot of a plug-in step selected in Plug-in Registration Tool with Start Profiling command available.":::

1. When the **Profiler Settings** dialog appears, accept the default settings and select **OK**.

    ![Profiler settings.](media/tutorial-debug-plug-in-profiler-settings.png)

> [!TIP]
> For alternate information about running the profiler installed with the Plug-in Registration Tool, see [Run the plug-in profiler from a Command Prompt window](#run-profiler-standalone).

#### [Power Platform Tools](#tab/pptools)

1. In Visual Studio, select **View** > **Power Platform Explorer** to open the view if it's not already open.

1. Expand the **Plug-in Assemblies** node, and then completely expand the **BasicPlugin.FollowupPlugin** assembly node.

1. Right-click the step registration (the lowest level node) of the plug-in and choose **Start Profiling**.

1. When the **Profiler Settings** dialog appears, accept the default settings and select **OK**.

    ![Profiler settings.](media/tutorial-debug-plug-in-profiler-settings.png)

---

## Capture a profile

In your model-driven (or other) app, create a new account to execute the plug-in. This action captures an instance of the plug-in executing and persists it as a Plug-in Profile table row in Dataverse. You can see this row in Power Apps under **Tables** > **Plug-in Profile** by choosing **Data**.

#### [Plug-in Registration Tool](#tab/prt)

1. In the Plug-in Registration tool, select **Debug**.

    ![Click Debug.](media/tutorial-debug-plug-in-capture-profile-debug.png)

1. In the **Replay Plug-in Execution** dialog, on the **Setup** tab, select the ![Select profile command.](media/tutorial-debug-plug-in-select-profile-command.png) icon to open the **Select Profile from CRM** dialog.

1. In the **Select Profile from CRM** dialog, select the profile where **Type Name** equals **BasicPlugin.FollowupPlugin** and represents the profile captured when you last triggered the plug-in.

    ![Select Profile from CRM dialog.](media/tutorial-debug-plug-in-select-profile-dialog.png)

#### [Power Platform Tools](#tab/pptools)

1. In Solution Explorer, right-click the plug-in class file in the plug-in library project and select **Debug**.

1. In the **Replay Plug-in Execution** dialog, on the **Setup** tab, select the ![Select profile command.](media/tutorial-debug-plug-in-select-profile-command.png) icon to open the **Select Profile from CRM** dialog.

1. In the **Select Profile from CRM** dialog, select the profile where **Type Name** equals **BasicPlugin.FollowupPlugin** and represents the profile captured when you last triggered the plug-in.

    ![Select Profile from CRM dialog.](media/tutorial-debug-plug-in-select-profile-dialog.png)

---

## Debug your plug-in

Follow these steps to debug your plug-in code.

#### [Plug-in Registration Tool](#tab/prt)

1. In the **Replay Plug-in Execution** dialog, on the **Setup** tab, in the **Specify Assembly** section, click the ellipses (**…**) button and choose the location of your `BasicPlugin.dll`.

    ![Replay plug-in execution.](media/tutorial-debug-plug-in-replay-plug-in-execution.png)

1. In your Visual Studio project, set a breakpoint in your plug-in class.

    ![Set a break point.](media/tutorial-debug-plug-in-set-break-point.png)

1. In your Visual Studio project, select **Debug** > **Attach to Process…**.

    ![Attach to process command.](media/tutorial-debug-plug-in-attach-to-process.png)

1. Select the **PluginRegistration.exe** process and click **Attach**.

    ![Attach to process dialog.](media/tutorial-debug-plug-in-attach-to-process-dialog.png)

    > [!NOTE]
    > The Plug-in Registration tool now runs in debug mode.

1. In the **Replay Plug-in Execution** dialog, click **Start Execution**.

    ![Start Execution.](media/tutorial-debug-plug-in-replay-plug-in-execution-debug.png)

1. In your Visual Studio project, the code pauses at the breakpoint you set earlier.

    ![Breakpoint hit.](media/tutorial-debug-plug-in-breakpoint-hit.png)

1. Step through your code to debug.

#### [Power Platform Tools](#tab/pptools)

1. In the **Replay Plug-in Execution** dialog, on the **Setup** tab, in the **Specify Assembly** section, click the ellipses (**…**) button and choose the location of your `BasicPlugin.dll`.

    ![Replay plug-in execution.](media/tutorial-debug-plug-in-replay-plug-in-execution.png)

1. In your Visual Studio project, set a breakpoint in your plug-in class.

    ![Set a break point.](media/tutorial-debug-plug-in-set-break-point.png)

1. In the **Replay Plug-in Execution** dialog, click **Start Execution**.

    ![Start Execution.](media/tutorial-debug-plug-in-replay-plug-in-execution-debug.png)

1. In your Visual Studio project, the code pauses at the breakpoint you set earlier.

    ![Breakpoint hit.](media/tutorial-debug-plug-in-breakpoint-hit.png)

1. Step through your code to debug.

---

## Stop profiling

Follow these steps to stop profiling the plug-in's execution.

#### [Plug-in Registration Tool](#tab/prt)

1. Close the **Replay Plug-in Execution** dialog.

1. In the Plug-in Registration tool, select **Stop Profiling**.

    ![Stop profiling.](media/tutorial-debug-plug-in-stop-profiling.png)

#### [Power Platform Tools](#tab/pptools)

1. Close the **Replay Plug-in Execution** dialog.

1. In the **Power Platform Explorer** view, right-click the step registration node (lowest level node) of the plug-in assembly and select **Stop Profiling**.

---

## Next steps

To learn more about common tasks you perform with plug-ins, continue to [Tutorial: Update a plug-in](tutorial-update-plug-in.md).

If you don't plan to continue to the next tutorial, unregister the BasicPlugin assembly you created in this step. For instructions, see [Unregister assembly, plug-in, and step](tutorial-update-plug-in.md#unregister-assembly-plug-in-and-step).

<a name="run-profiler-standalone"></a>

## Run the plug-in profiler from a Command Prompt window

#### [Plug-in Registration Tool](#tab/prt)

While it's often better to run the profiler interactively from the Plug-in Registration tool, you can run the profiler from a Command Prompt window independent of the tool. This method is useful to get the plug-in profile log from a customer's [!INCLUDE[pn_dynamics_crm](../../includes/pn-dynamics-crm.md)] apps server to debug a failed plug-in. A developer can use that log to replay the plug-in's execution in the Plug-in Registration tool and debug the plug-in by using [!INCLUDE[pn_Visual_Studio](../../includes/pn-visual-studio.md)].

### Procedure: run the plug-in profiler from a Command Prompt

1. Open a Command Prompt window and set the working directory to the folder where you downloaded the Plug-in Registration tool `PluginRegistration.exe`.
1. Type this command to see the available run-time parameters: `PluginProfiler.Debugger.exe /?`.  
1. Review the supported parameter list and re-run the PluginProfiler.Debugger.exe program with the appropriate parameters.

#### [Power Platform Tools](#tab/pptools)

The Plug-in Profiler isn't available as a command line tool from Power Platform Tools for Visual Studio.

---

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

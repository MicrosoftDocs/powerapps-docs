---
title: "Commanding scopes | MicrosoftDocs"
description: "Determine breadth of where commands are rendered"
Keywords: command bar, command designer, ribbon, action bar, Power Fx command, command component, button
author: caburk
ms.author: caburk
ms.reviewer: matp
ms.date: 11/15/2022
ms.subservice: mda-maker
ms.topic: how-to
search.audienceType: 
  - maker
  - developer
---
# Scopes for modern commands

Commands have one of three scopes. The scope determines whether a command (`schemaname = appaction`) will render for a table within a single app, for a table across all apps, or for all tables and all apps.

A command must be bound to a command bar location such as main grid or main form regardless of scope. Therefore, changing the scope will not render the command in different command bar locations such as main grid and main form.

- **App** This is the narrowest scope and **default behavior** when creating or editing commands using the modern command designer. Command designer is opened within the context of a model-driven app, table, and command bar location.
- **Table** Also known as entity scope. Bound to a specific table and command bar location. Not bound to any specific app. Therefore table scoped commands will render in all apps that use the table. For example, a table scope command for the account table and main form location will be present in all apps when viewing the main form for an account record.
- **Global** This is the broadest scope. Global scope commands are only bound to a command bar location, not an app or table. For example, a global scope command for the main form location is present in all apps within an environment when viewing the main form for every table.

> [!IMPORTANT]
> Commands using Power Fx for the action and/or visibility can't be converted to table or global scope at this time.
>
> When commands are nested within dropdown lists, groups, and split buttons, all must be set to the same scope.

If a global or table scope command is edited within modern command designer, a copy (instance) is created with app scope and linked to the original command. For example, editing a global scope command in command designer overrides the original global scope command but only for the specific app and table chosen when opening command designer. All other apps and tables will will render the original command. The copy (instance) now has it's own lifecycle. Changes to the original global scope command will not effect the new app scope instance and vice versa.

## Override table and global scoped commands

More narrow scopes can override a broader scope command at every level. The most narrow scope wins.

- A **table (entity) scoped** command overrides global scoped commands. You can define a command that will be the same across all tables, but modify the behavior only for specific tables.
- An **app scoped** command overrides all other scopes but only for a particular app and table.

## How to create a table scope command

1. Create one or more commands within your solution using command designer. Alternatively, create a separate solution and select **Add existing** > **Table**.  

1. Choose **Select objects**, and then add the desired commands.

1. Select **Export** to export your solution.

   :::image type="content" source="../../developer/model-driven-apps/media/export-solution-from-command-bar.png" alt-text="Export solution.":::

1. If you've made recent changes that haven't yet been published, select **Publish**. Then, select **Run** to check whether the solution has any issues or dependencies, and then select **Next**.

1. Select the **Unmanaged** option, and then select **Export**.

1. In the **Download** dialog box, select **Save**, and in the **Download complete** dialog box, select **Open Folder**.

1. Right-click to select the compressed .zip file that you downloaded, and then select **Extract All**.

1. Select a location to extract the files to, and then select **Extract**.

1. Open the folder to the extracted files, open the appaction.xml file, and find the desired command (appaction).

1. Delete the **appmoduleid** node from the xml.

   ```XML
    <appmoduleid>
      <uniquename>demo_DemoFestApp</uniquename>
    </appmoduleid>
   ```
1. Change the value of the **appaction uniquename**. Changing any one of the last characters is sufficient, such as from 1 to 2, or you can use more descriptive naming conventions if desired.


Example XML.

```XML
   <appaction uniquename="crdff_NewCommand!a078463b5d7c473d8965f0f80469f412!crdff_CustomApp!crdff_entity1!1">
  <buttonlabeltext default="Show Alert">
    <label description="Show Alert" languagecode="1033" />
   </buttonlabeltext>
   <buttonsequencepriority>10.0000000000</buttonsequencepriority>
   <context>1</context>
   <contextentity>
    <logicalname>crdff_entity1</logicalname>
   </contextentity>
   <fonticon>AALinkedInLogo</fonticon>
   <contextvalue>crdff_entity1</contextvalue>
   <hidden>0</hidden>
   <iscustomizable>1</iscustomizable>
   <location>1</location>
   <name>EntityScoped!a078463b5d7c473d8965f0f80469f412</name>
   <onclickeventjavascriptfunctionname>ShowAppAlert</onclickeventjavascriptfunctionname>
   <onclickeventjavascriptparameters>[]</onclickeventjavascriptparameters>
   <onclickeventjavascriptwebresourceid>
    <webresourceid>ac21ad24-3c11-ef11-b6u7-000d3a1d942c</webresourceid>
   </onclickeventjavascriptwebresourceid>
   <onclickeventtype>2</onclickeventtype>
   <statecode>0</statecode>
   <statuscode>1</statuscode>
   <type>0</type>
   </appaction>
```

After you've edited and saved the appaction.xml file, zip your solution in the same format it was exported in.  Then **Import** the solution back into your environment and test the behavior.
  
## How to create a global scope command

1. Follow the same steps above to edit the appaction.xml file.

1. **Delete** the **appmoduleid** node from the xml:

   ```XML
    <appmoduleid>
      <uniquename>demo_DemoFestApp</uniquename>
    </appmoduleid>
   ```

1. Change the value of the **appaction uniquename**. Changing any one of the last characters is sufficient, such as from 1 to 2, or you can use more descriptive naming conventions if desired.


1. **Delete** the **contextentity** and **contextvalue** nodes from the xml: 

   ```XML
   <contextentity>
    <logicalname>account</logicalname>
   </contextentity>
   <contextvalue>account</contextvalue>
   ```

1. Change the **context** value from 1 to 0.

   ```XML
   <appaction uniquename="crdff_NewCommand1!8fe72a85-1f84-431e-ac56-854f1bfadc4e!1">
   <buttonlabeltext default="Show Alert">
   <label description="Show Alert" languagecode="1033" />
   </buttonlabeltext>
   <buttonsequencepriority>10.0000000000</buttonsequencepriority>
   <context>0</context>
   <hidden>0</hidden>
   <iscustomizable>1</iscustomizable>
   <fonticon>AALinkedInLogo</fonticon>
   <location>1</location>
   <name>EntityScoped!a078463b5d7c473d8965f0f80469f412</name>
   <onclickeventjavascriptfunctionname>ShowGlobalAlert</onclickeventjavascriptfunctionname>
   <onclickeventjavascriptparameters>[]</onclickeventjavascriptparameters>
   <onclickeventjavascriptwebresourceid>
    <webresourceid>ac21ad24-3c01-ec11-b6e7-000d3a1d942c</webresourceid>
   </onclickeventjavascriptwebresourceid>
   <onclickeventtype>2</onclickeventtype>
   <statecode>0</statecode>
   <statuscode>1</statuscode>
   <type>0</type>
   </appaction>
    ```

After you've edited and saved the appaction.xml file, zip your solution in the same format it was exported in.  Then **Import** the solution back into your environment and test the behavior.

## How to override a global scope command with a table scope

This example is for when you want a global scope command to be the same everywhere *except* for a certain table.
- **Entity Scoped Action** will be visible on `crdff_entity1` grids in all apps except in `crdff_CustomApp`.
- **Global Scoped Action** will be visible on all the entity grids except `crdff_entity1`.

> [!NOTE]
> To override either global or table scope commands with an app scope command, simply edit the command using command designer.
>
> To override a global scoped command with a table scope command, modify the appactions.xml files so they have the same  ```XML <name> ```.

### Steps to override

1. Follow the steps in [How to create a global scope command](#how-to-create-a-global-scope-command), but create two commands using command designer.

1. As described in the steps, export your solution and edit the appactions.xml files.

1. Continue following the steps to create one global and one entity scope command.

1. Set the **name** property to be the exact same for both the global and entity scope commands.

#### Example global scope command XML

 ```XML
<appaction uniquename="crdff_NewCommand1!8fe72a85-1f84-431e-ac56-854f1bfadc4e!1">
<buttonlabeltext default="Show Alert">
  <label description="Show Alert" languagecode="1033" />
</buttonlabeltext>
<buttonsequencepriority>10.0000000000</buttonsequencepriority>
<context>0</context>
<hidden>0</hidden>
<iscustomizable>1</iscustomizable>
<fonticon>AALinkedInLogo</fonticon>
<location>1</location>
<name>EntityScoped!a078463b5d7c473d8965f0f80469f412</name>
<onclickeventjavascriptfunctionname>ShowGlobalAlert</onclickeventjavascriptfunctionname>
<onclickeventjavascriptparameters>[]</onclickeventjavascriptparameters>
<onclickeventjavascriptwebresourceid>
  <webresourceid>ac21ad24-3c01-ec11-b6e7-000d3a1d942c</webresourceid>
</onclickeventjavascriptwebresourceid>
<onclickeventtype>2</onclickeventtype>
<statecode>0</statecode>
<statuscode>1</statuscode>
<type>0</type>
</appaction>
```

#### Example table scope command XML

```XML
<appaction uniquename="crdff_NewCommand!a078463b5d7c473d8965f0f80469f412!crdff_entity1!1">
<buttonlabeltext default="Show Alert">
<label description="Show Alert" languagecode="1033" />
</buttonlabeltext>
<buttonsequencepriority>10.0000000000</buttonsequencepriority>
<context>1</context>
<contextentity>
<logicalname>crdff_entity1</logicalname>
</contextentity>
<fonticon>AALinkedInLogo</fonticon>
<contextvalue>crdff_entity1</contextvalue>
<hidden>0</hidden>
<iscustomizable>1</iscustomizable>
<location>1</location>
<name>EntityScoped!a078463b5d7c473d8965f0f80469f412</name>
<onclickeventjavascriptfunctionname>ShowEntityAlert</onclickeventjavascriptfunctionname>
<onclickeventjavascriptparameters>[]</onclickeventjavascriptparameters>
<onclickeventjavascriptwebresourceid>
<webresourceid>ac21ad24-3c01-ec11-b6e7-000d3a1d942c</webresourceid>
</onclickeventjavascriptwebresourceid>
<onclickeventtype>2</onclickeventtype>
<statecode>0</statecode>
<statuscode>1</statuscode>
<type>0</type>
</appaction>
```

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

---
title: "How to: Connect your code app to Azure SQL"
description: "Learn how to connect your code app to Azure SQL"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Connect your code app to Azure SQL

This guide walks through how to set up an Azure SQL Database and connect it to a Power Apps code app using the Power SDK. 

This guide covers:

- Provisioning an Azure SQL Server and database
- Creating SQL tables and stored procedures
- Connecting a Power Apps code app using the Power SDK

## Prerequisites

- An Azure subscription
- Access to the [Azure portal](https://portal.azure.com)
- [Power Platform environment with code apps enabled](../overview.md#enable-code-apps-on-a-power-platform-environment)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Node.js](https://nodejs.org/) (LTS version)
- [Power Platform Tools for VS Code](/power-platform/developer/cli/introduction)
- [SQL Server (mssql) VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql)

## Set Up Azure SQL Server and Database

1. Navigate to [Select SQL deployment option - Microsoft Azure](https://portal.azure.com/#create/Microsoft.AzureSQL)
1. Select **SQL database** -> Resource type: **Single database** -> **Create**
1. Fill in:
   - Resource group: Select **Create new** and enter a Resource group name, for example, `rg-codeapps-dev`
   - Database name: `sqldb-codeapps-dev`
   - Server: Select **Create new** and Fill in:
     - Server name: `sql-codeapps-dev`
     - Location: Select the closest region to your Power Platform environment.
     - Authentication method: **Use Microsoft Entra-only authentication**
     - Set Microsoft Entra admin: Select **Set admin**, and then **Select your own user**.
   - Select **OK**
1. Compute + storage: **General Purpose - Serverless**
1. Select **Next: Networking**  
1. Fill in:
   - Connectivity method: **Public endpoint**
   - Allow Azure services and resources to access this server: **Yes**
   - Add current client IP address: **Yes**
1. Select **Review + create** -> **Create**
1. Wait until the Deployment completes, and then select **Go to resource**

### Deploy sample data

1. Inside Visual Studio Code, select **Extensions** (<kbd>Ctrl + Shift + X</kbd>)
1. Locate the **SQL Server (mssql)** extension on the Activity Bar and open it, or use <kbd>Ctrl + Alt + D</kbd>
1. Under **Connections**, select **+ Add Connection**  

   :::image type="content" source="media/sql-addconnection.png" alt-text="Add Connection in VS Code SQL Server extension":::

1. In the **Connect to Database** dialog, select **Browse Azure**, select your subscription, resource group (for example: `rg-codeapps-dev`), Server (for example: `sql-codeapps-dev`), and then database (for example `sqldb-codeapps-dev` )
1. Under **Authentication type**, select **Microsoft Entra ID - Universal with MFA support**
1. Ensure you have your Azure portal open in your browser, and then select **Sign In**. You should be prompted to sign-in, and then see:

   :::image type="content" source="media/sql-signin.png" alt-text="Microsoft Entra sign-in prompt for SQL connection":::

1. Select Connect

   :::image type="content" source="media/sql-connect.png" alt-text="Connected to Azure SQL database in VS Code":::

1. In the SQL SERVER panel, right click on your database and select **New Query**

   :::image type="content" source="media/sql-newquery.png" alt-text="New Query command for database in VS Code SQL extension":::

1. In the new query window, paste the following SQL:

   ```sql
   -- Drop existing objects if they exist
   IF OBJECT_ID('dbo.Projects', 'U') IS NOT NULL DROP TABLE dbo.Projects;
   
   -- =============================================
   -- CREATE TABLES
   -- =============================================
   
   -- Projects Table
   CREATE TABLE [dbo].[Projects](
       [ProjectId] [int] IDENTITY(1,1) NOT NULL,
       [Name] [nvarchar](255) NOT NULL,
       [Description] [nvarchar](max) NULL,
       [StartDate] [date] NULL,
       [EndDate] [date] NULL,
       [Status] [nvarchar](50) NOT NULL DEFAULT ('Planning'),
       [Priority] [nvarchar](20) NOT NULL DEFAULT ('Medium'),
       [Budget] [decimal](18, 2) NULL,
       [ProjectManagerEmail] [nvarchar](255) NOT NULL,
       [CreatedBy] [nvarchar](255) NOT NULL,
       [CreatedDate] [datetime2](7) NOT NULL DEFAULT (getutcdate()),
       [IsActive] [bit] NOT NULL DEFAULT (1),
       CONSTRAINT [PK_Projects] PRIMARY KEY ([ProjectId])
   );
   GO
   
   -- =============================================
   -- ADD CONSTRAINTS
   -- =============================================
   
   -- Project Status Check
   ALTER TABLE [dbo].[Projects] ADD CONSTRAINT [CK_Projects_Status] 
   CHECK ([Status] IN ('Planning', 'Active', 'On Hold', 'Completed', 'Cancelled'));
   
   -- Project Priority Check
   ALTER TABLE [dbo].[Projects] ADD CONSTRAINT [CK_Projects_Priority] 
   CHECK ([Priority] IN ('Low', 'Medium', 'High', 'Critical'));
   GO
   
   -- =============================================
   -- STORED PROCEDURES
   -- =============================================
   
   -- Get All Projects
   IF OBJECT_ID('dbo.GetAllProjects', 'P') IS NOT NULL DROP PROCEDURE dbo.GetAllProjects;
   GO
   CREATE PROCEDURE [dbo].[GetAllProjects]
   AS
   BEGIN
       SET NOCOUNT ON;
       
       SELECT 
           [ProjectId], [Name], [Description], [StartDate], [EndDate],
           [Status], [Priority], [Budget], [ProjectManagerEmail],
           [CreatedBy], [CreatedDate], [IsActive]
       FROM [dbo].[Projects]
       WHERE [IsActive] = 1
       ORDER BY [CreatedDate] DESC;
   END
   GO
   
   -- Create Project
   IF OBJECT_ID('dbo.CreateProject', 'P') IS NOT NULL DROP PROCEDURE dbo.CreateProject;
   GO
   CREATE PROCEDURE [dbo].[CreateProject]
       @Name NVARCHAR(255),
       @Description NVARCHAR(MAX) = NULL,
       @StartDate DATE = NULL,
       @EndDate DATE = NULL,
       @Status NVARCHAR(50) = 'Planning',
       @Priority NVARCHAR(20) = 'Medium',
       @Budget DECIMAL(18,2) = NULL,
       @ProjectManagerEmail NVARCHAR(255),
       @CreatedBy NVARCHAR(255)
   AS
   BEGIN
       SET NOCOUNT ON;
       
       INSERT INTO [dbo].[Projects] (
           [Name], [Description], [StartDate], [EndDate], 
           [Status], [Priority], [Budget], [ProjectManagerEmail], [CreatedBy]
       )
       VALUES (
           @Name, @Description, @StartDate, @EndDate,
           @Status, @Priority, @Budget, @ProjectManagerEmail, @CreatedBy
       );
       
       SELECT SCOPE_IDENTITY() as ProjectId;
   END
   GO
   
   -- Update Project
   IF OBJECT_ID('dbo.UpdateProject', 'P') IS NOT NULL DROP PROCEDURE dbo.UpdateProject;
   GO
   CREATE PROCEDURE [dbo].[UpdateProject]
       @ProjectId INT,
       @Name NVARCHAR(255) = NULL,
       @Description NVARCHAR(MAX) = NULL,
       @StartDate DATE = NULL,
       @EndDate DATE = NULL,
       @Status NVARCHAR(50) = NULL,
       @Priority NVARCHAR(20) = NULL,
       @Budget DECIMAL(18,2) = NULL,
       @ProjectManagerEmail NVARCHAR(255) = NULL
   AS
   BEGIN
       SET NOCOUNT ON;
       
       UPDATE [dbo].[Projects]
       SET 
           [Name] = ISNULL(@Name, [Name]),
           [Description] = ISNULL(@Description, [Description]),
           [StartDate] = ISNULL(@StartDate, [StartDate]),
           [EndDate] = ISNULL(@EndDate, [EndDate]),
           [Status] = ISNULL(@Status, [Status]),
           [Priority] = ISNULL(@Priority, [Priority]),
           [Budget] = ISNULL(@Budget, [Budget]),
           [ProjectManagerEmail] = ISNULL(@ProjectManagerEmail, [ProjectManagerEmail])
       WHERE [ProjectId] = @ProjectId AND [IsActive] = 1;
       
       SELECT @@ROWCOUNT as RowsAffected;
   END
   GO
   
   -- Delete Project (Soft Delete)
   IF OBJECT_ID('dbo.DeleteProject', 'P') IS NOT NULL DROP PROCEDURE dbo.DeleteProject;
   GO
   CREATE PROCEDURE [dbo].[DeleteProject]
       @ProjectId INT
   AS
   BEGIN
       SET NOCOUNT ON;
       
       UPDATE [dbo].[Projects]
       SET [IsActive] = 0
       WHERE [ProjectId] = @ProjectId AND [IsActive] = 1;
       
       SELECT @@ROWCOUNT as RowsAffected;
   END
   GO
   
   -- =============================================
   -- SAMPLE DATA
   -- =============================================
   
   -- Insert Sample Projects
   INSERT INTO [dbo].[Projects] ([Name], [Description], [StartDate], [EndDate], [Status], [Priority], [Budget], [ProjectManagerEmail], [CreatedBy]) VALUES
   ('Website Redesign', 'Complete redesign of company website with modern UI/UX', '2025-06-01', '2025-08-31', 'Active', 'High', 75000.00, 'sarah.johnson@company.com', 'admin@company.com'),
   ('Mobile App Development', 'Develop iOS and Android mobile application for customer portal', '2025-07-01', '2025-12-31', 'Planning', 'Critical', 150000.00, 'mike.chen@company.com', 'admin@company.com'),
   ('Database Migration', 'Migrate legacy database to cloud infrastructure', '2025-05-15', '2025-09-30', 'Active', 'Medium', 50000.00, 'lisa.williams@company.com', 'admin@company.com');
   GO
   
   PRINT 'Projects-only database schema created successfully with sample data!';
   ```
   
1. Select the green play icon (<kbd>Ctrl-Shift-E</kbd>) to **Execute the query**.

1. You should see no errors in the **QUERY RESULTS** output.


### Initialize your Vite App

1. Open Visual Studio Code and open a new PowerShell terminal and enter:

   ```powershell
   mkdir C:\CodeApps -Force
   cd C:\CodeApps
   npm create vite@latest ProjectManagementApp -- --template react-ts
   cd C:\CodeApps\ProjectManagementApp
   npm install
   ```

1. If asked, agree to install `create-vite`
1. Accept the default package name `projectmanagementapp` by pressing **Enter**.
1. If asked to select a framework, select **React**.
1. If asked to select a variant, select **TypeScript**.
1. At this time, the Power SDK requires the port to be 3000 in the default configuration.

   Install the node type definitions using:

   ```powershell
   npm i --save-dev @types/node
   ```

   Open the `vite.config.ts`, and change it to:

   ```typescript
   import { defineConfig } from 'vite'
   import react from '@vitejs/plugin-react'
   import * as path from 'path'
   
   // https://vite.dev/config/
   export default defineConfig({
     base: "./",
     server: {
       host: "::",
       port: 3000,
     },
     plugins: [react()],
     resolve: {
       alias: {
         "@": path.resolve(__dirname, "./src"),
       },
     },
   });
   ```

1. **Save** the file.
1. Open the `tsconfig.app.json`, and set the value of `verbatimModuleSyntax` to be `false` . This setting is currently required to work with the Power SDK Generated code. (See [[Bug\] Power SDK generated code causes error with verbatimModuleSyntax enabled · Issue #14 ](https://github.com/microsoft/PowerAppsCodeApps/issues/14))
1. Enter the following to test your vite app:

   ```powershell
   npm run dev
   ```

1. The template project starts and runs locally. Browse to the `http://localhost:3000` address given.

   :::image type="content" source="media/sql-localhost.png" alt-text="Vite React app running on localhost port 3000":::

   > [!IMPORTANT]
   > If you don't see the port 3000, revisit the previous steps.

1. Press <kbd>Ctrl + C</kbd> to stop the local server when finish testing.

### Initialize your code app

1. Authenticate the Power Platform CLI against your Power Platform tenant:

   ```powershell
   pac auth create
   ```

   Sign-in as your Power Platform account when prompted.

   > [!NOTE]
   > You can also use the [Power Platform Tools VS Code Extension](/power-platform/developer/howto/install-vs-code-extension) to do sign-in.

1. **Select** your environment using:

   ```powershell
   pac env select -env <URL of your environment>
   ```

   You can also use the Power Platform Tools VS Code Extension to select the environment

1. **Initialize** your code app using:

   ```powershell
   pac code init --displayName "Project Management App" -l "C:\CodeApps\ProjectManagementApp\public\vite.svg"
   ```

   Notice that there's now a `power.config.json` file in your project.

1. **Install** the Power SDK using:

   ```powershell
   npm install --save-dev @microsoft/power-apps
   ```

1. **Open** the `package.json`, and update the existing line:

   ```json
   "dev": "vite"
   ```

   Change it to:

   ```json
   "dev": "start pac code run && vite",
   ```

   Save the updated `package.json`.

1. **Add a new file** under the `src` folder named `PowerProvider.tsx` and grab the code from [PowerProvider.tsx](https://github.com/microsoft/PowerAppsCodeApps/blob/main/docs/assets/PowerProvider.tsx)
1. **Save** the file.
1. **Open** `main.tsx` and add the following import under the existing imports:

   ```
   import PowerProvider from './PowerProvider.tsx'
   ```

1. **Update** `main.tsx`

   ```
   <StrictMode>
     <App />
   </StrictMode>,
   ```

   Change it to:

   ```
   <StrictMode>
     <PowerProvider>
       <App />
     </PowerProvider>
   </StrictMode>,
   ```

1. **Save** the file
1. You can now test the code app by using:
    ```
    npm run dev
    ```

   This command runs the Vite server and starts the Power SDK server:

   :::image type="content" source="media/sql-testapp.png" alt-text="Power SDK server console with app URL and status":::

1. Open the URL provided by the Power SDK Server.

   > [!IMPORTANT]
   > Open the url in the same browser profile as your power platform tenant.

1. You should see the app open similar to:

  :::image type="content" source="media/sql-vite-running-powerapps.png" alt-text="Vite app running in Power Apps with Power SDK":::

### Create a SQL Server Connection in Power Platform

1. Open [Power Apps](https://make.powerapps.com)
1. Select your **Environment**
1. Navigate to **Connections**. It might be in the **... More menu**.
1. Select **+ New Connection**

   :::image type="content" source="media/sql-createconnection.png" alt-text="+ New Connection in Power Apps maker portal":::

1. Select **SQL Server**
1. Select Authentication type: **Microsoft Entra ID Integrated**
1. Select **Create** and sign-in in the popup authentication prompt

## Add SQL table connections to your app

1. First list the available connections in your environment. You should see the connection you created:

   ```powershell
   pac connection list
   ```

   You should see a list similar to:

   :::image type="content" source="media/sql-connectionlist.png" alt-text="Power Platform connections list showing SQL connection":::

1. To add the projects table to the project, copy the connection ID (the first column) and use the following command:

   ```powershell
   pac code add-data-source -a "shared_sql" -c "[CONNECTION ID]"  -d "[SQL SERVER NAME].database.windows.net,[DATA BASE NAME]" -sp "dbo.GetAllProjects"
   ```

   For example:

   ```powershell
   pac code add-data-source -a "shared_sql" -c "aaaa0000bb11222233cc444444dddddd"  -d "sql-codeapps-dev.database.windows.net,sqldb-codeapps-dev" -sp "dbo.GetAllProjects"
   ```

1. Open the `Services` and `Models` folder, and observer the newly generated code. 
   

### Add Table of Projects

1. We use Fluent UI to show a table of projects, so downgrade to React 18 and install using:

   ```
   npm install react@^18.0.0 react-dom@^18.0.0 @types/react@^18.0.0 @types/react-dom@^18.0.0
   npm install @fluentui/react-components
   ```

1. Add a new file under `src` named `ProjectsTable.tsx` with the following code:

   ```typescript
   /**
    * ProjectsTable Component - Displays project data from Power Platform in a sortable DataGrid
    */
   import React, { useEffect, useState, useCallback, useMemo } from 'react';
   import {
     DataGrid,
     DataGridHeader,
     DataGridRow,
     DataGridHeaderCell,
     DataGridCell,
     DataGridBody,
     TableColumnDefinition,
     TableRowId,
     Spinner,
     MessageBar,
     Badge,
     makeStyles,
     tokens,
   } from '@fluentui/react-components';
   import { GetAllProjectsService } from './Services/GetAllProjectsService';
   
   // String formatting utility for localizable messages
   const formatMessage = (template: string, params: Record<string, string | number> = {}): string => {
     return template.replace(/\{(\w+)\}/g, (match, key) => {
       const value = params[key];
       return value !== undefined ? String(value) : match;
     });
   };
   
   // Common UI messages
   const MESSAGE_STRINGS = {
     LOADING: 'Loading data...',
     NO_DATA: 'No data found.',
     GENERIC_ERROR: 'An unexpected error occurred',
     LOAD_ERROR: 'Failed to load data. Please try again.',
     PROJECT_COUNTER_SINGLE: 'Showing {count} project',
     PROJECT_COUNTER_PLURAL: 'Showing {count} projects',
     COLUMN_PROJECT_NAME: 'Project Name',
     COLUMN_DESCRIPTION: 'Description',
     COLUMN_START_DATE: 'Start Date',
     COLUMN_END_DATE: 'End Date',
     COLUMN_STATUS: 'Status',
     COLUMN_PRIORITY: 'Priority',
     ARIA_LABEL_DATA_GRID: 'Projects data grid',
   } as const;
   
   // Project data type
   type ProjectItem = {
     ProjectId?: number;
     Name?: string;
     Description?: string;
     StartDate?: string;
     EndDate?: string;
     Status?: string;
     Priority?: string;
     Budget?: number;
     ProjectManagerEmail?: string;
     CreatedBy?: string;
     CreatedDate?: string;
     IsActive?: boolean;
   };
   
   // DataGrid columns
   const COLUMNS: TableColumnDefinition<ProjectItem>[] = [
     {
       columnId: 'name',
       compare: (a, b) => (a.Name || '').localeCompare(b.Name || ''),
       renderHeaderCell: () => MESSAGE_STRINGS.COLUMN_PROJECT_NAME,
       renderCell: (item) => item.Name || '',
     },
     {
       columnId: 'description',
       compare: (a, b) => (a.Description || '').localeCompare(b.Description || ''),
       renderHeaderCell: () => MESSAGE_STRINGS.COLUMN_DESCRIPTION,
       renderCell: (item) => item.Description || '',
     },
     {
       columnId: 'startDate',
       compare: (a, b) => new Date(a.StartDate || '').getTime() - new Date(b.StartDate || '').getTime(),
       renderHeaderCell: () => MESSAGE_STRINGS.COLUMN_START_DATE,
       renderCell: (item) => item.StartDate ? new Date(item.StartDate).toLocaleDateString() : '',
     },
     {
       columnId: 'endDate',
       compare: (a, b) => new Date(a.EndDate || '').getTime() - new Date(b.EndDate || '').getTime(),
       renderHeaderCell: () => MESSAGE_STRINGS.COLUMN_END_DATE,
       renderCell: (item) => item.EndDate ? new Date(item.EndDate).toLocaleDateString() : '',
     }, {
       columnId: 'status',
       compare: (a, b) => (a.Status || '').localeCompare(b.Status || ''),
       renderHeaderCell: () => MESSAGE_STRINGS.COLUMN_STATUS,
       renderCell: (item) => <StatusBadge status={item.Status || ''} />,
     },
     {
       columnId: 'priority',
       compare: (a, b) => (a.Priority || '').localeCompare(b.Priority || ''),
       renderHeaderCell: () => MESSAGE_STRINGS.COLUMN_PRIORITY,
       renderCell: (item) => <PriorityBadge priority={item.Priority || ''} />,
     },
   ];
   
   // Row ID generator
   const getRowId = (item: ProjectItem): TableRowId =>
     item.ProjectId?.toString() || `temp-${Date.now()}-${Math.random().toString(36).substring(2, 11)}`;
   
   // Extracts a user-friendly error message from various error types
   const extractErrorMessage = (
     error: unknown,
     fallbackMessage = MESSAGE_STRINGS.GENERIC_ERROR
   ): string => {
     if (error instanceof Error) {
       return error.message;
     }
     if (typeof error === 'string') {
       return error;
     } return fallbackMessage;
   };
   
   // Badge component for Priority
   const PriorityBadge: React.FC<{ priority: string }> = React.memo(({ priority }) => {
     const styles = useStyles();
     const badgeProps = useMemo(() => {
       const getPriorityAppearance = (priority: string) => {
         switch (priority?.toLowerCase()) {
           case 'critical':
             return { appearance: 'filled' as const, color: 'danger' as const };
           case 'high':
             return { appearance: 'filled' as const, color: 'important' as const };
           case 'medium':
             return { appearance: 'filled' as const, color: 'warning' as const };
           case 'low':
             return { appearance: 'filled' as const, color: 'success' as const };
           default:
             return { appearance: 'outline' as const, color: 'subtle' as const };
         }
       };
       return getPriorityAppearance(priority);
     }, [priority]);
   
     return (
       <Badge {...badgeProps} className={styles.badge}>
         {priority || 'Unknown'}
       </Badge>
     );
   });
   
   PriorityBadge.displayName = 'PriorityBadge';
   
   // Badge component for Status
   const StatusBadge: React.FC<{ status: string }> = React.memo(({ status }) => {
     const styles = useStyles();
     const badgeProps = useMemo(() => {
       const getStatusAppearance = (status: string) => {
         switch (status?.toLowerCase()) {
           case 'completed':
             return { appearance: 'filled' as const, color: 'success' as const };
           case 'active':
             return { appearance: 'filled' as const, color: 'brand' as const };
           case 'planning':
             return { appearance: 'filled' as const, color: 'informative' as const };
           case 'on hold':
             return { appearance: 'filled' as const, color: 'warning' as const };
           case 'cancelled':
             return { appearance: 'filled' as const, color: 'danger' as const };
           default:
             return { appearance: 'outline' as const, color: 'subtle' as const };
         }
       };
       return getStatusAppearance(status);
     }, [status]);
   
     return (
       <Badge {...badgeProps} className={styles.badge}>
         {status || 'Unknown'}
       </Badge>
     );
   });
   
   StatusBadge.displayName = 'StatusBadge';
   
   // Styles
   const useStyles = makeStyles({
     container: {
       padding: tokens.spacingVerticalXXL,
     },
     loadingContainer: {
       display: 'flex',
       alignItems: 'center',
       gap: tokens.spacingHorizontalS,
       padding: tokens.spacingVerticalXXL,
     },
     messageBar: {
       marginBottom: tokens.spacingVerticalXL,
     },
     projectCounter: {
       marginBottom: tokens.spacingVerticalM,
       fontSize: tokens.fontSizeBase200,
       color: tokens.colorNeutralForeground2,
     }, dataGrid: {
       width: '100%',
     },
     badge: {
       fontSize: tokens.fontSizeBase200,
       fontWeight: tokens.fontWeightMedium,
       textTransform: 'capitalize',
     },
   });
   
   // Custom hook to fetch and manage project data
   const useProjectsData = (): {
     projects: ProjectItem[];
     loading: boolean;
     error: string | null;
     refetch: () => Promise<void>;
   } => {
     const [projects, setProjects] = useState<ProjectItem[]>([]);
     const [loading, setLoading] = useState(true);
     const [error, setError] = useState<string | null>(null);
   
     const fetchProjects = useCallback(async () => {
       try {
         setLoading(true);
         setError(null); const result = await GetAllProjectsService.GetAllProjects();
         if (result.success && result.data?.ResultSets?.Table1) {
           const projectsData = Array.isArray(result.data.ResultSets.Table1)
             ? result.data.ResultSets.Table1 as ProjectItem[]
             : [result.data.ResultSets.Table1] as ProjectItem[];
           setProjects(projectsData);
         } else {
           const errorMsg = result.error instanceof Error
             ? result.error.message
             : result.error || MESSAGE_STRINGS.LOAD_ERROR;
           setError(errorMsg);
           console.error('Failed to fetch projects:', result.error);
         }
       } catch (error) {
         const errorMessage = extractErrorMessage(error, MESSAGE_STRINGS.GENERIC_ERROR);
         setError(errorMessage);
         console.error('Error fetching projects:', error);
       } finally {
         setLoading(false);
       }
     }, []);
   
     useEffect(() => {
       fetchProjects();
     }, [fetchProjects]);
   
     return { projects, loading, error, refetch: fetchProjects };
   };
   
   // UI Components
   const LoadingSpinner: React.FC = () => {
     const styles = useStyles();
     return (
       <div className={styles.loadingContainer}>
         <Spinner size="small" />
         <span>{MESSAGE_STRINGS.LOADING}</span>
       </div>
     );
   };
   
   const ErrorMessage: React.FC<{ error: string }> = ({ error }) => {
     const styles = useStyles();
     return (
       <MessageBar intent="error" className={styles.messageBar}>
         {error}
       </MessageBar>
     );
   };
   
   const EmptyState: React.FC = () => {
     const styles = useStyles();
     return (
       <MessageBar intent="info" className={styles.messageBar} style={{ textAlign: 'center' }}>
         {MESSAGE_STRINGS.NO_DATA}
       </MessageBar>
     );
   };
   
   const ProjectCounter: React.FC<{ count: number }> = ({ count }) => {
     const styles = useStyles();
   
     const counterMessage = useMemo(() => {
       return count === 1
         ? formatMessage(MESSAGE_STRINGS.PROJECT_COUNTER_SINGLE, { count })
         : formatMessage(MESSAGE_STRINGS.PROJECT_COUNTER_PLURAL, { count });
     }, [count]);
   
     return (
       <div className={styles.projectCounter}>
         {counterMessage}
       </div>
     );
   };
   
   // Main component
   const ProjectsTable: React.FC = () => {
     const styles = useStyles();
     const { projects, loading, error } = useProjectsData();
     const projectCount = useMemo(() => projects.length, [projects.length]);
     const memoizedProjects = useMemo(() => projects, [projects]);
     const dataGridProps = useMemo(() => ({
       items: memoizedProjects,
       columns: COLUMNS,
       sortable: true,
       getRowId,
       focusMode: "cell" as const,
       className: styles.dataGrid,
       "aria-label": MESSAGE_STRINGS.ARIA_LABEL_DATA_GRID,
     }), [memoizedProjects, styles.dataGrid]);
   
     if (loading) {
       return (
         <div className={styles.container}>
           <LoadingSpinner />
         </div>
       );
     }
   
     if (error) {
       return (
         <div className={styles.container}>
           <ErrorMessage error={error} />
         </div>
       );
     }
   
     if (projectCount === 0) {
       return (
         <div className={styles.container}>
           <EmptyState />
         </div>
       );
     }
     return (
       <div className={styles.container}>
         <ProjectCounter count={projectCount} />      <DataGrid {...dataGridProps}>
           <DataGridHeader>
             <DataGridRow>
               {({ renderHeaderCell }) => (
                 <DataGridHeaderCell>{renderHeaderCell()}</DataGridHeaderCell>
               )}
             </DataGridRow>
           </DataGridHeader>
           <DataGridBody<ProjectItem>>
             {({ item, rowId }) => (
               <DataGridRow<ProjectItem> key={rowId}>
                 {({ renderCell }) => (
                   <DataGridCell>{renderCell(item)}</DataGridCell>
                 )}
               </DataGridRow>
             )}
           </DataGridBody>
         </DataGrid>
       </div>
     );
   };
   
   export default React.memo(ProjectsTable);
   
   ```

1. Add the `FluentProvider` and `ProjectsTable` to `maint.tsx`:

   ```typescript
    import { StrictMode } from 'react'
    import { createRoot } from 'react-dom/client'
    import './index.css'
    import PowerProvider from './PowerProvider.tsx'
    import { FluentProvider, webLightTheme } from '@fluentui/react-components'
    import ProjectsTable from './ProjectsTable.tsx'

    createRoot(document.getElementById('root')!).render(
      <StrictMode>
        <PowerProvider>
          <FluentProvider theme={webLightTheme}>
            <ProjectsTable />
          </FluentProvider>
        </PowerProvider>
      </StrictMode>,
    )
   
   ```

1. Run your app using:

   ````
   npm run dev
   ````

   In the command window that opens up, open the app link provided:

   :::image type="content" source="media/sql-testapp.png" alt-text="Power SDK server console with app URL and status":::

1. When the app opens, you should see a consent dialog, select **Allow**

   :::image type="content" source="media/sql-consent.png" alt-text="Consent dialog requesting permissions for the app":::

1. You should see data grid of projects:

   :::image type="content" source="media/sql-datagrid.png" alt-text="Projects data grid with sortable columns and badges":::

### Publishing the App to Power Apps

1. Once your app is ready for publishing and sharing, make sure the Vite server is stopped using <kbd>Ctrl + C</kbd>, then use the following PowerShell:

   ```
   npm run build
   pac code push
   ```

1. Open the app using the link provided to test it out!

   :::image type="content" source="media/sql-pushed.png" alt-text="App published to Power Apps with Open app link":::

## Troubleshooting

This section covers common issues you might encounter while setting up Power Apps code apps with Azure SQL Database.

### Azure SQL Database Issues

You might experience these issues when using Azure SQL Databases.

- [Can't Connect to Azure SQL Database](#cant-connect-to-azure-sql-database)
- [SQL Query Execution Errors](#sql-query-execution-errors)


#### Can't Connect to Azure SQL Database

**Symptoms:**
- Connection timeout errors
- Authentication failures when connecting from VS Code SQL extension

**Solutions:**

1. **Check Firewall Settings:**

   - In Azure portal, navigate to your SQL Server
   - Go to **Security** → **Networking**
   - Ensure "Allow Azure services and resources to access this server" is set to **Yes**
   - Add your current client IP address to the firewall rules

1. **Verify Authentication Method:**

   - Ensure you're using **Microsoft Entra ID - Universal with MFA support** in VS Code
   - Make sure you're signed into the same Azure account in both Azure portal and VS Code
   - Try signing out and back in to refresh authentication tokens

1. **Check Network Connectivity:**

   ```powershell
   # Test connectivity to SQL Server
   Test-NetConnection -ComputerName "your-sql-server.database.windows.net" -Port 1433
   ```

#### SQL Query Execution Errors

**Symptoms:**

- Permission denied errors when executing SQL scripts
- Object already exists errors

**Solutions:**

1. **Permission Issues:**

   - Ensure your user account is set as the Microsoft Entra admin for the SQL Server
   - Verify you have `db_owner` or appropriate permissions on the database

1. **Object Exists Errors:**

   - The SQL script includes `DROP` statements - these are safe to run multiple times
   - If you get constraint errors, run the drop statements individually first

### Node.js and npm Issues

You might experience these issues when using Node.js and npm.

- [Port 3000 Already in Use](#port-3000-already-in-use)
- [Package Installation Failures](#package-installation-failures)
- [Runtime Connection Errors](#runtime-connection-errors)

#### Port 3000 Already in Use

**Symptoms:**

- "EADDRINUSE: address already in use :::3000"
- Vite server doesn't start

**Solutions:**

1. **Kill Existing Process:**

   ```powershell
   # Find process using port 3000
   netstat -ano | findstr :3000
   # Kill the process (replace PID with actual process ID)
   taskkill /PID [PID] /F
   ```

1. **Use Alternative Port:**

   - To use a different port, update `vite.config.ts`
   - Update Power SDK configuration accordingly

#### Package Installation Failures

**Symptoms:**

- npm install errors
- Module not found errors

**Solutions:**

1. **Clear npm Cache:**

   ```powershell
   npm cache clean --force
   npm install
   ```

1. **Delete node_modules and Reinstall:**

   ```powershell
   Remove-Item -Recurse -Force node_modules
   Remove-Item package-lock.json
   npm install
   ```

1. **Node Version Issues:**

   ```powershell
   # Check Node version
   node --version
   # Should be LTS version (18.x or 20.x)
   ```

#### Runtime Connection Errors

**Symptoms:**

- "Failed to load data" in the React app
- Connection refused errors

**Solutions:**

1. **Check Power Platform Connection:**

   - Verify the SQL Server connection is working in Power Platform
   - Test the connection in Power Platform maker portal

1. **Consent Issues:**

   - Ensure you give consent when the app first loads
   - Clear browser cache and try again

1. **Environment Mismatch:**

   - Verify you're running the app in the same environment where the connection was created
   - Check that the browser profile matches your Power Platform account
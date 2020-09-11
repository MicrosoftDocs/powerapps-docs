---
title: "Consume Common Data Service data with Azure Synapse Analytics | MicrosoftDocs"
description: "Use Azure Synapse Analytics to analyze Common Data Service data"
ms.custom: ""
ms.date: 08/28/2020
ms.reviewer: "matp"
author: sabinn-msft
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "powerapps"
ms.assetid: 
ms.author: "sabinn"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# View and query Common Data Service data with Azure Synapse Analytics

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Azure Synapse is an analytics service that brings together enterprise data warehousing and Big Data analytics. After you export data from Common Data Service to Azure Data Lake Storage Gen2 with the Export to data lake service, you can use Azure Synapse Analytics workspaces to view and query your data in a database, using Spark or T-SQL.

## Prerequisite

Before using Azure Synapse Analytics workspaces to analyze Common Data Service data, you must have already exported Common Data Service data using the Export to Data Lake service. More information: [Export entity data to Azure Data Lake Storage Gen2](export-to-data-lake.md)

## Create a synapse workspace 

1. Sign in to the [Azure portal](https://portal.azure.com), and then search for and select **Azure Synapse Analytics (workspaces preview)**.

1. Select **+ Add** to create a new workspace.

1. Provide the following information for the synapse workspace:
   - **Subscription**: Select the subscription containing the Export to Data Lake data.
   - **Resource group**: Select the resource containing the Export to Data Lake data.
   - **Workspace name**: Create any name for the workspace.
   - **Region**: Select the same region that was used with the Export to Data Lake service.
   - **Account name**: Select the same account that was used with the Export to Data Lake service.
   - **File system name**: Select the directory containing the Export to Data Lake data.
   - Check the box **Assign myself the Storage Blob Data Contributor role on the Data Lake Storage Gen2 account** to assign yourself the necessary roles.

   :::image type="content" source="media/configure-synapse-workspace1.png" alt-text="Configure the synapse workspace part 1":::

   :::image type="content" source="media/configure-synapse-workspace2.png" alt-text="Configure the synapse workspace part 2":::

1. Select **Create + review**. Review the configuration, and then select **Create**. 
1. Provide the **Admin username** and **Password** to access the SQL Server. Note these credentials for later steps. Leave all other default options.
 
## Configure access to the Synapse workspace storage container

1. Go to the storage container with the Common Data Service data and select **Access control (IAM)** from the left side bar. Select **Add** from the top menu, and then select **Add role assignment**.

   :::image type="content" source="media/synapse-workspace-access.png" alt-text="Configure Azure Synapse workspace access":::

1. Provide the following values in the **Add role assignment** page:
   - **Role**: Select **Storage Blob Data Reader**.
   - **Assign access to**: Select **Azure AD user, group, or service principal**.
   - **Select**: Enter the name of the Synapse workspace. 

1. Go back to the Synapse workspace. Select **Managed identities** from the left side bar. Ensure that the **Grant CONTROL to the workspace's managed identity on all SQL pools and SQL on-demand** check box is selected, and then select **Save**.

## Access the Synapse workspace with the SQL on-demand endpoint

1. Locate the **Overview** page of the newly created Synapse workspace. Copy the **SQL on-demand endpoint**.

   :::image type="content" source="media/synapse-workspace-endpoint.png" alt-text="Azure Synapse SQL Server endpoint":::

1. Open SQL Server Management Studio (SSMS). If you do not have SSMS, [Download SQL Server Management Studio ](/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15).
1. Provide the connection details for your Synapse workspace:
   - **Server type**: Select **Database Engine**.
   - **SQL server**: Paste the **SQL on-demand endpoint** that you copied in the previous step.
   - **Authentication type**: Select either **SQL Server Authentication** or enter the **Login** username whichever was set during the creation of the Synapse workspace. Alternatively, you may use **Azure Active Directory** as the **Authentication type** to sign in to your Synapse workspace.
   - Password: Enter the password set during the creation of the Synapse workspace.
1. Select **Connect**.

## Create a view for your data
1. In SSMS, right-click **Databases** on the left sidebar, and then select **New Database**.
1. Enter a **Database name**, and then select **OK**.
1. Right-click the new database, and then select **New Query**.
1. Configure the [Script to access the data](#script-to-access-the-data):
   - `@root`: Replace <storage_account_name> with the name of the storage account containing the Common Data Service data and replace <container_name> with the name of the container containing the model.json.
   - `@entity` : Replace <entity_name> with the name of the entity to view.
   - `@view` : Replace <view_name> with a name of your choice for the view.
1. Copy the updated [Script to access the data](#script-to-access-the-data) and paste it in to the **New Query** window, and then select **Execute** on the SSMS command bar.
1. Expand your database under the **Views** folder to access the new view. To view your data, right-click the new view, and then select **Select Top 100 Rows**.
1. Your data is displayed. To enter a different query, such as to filter by component ID, change the query in the top portion of the screen. Then select **Execute** on the SSMS command bar.

   :::image type="content" source="media/filter-by-id.png" alt-text="Filter query by ID":::

## Script to access the data

```tsql
/*  Script: Generate Synapse SQL Serverless view (v3.2) that reads the latest version of CDM files
*/

--> Fill in the root, entity, and view.
declare @root nvarchar(4000) = N'https://<storage_account_name>.dfs.core.windows.net/<container_name>/model.json'
declare @entity nvarchar(100) = '<entity_name>';
declare @view nvarchar(100) = 'dbo.<view_name>';
declare @partitions varchar(4000) = '';
declare @defaultFileType varchar(4000) = 'CSV'; --> file type that will be used in format setting is not in model.json

------------------------------------------------------------------------------------------------------------------
--      The magic begins here. 
------------------------------------------------------------------------------------------------------------------

--> Optionaly set partitions:
--set @partitions = ',[FILE PARTITION 1] = cdm.filepath(1), [FILE PARTITION 2] = cdm.filepath(2)';

SET QUOTED_IDENTIFIER OFF;

---------------------------------------------------------------------------
-- Step 1/ - load model.json
---------------------------------------------------------------------------
declare @json nvarchar(max);
declare @sqlGetModelJson nvarchar(max) = "
-- TODO: Replace this with SINGLE_CLOB
select @model_json = c.value
from openrowset(bulk '"+@root+"',
FORMAT='CSV',
        FIELDTERMINATOR ='0x0b', 
        FIELDQUOTE = '0x0b', 
        ROWTERMINATOR = '0x0b'
) WITH (value varchar(max)) c;
"

EXECUTE sp_executesql  
    @sqlGetModelJson  
    ,N'@model_json nvarchar(max) OUTPUT'  
    ,@model_json = @json OUTPUT;  
--> model.json is loaded in @modelJSON

declare @columns nvarchar(max) = '',
        @openrowset nvarchar(max) = '',
        @sql nvarchar(max) = '',
        @mapping nvarchar(max) = '';

declare @collation varchar(100) = (select collation_name from sys.databases where database_id = DB_ID())
if(@collation not like '%UTF8')
    set @collation = 'Latin1_General_100_CI_AS_SC_UTF8'

select 
        @columns += IIF(name IS NULL, '',  ( quotename(name) + ',')), 
        @mapping += IIF(name IS NULL, '', ( quotename(name) + ' ' + 
         CASE dataType
            WHEN 'int64' THEN 'bigint'
            WHEN 'int32' THEN 'int'
            WHEN 'dateTime' THEN 'datetime2'
            WHEN 'datetimeoffset' THEN 'datetimeoffset'
            WHEN 'decimal' THEN 'decimal'
            WHEN 'double' THEN 'float'
            WHEN 'boolean' THEN 'varchar(5)' --> True or False
            WHEN 'string' THEN 'nvarchar(max)'
            WHEN 'guid' THEN 'uniqueidentifier'
            WHEN 'json' THEN 'nvarchar(max)'
            ELSE dataType
         END + ','))
from openjson(@json, '$.entities') e
   cross apply openjson(e.value, '$.attributes')
with (name sysname, dataType sysname)
where json_value(e.value, '$.name') = @entity;

SET @columns = TRIM(',' FROM @columns);
SET @mapping = TRIM(',' FROM @mapping);

with locations as (
select location, [format], hasColumnHeader, delimiter, encoding
from openjson(@json, '$.entities') e
   cross apply openjson(e.value, '$.partitions')
with (  location nvarchar(4000),
        [format] nvarchar(50) '$.fileFormatSettings."$type"',
        [hasColumnHeader] bit '$.fileFormatSettings.columnHeaders',
        delimiter nvarchar(1) '$.fileFormatSettings.delimiter',
        [encoding] varchar(10) '$.fileFormatSettings.encoding')
where json_value(e.value, '$.name') = @entity
)

select *
into #files
from locations;
update #files set location = replace(location,':443','');

declare @domain varchar(max);
set @domain = (
select top 1 SUBSTRING(f.location, 0, charindex(t.value, f.location)) + t.value
from #files f
    cross apply string_split(f.location, '/') as t
group by charindex(t.value, f.location), t.value, SUBSTRING(f.location, 0, charindex(t.value, f.location))
having count(*) =  (select count(*) from #files)
order by charindex(t.value, f.location) desc
);

declare @filelist varchar(max) = ''
select @filelist += ''''+
        location+/*REPLACE(
                REPLACE(location, '.dfs.core.windows.net', '.dsf.core.windows.net'),
            ':443', '')*/
        +''','
from #files;

set @filelist = TRIM(' ,' FROM @filelist);

-- Grouping by wildcards
with t1 as (
    select  
            path = location,
            file_name = SUBSTRING(location, LEN(@domain)+1, 8000),
            [format], hasColumnHeader, delimiter, encoding
    from #files
),
t2 as (
select   [format], hasColumnHeader, delimiter, encoding,
         pattern = @domain
          + REPLACE(REPLACE(REPLACE(TRANSLATE(file_name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-', '#####################################'), '/#', '/*'), '#', ''), '_', '') + '*'
from t1)
select distinct pattern, [format], hasColumnHeader, delimiter, encoding
into #groups
from t2;

with rowsets as (
select rs = CONCAT( ' OPENROWSET( BULK ''',pattern,''',
                           FORMAT = ''', CASE [format] WHEN 'CsvFormatSettings' THEN 'CSV' ELSE @defaultFileType END ,''',
                           FIRSTROW = ',IIF(hasColumnHeader=1, '2', '1'),',
                           FIELDTERMINATOR = ''',delimiter,''')'), encoding
from #groups
)
-- TODO: Replace with STRING_AGG
SELECT  @sql += ' UNION ALL 
SELECT ' + @columns + @partitions + '
        FROM ' + rowsets.rs + '
        WITH (' +
        case encoding
                when 'UTF-8' then REPLACE(@mapping, 'nvarchar(max)', 'varchar(max) COLLATE  ' + @collation)
                else @mapping
        end  + ') as cdm
WHERE cdm.filepath() IN (' + @filelist +')'
FROM rowsets;

if( SUBSTRING( @sql, 1, 10) = ' UNION ALL')
    SET @sql = SUBSTRING( @sql, 12, 4000000);

set @sql = 'CREATE OR ALTER VIEW ' + @view + ' AS ' + @sql;
EXEC (@sql)
--SELECT [XML_F52E2B61-18A1-11d1-B105-00805F49916B] = @sql
--print @sql
go
drop table #files
drop table #groups
go

```

### See also
[Export entity data to Azure Data Lake Storage Gen2](export-to-data-lake.md)
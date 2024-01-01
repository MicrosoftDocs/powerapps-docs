### Install or verify that the following are installed

- Install Visual Studio Code. See [Download Visual Studio Code](https://code.visualstudio.com/download)
- Install the PowerShell extension for Visual Studio Code. See [PowerShell for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)
- Install PowerShell 7.4 or higher. See [Install PowerShell on Windows, Linux, and macOS](/powershell/scripting/install/installing-powershell)
- Install the Azure PowerShell AZ module. [How to install Azure PowerShell](/powershell/azure/install-azure-powershell)

### Verify installation

1. Open Visual Studio Code.
1. In the **Terminal** menu, select **New Terminal**.
1. In Visual Studio Code navigation pane, select the :::image type="icon" source="media/visual-studio-code-powershell-extension-icon.png" border="false"::: icon for the PowerShell extension.
1. Copy and paste the following script in the Visual Studio Code terminal window:

   ```powershell
   Write-Host 'PowerShell Version:'
   $PSVersionTable.PSVersion.ToString()
   Write-Host 'PowerShell Az version:'
   (Get-InstalledModule Az).Version
   ```

1. Press <kbd>Enter</kbd>. The output should resemble the following:

   ```powershell
   PowerShell Version:
   7.4.0
   PowerShell Az version:
   11.1.0
   ```

If you don't see something like this, install the prerequisites.
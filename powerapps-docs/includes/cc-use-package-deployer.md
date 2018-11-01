The Package Deployer tool is available as a [NuGet
package](https://go.microsoft.com/fwlink/?linkid=859205). To use the Package Deployer, you must download and extract it to your local computer using **nuget.exe.**<br/><br/>

Download **nuget.exe** from <https://www.nuget.org/downloads>, and save it to your computer, say **d:\\**. Then run the following command at the command prompt to extract the package contents to a folder, say **PD**, on your computer:<br/>

`d:\nuget install Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf -Version [VERSION] -O d:\PD`<br/><br/>
    
After you have extracted the Package Deployer tool, browse to the `[ExtractedLocation]\tools` folder to find the **PackageDeployer.exe** file. 

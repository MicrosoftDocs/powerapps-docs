param(
    [Parameter(Mandatory=$true)][string]$Folder
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$files = Get-ChildItem -Path $Folder -Filter *.png
foreach ($f in $files) {
    try {
        $fs = [System.IO.File]::OpenRead($f.FullName)
        $img = [System.Drawing.Image]::FromStream($fs)
        $bmp = New-Object System.Drawing.Bitmap $img
        $img.Dispose()
        $fs.Close()
        $fs.Dispose()

        $w = $bmp.Width; $h = $bmp.Height
        # Skip small images (likely not full studio screenshots)
        if ($h -lt 200 -or $w -lt 400) {
            Write-Host "$($f.Name): skipped (size $w x $h)"
            $bmp.Dispose()
            continue
        }
        # Detect black bar: check pixel at (600, 10). If it's dark (< 60 brightness),
        # scan down to find the first bright row (>= 200 brightness avg).
        $probe = $bmp.GetPixel([Math]::Min(600, $w - 1), 10)
        $probeB = ($probe.R + $probe.G + $probe.B) / 3
        if ($probeB -ge 60) {
            Write-Host "$($f.Name): no black bar (probe y=10 brightness=$probeB), skipped"
            $bmp.Dispose()
            continue
        }
        $cropY = 0
        $maxScan = [Math]::Min(200, $h)
        for ($y = 5; $y -lt $maxScan; $y++) {
            $p = $bmp.GetPixel([Math]::Min(600, $w - 1), $y)
            $b = ($p.R + $p.G + $p.B) / 3
            if ($b -ge 200) { $cropY = $y; break }
        }
        if ($cropY -le 2) {
            Write-Host "$($f.Name): could not find end of black bar, skipped"
            $bmp.Dispose()
            continue
        }
        if ($cropY -le 2) {
            Write-Host "$($f.Name): no black bar (cropY=$cropY), skipped"
            $bmp.Dispose()
            continue
        }
        $rect = New-Object System.Drawing.Rectangle 0, $cropY, $w, ($h - $cropY)
        $cropped = $bmp.Clone($rect, $bmp.PixelFormat)
        $bmp.Dispose()
        $tmp = "$($f.FullName).tmp.png"
        $cropped.Save($tmp, [System.Drawing.Imaging.ImageFormat]::Png)
        $cropped.Dispose()
        Move-Item -Force -Path $tmp -Destination $f.FullName
        Write-Host "$($f.Name): cropped top $cropY px -> $w x $($h - $cropY)"
    } catch {
        Write-Host "$($f.Name): ERROR $_"
    }
}

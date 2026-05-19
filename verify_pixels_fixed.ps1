Add-Type -AssemblyName System.Drawing
$base = 'c:\Users\mkaur\Downloads\github\powerapps-docs-pr\powerapps-docs\maker\canvas-apps\media\data-platform-create-app-scratch'

$checks = @(
    @{ file='close-data.png';    pts=@(@(284,50),@(300,50),@(300,78),@(282,60)) },
    @{ file='gallery-items.png'; pts=@(@(370,0),@(500,0),@(370,22),@(978,22)) },
    @{ file='final-browse.png';  pts=@(@(4,4),@(50,4),@(4,30),@(90,30)) },
    @{ file='field-list.png';    pts=@(@(2,2),@(120,2),@(2,40),@(240,40)) },
    @{ file='rename-browse.png'; pts=@(@(50,225),@(180,225),@(50,250)) }
)

foreach ($c in $checks) {
    $p = Join-Path $base $c.file
    if (Test-Path $p) {
        $info = Get-Item $p
        Write-Host "=== $($c.file) | LastWrite: $($info.LastWriteTime) | Size: $($info.Length) ==="
        $bm = New-Object System.Drawing.Bitmap $p
        foreach ($pt in $c.pts) {
            try {
                $px = $bm.GetPixel($pt[0], $pt[1])
                Write-Host "  ($($pt[0]),$($pt[1])) = R$($px.R) G$($px.G) B$($px.B)"
            } catch {
                Write-Host "  ($($pt[0]),$($pt[1])) = OUT OF BOUNDS ($($bm.Width)x$($bm.Height))"
            }
        }
        $bm.Dispose()
    } else {
        Write-Host "=== $($c.file) | NOT FOUND at $p ==="
    }
}
